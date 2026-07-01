from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_protected_virtual_machine import AsyncOperationOfProtectedVirtualMachine
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.protected_virtual_machine import ProtectedVirtualMachine
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    sync: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sync: bool | None | Unset
    if isinstance(sync, Unset):
        json_sync = UNSET
    else:
        json_sync = sync
    params["sync"] = json_sync

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/protectedItem/virtualMachines/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProtectedVirtualMachine
    | None
):
    if response.status_code == 200:
        response_200 = ProtectedVirtualMachine.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfProtectedVirtualMachine.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ProblemDetails404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AsyncOperationOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProtectedVirtualMachine
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProtectedVirtualMachine
]:
    """Get Protected Azure VM Data

     The HTTP GET request to the `/protectedItem/virtualMachines/{id}` endpoint retrieves information on
    a protected Azure VM with the specified ID.

    Args:
        id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfProtectedVirtualMachine | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedVirtualMachine]
    """

    kwargs = _get_kwargs(
        id=id,
        sync=sync,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProtectedVirtualMachine
    | None
):
    """Get Protected Azure VM Data

     The HTTP GET request to the `/protectedItem/virtualMachines/{id}` endpoint retrieves information on
    a protected Azure VM with the specified ID.

    Args:
        id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfProtectedVirtualMachine | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedVirtualMachine
    """

    return sync_detailed(
        id=id,
        client=client,
        sync=sync,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProtectedVirtualMachine
]:
    """Get Protected Azure VM Data

     The HTTP GET request to the `/protectedItem/virtualMachines/{id}` endpoint retrieves information on
    a protected Azure VM with the specified ID.

    Args:
        id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfProtectedVirtualMachine | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedVirtualMachine]
    """

    kwargs = _get_kwargs(
        id=id,
        sync=sync,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProtectedVirtualMachine
    | None
):
    """Get Protected Azure VM Data

     The HTTP GET request to the `/protectedItem/virtualMachines/{id}` endpoint retrieves information on
    a protected Azure VM with the specified ID.

    Args:
        id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfProtectedVirtualMachine | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedVirtualMachine
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            sync=sync,
        )
    ).parsed
