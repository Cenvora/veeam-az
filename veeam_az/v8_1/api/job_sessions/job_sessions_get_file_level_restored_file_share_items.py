from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_file_level_restored_file_share import PageOfFileLevelRestoredFileShare
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_trace_id import ProblemDetailsTraceId
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_job_session_id: str,
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
        "url": "/api/v8.1/jobSessions/{restore_job_session_id}/fileLevelRestoredFileShareItems".format(
            restore_job_session_id=quote(str(restore_job_session_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfFileLevelRestoredFileShare | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId | None:
    if response.status_code == 200:
        response_200 = PageOfFileLevelRestoredFileShare.from_dict(response.json())

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
) -> Response[PageOfFileLevelRestoredFileShare | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_job_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    name_search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfFileLevelRestoredFileShare | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId]:
    """Get File Share File-Level Restore Session Data

     The HTTP GET request to the `/jobSessions/{restoreJobSessionId}/fileLevelRestoredFileShareItems`
    endpoint retrieves a list of items restored during a File Share file-level restore session with the
    specified ID.

    Args:
        restore_job_session_id (str):
        name_search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfFileLevelRestoredFileShare | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId]
    """

    kwargs = _get_kwargs(
        restore_job_session_id=restore_job_session_id,
        name_search_pattern=name_search_pattern,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_job_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    name_search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfFileLevelRestoredFileShare | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId | None:
    """Get File Share File-Level Restore Session Data

     The HTTP GET request to the `/jobSessions/{restoreJobSessionId}/fileLevelRestoredFileShareItems`
    endpoint retrieves a list of items restored during a File Share file-level restore session with the
    specified ID.

    Args:
        restore_job_session_id (str):
        name_search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfFileLevelRestoredFileShare | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId
    """

    return sync_detailed(
        restore_job_session_id=restore_job_session_id,
        client=client,
        name_search_pattern=name_search_pattern,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    restore_job_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    name_search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfFileLevelRestoredFileShare | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId]:
    """Get File Share File-Level Restore Session Data

     The HTTP GET request to the `/jobSessions/{restoreJobSessionId}/fileLevelRestoredFileShareItems`
    endpoint retrieves a list of items restored during a File Share file-level restore session with the
    specified ID.

    Args:
        restore_job_session_id (str):
        name_search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfFileLevelRestoredFileShare | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId]
    """

    kwargs = _get_kwargs(
        restore_job_session_id=restore_job_session_id,
        name_search_pattern=name_search_pattern,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_job_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    name_search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfFileLevelRestoredFileShare | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId | None:
    """Get File Share File-Level Restore Session Data

     The HTTP GET request to the `/jobSessions/{restoreJobSessionId}/fileLevelRestoredFileShareItems`
    endpoint retrieves a list of items restored during a File Share file-level restore session with the
    specified ID.

    Args:
        restore_job_session_id (str):
        name_search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfFileLevelRestoredFileShare | ProblemDetails401 | ProblemDetails403 | ProblemDetailsTraceId
    """

    return (
        await asyncio_detailed(
            restore_job_session_id=restore_job_session_id,
            client=client,
            name_search_pattern=name_search_pattern,
            offset=offset,
            limit=limit,
        )
    ).parsed
