from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.date_time_info import DateTimeInfo
from ...models.problem_details_401 import ProblemDetails401
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/system/time",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DateTimeInfo | ProblemDetails401 | None:
    if response.status_code == 200:
        response_200 = DateTimeInfo.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DateTimeInfo | ProblemDetails401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DateTimeInfo | ProblemDetails401]:
    """Get Current Time Zone

     The HTTP GET request to the `/system/time` endpoint retrieves the current time zone in which backup
    appliance is operating.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DateTimeInfo | ProblemDetails401]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> DateTimeInfo | ProblemDetails401 | None:
    """Get Current Time Zone

     The HTTP GET request to the `/system/time` endpoint retrieves the current time zone in which backup
    appliance is operating.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DateTimeInfo | ProblemDetails401
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DateTimeInfo | ProblemDetails401]:
    """Get Current Time Zone

     The HTTP GET request to the `/system/time` endpoint retrieves the current time zone in which backup
    appliance is operating.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DateTimeInfo | ProblemDetails401]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> DateTimeInfo | ProblemDetails401 | None:
    """Get Current Time Zone

     The HTTP GET request to the `/system/time` endpoint retrieves the current time zone in which backup
    appliance is operating.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DateTimeInfo | ProblemDetails401
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
