from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_subscriptions_listing_result import AsyncOperationOfSubscriptionsListingResult
from ...models.client_login_parameters import ClientLoginParameters
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_415 import ProblemDetails415
from ...models.subscriptions_listing_result import SubscriptionsListingResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ClientLoginParameters | Unset = UNSET,
    edit_account_id: None | str | Unset = UNSET,
    skip_permissions_check: bool | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_edit_account_id: None | str | Unset
    if isinstance(edit_account_id, Unset):
        json_edit_account_id = UNSET
    else:
        json_edit_account_id = edit_account_id
    params["editAccountId"] = json_edit_account_id

    json_skip_permissions_check: bool | None | Unset
    if isinstance(skip_permissions_check, Unset):
        json_skip_permissions_check = UNSET
    else:
        json_skip_permissions_check = skip_permissions_check
    params["skipPermissionsCheck"] = json_skip_permissions_check

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/accounts/azure/service/listSubscriptionsByApp",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfSubscriptionsListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
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
    *,
    client: AuthenticatedClient | Client,
    body: ClientLoginParameters | Unset = UNSET,
    edit_account_id: None | str | Unset = UNSET,
    skip_permissions_check: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfSubscriptionsListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails415
    | SubscriptionsListingResult
]:
    """Get List of Subscriptions by Application

     The HTTP POST request to the `/accounts/azure/service/listSubscriptionsByApp` retrieves a list of
    subscriptions available for the service account connected to the existing Entra ID application.

    Args:
        edit_account_id (None | str | Unset):
        skip_permissions_check (bool | None | Unset):
        body (ClientLoginParameters | Unset): Specifies the login data of the Entra ID
            application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfSubscriptionsListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | SubscriptionsListingResult]
    """

    kwargs = _get_kwargs(
        body=body,
        edit_account_id=edit_account_id,
        skip_permissions_check=skip_permissions_check,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ClientLoginParameters | Unset = UNSET,
    edit_account_id: None | str | Unset = UNSET,
    skip_permissions_check: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfSubscriptionsListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails415
    | SubscriptionsListingResult
    | None
):
    """Get List of Subscriptions by Application

     The HTTP POST request to the `/accounts/azure/service/listSubscriptionsByApp` retrieves a list of
    subscriptions available for the service account connected to the existing Entra ID application.

    Args:
        edit_account_id (None | str | Unset):
        skip_permissions_check (bool | None | Unset):
        body (ClientLoginParameters | Unset): Specifies the login data of the Entra ID
            application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfSubscriptionsListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | SubscriptionsListingResult
    """

    return sync_detailed(
        client=client,
        body=body,
        edit_account_id=edit_account_id,
        skip_permissions_check=skip_permissions_check,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ClientLoginParameters | Unset = UNSET,
    edit_account_id: None | str | Unset = UNSET,
    skip_permissions_check: bool | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfSubscriptionsListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails415
    | SubscriptionsListingResult
]:
    """Get List of Subscriptions by Application

     The HTTP POST request to the `/accounts/azure/service/listSubscriptionsByApp` retrieves a list of
    subscriptions available for the service account connected to the existing Entra ID application.

    Args:
        edit_account_id (None | str | Unset):
        skip_permissions_check (bool | None | Unset):
        body (ClientLoginParameters | Unset): Specifies the login data of the Entra ID
            application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfSubscriptionsListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | SubscriptionsListingResult]
    """

    kwargs = _get_kwargs(
        body=body,
        edit_account_id=edit_account_id,
        skip_permissions_check=skip_permissions_check,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ClientLoginParameters | Unset = UNSET,
    edit_account_id: None | str | Unset = UNSET,
    skip_permissions_check: bool | None | Unset = UNSET,
) -> (
    AsyncOperationOfSubscriptionsListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails415
    | SubscriptionsListingResult
    | None
):
    """Get List of Subscriptions by Application

     The HTTP POST request to the `/accounts/azure/service/listSubscriptionsByApp` retrieves a list of
    subscriptions available for the service account connected to the existing Entra ID application.

    Args:
        edit_account_id (None | str | Unset):
        skip_permissions_check (bool | None | Unset):
        body (ClientLoginParameters | Unset): Specifies the login data of the Entra ID
            application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfSubscriptionsListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | SubscriptionsListingResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            edit_account_id=edit_account_id,
            skip_permissions_check=skip_permissions_check,
        )
    ).parsed
