from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cosmos_db_account_restore_options import CosmosDbAccountRestoreOptions
from ...models.job_session import JobSession
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import Response


def _get_kwargs(
    cosmos_db_account_id: str,
    *,
    body: CosmosDbAccountRestoreOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/protectedItem/cosmosDb/{cosmos_db_account_id}/restore".format(
            cosmos_db_account_id=quote(str(cosmos_db_account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    if response.status_code == 202:
        response_202 = JobSession.from_dict(response.json())

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
) -> Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
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
    body: CosmosDbAccountRestoreOptions,
) -> Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    """Perform Cosmos DB Account Point-in-time Restore

     The HTTP POST request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}/restore` endpoint launches
    a point-in-time restore operation for a Cosmos DB account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        body (CosmosDbAccountRestoreOptions): Specifies information for the Cosmos DB account
            point-in-time restore.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CosmosDbAccountRestoreOptions,
) -> JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    """Perform Cosmos DB Account Point-in-time Restore

     The HTTP POST request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}/restore` endpoint launches
    a point-in-time restore operation for a Cosmos DB account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        body (CosmosDbAccountRestoreOptions): Specifies information for the Cosmos DB account
            point-in-time restore.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        cosmos_db_account_id=cosmos_db_account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CosmosDbAccountRestoreOptions,
) -> Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    """Perform Cosmos DB Account Point-in-time Restore

     The HTTP POST request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}/restore` endpoint launches
    a point-in-time restore operation for a Cosmos DB account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        body (CosmosDbAccountRestoreOptions): Specifies information for the Cosmos DB account
            point-in-time restore.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CosmosDbAccountRestoreOptions,
) -> JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    """Perform Cosmos DB Account Point-in-time Restore

     The HTTP POST request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}/restore` endpoint launches
    a point-in-time restore operation for a Cosmos DB account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        body (CosmosDbAccountRestoreOptions): Specifies information for the Cosmos DB account
            point-in-time restore.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            cosmos_db_account_id=cosmos_db_account_id,
            client=client,
            body=body,
        )
    ).parsed
