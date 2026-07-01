from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.job_session import JobSession
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_409 import ProblemDetails409
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/restorePoints/virtualMachines/diskSnapshots/rescan",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | None:
    if response.status_code == 202:
        response_202 = JobSession.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails403.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ProblemDetails409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]:
    """Virtual Disk Snapshots Rescan

     The HTTP POST request to the `/restorePoints/virtualMachines/diskSnapshots/rescan` endpoint launches
    a snapshot rescan operation in the Microsoft Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | None:
    """Virtual Disk Snapshots Rescan

     The HTTP POST request to the `/restorePoints/virtualMachines/diskSnapshots/rescan` endpoint launches
    a snapshot rescan operation in the Microsoft Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]:
    """Virtual Disk Snapshots Rescan

     The HTTP POST request to the `/restorePoints/virtualMachines/diskSnapshots/rescan` endpoint launches
    a snapshot rescan operation in the Microsoft Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | None:
    """Virtual Disk Snapshots Rescan

     The HTTP POST request to the `/restorePoints/virtualMachines/diskSnapshots/rescan` endpoint launches
    a snapshot rescan operation in the Microsoft Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
