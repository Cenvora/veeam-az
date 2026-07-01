from http import HTTPStatus
from io import BytesIO
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.azure_authentication_result import AzureAuthenticationResult
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_415 import ProblemDetails415
from ...types import UNSET, File, Response


def _get_kwargs(
    *,
    body: AzureAuthenticationResult,
    subscription_id: UUID,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_subscription_id = str(subscription_id)
    params["subscriptionId"] = json_subscription_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/accounts/azure/service/exportPermissionsByToken",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: AzureAuthenticationResult,
    subscription_id: UUID,
) -> Response[File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]:
    r"""Export Permissions by Token

     The HTTP POST request to the `/accounts/azure/service/exportPermissionsByToken` endpoint exports a
    .JSON file with the full list of permissions that must be assigned to a service account to protect
    Azure resources associated with the specified subscription.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        subscription_id (UUID):
        body (AzureAuthenticationResult): Specifies information on authentication in Microsoft
            Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        body=body,
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AzureAuthenticationResult,
    subscription_id: UUID,
) -> File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | None:
    r"""Export Permissions by Token

     The HTTP POST request to the `/accounts/azure/service/exportPermissionsByToken` endpoint exports a
    .JSON file with the full list of permissions that must be assigned to a service account to protect
    Azure resources associated with the specified subscription.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        subscription_id (UUID):
        body (AzureAuthenticationResult): Specifies information on authentication in Microsoft
            Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415
    """

    return sync_detailed(
        client=client,
        body=body,
        subscription_id=subscription_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AzureAuthenticationResult,
    subscription_id: UUID,
) -> Response[File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]:
    r"""Export Permissions by Token

     The HTTP POST request to the `/accounts/azure/service/exportPermissionsByToken` endpoint exports a
    .JSON file with the full list of permissions that must be assigned to a service account to protect
    Azure resources associated with the specified subscription.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        subscription_id (UUID):
        body (AzureAuthenticationResult): Specifies information on authentication in Microsoft
            Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        body=body,
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AzureAuthenticationResult,
    subscription_id: UUID,
) -> File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | None:
    r"""Export Permissions by Token

     The HTTP POST request to the `/accounts/azure/service/exportPermissionsByToken` endpoint exports a
    .JSON file with the full list of permissions that must be assigned to a service account to protect
    Azure resources associated with the specified subscription.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        subscription_id (UUID):
        body (AzureAuthenticationResult): Specifies information on authentication in Microsoft
            Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            subscription_id=subscription_id,
        )
    ).parsed
