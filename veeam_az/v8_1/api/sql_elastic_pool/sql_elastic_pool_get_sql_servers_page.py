from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_page_of_sql_elastic_pool import AsyncOperationOfPageOfSqlElasticPool
from ...models.page_of_sql_elastic_pool import PageOfSqlElasticPool
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    json_sync: bool | None | Unset
    if isinstance(sync, Unset):
        json_sync = UNSET
    else:
        json_sync = sync
    params["Sync"] = json_sync

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/sqlElasticPools",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfPageOfSqlElasticPool
    | PageOfSqlElasticPool
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    if response.status_code == 200:
        response_200 = PageOfSqlElasticPool.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfPageOfSqlElasticPool.from_dict(response.json())

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
    AsyncOperationOfPageOfSqlElasticPool
    | PageOfSqlElasticPool
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
    sync: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfSqlElasticPool
    | PageOfSqlElasticPool
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
]:
    """Get Collection of Elastic Pools

     The HTTP GET request to the `/cloudInfrastructure/sqlElasticPools` endpoint retrieves a list of SQL
    elastic pools configured in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfSqlElasticPool | PageOfSqlElasticPool | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
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
    sync: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfSqlElasticPool
    | PageOfSqlElasticPool
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Collection of Elastic Pools

     The HTTP GET request to the `/cloudInfrastructure/sqlElasticPools` endpoint retrieves a list of SQL
    elastic pools configured in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfSqlElasticPool | PageOfSqlElasticPool | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        sync=sync,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfSqlElasticPool
    | PageOfSqlElasticPool
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
]:
    """Get Collection of Elastic Pools

     The HTTP GET request to the `/cloudInfrastructure/sqlElasticPools` endpoint retrieves a list of SQL
    elastic pools configured in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfSqlElasticPool | PageOfSqlElasticPool | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        sync=sync,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfSqlElasticPool
    | PageOfSqlElasticPool
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Collection of Elastic Pools

     The HTTP GET request to the `/cloudInfrastructure/sqlElasticPools` endpoint retrieves a list of SQL
    elastic pools configured in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        sync (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfSqlElasticPool | PageOfSqlElasticPool | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            sync=sync,
        )
    ).parsed
