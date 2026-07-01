from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_azure_storage_item import PageOfAzureStorageItem
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    azure_storage_id: str,
    *,
    search_pattern: None | str | Unset = UNSET,
    account_id: UUID,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["searchPattern"] = json_search_pattern

    json_account_id = str(account_id)
    params["accountId"] = json_account_id

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/storageAccounts/{azure_storage_id}/containers".format(
            azure_storage_id=quote(str(azure_storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfAzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    if response.status_code == 200:
        response_200 = PageOfAzureStorageItem.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ProblemDetails404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfAzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    azure_storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    search_pattern: None | str | Unset = UNSET,
    account_id: UUID,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfAzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    """Get Collection of Blob Containers

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{azureStorageId}/containers`
    endpoint retrieves a list of blob containers that reside in the Azure storage account with the
    specified ID.

    Args:
        azure_storage_id (str):
        search_pattern (None | str | Unset):
        account_id (UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfAzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        azure_storage_id=azure_storage_id,
        search_pattern=search_pattern,
        account_id=account_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    azure_storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    search_pattern: None | str | Unset = UNSET,
    account_id: UUID,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfAzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    """Get Collection of Blob Containers

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{azureStorageId}/containers`
    endpoint retrieves a list of blob containers that reside in the Azure storage account with the
    specified ID.

    Args:
        azure_storage_id (str):
        search_pattern (None | str | Unset):
        account_id (UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfAzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        azure_storage_id=azure_storage_id,
        client=client,
        search_pattern=search_pattern,
        account_id=account_id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    azure_storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    search_pattern: None | str | Unset = UNSET,
    account_id: UUID,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfAzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    """Get Collection of Blob Containers

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{azureStorageId}/containers`
    endpoint retrieves a list of blob containers that reside in the Azure storage account with the
    specified ID.

    Args:
        azure_storage_id (str):
        search_pattern (None | str | Unset):
        account_id (UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfAzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        azure_storage_id=azure_storage_id,
        search_pattern=search_pattern,
        account_id=account_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    azure_storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    search_pattern: None | str | Unset = UNSET,
    account_id: UUID,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfAzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    """Get Collection of Blob Containers

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{azureStorageId}/containers`
    endpoint retrieves a list of blob containers that reside in the Azure storage account with the
    specified ID.

    Args:
        azure_storage_id (str):
        search_pattern (None | str | Unset):
        account_id (UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfAzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            azure_storage_id=azure_storage_id,
            client=client,
            search_pattern=search_pattern,
            account_id=account_id,
            offset=offset,
            limit=limit,
        )
    ).parsed
