from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_repository_security_settings_data import (
    AsyncOperationOfRepositorySecuritySettingsData,
)
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_415 import ProblemDetails415
from ...models.repository_create_from_client_with_key_vault import RepositoryCreateFromClientWithKeyVault
from ...models.repository_security_settings_data import RepositorySecuritySettingsData
from ...types import Response


def _get_kwargs(
    *,
    body: RepositoryCreateFromClientWithKeyVault,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/repositories/settings/getMetadata",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfRepositorySecuritySettingsData
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails415
    | RepositorySecuritySettingsData
    | None
):
    if response.status_code == 200:
        response_200 = RepositorySecuritySettingsData.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfRepositorySecuritySettingsData.from_dict(response.json())

        return response_202

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
) -> Response[
    AsyncOperationOfRepositorySecuritySettingsData
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails415
    | RepositorySecuritySettingsData
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
    body: RepositoryCreateFromClientWithKeyVault,
) -> Response[
    AsyncOperationOfRepositorySecuritySettingsData
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails415
    | RepositorySecuritySettingsData
]:
    """Get Backup Repository Metadata

     The HTTP POST request to the `/repositories/settings/getMetadata` endpoint retrieves metadata for a
    backup repository with the specified settings.

    Args:
        body (RepositoryCreateFromClientWithKeyVault):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfRepositorySecuritySettingsData | ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | RepositorySecuritySettingsData]
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
    body: RepositoryCreateFromClientWithKeyVault,
) -> (
    AsyncOperationOfRepositorySecuritySettingsData
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails415
    | RepositorySecuritySettingsData
    | None
):
    """Get Backup Repository Metadata

     The HTTP POST request to the `/repositories/settings/getMetadata` endpoint retrieves metadata for a
    backup repository with the specified settings.

    Args:
        body (RepositoryCreateFromClientWithKeyVault):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfRepositorySecuritySettingsData | ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | RepositorySecuritySettingsData
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RepositoryCreateFromClientWithKeyVault,
) -> Response[
    AsyncOperationOfRepositorySecuritySettingsData
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails415
    | RepositorySecuritySettingsData
]:
    """Get Backup Repository Metadata

     The HTTP POST request to the `/repositories/settings/getMetadata` endpoint retrieves metadata for a
    backup repository with the specified settings.

    Args:
        body (RepositoryCreateFromClientWithKeyVault):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfRepositorySecuritySettingsData | ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | RepositorySecuritySettingsData]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RepositoryCreateFromClientWithKeyVault,
) -> (
    AsyncOperationOfRepositorySecuritySettingsData
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails415
    | RepositorySecuritySettingsData
    | None
):
    """Get Backup Repository Metadata

     The HTTP POST request to the `/repositories/settings/getMetadata` endpoint retrieves metadata for a
    backup repository with the specified settings.

    Args:
        body (RepositoryCreateFromClientWithKeyVault):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfRepositorySecuritySettingsData | ProblemDetails400 | ProblemDetails401 | ProblemDetails415 | RepositorySecuritySettingsData
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
