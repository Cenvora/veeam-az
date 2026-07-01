from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_protected_item import PageOfProtectedItem
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_trace_id import ProblemDetailsTraceId
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_job_session_id: str,
    *,
    name_search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_name_search_pattern: None | str | Unset
    if isinstance(name_search_pattern, Unset):
        json_name_search_pattern = UNSET
    else:
        json_name_search_pattern = name_search_pattern
    params["NameSearchPattern"] = json_name_search_pattern

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/jobSessions/{backup_job_session_id}/protectedItems".format(
            backup_job_session_id=quote(str(backup_job_session_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfProtectedItem | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId | None:
    if response.status_code == 200:
        response_200 = PageOfProtectedItem.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetailsTraceId.from_dict(response.json())

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
) -> Response[PageOfProtectedItem | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_job_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    name_search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfProtectedItem | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId]:
    """Get Backup Session Data

     The HTTP GET request to the `/jobSessions/{backupJobSessionId}/protectedItems` endpoint retrieves a
    list of Azure resources protected during the backup session with the specified ID.

    Args:
        backup_job_session_id (str):
        name_search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfProtectedItem | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId]
    """

    kwargs = _get_kwargs(
        backup_job_session_id=backup_job_session_id,
        name_search_pattern=name_search_pattern,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_job_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    name_search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfProtectedItem | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId | None:
    """Get Backup Session Data

     The HTTP GET request to the `/jobSessions/{backupJobSessionId}/protectedItems` endpoint retrieves a
    list of Azure resources protected during the backup session with the specified ID.

    Args:
        backup_job_session_id (str):
        name_search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfProtectedItem | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId
    """

    return sync_detailed(
        backup_job_session_id=backup_job_session_id,
        client=client,
        name_search_pattern=name_search_pattern,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    backup_job_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    name_search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfProtectedItem | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId]:
    """Get Backup Session Data

     The HTTP GET request to the `/jobSessions/{backupJobSessionId}/protectedItems` endpoint retrieves a
    list of Azure resources protected during the backup session with the specified ID.

    Args:
        backup_job_session_id (str):
        name_search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfProtectedItem | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId]
    """

    kwargs = _get_kwargs(
        backup_job_session_id=backup_job_session_id,
        name_search_pattern=name_search_pattern,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_job_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    name_search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfProtectedItem | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId | None:
    """Get Backup Session Data

     The HTTP GET request to the `/jobSessions/{backupJobSessionId}/protectedItems` endpoint retrieves a
    list of Azure resources protected during the backup session with the specified ID.

    Args:
        backup_job_session_id (str):
        name_search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfProtectedItem | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId
    """

    return (
        await asyncio_detailed(
            backup_job_session_id=backup_job_session_id,
            client=client,
            name_search_pattern=name_search_pattern,
            offset=offset,
            limit=limit,
        )
    ).parsed
