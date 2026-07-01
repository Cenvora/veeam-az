from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_share_manual_snapshot_request import FileShareManualSnapshotRequest
from ...models.job_session import JobSession
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_415 import ProblemDetails415
from ...types import Response


def _get_kwargs(
    *,
    body: FileShareManualSnapshotRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/fileShares/takeSnapshot",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[JobSession] | None:
    if response.status_code == 202:
        response_202 = []
        _response_202 = response.json()
        for response_202_item_data in _response_202:
            response_202_item = JobSession.from_dict(response_202_item_data)

            response_202.append(response_202_item)

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

    if response.status_code == 415:
        response_415 = ProblemDetails415.from_dict(response.json())

        return response_415

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[JobSession]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FileShareManualSnapshotRequest,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[JobSession]]:
    """Create Snapshots of File Shares

     The HTTP POST request to the `/fileShares/takeSnapshot` endpoint create snapshots of the specified
    Azure file shares.

    Args:
        body (FileShareManualSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[JobSession]]
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
    body: FileShareManualSnapshotRequest,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[JobSession] | None:
    """Create Snapshots of File Shares

     The HTTP POST request to the `/fileShares/takeSnapshot` endpoint create snapshots of the specified
    Azure file shares.

    Args:
        body (FileShareManualSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[JobSession]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FileShareManualSnapshotRequest,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[JobSession]]:
    """Create Snapshots of File Shares

     The HTTP POST request to the `/fileShares/takeSnapshot` endpoint create snapshots of the specified
    Azure file shares.

    Args:
        body (FileShareManualSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[JobSession]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FileShareManualSnapshotRequest,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[JobSession] | None:
    """Create Snapshots of File Shares

     The HTTP POST request to the `/fileShares/takeSnapshot` endpoint create snapshots of the specified
    Azure file shares.

    Args:
        body (FileShareManualSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[JobSession]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
