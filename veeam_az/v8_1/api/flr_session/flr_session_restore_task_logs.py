from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flr_session_restore_task_logs_request import FlrSessionRestoreTaskLogsRequest
from ...models.flr_session_restore_task_logs_response import FlrSessionRestoreTaskLogsResponse
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    flr_session_id: UUID,
    restore_task_id: UUID,
    *,
    body: FlrSessionRestoreTaskLogsRequest,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/flr/{flr_session_id}/restore/{restore_task_id}/logs".format(
            flr_session_id=quote(str(flr_session_id), safe=""),
            restore_task_id=quote(str(restore_task_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FlrSessionRestoreTaskLogsResponse
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    if response.status_code == 200:
        response_200 = FlrSessionRestoreTaskLogsResponse.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ProblemDetails404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FlrSessionRestoreTaskLogsResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    flr_session_id: UUID,
    restore_task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FlrSessionRestoreTaskLogsRequest,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FlrSessionRestoreTaskLogsResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    """Get Restore Logs

     The HTTP GET request to the `/api/v8.1/flr/{flrSessionId}/restore/{restoreTaskId}/logs` endpoint
    allows you to retrieve detailed logs for each item processed by a restore task with the specified
    ID.

    Args:
        flr_session_id (UUID):
        restore_task_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        body (FlrSessionRestoreTaskLogsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlrSessionRestoreTaskLogsResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        flr_session_id=flr_session_id,
        restore_task_id=restore_task_id,
        body=body,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    flr_session_id: UUID,
    restore_task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FlrSessionRestoreTaskLogsRequest,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FlrSessionRestoreTaskLogsResponse
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Get Restore Logs

     The HTTP GET request to the `/api/v8.1/flr/{flrSessionId}/restore/{restoreTaskId}/logs` endpoint
    allows you to retrieve detailed logs for each item processed by a restore task with the specified
    ID.

    Args:
        flr_session_id (UUID):
        restore_task_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        body (FlrSessionRestoreTaskLogsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlrSessionRestoreTaskLogsResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        flr_session_id=flr_session_id,
        restore_task_id=restore_task_id,
        client=client,
        body=body,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    flr_session_id: UUID,
    restore_task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FlrSessionRestoreTaskLogsRequest,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FlrSessionRestoreTaskLogsResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    """Get Restore Logs

     The HTTP GET request to the `/api/v8.1/flr/{flrSessionId}/restore/{restoreTaskId}/logs` endpoint
    allows you to retrieve detailed logs for each item processed by a restore task with the specified
    ID.

    Args:
        flr_session_id (UUID):
        restore_task_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        body (FlrSessionRestoreTaskLogsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlrSessionRestoreTaskLogsResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        flr_session_id=flr_session_id,
        restore_task_id=restore_task_id,
        body=body,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    flr_session_id: UUID,
    restore_task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FlrSessionRestoreTaskLogsRequest,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FlrSessionRestoreTaskLogsResponse
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Get Restore Logs

     The HTTP GET request to the `/api/v8.1/flr/{flrSessionId}/restore/{restoreTaskId}/logs` endpoint
    allows you to retrieve detailed logs for each item processed by a restore task with the specified
    ID.

    Args:
        flr_session_id (UUID):
        restore_task_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        body (FlrSessionRestoreTaskLogsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlrSessionRestoreTaskLogsResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            flr_session_id=flr_session_id,
            restore_task_id=restore_task_id,
            client=client,
            body=body,
            offset=offset,
            limit=limit,
        )
    ).parsed
