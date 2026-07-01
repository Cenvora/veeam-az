from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.top_policies_duration_report import TopPoliciesDurationReport
from ...models.top_policy_source import TopPolicySource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    source: TopPolicySource | Unset = UNSET,
    count: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/overview/topPoliciesDuration",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | TopPoliciesDurationReport | None:
    if response.status_code == 200:
        response_200 = TopPoliciesDurationReport.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | TopPoliciesDurationReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    source: TopPolicySource | Unset = UNSET,
    count: int | Unset = 10,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | TopPoliciesDurationReport]:
    """Get Policy Duration Report

     The HTTP GET request to the `/overview/topPoliciesDuration` endpoint retrieves top N backup policies
    for fluctuations in execution time (including retries).

    Args:
        source (TopPolicySource | Unset): Specifies the type of the policy session.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | TopPoliciesDurationReport]
    """

    kwargs = _get_kwargs(
        source=source,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    source: TopPolicySource | Unset = UNSET,
    count: int | Unset = 10,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | TopPoliciesDurationReport | None:
    """Get Policy Duration Report

     The HTTP GET request to the `/overview/topPoliciesDuration` endpoint retrieves top N backup policies
    for fluctuations in execution time (including retries).

    Args:
        source (TopPolicySource | Unset): Specifies the type of the policy session.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | TopPoliciesDurationReport
    """

    return sync_detailed(
        client=client,
        source=source,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    source: TopPolicySource | Unset = UNSET,
    count: int | Unset = 10,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | TopPoliciesDurationReport]:
    """Get Policy Duration Report

     The HTTP GET request to the `/overview/topPoliciesDuration` endpoint retrieves top N backup policies
    for fluctuations in execution time (including retries).

    Args:
        source (TopPolicySource | Unset): Specifies the type of the policy session.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | TopPoliciesDurationReport]
    """

    kwargs = _get_kwargs(
        source=source,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    source: TopPolicySource | Unset = UNSET,
    count: int | Unset = 10,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | TopPoliciesDurationReport | None:
    """Get Policy Duration Report

     The HTTP GET request to the `/overview/topPoliciesDuration` endpoint retrieves top N backup policies
    for fluctuations in execution time (including retries).

    Args:
        source (TopPolicySource | Unset): Specifies the type of the policy session.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | TopPoliciesDurationReport
    """

    return (
        await asyncio_detailed(
            client=client,
            source=source,
            count=count,
        )
    ).parsed
