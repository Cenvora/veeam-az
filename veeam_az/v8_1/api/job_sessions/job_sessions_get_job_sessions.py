import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.job_session_filter_type import JobSessionFilterType
from ...models.job_status import JobStatus
from ...models.page_of_job_session import PageOfJobSession
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    policy_id: None | Unset | UUID = UNSET,
    filter_: None | str | Unset = UNSET,
    status: list[JobStatus] | None | Unset = UNSET,
    types: list[JobSessionFilterType] | None | Unset = UNSET,
    from_utc: datetime.datetime | None | Unset = UNSET,
    to_utc: datetime.datetime | None | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    json_policy_id: None | str | Unset
    if isinstance(policy_id, Unset):
        json_policy_id = UNSET
    elif isinstance(policy_id, UUID):
        json_policy_id = str(policy_id)
    else:
        json_policy_id = policy_id
    params["PolicyId"] = json_policy_id

    json_filter_: None | str | Unset
    if isinstance(filter_, Unset):
        json_filter_ = UNSET
    else:
        json_filter_ = filter_
    params["Filter"] = json_filter_

    json_status: list[str] | None | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, list):
        json_status = []
        for status_type_0_item_data in status:
            status_type_0_item = status_type_0_item_data.value
            json_status.append(status_type_0_item)

    else:
        json_status = status
    params["Status"] = json_status

    json_types: list[str] | None | Unset
    if isinstance(types, Unset):
        json_types = UNSET
    elif isinstance(types, list):
        json_types = []
        for types_type_0_item_data in types:
            types_type_0_item = types_type_0_item_data.value
            json_types.append(types_type_0_item)

    else:
        json_types = types
    params["Types"] = json_types

    json_from_utc: None | str | Unset
    if isinstance(from_utc, Unset):
        json_from_utc = UNSET
    elif isinstance(from_utc, datetime.datetime):
        json_from_utc = from_utc.isoformat()
    else:
        json_from_utc = from_utc
    params["FromUtc"] = json_from_utc

    json_to_utc: None | str | Unset
    if isinstance(to_utc, Unset):
        json_to_utc = UNSET
    elif isinstance(to_utc, datetime.datetime):
        json_to_utc = to_utc.isoformat()
    else:
        json_to_utc = to_utc
    params["ToUtc"] = json_to_utc

    json_resource_id: None | str | Unset
    if isinstance(resource_id, Unset):
        json_resource_id = UNSET
    else:
        json_resource_id = resource_id
    params["ResourceId"] = json_resource_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/jobSessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfJobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfJobSession.from_dict(response.json())

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
) -> Response[PageOfJobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    policy_id: None | Unset | UUID = UNSET,
    filter_: None | str | Unset = UNSET,
    status: list[JobStatus] | None | Unset = UNSET,
    types: list[JobSessionFilterType] | None | Unset = UNSET,
    from_utc: datetime.datetime | None | Unset = UNSET,
    to_utc: datetime.datetime | None | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
) -> Response[PageOfJobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Sessions

     The HTTP GET request to the `/jobSessions` endpoint retrieves a list of Veeam Backup for Microsoft
    Azure sessions.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        policy_id (None | Unset | UUID):
        filter_ (None | str | Unset):
        status (list[JobStatus] | None | Unset):
        types (list[JobSessionFilterType] | None | Unset):
        from_utc (datetime.datetime | None | Unset):
        to_utc (datetime.datetime | None | Unset):
        resource_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfJobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        policy_id=policy_id,
        filter_=filter_,
        status=status,
        types=types,
        from_utc=from_utc,
        to_utc=to_utc,
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    policy_id: None | Unset | UUID = UNSET,
    filter_: None | str | Unset = UNSET,
    status: list[JobStatus] | None | Unset = UNSET,
    types: list[JobSessionFilterType] | None | Unset = UNSET,
    from_utc: datetime.datetime | None | Unset = UNSET,
    to_utc: datetime.datetime | None | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
) -> PageOfJobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Sessions

     The HTTP GET request to the `/jobSessions` endpoint retrieves a list of Veeam Backup for Microsoft
    Azure sessions.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        policy_id (None | Unset | UUID):
        filter_ (None | str | Unset):
        status (list[JobStatus] | None | Unset):
        types (list[JobSessionFilterType] | None | Unset):
        from_utc (datetime.datetime | None | Unset):
        to_utc (datetime.datetime | None | Unset):
        resource_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfJobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        policy_id=policy_id,
        filter_=filter_,
        status=status,
        types=types,
        from_utc=from_utc,
        to_utc=to_utc,
        resource_id=resource_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    policy_id: None | Unset | UUID = UNSET,
    filter_: None | str | Unset = UNSET,
    status: list[JobStatus] | None | Unset = UNSET,
    types: list[JobSessionFilterType] | None | Unset = UNSET,
    from_utc: datetime.datetime | None | Unset = UNSET,
    to_utc: datetime.datetime | None | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
) -> Response[PageOfJobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Sessions

     The HTTP GET request to the `/jobSessions` endpoint retrieves a list of Veeam Backup for Microsoft
    Azure sessions.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        policy_id (None | Unset | UUID):
        filter_ (None | str | Unset):
        status (list[JobStatus] | None | Unset):
        types (list[JobSessionFilterType] | None | Unset):
        from_utc (datetime.datetime | None | Unset):
        to_utc (datetime.datetime | None | Unset):
        resource_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfJobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        policy_id=policy_id,
        filter_=filter_,
        status=status,
        types=types,
        from_utc=from_utc,
        to_utc=to_utc,
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    policy_id: None | Unset | UUID = UNSET,
    filter_: None | str | Unset = UNSET,
    status: list[JobStatus] | None | Unset = UNSET,
    types: list[JobSessionFilterType] | None | Unset = UNSET,
    from_utc: datetime.datetime | None | Unset = UNSET,
    to_utc: datetime.datetime | None | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
) -> PageOfJobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Sessions

     The HTTP GET request to the `/jobSessions` endpoint retrieves a list of Veeam Backup for Microsoft
    Azure sessions.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        policy_id (None | Unset | UUID):
        filter_ (None | str | Unset):
        status (list[JobStatus] | None | Unset):
        types (list[JobSessionFilterType] | None | Unset):
        from_utc (datetime.datetime | None | Unset):
        to_utc (datetime.datetime | None | Unset):
        resource_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfJobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            policy_id=policy_id,
            filter_=filter_,
            status=status,
            types=types,
            from_utc=from_utc,
            to_utc=to_utc,
            resource_id=resource_id,
        )
    ).parsed
