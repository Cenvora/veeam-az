import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_file_share_restore_point import PageOfFileShareRestorePoint
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    file_share_id: None | str | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_file_share_id: None | str | Unset
    if isinstance(file_share_id, Unset):
        json_file_share_id = UNSET
    else:
        json_file_share_id = file_share_id
    params["FileShareId"] = json_file_share_id

    params["OnlyLatest"] = only_latest

    json_point_in_time: None | str | Unset
    if isinstance(point_in_time, Unset):
        json_point_in_time = UNSET
    elif isinstance(point_in_time, datetime.datetime):
        json_point_in_time = point_in_time.isoformat()
    else:
        json_point_in_time = point_in_time
    params["PointInTime"] = json_point_in_time

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/restorePoints/fileShares",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfFileShareRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfFileShareRestorePoint.from_dict(response.json())

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
) -> Response[PageOfFileShareRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    file_share_id: None | str | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfFileShareRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get File Share Restore Points

     The HTTP GET request to the `/restorePoints/fileShares` endpoint retrieves a list of restore points
    created for Azure file shares and available for Veeam Backup for Microsoft Azure.

    Args:
        file_share_id (None | str | Unset):
        only_latest (bool | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfFileShareRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        file_share_id=file_share_id,
        only_latest=only_latest,
        point_in_time=point_in_time,
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
    file_share_id: None | str | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfFileShareRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get File Share Restore Points

     The HTTP GET request to the `/restorePoints/fileShares` endpoint retrieves a list of restore points
    created for Azure file shares and available for Veeam Backup for Microsoft Azure.

    Args:
        file_share_id (None | str | Unset):
        only_latest (bool | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfFileShareRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        file_share_id=file_share_id,
        only_latest=only_latest,
        point_in_time=point_in_time,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    file_share_id: None | str | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfFileShareRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get File Share Restore Points

     The HTTP GET request to the `/restorePoints/fileShares` endpoint retrieves a list of restore points
    created for Azure file shares and available for Veeam Backup for Microsoft Azure.

    Args:
        file_share_id (None | str | Unset):
        only_latest (bool | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfFileShareRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        file_share_id=file_share_id,
        only_latest=only_latest,
        point_in_time=point_in_time,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    file_share_id: None | str | Unset = UNSET,
    only_latest: bool | Unset = UNSET,
    point_in_time: datetime.datetime | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfFileShareRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get File Share Restore Points

     The HTTP GET request to the `/restorePoints/fileShares` endpoint retrieves a list of restore points
    created for Azure file shares and available for Veeam Backup for Microsoft Azure.

    Args:
        file_share_id (None | str | Unset):
        only_latest (bool | Unset):
        point_in_time (datetime.datetime | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfFileShareRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            file_share_id=file_share_id,
            only_latest=only_latest,
            point_in_time=point_in_time,
            offset=offset,
            limit=limit,
        )
    ).parsed
