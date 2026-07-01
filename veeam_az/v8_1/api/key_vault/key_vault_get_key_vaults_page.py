from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_page_of_key_vault import AsyncOperationOfPageOfKeyVault
from ...models.page_of_key_vault import PageOfKeyVault
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    json_region_ids: list[str] | None | Unset
    if isinstance(region_ids, Unset):
        json_region_ids = UNSET
    elif isinstance(region_ids, list):
        json_region_ids = region_ids

    else:
        json_region_ids = region_ids
    params["RegionIds"] = json_region_ids

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["SearchPattern"] = json_search_pattern

    json_sync: bool | None | Unset
    if isinstance(sync, Unset):
        json_sync = UNSET
    else:
        json_sync = sync
    params["Sync"] = json_sync

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/keyVaults",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AsyncOperationOfPageOfKeyVault | PageOfKeyVault | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfKeyVault.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfPageOfKeyVault.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AsyncOperationOfPageOfKeyVault | PageOfKeyVault | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
]:
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
    region_ids: list[str] | None | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfKeyVault | PageOfKeyVault | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
]:
    """Get Collection of Key Vaults

     The HTTP GET request to the `/cloudInfrastructure/keyVaults` endpoint retrieves a list of Key Vaults
    available for Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        region_ids (list[str] | None | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfKeyVault | PageOfKeyVault | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        region_ids=region_ids,
        search_pattern=search_pattern,
        sync=sync,
        subscription_id=subscription_id,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
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
    region_ids: list[str] | None | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> AsyncOperationOfPageOfKeyVault | PageOfKeyVault | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Key Vaults

     The HTTP GET request to the `/cloudInfrastructure/keyVaults` endpoint retrieves a list of Key Vaults
    available for Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        region_ids (list[str] | None | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfKeyVault | PageOfKeyVault | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        region_ids=region_ids,
        search_pattern=search_pattern,
        sync=sync,
        subscription_id=subscription_id,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfKeyVault | PageOfKeyVault | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
]:
    """Get Collection of Key Vaults

     The HTTP GET request to the `/cloudInfrastructure/keyVaults` endpoint retrieves a list of Key Vaults
    available for Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        region_ids (list[str] | None | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfKeyVault | PageOfKeyVault | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        region_ids=region_ids,
        search_pattern=search_pattern,
        sync=sync,
        subscription_id=subscription_id,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> AsyncOperationOfPageOfKeyVault | PageOfKeyVault | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Key Vaults

     The HTTP GET request to the `/cloudInfrastructure/keyVaults` endpoint retrieves a list of Key Vaults
    available for Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        region_ids (list[str] | None | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfKeyVault | PageOfKeyVault | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            region_ids=region_ids,
            search_pattern=search_pattern,
            sync=sync,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
        )
    ).parsed
