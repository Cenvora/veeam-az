from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flr_session_restore_task_start_request import FlrSessionRestoreTaskStartRequest
from ...models.flr_session_restore_task_start_response import FlrSessionRestoreTaskStartResponse
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import Response


def _get_kwargs(
    flr_session_id: UUID,
    *,
    body: FlrSessionRestoreTaskStartRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/flr/{flr_session_id}/restore".format(
            flr_session_id=quote(str(flr_session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FlrSessionRestoreTaskStartResponse
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    if response.status_code == 200:
        response_200 = FlrSessionRestoreTaskStartResponse.from_dict(response.json())

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
    FlrSessionRestoreTaskStartResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    flr_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FlrSessionRestoreTaskStartRequest,
) -> Response[
    FlrSessionRestoreTaskStartResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    """Restore Files and Folders

     The HTTP POST request to the `/api/v8.1/flr/{flrSessionId}/restore` endpoint allows you to restore
    specific items from an FLR session with the specified ID.

    Args:
        flr_session_id (UUID):
        body (FlrSessionRestoreTaskStartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlrSessionRestoreTaskStartResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        flr_session_id=flr_session_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    flr_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FlrSessionRestoreTaskStartRequest,
) -> (
    FlrSessionRestoreTaskStartResponse
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Restore Files and Folders

     The HTTP POST request to the `/api/v8.1/flr/{flrSessionId}/restore` endpoint allows you to restore
    specific items from an FLR session with the specified ID.

    Args:
        flr_session_id (UUID):
        body (FlrSessionRestoreTaskStartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlrSessionRestoreTaskStartResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        flr_session_id=flr_session_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    flr_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FlrSessionRestoreTaskStartRequest,
) -> Response[
    FlrSessionRestoreTaskStartResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    """Restore Files and Folders

     The HTTP POST request to the `/api/v8.1/flr/{flrSessionId}/restore` endpoint allows you to restore
    specific items from an FLR session with the specified ID.

    Args:
        flr_session_id (UUID):
        body (FlrSessionRestoreTaskStartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlrSessionRestoreTaskStartResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        flr_session_id=flr_session_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    flr_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FlrSessionRestoreTaskStartRequest,
) -> (
    FlrSessionRestoreTaskStartResponse
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Restore Files and Folders

     The HTTP POST request to the `/api/v8.1/flr/{flrSessionId}/restore` endpoint allows you to restore
    specific items from an FLR session with the specified ID.

    Args:
        flr_session_id (UUID):
        body (FlrSessionRestoreTaskStartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlrSessionRestoreTaskStartResponse | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            flr_session_id=flr_session_id,
            client=client,
            body=body,
        )
    ).parsed
