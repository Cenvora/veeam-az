from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.job_session import JobSession
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.protected_data_backup_tier import ProtectedDataBackupTier
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cosmos_db_account_id: str,
    *,
    backup_tier: ProtectedDataBackupTier | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_backup_tier: str | Unset = UNSET
    if not isinstance(backup_tier, Unset):
        json_backup_tier = backup_tier.value

    params["BackupTier"] = json_backup_tier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/protectedItem/cosmosDb/{cosmos_db_account_id}/deleteBackups".format(
            cosmos_db_account_id=quote(str(cosmos_db_account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    if response.status_code == 202:
        response_202 = JobSession.from_dict(response.json())

        return response_202

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    backup_tier: ProtectedDataBackupTier | Unset = UNSET,
) -> Response[Any | JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    """Remove Backups of Protected Cosmos DB Account

     The HTTP POST request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}/deleteBackups` endpoint
    removes backups created using the *Backup to repository* option for a Cosmos DB for PostgreSQL
    account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        backup_tier (ProtectedDataBackupTier | Unset): Defines whether you want to delete
            *Archive*, Standard (*NonArchive*) or *All* backups created for the specified Azure
            resources. By default, Veeam Backup for Microsoft Azure deletes all backups.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        backup_tier=backup_tier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    backup_tier: ProtectedDataBackupTier | Unset = UNSET,
) -> Any | JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    """Remove Backups of Protected Cosmos DB Account

     The HTTP POST request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}/deleteBackups` endpoint
    removes backups created using the *Backup to repository* option for a Cosmos DB for PostgreSQL
    account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        backup_tier (ProtectedDataBackupTier | Unset): Defines whether you want to delete
            *Archive*, Standard (*NonArchive*) or *All* backups created for the specified Azure
            resources. By default, Veeam Backup for Microsoft Azure deletes all backups.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        cosmos_db_account_id=cosmos_db_account_id,
        client=client,
        backup_tier=backup_tier,
    ).parsed


async def asyncio_detailed(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    backup_tier: ProtectedDataBackupTier | Unset = UNSET,
) -> Response[Any | JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    """Remove Backups of Protected Cosmos DB Account

     The HTTP POST request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}/deleteBackups` endpoint
    removes backups created using the *Backup to repository* option for a Cosmos DB for PostgreSQL
    account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        backup_tier (ProtectedDataBackupTier | Unset): Defines whether you want to delete
            *Archive*, Standard (*NonArchive*) or *All* backups created for the specified Azure
            resources. By default, Veeam Backup for Microsoft Azure deletes all backups.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        backup_tier=backup_tier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    backup_tier: ProtectedDataBackupTier | Unset = UNSET,
) -> Any | JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    """Remove Backups of Protected Cosmos DB Account

     The HTTP POST request to the `/protectedItem/cosmosDb/{cosmosDbAccountId}/deleteBackups` endpoint
    removes backups created using the *Backup to repository* option for a Cosmos DB for PostgreSQL
    account with the specified ID.

    Args:
        cosmos_db_account_id (str):
        backup_tier (ProtectedDataBackupTier | Unset): Defines whether you want to delete
            *Archive*, Standard (*NonArchive*) or *All* backups created for the specified Azure
            resources. By default, Veeam Backup for Microsoft Azure deletes all backups.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            cosmos_db_account_id=cosmos_db_account_id,
            client=client,
            backup_tier=backup_tier,
        )
    ).parsed
