from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.schedule_type import ScheduleType
from ...models.sla_filter_session_status import SlaFilterSessionStatus
from ...models.sla_time_series_point import SlaTimeSeriesPoint
from ...types import UNSET, Response, Unset


def _get_kwargs(
    policy_id: UUID,
    *,
    sla_filter_session_status: SlaFilterSessionStatus | Unset = UNSET,
    schedule_type: ScheduleType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sla_filter_session_status: str | Unset = UNSET
    if not isinstance(sla_filter_session_status, Unset):
        json_sla_filter_session_status = sla_filter_session_status.value

    params["SlaFilterSessionStatus"] = json_sla_filter_session_status

    json_schedule_type: str | Unset = UNSET
    if not isinstance(schedule_type, Unset):
        json_schedule_type = schedule_type.value

    params["ScheduleType"] = json_schedule_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/policy/slaBased/slaTimeSeries/{policy_id}".format(
            policy_id=quote(str(policy_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[SlaTimeSeriesPoint] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SlaTimeSeriesPoint.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[SlaTimeSeriesPoint]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    sla_filter_session_status: SlaFilterSessionStatus | Unset = UNSET,
    schedule_type: ScheduleType | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[SlaTimeSeriesPoint]]:
    """Get SLA Results per Period

     The HTTP GET request to the `/policy/slaBased/slaTimeSeries/{policyId}` endpoint retrieves
    information on each available calculated period (day, week or month) of a specific schedule type
    configured the SLA-based backup policy with the specified ID.

    Args:
        policy_id (UUID):
        sla_filter_session_status (SlaFilterSessionStatus | Unset): Session status.
        schedule_type (ScheduleType | Unset): Schedule type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[SlaTimeSeriesPoint]]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        sla_filter_session_status=sla_filter_session_status,
        schedule_type=schedule_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    sla_filter_session_status: SlaFilterSessionStatus | Unset = UNSET,
    schedule_type: ScheduleType | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[SlaTimeSeriesPoint] | None:
    """Get SLA Results per Period

     The HTTP GET request to the `/policy/slaBased/slaTimeSeries/{policyId}` endpoint retrieves
    information on each available calculated period (day, week or month) of a specific schedule type
    configured the SLA-based backup policy with the specified ID.

    Args:
        policy_id (UUID):
        sla_filter_session_status (SlaFilterSessionStatus | Unset): Session status.
        schedule_type (ScheduleType | Unset): Schedule type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[SlaTimeSeriesPoint]
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
        sla_filter_session_status=sla_filter_session_status,
        schedule_type=schedule_type,
    ).parsed


async def asyncio_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    sla_filter_session_status: SlaFilterSessionStatus | Unset = UNSET,
    schedule_type: ScheduleType | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[SlaTimeSeriesPoint]]:
    """Get SLA Results per Period

     The HTTP GET request to the `/policy/slaBased/slaTimeSeries/{policyId}` endpoint retrieves
    information on each available calculated period (day, week or month) of a specific schedule type
    configured the SLA-based backup policy with the specified ID.

    Args:
        policy_id (UUID):
        sla_filter_session_status (SlaFilterSessionStatus | Unset): Session status.
        schedule_type (ScheduleType | Unset): Schedule type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[SlaTimeSeriesPoint]]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        sla_filter_session_status=sla_filter_session_status,
        schedule_type=schedule_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    sla_filter_session_status: SlaFilterSessionStatus | Unset = UNSET,
    schedule_type: ScheduleType | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[SlaTimeSeriesPoint] | None:
    """Get SLA Results per Period

     The HTTP GET request to the `/policy/slaBased/slaTimeSeries/{policyId}` endpoint retrieves
    information on each available calculated period (day, week or month) of a specific schedule type
    configured the SLA-based backup policy with the specified ID.

    Args:
        policy_id (UUID):
        sla_filter_session_status (SlaFilterSessionStatus | Unset): Session status.
        schedule_type (ScheduleType | Unset): Schedule type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[SlaTimeSeriesPoint]
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            sla_filter_session_status=sla_filter_session_status,
            schedule_type=schedule_type,
        )
    ).parsed
