import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cosmos_db_backup_destination import CosmosDbBackupDestination
from ...models.data_retrieval_status import DataRetrievalStatus
from ...models.page_of_cosmos_db_restore_point import PageOfCosmosDbRestorePoint
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.storage_access_tier import StorageAccessTier
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cosmos_db_account_id: None | str | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    storage_access_tier: list[StorageAccessTier] | None | Unset = UNSET,
    immutability_enabled: bool | Unset = UNSET,
    backup_destination: list[CosmosDbBackupDestination] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_cosmos_db_account_id: None | str | Unset
    if isinstance(cosmos_db_account_id, Unset):
        json_cosmos_db_account_id = UNSET
    else:
        json_cosmos_db_account_id = cosmos_db_account_id
    params["CosmosDbAccountId"] = json_cosmos_db_account_id

    params["OnlyLatest"] = only_latest

    json_data_retrieval_statuses: list[str] | None | Unset
    if isinstance(data_retrieval_statuses, Unset):
        json_data_retrieval_statuses = UNSET
    elif isinstance(data_retrieval_statuses, list):
        json_data_retrieval_statuses = []
        for data_retrieval_statuses_type_0_item_data in data_retrieval_statuses:
            data_retrieval_statuses_type_0_item = data_retrieval_statuses_type_0_item_data.value
            json_data_retrieval_statuses.append(data_retrieval_statuses_type_0_item)

    else:
        json_data_retrieval_statuses = data_retrieval_statuses
    params["DataRetrievalStatuses"] = json_data_retrieval_statuses

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

    json_storage_access_tier: list[str] | None | Unset
    if isinstance(storage_access_tier, Unset):
        json_storage_access_tier = UNSET
    elif isinstance(storage_access_tier, list):
        json_storage_access_tier = []
        for storage_access_tier_type_0_item_data in storage_access_tier:
            storage_access_tier_type_0_item = storage_access_tier_type_0_item_data.value
            json_storage_access_tier.append(storage_access_tier_type_0_item)

    else:
        json_storage_access_tier = storage_access_tier
    params["StorageAccessTier"] = json_storage_access_tier

    params["ImmutabilityEnabled"] = immutability_enabled

    json_backup_destination: list[str] | None | Unset
    if isinstance(backup_destination, Unset):
        json_backup_destination = UNSET
    elif isinstance(backup_destination, list):
        json_backup_destination = []
        for backup_destination_type_0_item_data in backup_destination:
            backup_destination_type_0_item = backup_destination_type_0_item_data.value
            json_backup_destination.append(backup_destination_type_0_item)

    else:
        json_backup_destination = backup_destination
    params["BackupDestination"] = json_backup_destination

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/restorePoints/cosmosDb/repository",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfCosmosDbRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfCosmosDbRestorePoint.from_dict(response.json())

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
) -> Response[PageOfCosmosDbRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cosmos_db_account_id: None | str | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    storage_access_tier: list[StorageAccessTier] | None | Unset = UNSET,
    immutability_enabled: bool | Unset = UNSET,
    backup_destination: list[CosmosDbBackupDestination] | None | Unset = UNSET,
) -> Response[PageOfCosmosDbRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Cosmos DB Restore Points

     The HTTP GET request to the `/restorePoints/cosmosDb/repository` endpoint retrieves a list of
    restore points created for Cosmos DB by Veeam Backup for Microsoft Azure.

    Args:
        cosmos_db_account_id (None | str | Unset):
        only_latest (bool | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):
        storage_access_tier (list[StorageAccessTier] | None | Unset):
        immutability_enabled (bool | Unset):
        backup_destination (list[CosmosDbBackupDestination] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfCosmosDbRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        only_latest=only_latest,
        data_retrieval_statuses=data_retrieval_statuses,
        point_in_time=point_in_time,
        offset=offset,
        limit=limit,
        storage_access_tier=storage_access_tier,
        immutability_enabled=immutability_enabled,
        backup_destination=backup_destination,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    cosmos_db_account_id: None | str | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    storage_access_tier: list[StorageAccessTier] | None | Unset = UNSET,
    immutability_enabled: bool | Unset = UNSET,
    backup_destination: list[CosmosDbBackupDestination] | None | Unset = UNSET,
) -> PageOfCosmosDbRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Cosmos DB Restore Points

     The HTTP GET request to the `/restorePoints/cosmosDb/repository` endpoint retrieves a list of
    restore points created for Cosmos DB by Veeam Backup for Microsoft Azure.

    Args:
        cosmos_db_account_id (None | str | Unset):
        only_latest (bool | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):
        storage_access_tier (list[StorageAccessTier] | None | Unset):
        immutability_enabled (bool | Unset):
        backup_destination (list[CosmosDbBackupDestination] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfCosmosDbRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        cosmos_db_account_id=cosmos_db_account_id,
        only_latest=only_latest,
        data_retrieval_statuses=data_retrieval_statuses,
        point_in_time=point_in_time,
        offset=offset,
        limit=limit,
        storage_access_tier=storage_access_tier,
        immutability_enabled=immutability_enabled,
        backup_destination=backup_destination,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cosmos_db_account_id: None | str | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    storage_access_tier: list[StorageAccessTier] | None | Unset = UNSET,
    immutability_enabled: bool | Unset = UNSET,
    backup_destination: list[CosmosDbBackupDestination] | None | Unset = UNSET,
) -> Response[PageOfCosmosDbRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Cosmos DB Restore Points

     The HTTP GET request to the `/restorePoints/cosmosDb/repository` endpoint retrieves a list of
    restore points created for Cosmos DB by Veeam Backup for Microsoft Azure.

    Args:
        cosmos_db_account_id (None | str | Unset):
        only_latest (bool | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):
        storage_access_tier (list[StorageAccessTier] | None | Unset):
        immutability_enabled (bool | Unset):
        backup_destination (list[CosmosDbBackupDestination] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfCosmosDbRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        only_latest=only_latest,
        data_retrieval_statuses=data_retrieval_statuses,
        point_in_time=point_in_time,
        offset=offset,
        limit=limit,
        storage_access_tier=storage_access_tier,
        immutability_enabled=immutability_enabled,
        backup_destination=backup_destination,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cosmos_db_account_id: None | str | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    storage_access_tier: list[StorageAccessTier] | None | Unset = UNSET,
    immutability_enabled: bool | Unset = UNSET,
    backup_destination: list[CosmosDbBackupDestination] | None | Unset = UNSET,
) -> PageOfCosmosDbRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Cosmos DB Restore Points

     The HTTP GET request to the `/restorePoints/cosmosDb/repository` endpoint retrieves a list of
    restore points created for Cosmos DB by Veeam Backup for Microsoft Azure.

    Args:
        cosmos_db_account_id (None | str | Unset):
        only_latest (bool | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):
        storage_access_tier (list[StorageAccessTier] | None | Unset):
        immutability_enabled (bool | Unset):
        backup_destination (list[CosmosDbBackupDestination] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfCosmosDbRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            cosmos_db_account_id=cosmos_db_account_id,
            only_latest=only_latest,
            data_retrieval_statuses=data_retrieval_statuses,
            point_in_time=point_in_time,
            offset=offset,
            limit=limit,
            storage_access_tier=storage_access_tier,
            immutability_enabled=immutability_enabled,
            backup_destination=backup_destination,
        )
    ).parsed
