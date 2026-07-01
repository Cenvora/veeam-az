from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_boolean import AsyncOperationOfBoolean
from ...models.azure_authentication_result import AzureAuthenticationResult
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.problem_details_409 import ProblemDetails409
from ...models.problem_details_415 import ProblemDetails415
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AzureAuthenticationResult | Unset = UNSET,
    application_id: None | str | Unset = UNSET,
    edit_account_id: None | str | Unset = UNSET,
    tenant_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_application_id: None | str | Unset
    if isinstance(application_id, Unset):
        json_application_id = UNSET
    else:
        json_application_id = application_id
    params["applicationId"] = json_application_id

    json_edit_account_id: None | str | Unset
    if isinstance(edit_account_id, Unset):
        json_edit_account_id = UNSET
    else:
        json_edit_account_id = edit_account_id
    params["editAccountId"] = json_edit_account_id

    json_tenant_id: None | str | Unset
    if isinstance(tenant_id, Unset):
        json_tenant_id = UNSET
    else:
        json_tenant_id = tenant_id
    params["tenantId"] = json_tenant_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/accounts/azure/service/isUserOwnerOfAdApp",
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
    AsyncOperationOfBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | bool
    | None
):
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfBoolean.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ProblemDetails409.from_dict(response.json())

        return response_409

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
    AsyncOperationOfBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | bool
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
    body: AzureAuthenticationResult | Unset = UNSET,
    application_id: None | str | Unset = UNSET,
    edit_account_id: None | str | Unset = UNSET,
    tenant_id: None | str | Unset = UNSET,
) -> Response[
    AsyncOperationOfBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | bool
]:
    r"""Validate User

     The HTTP POST request to the `/accounts/azure/service/isUserOwnerOfAdApp` endpoint checks whether
    the Microsoft Azure account authenticated to the Microsoft Azure Cross-platform Command Line
    Interface (Azure CLI) is the owner of the specified Entra ID application.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        application_id (None | str | Unset):
        edit_account_id (None | str | Unset):
        tenant_id (None | str | Unset):
        body (AzureAuthenticationResult | Unset): Specifies information on authentication in
            Microsoft Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfBoolean | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | bool]
    """

    kwargs = _get_kwargs(
        body=body,
        application_id=application_id,
        edit_account_id=edit_account_id,
        tenant_id=tenant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AzureAuthenticationResult | Unset = UNSET,
    application_id: None | str | Unset = UNSET,
    edit_account_id: None | str | Unset = UNSET,
    tenant_id: None | str | Unset = UNSET,
) -> (
    AsyncOperationOfBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | bool
    | None
):
    r"""Validate User

     The HTTP POST request to the `/accounts/azure/service/isUserOwnerOfAdApp` endpoint checks whether
    the Microsoft Azure account authenticated to the Microsoft Azure Cross-platform Command Line
    Interface (Azure CLI) is the owner of the specified Entra ID application.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        application_id (None | str | Unset):
        edit_account_id (None | str | Unset):
        tenant_id (None | str | Unset):
        body (AzureAuthenticationResult | Unset): Specifies information on authentication in
            Microsoft Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfBoolean | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | bool
    """

    return sync_detailed(
        client=client,
        body=body,
        application_id=application_id,
        edit_account_id=edit_account_id,
        tenant_id=tenant_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AzureAuthenticationResult | Unset = UNSET,
    application_id: None | str | Unset = UNSET,
    edit_account_id: None | str | Unset = UNSET,
    tenant_id: None | str | Unset = UNSET,
) -> Response[
    AsyncOperationOfBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | bool
]:
    r"""Validate User

     The HTTP POST request to the `/accounts/azure/service/isUserOwnerOfAdApp` endpoint checks whether
    the Microsoft Azure account authenticated to the Microsoft Azure Cross-platform Command Line
    Interface (Azure CLI) is the owner of the specified Entra ID application.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        application_id (None | str | Unset):
        edit_account_id (None | str | Unset):
        tenant_id (None | str | Unset):
        body (AzureAuthenticationResult | Unset): Specifies information on authentication in
            Microsoft Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfBoolean | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | bool]
    """

    kwargs = _get_kwargs(
        body=body,
        application_id=application_id,
        edit_account_id=edit_account_id,
        tenant_id=tenant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AzureAuthenticationResult | Unset = UNSET,
    application_id: None | str | Unset = UNSET,
    edit_account_id: None | str | Unset = UNSET,
    tenant_id: None | str | Unset = UNSET,
) -> (
    AsyncOperationOfBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | bool
    | None
):
    r"""Validate User

     The HTTP POST request to the `/accounts/azure/service/isUserOwnerOfAdApp` endpoint checks whether
    the Microsoft Azure account authenticated to the Microsoft Azure Cross-platform Command Line
    Interface (Azure CLI) is the owner of the specified Entra ID application.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        application_id (None | str | Unset):
        edit_account_id (None | str | Unset):
        tenant_id (None | str | Unset):
        body (AzureAuthenticationResult | Unset): Specifies information on authentication in
            Microsoft Azure environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfBoolean | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | bool
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            application_id=application_id,
            edit_account_id=edit_account_id,
            tenant_id=tenant_id,
        )
    ).parsed
