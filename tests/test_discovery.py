"""Tests for API version detection.

Served against httpx.MockTransport, so the probing behaviour is exercised for real rather
than mocked out.
"""

import httpx
import pytest

from veeam_az.discovery import (
    RestApiEndpoint,
    detect_api_version,
    detect_rest_api,
    newest_first,
    probe_url,
)
from veeam_az.versions import VERSION_TO_PACKAGE

BASE_URL = "https://vbaz.example.com"


def make_client(served, status_for_unserved=404, served_status=401, fail_with=None):
    """An httpx client whose appliance routes only the given versions.

    A served version answers 401 by default, which is what an unauthenticated probe of a
    real appliance gets: the route exists and the bearer token is missing.
    """
    requested = []

    def handler(request):
        requested.append(str(request.url))
        if fail_with is not None:
            raise fail_with
        for version in served:
            if request.url.path == f"/api/v{version}/system/about":
                return httpx.Response(served_status)
        return httpx.Response(status_for_unserved)

    return httpx.AsyncClient(transport=httpx.MockTransport(handler)), requested


def test_probe_url_adds_the_v_prefix():
    """API paths carry a "v" that the version strings do not."""
    assert probe_url(BASE_URL, "8.1") == f"{BASE_URL}/api/v8.1/system/about"


def test_probe_url_tolerates_a_trailing_slash():
    assert probe_url(BASE_URL + "/", "8.1").count("//") == 1


@pytest.mark.parametrize(
    "versions,expected",
    [
        (["8.1", "9.0"], ["9.0", "8.1"]),
        # Numeric ordering, which string sorting would get wrong
        (["8.9", "8.10"], ["8.10", "8.9"]),
        # Differing depths compare as if padded with zeroes rather than raising
        (["8", "8.1"], ["8.1", "8"]),
        # Unrecognizable entries are dropped rather than ordered arbitrarily
        (["8.1", "nonsense", None, ""], ["8.1"]),
        ([], []),
    ],
)
def test_newest_first(versions, expected):
    assert newest_first(versions) == expected


@pytest.mark.asyncio
async def test_detects_the_version_the_appliance_serves():
    client, _ = make_client(served=list(VERSION_TO_PACKAGE))

    detected = await detect_api_version(BASE_URL, client=client)

    assert detected == newest_first(VERSION_TO_PACKAGE)[0]


@pytest.mark.asyncio
async def test_detects_the_newest_of_several():
    """An older appliance must not be handed a newer version."""
    client, _ = make_client(served=["8.1"])

    detected = await detect_api_version(BASE_URL, client=client, versions=["8.1", "9.0"])

    assert detected == "8.1"


@pytest.mark.asyncio
@pytest.mark.parametrize("status", [200, 401, 403])
async def test_any_routed_status_counts_as_served(status):
    """The question is whether the path routes, not whether the probe was allowed."""
    client, _ = make_client(served=["8.1"], served_status=status)

    assert await detect_api_version(BASE_URL, client=client) == "8.1"


@pytest.mark.asyncio
async def test_probes_only_versions_this_package_supports():
    """Reporting a version the SDK cannot speak would be useless to the caller."""
    client, requested = make_client(served=list(VERSION_TO_PACKAGE))

    await detect_api_version(BASE_URL, client=client)

    probed = {url.split("/api/v")[1].split("/")[0] for url in requested}
    assert probed == set(VERSION_TO_PACKAGE)


@pytest.mark.asyncio
async def test_returns_none_when_no_version_answers():
    """The caller then falls back to a version of its own choosing."""
    client, _ = make_client(served=[])

    assert await detect_api_version(BASE_URL, client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_the_appliance_is_unreachable():
    client, _ = make_client(served=[], fail_with=httpx.ConnectError("unreachable"))

    assert await detect_api_version(BASE_URL, client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_a_probe_times_out():
    client, _ = make_client(served=[], fail_with=httpx.ReadTimeout("too slow"))

    assert await detect_api_version(BASE_URL, client=client) is None


@pytest.mark.asyncio
async def test_a_single_failing_probe_does_not_hide_the_others():
    """One version timing out must not lose a version that did answer."""

    def handler(request):
        if request.url.path == "/api/v9.0/system/about":
            raise httpx.ReadTimeout("too slow")
        if request.url.path == "/api/v8.1/system/about":
            return httpx.Response(401)
        return httpx.Response(404)

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))

    detected = await detect_api_version(BASE_URL, client=client, versions=["9.0", "8.1"])

    assert detected == "8.1"


@pytest.mark.asyncio
async def test_empty_candidate_list_makes_no_requests():
    client, requested = make_client(served=[])

    assert await detect_api_version(BASE_URL, client=client, versions=[]) is None
    assert requested == []


@pytest.mark.asyncio
async def test_caller_supplied_client_is_left_open():
    """Reusing a caller's client must not close it out from under them."""
    client, _ = make_client(served=list(VERSION_TO_PACKAGE))

    await detect_api_version(BASE_URL, client=client)

    assert not client.is_closed
    await client.aclose()


@pytest.mark.asyncio
async def test_detected_version_is_usable_with_veeam_client():
    """Detection is only useful if its result routes to a real SDK package."""
    from veeam_az.client import VeeamClient

    client, _ = make_client(served=list(VERSION_TO_PACKAGE))
    detected = await detect_api_version(BASE_URL, client=client)

    vc = VeeamClient(host=BASE_URL, api_version=detected, token="token")
    assert vc.package == VERSION_TO_PACKAGE[detected]


# ---------------------------------------------------------------------------
# Endpoint detection: which port, and which version on it
# ---------------------------------------------------------------------------


def make_endpoint_client(served, fail_with=None):
    """A client whose appliance routes only the given (port, version) pairs.

    httpx reports url.port as None for a scheme's default port, so an https URL written as
    ":443" arrives here with no port at all — hence the fallback. A real appliance still
    sees the TCP port it was reached on.
    """
    requested = []

    def port_of(request):
        return request.url.port or 443

    def handler(request):
        requested.append((port_of(request), str(request.url.path)))
        if fail_with is not None:
            raise fail_with
        for port, version in served:
            if port_of(request) == port and request.url.path == f"/api/v{version}/system/about":
                return httpx.Response(401)
        return httpx.Response(404)

    return httpx.AsyncClient(transport=httpx.MockTransport(handler)), requested


@pytest.mark.asyncio
async def test_finds_the_default_port():
    client, _ = make_endpoint_client([(443, "8.1")])

    endpoint = await detect_rest_api("vbaz.example.com", client=client)

    assert endpoint == RestApiEndpoint(port=443, api_version="8.1")


@pytest.mark.asyncio
async def test_port_order_is_the_callers_choice():
    """A deployment behind a port-forwarding proxy can be anywhere."""
    client, _ = make_endpoint_client([(443, "8.1"), (8443, "8.1")])

    endpoint = await detect_rest_api("vbaz.example.com", ports=(8443, 443), client=client)

    assert endpoint.port == 8443


@pytest.mark.asyncio
async def test_probes_every_port_and_version_combination():
    client, requested = make_endpoint_client([])

    await detect_rest_api(
        "vbaz.example.com", ports=(443, 8443), client=client, versions=["8.1", "9.0"]
    )

    assert sorted(requested) == sorted(
        [
            (port, f"/api/v{version}/system/about")
            for port in (443, 8443)
            for version in ("8.1", "9.0")
        ]
    )


@pytest.mark.asyncio
async def test_returns_none_when_no_port_answers():
    """Caller keeps whatever the user configured rather than guessing."""
    client, _ = make_endpoint_client([])

    assert await detect_rest_api("vbaz.example.com", client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_the_host_is_unreachable():
    client, _ = make_endpoint_client([], fail_with=httpx.ConnectError("no route"))

    assert await detect_rest_api("vbaz.example.com", client=client) is None


@pytest.mark.asyncio
async def test_no_ports_means_no_requests():
    client, requested = make_endpoint_client([])

    assert await detect_rest_api("vbaz.example.com", ports=(), client=client) is None
    assert requested == []


@pytest.mark.asyncio
async def test_detected_endpoint_builds_a_working_base_url():
    """The result should drop straight into a VeeamClient host argument."""
    from veeam_az.client import VeeamClient

    client, _ = make_endpoint_client([(443, "8.1")])
    endpoint = await detect_rest_api("vbaz.example.com", client=client)

    vc = VeeamClient(
        host=f"https://vbaz.example.com{endpoint.base_url_suffix}",
        api_version=endpoint.api_version,
        token="token",
    )
    assert vc.host == "https://vbaz.example.com:443"
    assert vc.package == VERSION_TO_PACKAGE[endpoint.api_version]
