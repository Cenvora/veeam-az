from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_nullable_storage_account import AsyncOperationOfNullableStorageAccount
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.storage_account import StorageAccount
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_account_id: str,
    *,
    sync: bool | None | Unset = UNSET,
    service_account_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sync: bool | None | Unset
    if isinstance(sync, Unset):
        json_sync = UNSET
    else:
        json_sync = sync
    params["sync"] = json_sync

    json_service_account_id: None | str | Unset
    if isinstance(service_account_id, Unset):
        json_service_account_id = UNSET
    else:
        json_service_account_id = service_account_id
    params["serviceAccountId"] = json_service_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/storageAccounts/{storage_account_id}".format(
            storage_account_id=quote(str(storage_account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfNullableStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccount
    | None
):
    if response.status_code == 200:
        response_200 = StorageAccount.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfNullableStorageAccount.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ProblemDetails404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AsyncOperationOfNullableStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccount
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
    service_account_id: None | str | Unset = UNSET,
) -> Response[
    AsyncOperationOfNullableStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccount
]:
    """Get Storage Account Data

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{storageAccountId}` endpoint
    retrieves information on Azure storage account with the specified ID.

    Args:
        storage_account_id (str):
        sync (bool | None | Unset):
        service_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfNullableStorageAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | StorageAccount]
    """

    kwargs = _get_kwargs(
        storage_account_id=storage_account_id,
        sync=sync,
        service_account_id=service_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
    service_account_id: None | str | Unset = UNSET,
) -> (
    AsyncOperationOfNullableStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccount
    | None
):
    """Get Storage Account Data

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{storageAccountId}` endpoint
    retrieves information on Azure storage account with the specified ID.

    Args:
        storage_account_id (str):
        sync (bool | None | Unset):
        service_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfNullableStorageAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | StorageAccount
    """

    return sync_detailed(
        storage_account_id=storage_account_id,
        client=client,
        sync=sync,
        service_account_id=service_account_id,
    ).parsed


async def asyncio_detailed(
    storage_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
    service_account_id: None | str | Unset = UNSET,
) -> Response[
    AsyncOperationOfNullableStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccount
]:
    """Get Storage Account Data

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{storageAccountId}` endpoint
    retrieves information on Azure storage account with the specified ID.

    Args:
        storage_account_id (str):
        sync (bool | None | Unset):
        service_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfNullableStorageAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | StorageAccount]
    """

    kwargs = _get_kwargs(
        storage_account_id=storage_account_id,
        sync=sync,
        service_account_id=service_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
    service_account_id: None | str | Unset = UNSET,
) -> (
    AsyncOperationOfNullableStorageAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccount
    | None
):
    """Get Storage Account Data

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{storageAccountId}` endpoint
    retrieves information on Azure storage account with the specified ID.

    Args:
        storage_account_id (str):
        sync (bool | None | Unset):
        service_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfNullableStorageAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | StorageAccount
    """

    return (
        await asyncio_detailed(
            storage_account_id=storage_account_id,
            client=client,
            sync=sync,
            service_account_id=service_account_id,
        )
    ).parsed
