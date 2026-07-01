from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_disk_snapshot import PageOfDiskSnapshot
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    restore_point_id: None | Unset | UUID = UNSET,
    virtual_machine_id: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_restore_point_id: None | str | Unset
    if isinstance(restore_point_id, Unset):
        json_restore_point_id = UNSET
    elif isinstance(restore_point_id, UUID):
        json_restore_point_id = str(restore_point_id)
    else:
        json_restore_point_id = restore_point_id
    params["RestorePointId"] = json_restore_point_id

    json_virtual_machine_id: None | str | Unset
    if isinstance(virtual_machine_id, Unset):
        json_virtual_machine_id = UNSET
    else:
        json_virtual_machine_id = virtual_machine_id
    params["VirtualMachineId"] = json_virtual_machine_id

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/restorePoints/virtualMachines/diskSnapshots",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfDiskSnapshot | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfDiskSnapshot.from_dict(response.json())

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
) -> Response[PageOfDiskSnapshot | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    restore_point_id: None | Unset | UUID = UNSET,
    virtual_machine_id: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfDiskSnapshot | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Virtual Disk Snapshots

     The HTTP GET request to the `/restorePoints/virtualMachines/diskSnapshots` endpoint retrieves a list
    of virtual disk snapshots of Azure VMs.

    Args:
        restore_point_id (None | Unset | UUID):
        virtual_machine_id (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfDiskSnapshot | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
        virtual_machine_id=virtual_machine_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    restore_point_id: None | Unset | UUID = UNSET,
    virtual_machine_id: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfDiskSnapshot | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Virtual Disk Snapshots

     The HTTP GET request to the `/restorePoints/virtualMachines/diskSnapshots` endpoint retrieves a list
    of virtual disk snapshots of Azure VMs.

    Args:
        restore_point_id (None | Unset | UUID):
        virtual_machine_id (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfDiskSnapshot | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        restore_point_id=restore_point_id,
        virtual_machine_id=virtual_machine_id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    restore_point_id: None | Unset | UUID = UNSET,
    virtual_machine_id: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfDiskSnapshot | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Virtual Disk Snapshots

     The HTTP GET request to the `/restorePoints/virtualMachines/diskSnapshots` endpoint retrieves a list
    of virtual disk snapshots of Azure VMs.

    Args:
        restore_point_id (None | Unset | UUID):
        virtual_machine_id (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfDiskSnapshot | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
        virtual_machine_id=virtual_machine_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    restore_point_id: None | Unset | UUID = UNSET,
    virtual_machine_id: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfDiskSnapshot | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Virtual Disk Snapshots

     The HTTP GET request to the `/restorePoints/virtualMachines/diskSnapshots` endpoint retrieves a list
    of virtual disk snapshots of Azure VMs.

    Args:
        restore_point_id (None | Unset | UUID):
        virtual_machine_id (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfDiskSnapshot | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            restore_point_id=restore_point_id,
            virtual_machine_id=virtual_machine_id,
            offset=offset,
            limit=limit,
        )
    ).parsed
