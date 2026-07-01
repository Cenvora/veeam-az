import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_vnet_restore_point import PageOfVnetRestorePoint
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.vnet_backup_destination import VnetBackupDestination
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    region_id: None | str | Unset = UNSET,
    subscription_id: None | str | Unset = UNSET,
    backup_destinations: list[VnetBackupDestination] | None | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_region_id: None | str | Unset
    if isinstance(region_id, Unset):
        json_region_id = UNSET
    else:
        json_region_id = region_id
    params["RegionId"] = json_region_id

    json_subscription_id: None | str | Unset
    if isinstance(subscription_id, Unset):
        json_subscription_id = UNSET
    else:
        json_subscription_id = subscription_id
    params["SubscriptionId"] = json_subscription_id

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

    params["OnlyLatest"] = only_latest

    json_point_in_time: None | str | Unset
    if isinstance(point_in_time, Unset):
        json_point_in_time = UNSET
    elif isinstance(point_in_time, datetime.datetime):
        json_point_in_time = point_in_time.isoformat()
    else:
        json_point_in_time = point_in_time
    params["PointInTime"] = json_point_in_time

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/restorePoints/vnets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfVnetRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfVnetRestorePoint.from_dict(response.json())

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
) -> Response[PageOfVnetRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    region_id: None | str | Unset = UNSET,
    subscription_id: None | str | Unset = UNSET,
    backup_destinations: list[VnetBackupDestination] | None | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfVnetRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Virtual Network Configuration Restore Points

     The HTTP GET request to the `/restorePoints/vnets` endpoint retrieves a list of restore points
    created for virtual network configurations in the Veeam Backup for Microsoft Azure configuration
    database.

    Args:
        region_id (None | str | Unset):
        subscription_id (None | str | Unset):
        backup_destinations (list[VnetBackupDestination] | None | Unset):
        only_latest (bool | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfVnetRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        subscription_id=subscription_id,
        backup_destinations=backup_destinations,
        only_latest=only_latest,
        point_in_time=point_in_time,
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
    region_id: None | str | Unset = UNSET,
    subscription_id: None | str | Unset = UNSET,
    backup_destinations: list[VnetBackupDestination] | None | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfVnetRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Virtual Network Configuration Restore Points

     The HTTP GET request to the `/restorePoints/vnets` endpoint retrieves a list of restore points
    created for virtual network configurations in the Veeam Backup for Microsoft Azure configuration
    database.

    Args:
        region_id (None | str | Unset):
        subscription_id (None | str | Unset):
        backup_destinations (list[VnetBackupDestination] | None | Unset):
        only_latest (bool | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfVnetRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        region_id=region_id,
        subscription_id=subscription_id,
        backup_destinations=backup_destinations,
        only_latest=only_latest,
        point_in_time=point_in_time,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    region_id: None | str | Unset = UNSET,
    subscription_id: None | str | Unset = UNSET,
    backup_destinations: list[VnetBackupDestination] | None | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfVnetRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Virtual Network Configuration Restore Points

     The HTTP GET request to the `/restorePoints/vnets` endpoint retrieves a list of restore points
    created for virtual network configurations in the Veeam Backup for Microsoft Azure configuration
    database.

    Args:
        region_id (None | str | Unset):
        subscription_id (None | str | Unset):
        backup_destinations (list[VnetBackupDestination] | None | Unset):
        only_latest (bool | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfVnetRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        subscription_id=subscription_id,
        backup_destinations=backup_destinations,
        only_latest=only_latest,
        point_in_time=point_in_time,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    region_id: None | str | Unset = UNSET,
    subscription_id: None | str | Unset = UNSET,
    backup_destinations: list[VnetBackupDestination] | None | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfVnetRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Virtual Network Configuration Restore Points

     The HTTP GET request to the `/restorePoints/vnets` endpoint retrieves a list of restore points
    created for virtual network configurations in the Veeam Backup for Microsoft Azure configuration
    database.

    Args:
        region_id (None | str | Unset):
        subscription_id (None | str | Unset):
        backup_destinations (list[VnetBackupDestination] | None | Unset):
        only_latest (bool | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfVnetRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            region_id=region_id,
            subscription_id=subscription_id,
            backup_destinations=backup_destinations,
            only_latest=only_latest,
            point_in_time=point_in_time,
            offset=offset,
            limit=limit,
        )
    ).parsed
