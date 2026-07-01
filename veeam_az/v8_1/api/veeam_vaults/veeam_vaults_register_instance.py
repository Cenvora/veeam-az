from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.veeam_vault_registration_info import VeeamVaultRegistrationInfo
from ...models.veeam_vault_registration_request import VeeamVaultRegistrationRequest
from ...types import Response


def _get_kwargs(
    *,
    body: VeeamVaultRegistrationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/veeamVaults/registration",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | VeeamVaultRegistrationInfo | None:
    if response.status_code == 200:
        response_200 = VeeamVaultRegistrationInfo.from_dict(response.json())

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
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | VeeamVaultRegistrationInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VeeamVaultRegistrationRequest,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | VeeamVaultRegistrationInfo]:
    r"""Register Veeam Data Cloud Vault

     The HTTP POST request to the `/veeamVaults/registration` endpoint allows you to register your backup
    appliance in Veeam Data Cloud Vault. <br> <div class=\"note\"><strong>NOTE</strong> <br>To complete
    this operation, obtain the value of the `token` parameter. To do that, send the HTTP POST request to
    the [Generate Veeam Data Cloud Vault Registration
    Token](#tag/VeeamVaults/operation/VeeamVaults_CompleteSignIn) endpoint.</div>

    Args:
        body (VeeamVaultRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | VeeamVaultRegistrationInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: VeeamVaultRegistrationRequest,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | VeeamVaultRegistrationInfo | None:
    r"""Register Veeam Data Cloud Vault

     The HTTP POST request to the `/veeamVaults/registration` endpoint allows you to register your backup
    appliance in Veeam Data Cloud Vault. <br> <div class=\"note\"><strong>NOTE</strong> <br>To complete
    this operation, obtain the value of the `token` parameter. To do that, send the HTTP POST request to
    the [Generate Veeam Data Cloud Vault Registration
    Token](#tag/VeeamVaults/operation/VeeamVaults_CompleteSignIn) endpoint.</div>

    Args:
        body (VeeamVaultRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | VeeamVaultRegistrationInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VeeamVaultRegistrationRequest,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | VeeamVaultRegistrationInfo]:
    r"""Register Veeam Data Cloud Vault

     The HTTP POST request to the `/veeamVaults/registration` endpoint allows you to register your backup
    appliance in Veeam Data Cloud Vault. <br> <div class=\"note\"><strong>NOTE</strong> <br>To complete
    this operation, obtain the value of the `token` parameter. To do that, send the HTTP POST request to
    the [Generate Veeam Data Cloud Vault Registration
    Token](#tag/VeeamVaults/operation/VeeamVaults_CompleteSignIn) endpoint.</div>

    Args:
        body (VeeamVaultRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | VeeamVaultRegistrationInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: VeeamVaultRegistrationRequest,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | VeeamVaultRegistrationInfo | None:
    r"""Register Veeam Data Cloud Vault

     The HTTP POST request to the `/veeamVaults/registration` endpoint allows you to register your backup
    appliance in Veeam Data Cloud Vault. <br> <div class=\"note\"><strong>NOTE</strong> <br>To complete
    this operation, obtain the value of the `token` parameter. To do that, send the HTTP POST request to
    the [Generate Veeam Data Cloud Vault Registration
    Token](#tag/VeeamVaults/operation/VeeamVaults_CompleteSignIn) endpoint.</div>

    Args:
        body (VeeamVaultRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | VeeamVaultRegistrationInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
