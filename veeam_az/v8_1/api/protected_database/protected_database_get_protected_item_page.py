from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_page_of_protected_database import AsyncOperationOfPageOfProtectedDatabase
from ...models.page_of_protected_database import PageOfProtectedDatabase
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    server_id: None | str | Unset = UNSET,
    database_ids: list[str] | None | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
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

    json_server_id: None | str | Unset
    if isinstance(server_id, Unset):
        json_server_id = UNSET
    else:
        json_server_id = server_id
    params["ServerId"] = json_server_id

    json_database_ids: list[str] | None | Unset
    if isinstance(database_ids, Unset):
        json_database_ids = UNSET
    elif isinstance(database_ids, list):
        json_database_ids = database_ids

    else:
        json_database_ids = database_ids
    params["DatabaseIds"] = json_database_ids

    json_sync: bool | None | Unset
    if isinstance(sync, Unset):
        json_sync = UNSET
    else:
        json_sync = sync
    params["Sync"] = json_sync

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/protectedItem/sql",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfPageOfProtectedDatabase
    | PageOfProtectedDatabase
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    if response.status_code == 200:
        response_200 = PageOfProtectedDatabase.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfPageOfProtectedDatabase.from_dict(response.json())

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
    AsyncOperationOfPageOfProtectedDatabase
    | PageOfProtectedDatabase
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
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    server_id: None | str | Unset = UNSET,
    database_ids: list[str] | None | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfProtectedDatabase
    | PageOfProtectedDatabase
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
]:
    """Get Collection of Protected SQL Databases

     The HTTP GET request to the `/protectedItem/sql` endpoint retrieves a list of SQL databases
    protected by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        server_id (None | str | Unset):
        database_ids (list[str] | None | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfProtectedDatabase | PageOfProtectedDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
        server_id=server_id,
        database_ids=database_ids,
        sync=sync,
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
    search_pattern: None | str | Unset = UNSET,
    server_id: None | str | Unset = UNSET,
    database_ids: list[str] | None | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfProtectedDatabase
    | PageOfProtectedDatabase
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Collection of Protected SQL Databases

     The HTTP GET request to the `/protectedItem/sql` endpoint retrieves a list of SQL databases
    protected by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        server_id (None | str | Unset):
        database_ids (list[str] | None | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfProtectedDatabase | PageOfProtectedDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
        server_id=server_id,
        database_ids=database_ids,
        sync=sync,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    server_id: None | str | Unset = UNSET,
    database_ids: list[str] | None | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfProtectedDatabase
    | PageOfProtectedDatabase
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
]:
    """Get Collection of Protected SQL Databases

     The HTTP GET request to the `/protectedItem/sql` endpoint retrieves a list of SQL databases
    protected by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        server_id (None | str | Unset):
        database_ids (list[str] | None | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfProtectedDatabase | PageOfProtectedDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
        server_id=server_id,
        database_ids=database_ids,
        sync=sync,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    server_id: None | str | Unset = UNSET,
    database_ids: list[str] | None | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfProtectedDatabase
    | PageOfProtectedDatabase
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Collection of Protected SQL Databases

     The HTTP GET request to the `/protectedItem/sql` endpoint retrieves a list of SQL databases
    protected by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        server_id (None | str | Unset):
        database_ids (list[str] | None | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfProtectedDatabase | PageOfProtectedDatabase | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            search_pattern=search_pattern,
            server_id=server_id,
            database_ids=database_ids,
            sync=sync,
        )
    ).parsed
