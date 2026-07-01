from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_repository import PageOfRepository
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_409 import ProblemDetails409
from ...models.repository_status import RepositoryStatus
from ...models.repository_type import RepositoryType
from ...models.storage_tier import StorageTier
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: list[RepositoryStatus] | None | Unset = UNSET,
    type_: list[RepositoryType] | None | Unset = UNSET,
    tier: list[StorageTier] | None | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    is_encrypted: bool | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
    immutability_enabled: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: list[str] | None | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, list):
        json_status = []
        for status_type_0_item_data in status:
            status_type_0_item = status_type_0_item_data.value
            json_status.append(status_type_0_item)

    else:
        json_status = status
    params["Status"] = json_status

    json_type_: list[str] | None | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, list):
        json_type_ = []
        for type_type_0_item_data in type_:
            type_type_0_item = type_type_0_item_data.value
            json_type_.append(type_type_0_item)

    else:
        json_type_ = type_
    params["Type"] = json_type_

    json_tier: list[str] | None | Unset
    if isinstance(tier, Unset):
        json_tier = UNSET
    elif isinstance(tier, list):
        json_tier = []
        for tier_type_0_item_data in tier:
            tier_type_0_item = tier_type_0_item_data.value
            json_tier.append(tier_type_0_item)

    else:
        json_tier = tier
    params["Tier"] = json_tier

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["SearchPattern"] = json_search_pattern

    json_is_encrypted: bool | None | Unset
    if isinstance(is_encrypted, Unset):
        json_is_encrypted = UNSET
    else:
        json_is_encrypted = is_encrypted
    params["IsEncrypted"] = json_is_encrypted

    params["Offset"] = offset

    params["Limit"] = limit

    json_tenant_id: None | str | Unset
    if isinstance(tenant_id, Unset):
        json_tenant_id = UNSET
    elif isinstance(tenant_id, UUID):
        json_tenant_id = str(tenant_id)
    else:
        json_tenant_id = tenant_id
    params["TenantId"] = json_tenant_id

    params["ServiceAccountId"] = service_account_id

    json_immutability_enabled: bool | None | Unset
    if isinstance(immutability_enabled, Unset):
        json_immutability_enabled = UNSET
    else:
        json_immutability_enabled = immutability_enabled
    params["ImmutabilityEnabled"] = json_immutability_enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/repositories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRepository | ProblemDetails400 | ProblemDetails401 | ProblemDetails409 | None:
    if response.status_code == 200:
        response_200 = PageOfRepository.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = ProblemDetails409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRepository | ProblemDetails400 | ProblemDetails401 | ProblemDetails409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: list[RepositoryStatus] | None | Unset = UNSET,
    type_: list[RepositoryType] | None | Unset = UNSET,
    tier: list[StorageTier] | None | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    is_encrypted: bool | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
    immutability_enabled: bool | None | Unset = UNSET,
) -> Response[PageOfRepository | ProblemDetails400 | ProblemDetails401 | ProblemDetails409]:
    """Get Collection of Backup Repositories

     The HTTP GET request to the `/repositories` endpoint retrieves a list of backup repositories added
    to the Veeam Backup for Microsoft Azure configuration database.

    Args:
        status (list[RepositoryStatus] | None | Unset):
        type_ (list[RepositoryType] | None | Unset):
        tier (list[StorageTier] | None | Unset):
        search_pattern (None | str | Unset):
        is_encrypted (bool | None | Unset):
        offset (int | Unset):
        limit (int | Unset):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):
        immutability_enabled (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRepository | ProblemDetails400 | ProblemDetails401 | ProblemDetails409]
    """

    kwargs = _get_kwargs(
        status=status,
        type_=type_,
        tier=tier,
        search_pattern=search_pattern,
        is_encrypted=is_encrypted,
        offset=offset,
        limit=limit,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
        immutability_enabled=immutability_enabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: list[RepositoryStatus] | None | Unset = UNSET,
    type_: list[RepositoryType] | None | Unset = UNSET,
    tier: list[StorageTier] | None | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    is_encrypted: bool | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
    immutability_enabled: bool | None | Unset = UNSET,
) -> PageOfRepository | ProblemDetails400 | ProblemDetails401 | ProblemDetails409 | None:
    """Get Collection of Backup Repositories

     The HTTP GET request to the `/repositories` endpoint retrieves a list of backup repositories added
    to the Veeam Backup for Microsoft Azure configuration database.

    Args:
        status (list[RepositoryStatus] | None | Unset):
        type_ (list[RepositoryType] | None | Unset):
        tier (list[StorageTier] | None | Unset):
        search_pattern (None | str | Unset):
        is_encrypted (bool | None | Unset):
        offset (int | Unset):
        limit (int | Unset):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):
        immutability_enabled (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRepository | ProblemDetails400 | ProblemDetails401 | ProblemDetails409
    """

    return sync_detailed(
        client=client,
        status=status,
        type_=type_,
        tier=tier,
        search_pattern=search_pattern,
        is_encrypted=is_encrypted,
        offset=offset,
        limit=limit,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
        immutability_enabled=immutability_enabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: list[RepositoryStatus] | None | Unset = UNSET,
    type_: list[RepositoryType] | None | Unset = UNSET,
    tier: list[StorageTier] | None | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    is_encrypted: bool | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
    immutability_enabled: bool | None | Unset = UNSET,
) -> Response[PageOfRepository | ProblemDetails400 | ProblemDetails401 | ProblemDetails409]:
    """Get Collection of Backup Repositories

     The HTTP GET request to the `/repositories` endpoint retrieves a list of backup repositories added
    to the Veeam Backup for Microsoft Azure configuration database.

    Args:
        status (list[RepositoryStatus] | None | Unset):
        type_ (list[RepositoryType] | None | Unset):
        tier (list[StorageTier] | None | Unset):
        search_pattern (None | str | Unset):
        is_encrypted (bool | None | Unset):
        offset (int | Unset):
        limit (int | Unset):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):
        immutability_enabled (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRepository | ProblemDetails400 | ProblemDetails401 | ProblemDetails409]
    """

    kwargs = _get_kwargs(
        status=status,
        type_=type_,
        tier=tier,
        search_pattern=search_pattern,
        is_encrypted=is_encrypted,
        offset=offset,
        limit=limit,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
        immutability_enabled=immutability_enabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: list[RepositoryStatus] | None | Unset = UNSET,
    type_: list[RepositoryType] | None | Unset = UNSET,
    tier: list[StorageTier] | None | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    is_encrypted: bool | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
    immutability_enabled: bool | None | Unset = UNSET,
) -> PageOfRepository | ProblemDetails400 | ProblemDetails401 | ProblemDetails409 | None:
    """Get Collection of Backup Repositories

     The HTTP GET request to the `/repositories` endpoint retrieves a list of backup repositories added
    to the Veeam Backup for Microsoft Azure configuration database.

    Args:
        status (list[RepositoryStatus] | None | Unset):
        type_ (list[RepositoryType] | None | Unset):
        tier (list[StorageTier] | None | Unset):
        search_pattern (None | str | Unset):
        is_encrypted (bool | None | Unset):
        offset (int | Unset):
        limit (int | Unset):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):
        immutability_enabled (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRepository | ProblemDetails400 | ProblemDetails401 | ProblemDetails409
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            type_=type_,
            tier=tier,
            search_pattern=search_pattern,
            is_encrypted=is_encrypted,
            offset=offset,
            limit=limit,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            immutability_enabled=immutability_enabled,
        )
    ).parsed
