from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cosmos_db_continuous_restore_point import CosmosDbContinuousRestorePoint
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import Response


def _get_kwargs(
    restore_point_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/restorePoints/cosmosDb/continuous/{restore_point_id}".format(
            restore_point_id=quote(str(restore_point_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CosmosDbContinuousRestorePoint
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    if response.status_code == 200:
        response_200 = CosmosDbContinuousRestorePoint.from_dict(response.json())

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
) -> Response[
    CosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    CosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    """Get Cosmos DB Continuous Restore Point Data

     The HTTP GET request to the `/restorePoints/cosmosDb/continuous/{restorePointId}` endpoint retrieves
    information on a restorable timestamp with the specified ID.

    Args:
        restore_point_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> (
    CosmosDbContinuousRestorePoint
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Get Cosmos DB Continuous Restore Point Data

     The HTTP GET request to the `/restorePoints/cosmosDb/continuous/{restorePointId}` endpoint retrieves
    information on a restorable timestamp with the specified ID.

    Args:
        restore_point_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        restore_point_id=restore_point_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    CosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    """Get Cosmos DB Continuous Restore Point Data

     The HTTP GET request to the `/restorePoints/cosmosDb/continuous/{restorePointId}` endpoint retrieves
    information on a restorable timestamp with the specified ID.

    Args:
        restore_point_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> (
    CosmosDbContinuousRestorePoint
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Get Cosmos DB Continuous Restore Point Data

     The HTTP GET request to the `/restorePoints/cosmosDb/continuous/{restorePointId}` endpoint retrieves
    information on a restorable timestamp with the specified ID.

    Args:
        restore_point_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            restore_point_id=restore_point_id,
            client=client,
        )
    ).parsed
