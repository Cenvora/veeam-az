from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.protected_database import ProtectedDatabase
from ...types import UNSET, Response, Unset


def _get_kwargs(
    database_id: str,
    *,
    sync: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sync: bool | None | Unset
    if isinstance(sync, Unset):
        json_sync = UNSET
    else:
        json_sync = sync
    params["sync"] = json_sync

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/protectedItem/sql/{database_id}".format(
            database_id=quote(str(database_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedDatabase | None:
    if response.status_code == 200:
        response_200 = ProtectedDatabase.from_dict(response.json())

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
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedDatabase]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    database_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedDatabase]:
    """Get Protected SQL Database Data

     The HTTP GET request to the `/protectedItem/sql/{databaseId}` endpoint retrieves information on a
    protected SQL database with the specified ID.

    Args:
        database_id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedDatabase]
    """

    kwargs = _get_kwargs(
        database_id=database_id,
        sync=sync,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    database_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedDatabase | None:
    """Get Protected SQL Database Data

     The HTTP GET request to the `/protectedItem/sql/{databaseId}` endpoint retrieves information on a
    protected SQL database with the specified ID.

    Args:
        database_id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedDatabase
    """

    return sync_detailed(
        database_id=database_id,
        client=client,
        sync=sync,
    ).parsed


async def asyncio_detailed(
    database_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedDatabase]:
    """Get Protected SQL Database Data

     The HTTP GET request to the `/protectedItem/sql/{databaseId}` endpoint retrieves information on a
    protected SQL database with the specified ID.

    Args:
        database_id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedDatabase]
    """

    kwargs = _get_kwargs(
        database_id=database_id,
        sync=sync,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    database_id: str,
    *,
    client: AuthenticatedClient | Client,
    sync: bool | None | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedDatabase | None:
    """Get Protected SQL Database Data

     The HTTP GET request to the `/protectedItem/sql/{databaseId}` endpoint retrieves information on a
    protected SQL database with the specified ID.

    Args:
        database_id (str):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProtectedDatabase
    """

    return (
        await asyncio_detailed(
            database_id=database_id,
            client=client,
            sync=sync,
        )
    ).parsed
