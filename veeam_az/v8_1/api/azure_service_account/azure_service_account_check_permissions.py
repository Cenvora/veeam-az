from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_subscriptions_listing_result import AsyncOperationOfSubscriptionsListingResult
from ...models.azure_account_purpose import AzureAccountPurpose
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.problem_details_415 import ProblemDetails415
from ...models.subscriptions_listing_result import SubscriptionsListingResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: UUID,
    *,
    subscription_id: list[UUID] | None | Unset = UNSET,
    purposes: list[AzureAccountPurpose] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_subscription_id: list[str] | None | Unset
    if isinstance(subscription_id, Unset):
        json_subscription_id = UNSET
    elif isinstance(subscription_id, list):
        json_subscription_id = []
        for subscription_id_type_0_item_data in subscription_id:
            subscription_id_type_0_item = str(subscription_id_type_0_item_data)
            json_subscription_id.append(subscription_id_type_0_item)

    else:
        json_subscription_id = subscription_id
    params["subscriptionId"] = json_subscription_id

    json_purposes: list[str] | None | Unset
    if isinstance(purposes, Unset):
        json_purposes = UNSET
    elif isinstance(purposes, list):
        json_purposes = []
        for purposes_type_0_item_data in purposes:
            purposes_type_0_item = purposes_type_0_item_data.value
            json_purposes.append(purposes_type_0_item)

    else:
        json_purposes = purposes
    params["purposes"] = json_purposes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/accounts/azure/service/{account_id}/checkPermissions".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfSubscriptionsListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SubscriptionsListingResult
    | None
):
    if response.status_code == 200:
        response_200 = SubscriptionsListingResult.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfSubscriptionsListingResult.from_dict(response.json())

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

    if response.status_code == 415:
        response_415 = ProblemDetails415.from_dict(response.json())

        return response_415

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AsyncOperationOfSubscriptionsListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SubscriptionsListingResult
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    subscription_id: list[UUID] | None | Unset = UNSET,
    purposes: list[AzureAccountPurpose] | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfSubscriptionsListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SubscriptionsListingResult
]:
    """Verify Service Account Permissions

     The HTTP POST request to the `/accounts/azure/service/{accountId}/checkPermissions` checks whether
    the specified service account has all the permissions required to protect resources that belong to
    the specified Azure subscription.

    Args:
        account_id (UUID):
        subscription_id (list[UUID] | None | Unset):
        purposes (list[AzureAccountPurpose] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfSubscriptionsListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | SubscriptionsListingResult]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        subscription_id=subscription_id,
        purposes=purposes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    subscription_id: list[UUID] | None | Unset = UNSET,
    purposes: list[AzureAccountPurpose] | None | Unset = UNSET,
) -> (
    AsyncOperationOfSubscriptionsListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SubscriptionsListingResult
    | None
):
    """Verify Service Account Permissions

     The HTTP POST request to the `/accounts/azure/service/{accountId}/checkPermissions` checks whether
    the specified service account has all the permissions required to protect resources that belong to
    the specified Azure subscription.

    Args:
        account_id (UUID):
        subscription_id (list[UUID] | None | Unset):
        purposes (list[AzureAccountPurpose] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfSubscriptionsListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | SubscriptionsListingResult
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        subscription_id=subscription_id,
        purposes=purposes,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    subscription_id: list[UUID] | None | Unset = UNSET,
    purposes: list[AzureAccountPurpose] | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfSubscriptionsListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SubscriptionsListingResult
]:
    """Verify Service Account Permissions

     The HTTP POST request to the `/accounts/azure/service/{accountId}/checkPermissions` checks whether
    the specified service account has all the permissions required to protect resources that belong to
    the specified Azure subscription.

    Args:
        account_id (UUID):
        subscription_id (list[UUID] | None | Unset):
        purposes (list[AzureAccountPurpose] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfSubscriptionsListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | SubscriptionsListingResult]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        subscription_id=subscription_id,
        purposes=purposes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    subscription_id: list[UUID] | None | Unset = UNSET,
    purposes: list[AzureAccountPurpose] | None | Unset = UNSET,
) -> (
    AsyncOperationOfSubscriptionsListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SubscriptionsListingResult
    | None
):
    """Verify Service Account Permissions

     The HTTP POST request to the `/accounts/azure/service/{accountId}/checkPermissions` checks whether
    the specified service account has all the permissions required to protect resources that belong to
    the specified Azure subscription.

    Args:
        account_id (UUID):
        subscription_id (list[UUID] | None | Unset):
        purposes (list[AzureAccountPurpose] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfSubscriptionsListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | SubscriptionsListingResult
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            subscription_id=subscription_id,
            purposes=purposes,
        )
    ).parsed
