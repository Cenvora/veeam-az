from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.azure_storage_item import AzureStorageItem
from ...models.azure_storage_item_creation_config import AzureStorageItemCreationConfig
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.problem_details_409 import ProblemDetails409
from ...types import Response


def _get_kwargs(
    azure_storage_id: str,
    *,
    body: AzureStorageItemCreationConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/cloudInfrastructure/storageAccounts/{azure_storage_id}/containers".format(
            azure_storage_id=quote(str(azure_storage_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AzureStorageItem
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | None
):
    if response.status_code == 201:
        response_201 = AzureStorageItem.from_dict(response.json())

        return response_201

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

    if response.status_code == 409:
        response_409 = ProblemDetails409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409
]:
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
    body: AzureStorageItemCreationConfig,
) -> Response[
    AzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409
]:
    """Create Blob Container in Storage Account

     The HTTP POST request to the `/cloudInfrastructure/storageAccounts/{azureStorageId}/containers`
    endpoint creates a new blob container in a storage account with the specified ID.

    Args:
        azure_storage_id (str):
        body (AzureStorageItemCreationConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409]
    """

    kwargs = _get_kwargs(
        azure_storage_id=azure_storage_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    azure_storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AzureStorageItemCreationConfig,
) -> (
    AzureStorageItem
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | None
):
    """Create Blob Container in Storage Account

     The HTTP POST request to the `/cloudInfrastructure/storageAccounts/{azureStorageId}/containers`
    endpoint creates a new blob container in a storage account with the specified ID.

    Args:
        azure_storage_id (str):
        body (AzureStorageItemCreationConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409
    """

    return sync_detailed(
        azure_storage_id=azure_storage_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    azure_storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AzureStorageItemCreationConfig,
) -> Response[
    AzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409
]:
    """Create Blob Container in Storage Account

     The HTTP POST request to the `/cloudInfrastructure/storageAccounts/{azureStorageId}/containers`
    endpoint creates a new blob container in a storage account with the specified ID.

    Args:
        azure_storage_id (str):
        body (AzureStorageItemCreationConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409]
    """

    kwargs = _get_kwargs(
        azure_storage_id=azure_storage_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    azure_storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AzureStorageItemCreationConfig,
) -> (
    AzureStorageItem
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | None
):
    """Create Blob Container in Storage Account

     The HTTP POST request to the `/cloudInfrastructure/storageAccounts/{azureStorageId}/containers`
    endpoint creates a new blob container in a storage account with the specified ID.

    Args:
        azure_storage_id (str):
        body (AzureStorageItemCreationConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AzureStorageItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409
    """

    return (
        await asyncio_detailed(
            azure_storage_id=azure_storage_id,
            client=client,
            body=body,
        )
    ).parsed
