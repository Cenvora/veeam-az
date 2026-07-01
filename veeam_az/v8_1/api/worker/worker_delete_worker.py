from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import Response


def _get_kwargs(
    vm_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v8.1/workers/{vm_name}".format(
            vm_name=quote(str(vm_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vm_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ProblemDetails401 | ProblemDetails403]:
    """Remove Worker Instance

     The HTTP DELETE request to the `/workers/{vmName}` endpoint removes a worker instance with the
    specified name from the Microsoft Azure environment.

    Args:
        vm_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        vm_name=vm_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vm_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ProblemDetails401 | ProblemDetails403 | None:
    """Remove Worker Instance

     The HTTP DELETE request to the `/workers/{vmName}` endpoint removes a worker instance with the
    specified name from the Microsoft Azure environment.

    Args:
        vm_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        vm_name=vm_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    vm_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ProblemDetails401 | ProblemDetails403]:
    """Remove Worker Instance

     The HTTP DELETE request to the `/workers/{vmName}` endpoint removes a worker instance with the
    specified name from the Microsoft Azure environment.

    Args:
        vm_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        vm_name=vm_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vm_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ProblemDetails401 | ProblemDetails403 | None:
    """Remove Worker Instance

     The HTTP DELETE request to the `/workers/{vmName}` endpoint removes a worker instance with the
    specified name from the Microsoft Azure environment.

    Args:
        vm_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            vm_name=vm_name,
            client=client,
        )
    ).parsed
