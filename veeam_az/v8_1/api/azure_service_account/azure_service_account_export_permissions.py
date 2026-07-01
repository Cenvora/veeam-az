from http import HTTPStatus
from io import BytesIO
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_415 import ProblemDetails415
from ...types import UNSET, File, Response


def _get_kwargs(
    *,
    account_id: UUID,
    subscription_id: UUID,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_account_id = str(account_id)
    params["accountId"] = json_account_id

    json_subscription_id = str(subscription_id)
    params["subscriptionId"] = json_subscription_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/accounts/azure/service/exportPermissions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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

    if response.status_code == 415:
        response_415 = ProblemDetails415.from_dict(response.json())

        return response_415

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    subscription_id: UUID,
) -> Response[File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]:
    """Export Service Account Required Permissions

     The HTTP POST request to the `/accounts/azure/service/exportPermissions` endpoint exports a .JSON
    file with the full list of permissions required to perform operations selected for the service
    account with the specified ID.

    Args:
        account_id (UUID):
        subscription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    subscription_id: UUID,
) -> File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | None:
    """Export Service Account Required Permissions

     The HTTP POST request to the `/accounts/azure/service/exportPermissions` endpoint exports a .JSON
    file with the full list of permissions required to perform operations selected for the service
    account with the specified ID.

    Args:
        account_id (UUID):
        subscription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        subscription_id=subscription_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    subscription_id: UUID,
) -> Response[File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]:
    """Export Service Account Required Permissions

     The HTTP POST request to the `/accounts/azure/service/exportPermissions` endpoint exports a .JSON
    file with the full list of permissions required to perform operations selected for the service
    account with the specified ID.

    Args:
        account_id (UUID):
        subscription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    subscription_id: UUID,
) -> File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | None:
    """Export Service Account Required Permissions

     The HTTP POST request to the `/accounts/azure/service/exportPermissions` endpoint exports a .JSON
    file with the full list of permissions required to perform operations selected for the service
    account with the specified ID.

    Args:
        account_id (UUID):
        subscription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            subscription_id=subscription_id,
        )
    ).parsed
