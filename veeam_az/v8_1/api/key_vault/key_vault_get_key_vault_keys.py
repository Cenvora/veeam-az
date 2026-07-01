from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_page_of_key_vault_key import AsyncOperationOfPageOfKeyVaultKey
from ...models.page_of_key_vault_key import PageOfKeyVaultKey
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key_vault_id: str,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    service_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["SearchPattern"] = json_search_pattern

    json_service_account_id: str | Unset = UNSET
    if not isinstance(service_account_id, Unset):
        json_service_account_id = str(service_account_id)
    params["ServiceAccountId"] = json_service_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/keyVaults/{key_vault_id}/keys".format(
            key_vault_id=quote(str(key_vault_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfPageOfKeyVaultKey
    | PageOfKeyVaultKey
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    if response.status_code == 200:
        response_200 = PageOfKeyVaultKey.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfPageOfKeyVaultKey.from_dict(response.json())

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
    AsyncOperationOfPageOfKeyVaultKey
    | PageOfKeyVaultKey
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_vault_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    service_account_id: UUID | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfKeyVaultKey
    | PageOfKeyVaultKey
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
]:
    """Get Collection of Keys

     The HTTP GET request to the `/cloudInfrastructure/keyVaults/{keyVaultId}/keys` endpoint retrieves a
    list of cryptographic keys stored in a Key Vault with the specified ID.

    Args:
        key_vault_id (str):
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        service_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfKeyVaultKey | PageOfKeyVaultKey | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        key_vault_id=key_vault_id,
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
        service_account_id=service_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_vault_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    service_account_id: UUID | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfKeyVaultKey
    | PageOfKeyVaultKey
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Get Collection of Keys

     The HTTP GET request to the `/cloudInfrastructure/keyVaults/{keyVaultId}/keys` endpoint retrieves a
    list of cryptographic keys stored in a Key Vault with the specified ID.

    Args:
        key_vault_id (str):
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        service_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfKeyVaultKey | PageOfKeyVaultKey | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        key_vault_id=key_vault_id,
        client=client,
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
        service_account_id=service_account_id,
    ).parsed


async def asyncio_detailed(
    key_vault_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    service_account_id: UUID | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfKeyVaultKey
    | PageOfKeyVaultKey
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
]:
    """Get Collection of Keys

     The HTTP GET request to the `/cloudInfrastructure/keyVaults/{keyVaultId}/keys` endpoint retrieves a
    list of cryptographic keys stored in a Key Vault with the specified ID.

    Args:
        key_vault_id (str):
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        service_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfKeyVaultKey | PageOfKeyVaultKey | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        key_vault_id=key_vault_id,
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
        service_account_id=service_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_vault_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    service_account_id: UUID | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfKeyVaultKey
    | PageOfKeyVaultKey
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Get Collection of Keys

     The HTTP GET request to the `/cloudInfrastructure/keyVaults/{keyVaultId}/keys` endpoint retrieves a
    list of cryptographic keys stored in a Key Vault with the specified ID.

    Args:
        key_vault_id (str):
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        service_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfKeyVaultKey | PageOfKeyVaultKey | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            key_vault_id=key_vault_id,
            client=client,
            offset=offset,
            limit=limit,
            search_pattern=search_pattern,
            service_account_id=service_account_id,
        )
    ).parsed
