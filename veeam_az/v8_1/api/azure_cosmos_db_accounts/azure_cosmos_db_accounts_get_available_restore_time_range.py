from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cosmos_db_account_restore_time_range import CosmosDbAccountRestoreTimeRange
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cosmos_db_account_id: str,
    *,
    service_account_id: None | Unset | UUID = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_service_account_id: None | str | Unset
    if isinstance(service_account_id, Unset):
        json_service_account_id = UNSET
    elif isinstance(service_account_id, UUID):
        json_service_account_id = str(service_account_id)
    else:
        json_service_account_id = service_account_id
    params["ServiceAccountId"] = json_service_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/cosmosDb/{cosmos_db_account_id}/availableRestoreTimeRange".format(
            cosmos_db_account_id=quote(str(cosmos_db_account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CosmosDbAccountRestoreTimeRange
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    if response.status_code == 200:
        response_200 = CosmosDbAccountRestoreTimeRange.from_dict(response.json())

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
    CosmosDbAccountRestoreTimeRange | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
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
    service_account_id: None | Unset | UUID = UNSET,
) -> Response[
    CosmosDbAccountRestoreTimeRange | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    """Get Cosmos DB Account Point-in-time Restore Period

     The HTTP GET request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/availableRestoreTimeRange` endpoint retrieves a
    time period within which a restore point for the specified Cosmos DB account can be selected.

    Args:
        cosmos_db_account_id (str):
        service_account_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CosmosDbAccountRestoreTimeRange | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
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
    service_account_id: None | Unset | UUID = UNSET,
) -> (
    CosmosDbAccountRestoreTimeRange
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Get Cosmos DB Account Point-in-time Restore Period

     The HTTP GET request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/availableRestoreTimeRange` endpoint retrieves a
    time period within which a restore point for the specified Cosmos DB account can be selected.

    Args:
        cosmos_db_account_id (str):
        service_account_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CosmosDbAccountRestoreTimeRange | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        cosmos_db_account_id=cosmos_db_account_id,
        client=client,
        service_account_id=service_account_id,
    ).parsed


async def asyncio_detailed(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    service_account_id: None | Unset | UUID = UNSET,
) -> Response[
    CosmosDbAccountRestoreTimeRange | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    """Get Cosmos DB Account Point-in-time Restore Period

     The HTTP GET request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/availableRestoreTimeRange` endpoint retrieves a
    time period within which a restore point for the specified Cosmos DB account can be selected.

    Args:
        cosmos_db_account_id (str):
        service_account_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CosmosDbAccountRestoreTimeRange | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        service_account_id=service_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    service_account_id: None | Unset | UUID = UNSET,
) -> (
    CosmosDbAccountRestoreTimeRange
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Get Cosmos DB Account Point-in-time Restore Period

     The HTTP GET request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/availableRestoreTimeRange` endpoint retrieves a
    time period within which a restore point for the specified Cosmos DB account can be selected.

    Args:
        cosmos_db_account_id (str):
        service_account_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CosmosDbAccountRestoreTimeRange | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            cosmos_db_account_id=cosmos_db_account_id,
            client=client,
            service_account_id=service_account_id,
        )
    ).parsed
