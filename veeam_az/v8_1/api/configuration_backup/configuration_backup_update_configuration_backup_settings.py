from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.configuration_backup_settings import ConfigurationBackupSettings
from ...models.configuration_backup_settings_from_client import ConfigurationBackupSettingsFromClient
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import Response


def _get_kwargs(
    *,
    body: ConfigurationBackupSettingsFromClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v8.1/configurationBackup/settings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfigurationBackupSettings | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = ConfigurationBackupSettings.from_dict(response.json())

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
) -> Response[ConfigurationBackupSettings | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfigurationBackupSettingsFromClient,
) -> Response[ConfigurationBackupSettings | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Modify Configuration Backup Settings

     The HTTP PUT request to the `/configurationBackup/settings` endpoint changes settings configured to
    perform backup of the Veeam Backup for Microsoft Azure configuration database.

    Args:
        body (ConfigurationBackupSettingsFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigurationBackupSettings | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
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
    body: ConfigurationBackupSettingsFromClient,
) -> ConfigurationBackupSettings | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Modify Configuration Backup Settings

     The HTTP PUT request to the `/configurationBackup/settings` endpoint changes settings configured to
    perform backup of the Veeam Backup for Microsoft Azure configuration database.

    Args:
        body (ConfigurationBackupSettingsFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigurationBackupSettings | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfigurationBackupSettingsFromClient,
) -> Response[ConfigurationBackupSettings | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Modify Configuration Backup Settings

     The HTTP PUT request to the `/configurationBackup/settings` endpoint changes settings configured to
    perform backup of the Veeam Backup for Microsoft Azure configuration database.

    Args:
        body (ConfigurationBackupSettingsFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigurationBackupSettings | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ConfigurationBackupSettingsFromClient,
) -> ConfigurationBackupSettings | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Modify Configuration Backup Settings

     The HTTP PUT request to the `/configurationBackup/settings` endpoint changes settings configured to
    perform backup of the Veeam Backup for Microsoft Azure configuration database.

    Args:
        body (ConfigurationBackupSettingsFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigurationBackupSettings | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
