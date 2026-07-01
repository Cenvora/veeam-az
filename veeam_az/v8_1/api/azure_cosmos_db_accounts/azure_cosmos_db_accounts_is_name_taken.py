from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_415 import ProblemDetails415
from ...types import UNSET, Response


def _get_kwargs(
    *,
    account_name: str,
    subscription_id: UUID,
    service_account_id: UUID,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountName"] = account_name

    json_subscription_id = str(subscription_id)
    params["subscriptionId"] = json_subscription_id

    json_service_account_id = str(service_account_id)
    params["serviceAccountId"] = json_service_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/cloudInfrastructure/cosmosDb/isNameTaken",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if response.status_code == 415:
        response_415 = ProblemDetails415.from_dict(response.json())

        return response_415

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | bool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_name: str,
    subscription_id: UUID,
    service_account_id: UUID,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | bool]:
    """Validate Cosmos DB Account Name

     The HTTP POST request to the `/cloudInfrastructure/cosmosDb/isNameTaken` endpoint checks whether a
    Cosmos DB account with the specified name already exists in the specified subscription.

    Args:
        account_name (str):
        subscription_id (UUID):
        service_account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | bool]
    """

    kwargs = _get_kwargs(
        account_name=account_name,
        subscription_id=subscription_id,
        service_account_id=service_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_name: str,
    subscription_id: UUID,
    service_account_id: UUID,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | bool | None:
    """Validate Cosmos DB Account Name

     The HTTP POST request to the `/cloudInfrastructure/cosmosDb/isNameTaken` endpoint checks whether a
    Cosmos DB account with the specified name already exists in the specified subscription.

    Args:
        account_name (str):
        subscription_id (UUID):
        service_account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | bool
    """

    return sync_detailed(
        client=client,
        account_name=account_name,
        subscription_id=subscription_id,
        service_account_id=service_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_name: str,
    subscription_id: UUID,
    service_account_id: UUID,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | bool]:
    """Validate Cosmos DB Account Name

     The HTTP POST request to the `/cloudInfrastructure/cosmosDb/isNameTaken` endpoint checks whether a
    Cosmos DB account with the specified name already exists in the specified subscription.

    Args:
        account_name (str):
        subscription_id (UUID):
        service_account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | bool]
    """

    kwargs = _get_kwargs(
        account_name=account_name,
        subscription_id=subscription_id,
        service_account_id=service_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_name: str,
    subscription_id: UUID,
    service_account_id: UUID,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | bool | None:
    """Validate Cosmos DB Account Name

     The HTTP POST request to the `/cloudInfrastructure/cosmosDb/isNameTaken` endpoint checks whether a
    Cosmos DB account with the specified name already exists in the specified subscription.

    Args:
        account_name (str):
        subscription_id (UUID):
        service_account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | bool
    """

    return (
        await asyncio_detailed(
            client=client,
            account_name=account_name,
            subscription_id=subscription_id,
            service_account_id=service_account_id,
        )
    ).parsed
