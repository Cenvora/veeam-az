from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.azure_subscription import AzureSubscription
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import Response


def _get_kwargs(
    subscription_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/subscriptions/{subscription_id}".format(
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = AzureSubscription.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Microsoft Azure Subscription Data

     The  HTTP GET request to the `/cloudInfrastructure/subscriptions/{subscriptionId}` endpoint
    retrieves information on a subscription with the specified ID.

    Args:
        subscription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> AzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Microsoft Azure Subscription Data

     The  HTTP GET request to the `/cloudInfrastructure/subscriptions/{subscriptionId}` endpoint
    retrieves information on a subscription with the specified ID.

    Args:
        subscription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    subscription_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Microsoft Azure Subscription Data

     The  HTTP GET request to the `/cloudInfrastructure/subscriptions/{subscriptionId}` endpoint
    retrieves information on a subscription with the specified ID.

    Args:
        subscription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> AzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Microsoft Azure Subscription Data

     The  HTTP GET request to the `/cloudInfrastructure/subscriptions/{subscriptionId}` endpoint
    retrieves information on a subscription with the specified ID.

    Args:
        subscription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
