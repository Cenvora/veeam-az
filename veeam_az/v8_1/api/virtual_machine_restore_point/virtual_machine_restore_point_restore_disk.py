from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disk_bulk_restore_options import DiskBulkRestoreOptions
from ...models.job_session import JobSession
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.problem_details_415 import ProblemDetails415
from ...types import Response


def _get_kwargs(
    restore_point_id: UUID,
    *,
    body: DiskBulkRestoreOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/restorePoints/virtualMachines/{restore_point_id}/restoreDisk".format(
            restore_point_id=quote(str(restore_point_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    JobSession
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | None
):
    if response.status_code == 202:
        response_202 = JobSession.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ProblemDetails404.from_dict(response.json())

        return response_404

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
    JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DiskBulkRestoreOptions,
) -> Response[
    JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415
]:
    """Perform Virtual Disk Restore

     The HTTP POST request to the `/restorePoints/virtualMachines/{restorePointId}/restoreDisk` endpoint
    launches a disk restore operation using a specific restore point of an Azure VM.

    Args:
        restore_point_id (UUID):
        body (DiskBulkRestoreOptions): Specifies disk restore settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DiskBulkRestoreOptions,
) -> (
    JobSession
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | None
):
    """Perform Virtual Disk Restore

     The HTTP POST request to the `/restorePoints/virtualMachines/{restorePointId}/restoreDisk` endpoint
    launches a disk restore operation using a specific restore point of an Azure VM.

    Args:
        restore_point_id (UUID):
        body (DiskBulkRestoreOptions): Specifies disk restore settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415
    """

    return sync_detailed(
        restore_point_id=restore_point_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DiskBulkRestoreOptions,
) -> Response[
    JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415
]:
    """Perform Virtual Disk Restore

     The HTTP POST request to the `/restorePoints/virtualMachines/{restorePointId}/restoreDisk` endpoint
    launches a disk restore operation using a specific restore point of an Azure VM.

    Args:
        restore_point_id (UUID):
        body (DiskBulkRestoreOptions): Specifies disk restore settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DiskBulkRestoreOptions,
) -> (
    JobSession
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | None
):
    """Perform Virtual Disk Restore

     The HTTP POST request to the `/restorePoints/virtualMachines/{restorePointId}/restoreDisk` endpoint
    launches a disk restore operation using a specific restore point of an Azure VM.

    Args:
        restore_point_id (UUID):
        body (DiskBulkRestoreOptions): Specifies disk restore settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415
    """

    return (
        await asyncio_detailed(
            restore_point_id=restore_point_id,
            client=client,
            body=body,
        )
    ).parsed
