from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_page_of_cosmos_db_account import AsyncOperationOfPageOfCosmosDbAccount
from ...models.cosmos_db_options import CosmosDbOptions
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CosmosDbOptions | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/cosmosDb/rescan",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AsyncOperationOfPageOfCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 202:
        response_202 = AsyncOperationOfPageOfCosmosDbAccount.from_dict(response.json())

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
) -> Response[AsyncOperationOfPageOfCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CosmosDbOptions | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[AsyncOperationOfPageOfCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Rescan Cosmos DB Accounts

     The HTTP POST request to the `/cosmosDb/rescan` endpoint launches a rescan operation for Cosmos DB
    accounts in Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        body (CosmosDbOptions | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        body=body,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CosmosDbOptions | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> AsyncOperationOfPageOfCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Rescan Cosmos DB Accounts

     The HTTP POST request to the `/cosmosDb/rescan` endpoint launches a rescan operation for Cosmos DB
    accounts in Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        body (CosmosDbOptions | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        body=body,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CosmosDbOptions | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[AsyncOperationOfPageOfCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Rescan Cosmos DB Accounts

     The HTTP POST request to the `/cosmosDb/rescan` endpoint launches a rescan operation for Cosmos DB
    accounts in Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        body (CosmosDbOptions | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        body=body,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CosmosDbOptions | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> AsyncOperationOfPageOfCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Rescan Cosmos DB Accounts

     The HTTP POST request to the `/cosmosDb/rescan` endpoint launches a rescan operation for Cosmos DB
    accounts in Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        body (CosmosDbOptions | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfCosmosDbAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            offset=offset,
            limit=limit,
        )
    ).parsed
