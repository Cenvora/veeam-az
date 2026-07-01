from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_protected_cosmos_db_account import AsyncOperationOfProtectedCosmosDbAccount
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.protected_cosmos_db_account import ProtectedCosmosDbAccount
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cosmos_db_account_id: str,
    *,
    sync: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sync: bool | None | Unset
    if isinstance(sync, Unset):
        json_sync = UNSET
    else:
        json_sync = sync
    params["Sync"] = json_sync

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/protectedItem/cosmosDb/{cosmos_db_account_id}".format(
            cosmos_db_account_id=quote(str(cosmos_db_account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfProtectedCosmosDbAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProtectedCosmosDbAccount
    | None
):
    if response.status_code == 200:
        response_200 = ProtectedCosmosDbAccount.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfProtectedCosmosDbAccount.from_dict(response.json())

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
    AsyncOperationOfProtectedCosmosDbAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProtectedCosmosDbAccount
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfProtectedCosmosDbAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProtectedCosmosDbAccount
]:
    """Get Protected Cosmos DB Account Data

     The HTTP GET request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}` endpoint retrieves
    information on a protected Cosmos DB account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfProtectedCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedCosmosDbAccount]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        sync=sync,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfProtectedCosmosDbAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProtectedCosmosDbAccount
    | None
):
    """Get Protected Cosmos DB Account Data

     The HTTP GET request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}` endpoint retrieves
    information on a protected Cosmos DB account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfProtectedCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedCosmosDbAccount
    """

    return sync_detailed(
        cosmos_db_account_id=cosmos_db_account_id,
        client=client,
        sync=sync,
    ).parsed


async def asyncio_detailed(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfProtectedCosmosDbAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProtectedCosmosDbAccount
]:
    """Get Protected Cosmos DB Account Data

     The HTTP GET request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}` endpoint retrieves
    information on a protected Cosmos DB account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfProtectedCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedCosmosDbAccount]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        sync=sync,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfProtectedCosmosDbAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProtectedCosmosDbAccount
    | None
):
    """Get Protected Cosmos DB Account Data

     The HTTP GET request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}` endpoint retrieves
    information on a protected Cosmos DB account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfProtectedCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedCosmosDbAccount
    """

    return (
        await asyncio_detailed(
            cosmos_db_account_id=cosmos_db_account_id,
            client=client,
            sync=sync,
        )
    ).parsed
