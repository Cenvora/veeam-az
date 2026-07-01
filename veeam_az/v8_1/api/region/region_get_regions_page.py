from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_page_of_region import AsyncOperationOfPageOfRegion
from ...models.page_of_region import PageOfRegion
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.resource_provider_type import ResourceProviderType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: UUID | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    resource_provider_types: list[ResourceProviderType] | None | Unset = UNSET,
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

    json_service_account_id: str | Unset = UNSET
    if not isinstance(service_account_id, Unset):
        json_service_account_id = str(service_account_id)
    params["ServiceAccountId"] = json_service_account_id

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

    json_resource_provider_types: list[str] | None | Unset
    if isinstance(resource_provider_types, Unset):
        json_resource_provider_types = UNSET
    elif isinstance(resource_provider_types, list):
        json_resource_provider_types = []
        for resource_provider_types_type_0_item_data in resource_provider_types:
            resource_provider_types_type_0_item = resource_provider_types_type_0_item_data.value
            json_resource_provider_types.append(resource_provider_types_type_0_item)

    else:
        json_resource_provider_types = resource_provider_types
    params["ResourceProviderTypes"] = json_resource_provider_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/regions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AsyncOperationOfPageOfRegion | PageOfRegion | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfRegion.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfPageOfRegion.from_dict(response.json())

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
) -> Response[AsyncOperationOfPageOfRegion | PageOfRegion | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
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
    service_account_id: UUID | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    resource_provider_types: list[ResourceProviderType] | None | Unset = UNSET,
) -> Response[AsyncOperationOfPageOfRegion | PageOfRegion | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Azure Regions

     The HTTP GET request to the `/cloudInfrastructure/regions` endpoint retrieves a list of Azure
    regions available in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (UUID | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        resource_provider_types (list[ResourceProviderType] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfRegion | PageOfRegion | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        subscription_id=subscription_id,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
        search_pattern=search_pattern,
        sync=sync,
        resource_provider_types=resource_provider_types,
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
    service_account_id: UUID | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    resource_provider_types: list[ResourceProviderType] | None | Unset = UNSET,
) -> AsyncOperationOfPageOfRegion | PageOfRegion | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Azure Regions

     The HTTP GET request to the `/cloudInfrastructure/regions` endpoint retrieves a list of Azure
    regions available in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (UUID | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        resource_provider_types (list[ResourceProviderType] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfRegion | PageOfRegion | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        subscription_id=subscription_id,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
        search_pattern=search_pattern,
        sync=sync,
        resource_provider_types=resource_provider_types,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: UUID | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    resource_provider_types: list[ResourceProviderType] | None | Unset = UNSET,
) -> Response[AsyncOperationOfPageOfRegion | PageOfRegion | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Azure Regions

     The HTTP GET request to the `/cloudInfrastructure/regions` endpoint retrieves a list of Azure
    regions available in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (UUID | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        resource_provider_types (list[ResourceProviderType] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfRegion | PageOfRegion | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        subscription_id=subscription_id,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
        search_pattern=search_pattern,
        sync=sync,
        resource_provider_types=resource_provider_types,
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
    service_account_id: UUID | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    resource_provider_types: list[ResourceProviderType] | None | Unset = UNSET,
) -> AsyncOperationOfPageOfRegion | PageOfRegion | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Azure Regions

     The HTTP GET request to the `/cloudInfrastructure/regions` endpoint retrieves a list of Azure
    regions available in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        subscription_id (None | Unset | UUID):
        tenant_id (None | Unset | UUID):
        service_account_id (UUID | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        resource_provider_types (list[ResourceProviderType] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfRegion | PageOfRegion | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
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
            sync=sync,
            resource_provider_types=resource_provider_types,
        )
    ).parsed
