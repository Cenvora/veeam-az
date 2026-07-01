from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_protected_vnet import PageOfProtectedVnet
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.vnet_backup_destination import VnetBackupDestination
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    backup_destinations: list[VnetBackupDestination] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    json_backup_destinations: list[str] | None | Unset
    if isinstance(backup_destinations, Unset):
        json_backup_destinations = UNSET
    elif isinstance(backup_destinations, list):
        json_backup_destinations = []
        for backup_destinations_type_0_item_data in backup_destinations:
            backup_destinations_type_0_item = backup_destinations_type_0_item_data.value
            json_backup_destinations.append(backup_destinations_type_0_item)

    else:
        json_backup_destinations = backup_destinations
    params["BackupDestinations"] = json_backup_destinations

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/protectedItem/vnet",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfProtectedVnet | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfProtectedVnet.from_dict(response.json())

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
) -> Response[PageOfProtectedVnet | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    backup_destinations: list[VnetBackupDestination] | None | Unset = UNSET,
) -> Response[PageOfProtectedVnet | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Protected Azure Virtual Networks

     The HTTP GET request to the `/protectedItem/vnet` endpoint retrieves a list of virtual networks
    whose configurations are protected by Veeam Backup for Microsoft Azure to a .CSV or an .XML file.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        backup_destinations (list[VnetBackupDestination] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfProtectedVnet | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        backup_destinations=backup_destinations,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    backup_destinations: list[VnetBackupDestination] | None | Unset = UNSET,
) -> PageOfProtectedVnet | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Protected Azure Virtual Networks

     The HTTP GET request to the `/protectedItem/vnet` endpoint retrieves a list of virtual networks
    whose configurations are protected by Veeam Backup for Microsoft Azure to a .CSV or an .XML file.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        backup_destinations (list[VnetBackupDestination] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfProtectedVnet | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        backup_destinations=backup_destinations,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    backup_destinations: list[VnetBackupDestination] | None | Unset = UNSET,
) -> Response[PageOfProtectedVnet | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Protected Azure Virtual Networks

     The HTTP GET request to the `/protectedItem/vnet` endpoint retrieves a list of virtual networks
    whose configurations are protected by Veeam Backup for Microsoft Azure to a .CSV or an .XML file.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        backup_destinations (list[VnetBackupDestination] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfProtectedVnet | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        backup_destinations=backup_destinations,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    backup_destinations: list[VnetBackupDestination] | None | Unset = UNSET,
) -> PageOfProtectedVnet | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Protected Azure Virtual Networks

     The HTTP GET request to the `/protectedItem/vnet` endpoint retrieves a list of virtual networks
    whose configurations are protected by Veeam Backup for Microsoft Azure to a .CSV or an .XML file.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        backup_destinations (list[VnetBackupDestination] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfProtectedVnet | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            backup_destinations=backup_destinations,
        )
    ).parsed
