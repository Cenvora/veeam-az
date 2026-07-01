from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_page_of_storage_account import AsyncOperationOfPageOfStorageAccount
from ...models.page_of_storage_account import PageOfStorageAccount
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    subscription_id: None | Unset | UUID = UNSET,
    account_id: None | str | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    name: None | str | Unset = UNSET,
    resource_group_name: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    repository_compatible: bool | Unset = False,
    vhd_compatible: bool | Unset = False,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    service_account_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_subscription_id: None | str | Unset
    if isinstance(subscription_id, Unset):
        json_subscription_id = UNSET
    elif isinstance(subscription_id, UUID):
        json_subscription_id = str(subscription_id)
    else:
        json_subscription_id = subscription_id
    params["subscriptionId"] = json_subscription_id

    json_account_id: None | str | Unset
    if isinstance(account_id, Unset):
        json_account_id = UNSET
    else:
        json_account_id = account_id
    params["accountId"] = json_account_id

    json_region_ids: list[str] | None | Unset
    if isinstance(region_ids, Unset):
        json_region_ids = UNSET
    elif isinstance(region_ids, list):
        json_region_ids = region_ids

    else:
        json_region_ids = region_ids
    params["regionIds"] = json_region_ids

    json_name: None | str | Unset
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    json_resource_group_name: None | str | Unset
    if isinstance(resource_group_name, Unset):
        json_resource_group_name = UNSET
    else:
        json_resource_group_name = resource_group_name
    params["resourceGroupName"] = json_resource_group_name

    json_sync: bool | None | Unset
    if isinstance(sync, Unset):
        json_sync = UNSET
    else:
        json_sync = sync
    params["sync"] = json_sync

    params["repositoryCompatible"] = repository_compatible

    params["vhdCompatible"] = vhd_compatible

    params["offset"] = offset

    params["limit"] = limit

    json_service_account_id: None | str | Unset
    if isinstance(service_account_id, Unset):
        json_service_account_id = UNSET
    else:
        json_service_account_id = service_account_id
    params["serviceAccountId"] = json_service_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/storageAccounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfPageOfStorageAccount
    | PageOfStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    if response.status_code == 200:
        response_200 = PageOfStorageAccount.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfPageOfStorageAccount.from_dict(response.json())

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
    AsyncOperationOfPageOfStorageAccount
    | PageOfStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
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
    subscription_id: None | Unset | UUID = UNSET,
    account_id: None | str | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    name: None | str | Unset = UNSET,
    resource_group_name: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    repository_compatible: bool | Unset = False,
    vhd_compatible: bool | Unset = False,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    service_account_id: None | str | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfStorageAccount
    | PageOfStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
]:
    """Get Collection of Storage Accounts

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts` endpoint retrieves a list of
    Azure storage accounts to which Veeam Backup for Microsoft Azure has permissions.

    Args:
        subscription_id (None | Unset | UUID):
        account_id (None | str | Unset):
        region_ids (list[str] | None | Unset):
        name (None | str | Unset):
        resource_group_name (None | str | Unset):
        sync (bool | None | Unset):
        repository_compatible (bool | Unset):  Default: False.
        vhd_compatible (bool | Unset):  Default: False.
        offset (int | Unset):
        limit (int | Unset):
        service_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfStorageAccount | PageOfStorageAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        account_id=account_id,
        region_ids=region_ids,
        name=name,
        resource_group_name=resource_group_name,
        sync=sync,
        repository_compatible=repository_compatible,
        vhd_compatible=vhd_compatible,
        offset=offset,
        limit=limit,
        service_account_id=service_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    subscription_id: None | Unset | UUID = UNSET,
    account_id: None | str | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    name: None | str | Unset = UNSET,
    resource_group_name: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    repository_compatible: bool | Unset = False,
    vhd_compatible: bool | Unset = False,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    service_account_id: None | str | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfStorageAccount
    | PageOfStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Collection of Storage Accounts

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts` endpoint retrieves a list of
    Azure storage accounts to which Veeam Backup for Microsoft Azure has permissions.

    Args:
        subscription_id (None | Unset | UUID):
        account_id (None | str | Unset):
        region_ids (list[str] | None | Unset):
        name (None | str | Unset):
        resource_group_name (None | str | Unset):
        sync (bool | None | Unset):
        repository_compatible (bool | Unset):  Default: False.
        vhd_compatible (bool | Unset):  Default: False.
        offset (int | Unset):
        limit (int | Unset):
        service_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfStorageAccount | PageOfStorageAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        subscription_id=subscription_id,
        account_id=account_id,
        region_ids=region_ids,
        name=name,
        resource_group_name=resource_group_name,
        sync=sync,
        repository_compatible=repository_compatible,
        vhd_compatible=vhd_compatible,
        offset=offset,
        limit=limit,
        service_account_id=service_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    subscription_id: None | Unset | UUID = UNSET,
    account_id: None | str | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    name: None | str | Unset = UNSET,
    resource_group_name: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    repository_compatible: bool | Unset = False,
    vhd_compatible: bool | Unset = False,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    service_account_id: None | str | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfStorageAccount
    | PageOfStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
]:
    """Get Collection of Storage Accounts

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts` endpoint retrieves a list of
    Azure storage accounts to which Veeam Backup for Microsoft Azure has permissions.

    Args:
        subscription_id (None | Unset | UUID):
        account_id (None | str | Unset):
        region_ids (list[str] | None | Unset):
        name (None | str | Unset):
        resource_group_name (None | str | Unset):
        sync (bool | None | Unset):
        repository_compatible (bool | Unset):  Default: False.
        vhd_compatible (bool | Unset):  Default: False.
        offset (int | Unset):
        limit (int | Unset):
        service_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfStorageAccount | PageOfStorageAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        account_id=account_id,
        region_ids=region_ids,
        name=name,
        resource_group_name=resource_group_name,
        sync=sync,
        repository_compatible=repository_compatible,
        vhd_compatible=vhd_compatible,
        offset=offset,
        limit=limit,
        service_account_id=service_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    subscription_id: None | Unset | UUID = UNSET,
    account_id: None | str | Unset = UNSET,
    region_ids: list[str] | None | Unset = UNSET,
    name: None | str | Unset = UNSET,
    resource_group_name: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    repository_compatible: bool | Unset = False,
    vhd_compatible: bool | Unset = False,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    service_account_id: None | str | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfStorageAccount
    | PageOfStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Collection of Storage Accounts

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts` endpoint retrieves a list of
    Azure storage accounts to which Veeam Backup for Microsoft Azure has permissions.

    Args:
        subscription_id (None | Unset | UUID):
        account_id (None | str | Unset):
        region_ids (list[str] | None | Unset):
        name (None | str | Unset):
        resource_group_name (None | str | Unset):
        sync (bool | None | Unset):
        repository_compatible (bool | Unset):  Default: False.
        vhd_compatible (bool | Unset):  Default: False.
        offset (int | Unset):
        limit (int | Unset):
        service_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfStorageAccount | PageOfStorageAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            subscription_id=subscription_id,
            account_id=account_id,
            region_ids=region_ids,
            name=name,
            resource_group_name=resource_group_name,
            sync=sync,
            repository_compatible=repository_compatible,
            vhd_compatible=vhd_compatible,
            offset=offset,
            limit=limit,
            service_account_id=service_account_id,
        )
    ).parsed
