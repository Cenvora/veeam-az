from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_veeam_vault_account_import_result import AsyncOperationOfVeeamVaultAccountImportResult
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_404 import ProblemDetails404
from ...models.problem_details_409 import ProblemDetails409
from ...models.problem_details_415 import ProblemDetails415
from ...models.veeam_vault_account_import import VeeamVaultAccountImport
from ...models.veeam_vault_account_import_result import VeeamVaultAccountImportResult
from ...types import Response


def _get_kwargs(
    *,
    body: VeeamVaultAccountImport,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/veeamVaults/importAccount",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfVeeamVaultAccountImportResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | VeeamVaultAccountImportResult
    | None
):
    if response.status_code == 200:
        response_200 = VeeamVaultAccountImportResult.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfVeeamVaultAccountImportResult.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ProblemDetails404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ProblemDetails409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = ProblemDetails415.from_dict(response.json())

        return response_415

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AsyncOperationOfVeeamVaultAccountImportResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | VeeamVaultAccountImportResult
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
    body: VeeamVaultAccountImport,
) -> Response[
    AsyncOperationOfVeeamVaultAccountImportResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | VeeamVaultAccountImportResult
]:
    """Import Storage Vault Data

     The HTTP POST request to the `/veeamVaults/importAccount` endpoint imports data of a specific
    storage vault from Veeam Data Cloud to the Veeam Backup for Microsoft Azure configuration database.
    You can then use the imported data as an input in the HTTP POST request to the [Add Backup
    Repository](#tag/Repository/operation/Repository_CreateRepository) endpoint.

    Args:
        body (VeeamVaultAccountImport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfVeeamVaultAccountImportResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | VeeamVaultAccountImportResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: VeeamVaultAccountImport,
) -> (
    AsyncOperationOfVeeamVaultAccountImportResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | VeeamVaultAccountImportResult
    | None
):
    """Import Storage Vault Data

     The HTTP POST request to the `/veeamVaults/importAccount` endpoint imports data of a specific
    storage vault from Veeam Data Cloud to the Veeam Backup for Microsoft Azure configuration database.
    You can then use the imported data as an input in the HTTP POST request to the [Add Backup
    Repository](#tag/Repository/operation/Repository_CreateRepository) endpoint.

    Args:
        body (VeeamVaultAccountImport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfVeeamVaultAccountImportResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | VeeamVaultAccountImportResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VeeamVaultAccountImport,
) -> Response[
    AsyncOperationOfVeeamVaultAccountImportResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | VeeamVaultAccountImportResult
]:
    """Import Storage Vault Data

     The HTTP POST request to the `/veeamVaults/importAccount` endpoint imports data of a specific
    storage vault from Veeam Data Cloud to the Veeam Backup for Microsoft Azure configuration database.
    You can then use the imported data as an input in the HTTP POST request to the [Add Backup
    Repository](#tag/Repository/operation/Repository_CreateRepository) endpoint.

    Args:
        body (VeeamVaultAccountImport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfVeeamVaultAccountImportResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | VeeamVaultAccountImportResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: VeeamVaultAccountImport,
) -> (
    AsyncOperationOfVeeamVaultAccountImportResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | VeeamVaultAccountImportResult
    | None
):
    """Import Storage Vault Data

     The HTTP POST request to the `/veeamVaults/importAccount` endpoint imports data of a specific
    storage vault from Veeam Data Cloud to the Veeam Backup for Microsoft Azure configuration database.
    You can then use the imported data as an input in the HTTP POST request to the [Add Backup
    Repository](#tag/Repository/operation/Repository_CreateRepository) endpoint.

    Args:
        body (VeeamVaultAccountImport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfVeeamVaultAccountImportResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | VeeamVaultAccountImportResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
