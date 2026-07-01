from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cosmos_db_estimate_throughput_cost_request import CosmosDbEstimateThroughputCostRequest
from ...models.cosmos_db_throughput_cost import CosmosDbThroughputCost
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import UNSET, Response


def _get_kwargs(
    cosmos_db_account_id: str,
    *,
    body: CosmosDbEstimateThroughputCostRequest,
    service_account_id: UUID,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_service_account_id = str(service_account_id)
    params["serviceAccountId"] = json_service_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/cloudInfrastructure/cosmosDb/{cosmos_db_account_id}/estimateThroughputCost".format(
            cosmos_db_account_id=quote(str(cosmos_db_account_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CosmosDbThroughputCost | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    if response.status_code == 200:
        response_200 = CosmosDbThroughputCost.from_dict(response.json())

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
) -> Response[CosmosDbThroughputCost | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
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
    body: CosmosDbEstimateThroughputCostRequest,
    service_account_id: UUID,
) -> Response[CosmosDbThroughputCost | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    """Calculate Cost of Cosmos DB Account Throughput

     The HTTP POST request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/estimateThroughputCost` endpoint calculates the
    estimated hourly/daily/monthly cost for the specified throughput settings.

    Args:
        cosmos_db_account_id (str):
        service_account_id (UUID):
        body (CosmosDbEstimateThroughputCostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CosmosDbThroughputCost | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        body=body,
        service_account_id=service_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CosmosDbEstimateThroughputCostRequest,
    service_account_id: UUID,
) -> CosmosDbThroughputCost | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    """Calculate Cost of Cosmos DB Account Throughput

     The HTTP POST request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/estimateThroughputCost` endpoint calculates the
    estimated hourly/daily/monthly cost for the specified throughput settings.

    Args:
        cosmos_db_account_id (str):
        service_account_id (UUID):
        body (CosmosDbEstimateThroughputCostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CosmosDbThroughputCost | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        cosmos_db_account_id=cosmos_db_account_id,
        client=client,
        body=body,
        service_account_id=service_account_id,
    ).parsed


async def asyncio_detailed(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CosmosDbEstimateThroughputCostRequest,
    service_account_id: UUID,
) -> Response[CosmosDbThroughputCost | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    """Calculate Cost of Cosmos DB Account Throughput

     The HTTP POST request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/estimateThroughputCost` endpoint calculates the
    estimated hourly/daily/monthly cost for the specified throughput settings.

    Args:
        cosmos_db_account_id (str):
        service_account_id (UUID):
        body (CosmosDbEstimateThroughputCostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CosmosDbThroughputCost | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        body=body,
        service_account_id=service_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CosmosDbEstimateThroughputCostRequest,
    service_account_id: UUID,
) -> CosmosDbThroughputCost | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    """Calculate Cost of Cosmos DB Account Throughput

     The HTTP POST request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/estimateThroughputCost` endpoint calculates the
    estimated hourly/daily/monthly cost for the specified throughput settings.

    Args:
        cosmos_db_account_id (str):
        service_account_id (UUID):
        body (CosmosDbEstimateThroughputCostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CosmosDbThroughputCost | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            cosmos_db_account_id=cosmos_db_account_id,
            client=client,
            body=body,
            service_account_id=service_account_id,
        )
    ).parsed
