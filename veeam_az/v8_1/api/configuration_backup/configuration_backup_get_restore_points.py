from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_configuration_restore_point import PageOfConfigurationRestorePoint
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    repository_id: None | Unset | UUID = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_repository_id: None | str | Unset
    if isinstance(repository_id, Unset):
        json_repository_id = UNSET
    elif isinstance(repository_id, UUID):
        json_repository_id = str(repository_id)
    else:
        json_repository_id = repository_id
    params["RepositoryId"] = json_repository_id

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/configurationBackup/restorePoints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfConfigurationRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfConfigurationRestorePoint.from_dict(response.json())

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
) -> Response[PageOfConfigurationRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    repository_id: None | Unset | UUID = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfConfigurationRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Configuration Backup Restore Points

     The HTTP GET request to the `/configurationBackup/restorePoints` endpoint retrieves a list of
    restore points created for the Veeam Backup for Microsoft Azure configuration database.

    Args:
        repository_id (None | Unset | UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfConfigurationRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    repository_id: None | Unset | UUID = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfConfigurationRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Configuration Backup Restore Points

     The HTTP GET request to the `/configurationBackup/restorePoints` endpoint retrieves a list of
    restore points created for the Veeam Backup for Microsoft Azure configuration database.

    Args:
        repository_id (None | Unset | UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfConfigurationRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        repository_id=repository_id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    repository_id: None | Unset | UUID = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfConfigurationRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Configuration Backup Restore Points

     The HTTP GET request to the `/configurationBackup/restorePoints` endpoint retrieves a list of
    restore points created for the Veeam Backup for Microsoft Azure configuration database.

    Args:
        repository_id (None | Unset | UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfConfigurationRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    repository_id: None | Unset | UUID = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfConfigurationRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Configuration Backup Restore Points

     The HTTP GET request to the `/configurationBackup/restorePoints` endpoint retrieves a list of
    restore points created for the Veeam Backup for Microsoft Azure configuration database.

    Args:
        repository_id (None | Unset | UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfConfigurationRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            repository_id=repository_id,
            offset=offset,
            limit=limit,
        )
    ).parsed
