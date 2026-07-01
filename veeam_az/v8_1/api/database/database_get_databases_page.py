from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credentials_state_filter_options import CredentialsStateFilterOptions
from ...models.page_of_database import PageOfDatabase
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.protection_status import ProtectionStatus
from ...models.sql_backup_destination_filter_options import SqlBackupDestinationFilterOptions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    credentials_state: CredentialsStateFilterOptions | Unset = UNSET,
    assignable_by_sql_account_id: int | None | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    protection_status: list[ProtectionStatus] | None | Unset = UNSET,
    backup_destination: list[SqlBackupDestinationFilterOptions] | None | Unset = UNSET,
    db_from_protected_regions: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    json_subscription_id: None | str | Unset
    if isinstance(subscription_id, Unset):
        json_subscription_id = UNSET
    elif isinstance(subscription_id, UUID):
        json_subscription_id = str(subscription_id)
    else:
        json_subscription_id = subscription_id
    params["SubscriptionId"] = json_subscription_id

    json_tenant_id: None | str | Unset
    if isinstance(tenant_id, Unset):
        json_tenant_id = UNSET
    elif isinstance(tenant_id, UUID):
        json_tenant_id = str(tenant_id)
    else:
        json_tenant_id = tenant_id
    params["TenantId"] = json_tenant_id

    params["ServiceAccountId"] = service_account_id

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["SearchPattern"] = json_search_pattern

    json_credentials_state: str | Unset = UNSET
    if not isinstance(credentials_state, Unset):
        json_credentials_state = credentials_state.value

    params["CredentialsState"] = json_credentials_state

    json_assignable_by_sql_account_id: int | None | Unset
    if isinstance(assignable_by_sql_account_id, Unset):
        json_assignable_by_sql_account_id = UNSET
    else:
        json_assignable_by_sql_account_id = assignable_by_sql_account_id
    params["AssignableBySqlAccountId"] = json_assignable_by_sql_account_id

    json_region_ids: list[str] | None | Unset
    if isinstance(region_ids, Unset):
        json_region_ids = UNSET
    elif isinstance(region_ids, list):
        json_region_ids = region_ids

    else:
        json_region_ids = region_ids
    params["RegionIds"] = json_region_ids

    json_protection_status: list[str] | None | Unset
    if isinstance(protection_status, Unset):
        json_protection_status = UNSET
    elif isinstance(protection_status, list):
        json_protection_status = []
        for protection_status_type_0_item_data in protection_status:
            protection_status_type_0_item = protection_status_type_0_item_data.value
            json_protection_status.append(protection_status_type_0_item)

    else:
        json_protection_status = protection_status
    params["ProtectionStatus"] = json_protection_status

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

    params["DbFromProtectedRegions"] = db_from_protected_regions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/databases",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfDatabase.from_dict(response.json())

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
) -> Response[PageOfDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
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
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    credentials_state: CredentialsStateFilterOptions | Unset = UNSET,
    assignable_by_sql_account_id: int | None | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    protection_status: list[ProtectionStatus] | None | Unset = UNSET,
    backup_destination: list[SqlBackupDestinationFilterOptions] | None | Unset = UNSET,
    db_from_protected_regions: bool | Unset = UNSET,
) -> Response[PageOfDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of SQL Databases

     The HTTP GET request to the `/databases` endpoint retrieves all SQL databases that can be protected
    by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):
        search_pattern (None | str | Unset):
        credentials_state (CredentialsStateFilterOptions | Unset):
        assignable_by_sql_account_id (int | None | Unset):
        region_ids (list[str] | None | Unset):
        protection_status (list[ProtectionStatus] | None | Unset):
        backup_destination (list[SqlBackupDestinationFilterOptions] | None | Unset):
        db_from_protected_regions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        subscription_id=subscription_id,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
        search_pattern=search_pattern,
        credentials_state=credentials_state,
        assignable_by_sql_account_id=assignable_by_sql_account_id,
        region_ids=region_ids,
        protection_status=protection_status,
        backup_destination=backup_destination,
        db_from_protected_regions=db_from_protected_regions,
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
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    credentials_state: CredentialsStateFilterOptions | Unset = UNSET,
    assignable_by_sql_account_id: int | None | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    protection_status: list[ProtectionStatus] | None | Unset = UNSET,
    backup_destination: list[SqlBackupDestinationFilterOptions] | None | Unset = UNSET,
    db_from_protected_regions: bool | Unset = UNSET,
) -> PageOfDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of SQL Databases

     The HTTP GET request to the `/databases` endpoint retrieves all SQL databases that can be protected
    by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):
        search_pattern (None | str | Unset):
        credentials_state (CredentialsStateFilterOptions | Unset):
        assignable_by_sql_account_id (int | None | Unset):
        region_ids (list[str] | None | Unset):
        protection_status (list[ProtectionStatus] | None | Unset):
        backup_destination (list[SqlBackupDestinationFilterOptions] | None | Unset):
        db_from_protected_regions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        subscription_id=subscription_id,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
        search_pattern=search_pattern,
        credentials_state=credentials_state,
        assignable_by_sql_account_id=assignable_by_sql_account_id,
        region_ids=region_ids,
        protection_status=protection_status,
        backup_destination=backup_destination,
        db_from_protected_regions=db_from_protected_regions,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    credentials_state: CredentialsStateFilterOptions | Unset = UNSET,
    assignable_by_sql_account_id: int | None | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    protection_status: list[ProtectionStatus] | None | Unset = UNSET,
    backup_destination: list[SqlBackupDestinationFilterOptions] | None | Unset = UNSET,
    db_from_protected_regions: bool | Unset = UNSET,
) -> Response[PageOfDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of SQL Databases

     The HTTP GET request to the `/databases` endpoint retrieves all SQL databases that can be protected
    by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):
        search_pattern (None | str | Unset):
        credentials_state (CredentialsStateFilterOptions | Unset):
        assignable_by_sql_account_id (int | None | Unset):
        region_ids (list[str] | None | Unset):
        protection_status (list[ProtectionStatus] | None | Unset):
        backup_destination (list[SqlBackupDestinationFilterOptions] | None | Unset):
        db_from_protected_regions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        subscription_id=subscription_id,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
        search_pattern=search_pattern,
        credentials_state=credentials_state,
        assignable_by_sql_account_id=assignable_by_sql_account_id,
        region_ids=region_ids,
        protection_status=protection_status,
        backup_destination=backup_destination,
        db_from_protected_regions=db_from_protected_regions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    credentials_state: CredentialsStateFilterOptions | Unset = UNSET,
    assignable_by_sql_account_id: int | None | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    protection_status: list[ProtectionStatus] | None | Unset = UNSET,
    backup_destination: list[SqlBackupDestinationFilterOptions] | None | Unset = UNSET,
    db_from_protected_regions: bool | Unset = UNSET,
) -> PageOfDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of SQL Databases

     The HTTP GET request to the `/databases` endpoint retrieves all SQL databases that can be protected
    by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):
        search_pattern (None | str | Unset):
        credentials_state (CredentialsStateFilterOptions | Unset):
        assignable_by_sql_account_id (int | None | Unset):
        region_ids (list[str] | None | Unset):
        protection_status (list[ProtectionStatus] | None | Unset):
        backup_destination (list[SqlBackupDestinationFilterOptions] | None | Unset):
        db_from_protected_regions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            search_pattern=search_pattern,
            credentials_state=credentials_state,
            assignable_by_sql_account_id=assignable_by_sql_account_id,
            region_ids=region_ids,
            protection_status=protection_status,
            backup_destination=backup_destination,
            db_from_protected_regions=db_from_protected_regions,
        )
    ).parsed
