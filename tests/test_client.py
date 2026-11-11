"""Tests for VeeamClient version resolution and host normalisation."""

import importlib

import pytest

from veeam_az import VeeamClient
from veeam_az.versions import VERSION_TO_PACKAGE, resolve_api_version


@pytest.mark.parametrize(
    ("given", "expected"),
    [
        ("8", "8"),
        ("8.0", "8"),
        ("8.1", "8"),
        ("v8", "8"),
        ("V8.1", "8"),
        ("9", "9"),
        ("9.0", "9"),
        (" v9 ", "9"),
    ],
)
def test_resolve_api_version_aliases(given, expected):
    assert resolve_api_version(given) == expected


@pytest.mark.parametrize("bad", ["7", "8.2", "10", ""])
def test_resolve_api_version_rejects_unknown(bad):
    with pytest.raises(ValueError, match="Unsupported API version"):
        resolve_api_version(bad)


@pytest.mark.parametrize("version", sorted(VERSION_TO_PACKAGE))
def test_every_package_targets_its_own_path(version):
    """The generated login operation must call /api/oauth2/token and an endpoint under /api/v{version}/."""
    pkg = VERSION_TO_PACKAGE[version]
    about = importlib.import_module(f"{pkg}.api.system.system_get_about")
    kwargs = about._get_kwargs()
    assert kwargs["url"] == f"/api/v{version}/system/about"


def test_client_maps_alias_to_package():
    vc = VeeamClient(host="vbaz", api_version="8.1", token="t")
    assert vc.api_version == "8"
    assert vc.package == "veeam_az.v8"


@pytest.mark.parametrize(
    ("host", "expected"),
    [
        ("pgtsbak038", "https://pgtsbak038"),
        ("vbaz.example.com:8443", "https://vbaz.example.com:8443"),
        ("10.0.0.5", "https://10.0.0.5"),
        ("fe80::1", "https://[fe80::1]"),
        ("[fe80::1]:443", "https://[fe80::1]:443"),
        ("http://lab-vbaz", "http://lab-vbaz"),
        ("https://vbaz.example.com/", "https://vbaz.example.com"),
        ("https://vbaz.example.com/api", "https://vbaz.example.com"),
        ("https://vbaz.example.com/api/v8", "https://vbaz.example.com"),
        ("  https://vbaz.example.com/API/v8.1/  ", "https://vbaz.example.com"),
    ],
)
def test_normalize_host(host, expected):
    assert VeeamClient._normalize_host(host) == expected


def test_requires_credentials():
    with pytest.raises(ValueError):
        VeeamClient(host="vbaz", api_version="9")
