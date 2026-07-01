from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_nullable_storage_account_capabilities import (
    AsyncOperationOfNullableStorageAccountCapabilities,
)
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.storage_account_capabilities import StorageAccountCapabilities
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_account_id: str,
    *,
    account_id: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_account_id: None | str | Unset
    if isinstance(account_id, Unset):
        json_account_id = UNSET
    else:
        json_account_id = account_id
    params["accountId"] = json_account_id

    json_sync: bool | None | Unset
    if isinstance(sync, Unset):
        json_sync = UNSET
    else:
        json_sync = sync
    params["sync"] = json_sync

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/storageAccounts/{storage_account_id}/capabilities".format(
            storage_account_id=quote(str(storage_account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfNullableStorageAccountCapabilities
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccountCapabilities
    | None
):
    if response.status_code == 200:
        response_200 = StorageAccountCapabilities.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfNullableStorageAccountCapabilities.from_dict(response.json())

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
    AsyncOperationOfNullableStorageAccountCapabilities
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccountCapabilities
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
    account_id: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfNullableStorageAccountCapabilities
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccountCapabilities
]:
    """Get Storage Account Capabilities

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{storageAccountId}/capabilities`
    endpoint verifies whether a specific storage account supports archive tier.

    Args:
        storage_account_id (str):
        account_id (None | str | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfNullableStorageAccountCapabilities | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | StorageAccountCapabilities]
    """

    kwargs = _get_kwargs(
        storage_account_id=storage_account_id,
        account_id=account_id,
        sync=sync,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfNullableStorageAccountCapabilities
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccountCapabilities
    | None
):
    """Get Storage Account Capabilities

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{storageAccountId}/capabilities`
    endpoint verifies whether a specific storage account supports archive tier.

    Args:
        storage_account_id (str):
        account_id (None | str | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfNullableStorageAccountCapabilities | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | StorageAccountCapabilities
    """

    return sync_detailed(
        storage_account_id=storage_account_id,
        client=client,
        account_id=account_id,
        sync=sync,
    ).parsed


async def asyncio_detailed(
    storage_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfNullableStorageAccountCapabilities
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccountCapabilities
]:
    """Get Storage Account Capabilities

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{storageAccountId}/capabilities`
    endpoint verifies whether a specific storage account supports archive tier.

    Args:
        storage_account_id (str):
        account_id (None | str | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfNullableStorageAccountCapabilities | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | StorageAccountCapabilities]
    """

    kwargs = _get_kwargs(
        storage_account_id=storage_account_id,
        account_id=account_id,
        sync=sync,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfNullableStorageAccountCapabilities
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | StorageAccountCapabilities
    | None
):
    """Get Storage Account Capabilities

     The HTTP GET request to the `/cloudInfrastructure/storageAccounts/{storageAccountId}/capabilities`
    endpoint verifies whether a specific storage account supports archive tier.

    Args:
        storage_account_id (str):
        account_id (None | str | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfNullableStorageAccountCapabilities | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | StorageAccountCapabilities
    """

    return (
        await asyncio_detailed(
            storage_account_id=storage_account_id,
            client=client,
            account_id=account_id,
            sync=sync,
        )
    ).parsed
