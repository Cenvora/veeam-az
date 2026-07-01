import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_sla_session_report_row import PageOfSlaSessionReportRow
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.schedule_type import ScheduleType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    policy_id: UUID,
    instance_id: str,
    *,
    date_from: datetime.date,
    date_to: datetime.date,
    schedule_type: ScheduleType | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_date_from = date_from.isoformat()
    params["dateFrom"] = json_date_from

    json_date_to = date_to.isoformat()
    params["dateTo"] = json_date_to

    json_schedule_type: str | Unset = UNSET
    if not isinstance(schedule_type, Unset):
        json_schedule_type = schedule_type.value

    params["ScheduleType"] = json_schedule_type

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/policy/slaBased/slaSessions/{policy_id}/{instance_id}".format(
            policy_id=quote(str(policy_id), safe=""),
            instance_id=quote(str(instance_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfSlaSessionReportRow | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfSlaSessionReportRow.from_dict(response.json())

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
) -> Response[PageOfSlaSessionReportRow | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_id: UUID,
    instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    date_from: datetime.date,
    date_to: datetime.date,
    schedule_type: ScheduleType | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfSlaSessionReportRow | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get SLA-Based Backup Policy Sessions per VM

     The HTTP GET request to the `/policy/slaBased/slaSessions/{policyId}/{instanceId}` endpoint
    retrieves information on each session performed for a specific Azure VM protected by the SLA-based
    backup policy with the specified ID.

    Args:
        policy_id (UUID):
        instance_id (str):
        date_from (datetime.date):
        date_to (datetime.date):
        schedule_type (ScheduleType | Unset): Schedule type.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfSlaSessionReportRow | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        instance_id=instance_id,
        date_from=date_from,
        date_to=date_to,
        schedule_type=schedule_type,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy_id: UUID,
    instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    date_from: datetime.date,
    date_to: datetime.date,
    schedule_type: ScheduleType | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfSlaSessionReportRow | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get SLA-Based Backup Policy Sessions per VM

     The HTTP GET request to the `/policy/slaBased/slaSessions/{policyId}/{instanceId}` endpoint
    retrieves information on each session performed for a specific Azure VM protected by the SLA-based
    backup policy with the specified ID.

    Args:
        policy_id (UUID):
        instance_id (str):
        date_from (datetime.date):
        date_to (datetime.date):
        schedule_type (ScheduleType | Unset): Schedule type.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfSlaSessionReportRow | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        policy_id=policy_id,
        instance_id=instance_id,
        client=client,
        date_from=date_from,
        date_to=date_to,
        schedule_type=schedule_type,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    policy_id: UUID,
    instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    date_from: datetime.date,
    date_to: datetime.date,
    schedule_type: ScheduleType | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfSlaSessionReportRow | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get SLA-Based Backup Policy Sessions per VM

     The HTTP GET request to the `/policy/slaBased/slaSessions/{policyId}/{instanceId}` endpoint
    retrieves information on each session performed for a specific Azure VM protected by the SLA-based
    backup policy with the specified ID.

    Args:
        policy_id (UUID):
        instance_id (str):
        date_from (datetime.date):
        date_to (datetime.date):
        schedule_type (ScheduleType | Unset): Schedule type.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfSlaSessionReportRow | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        instance_id=instance_id,
        date_from=date_from,
        date_to=date_to,
        schedule_type=schedule_type,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: UUID,
    instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    date_from: datetime.date,
    date_to: datetime.date,
    schedule_type: ScheduleType | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfSlaSessionReportRow | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get SLA-Based Backup Policy Sessions per VM

     The HTTP GET request to the `/policy/slaBased/slaSessions/{policyId}/{instanceId}` endpoint
    retrieves information on each session performed for a specific Azure VM protected by the SLA-based
    backup policy with the specified ID.

    Args:
        policy_id (UUID):
        instance_id (str):
        date_from (datetime.date):
        date_to (datetime.date):
        schedule_type (ScheduleType | Unset): Schedule type.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfSlaSessionReportRow | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            instance_id=instance_id,
            client=client,
            date_from=date_from,
            date_to=date_to,
            schedule_type=schedule_type,
            offset=offset,
            limit=limit,
        )
    ).parsed
