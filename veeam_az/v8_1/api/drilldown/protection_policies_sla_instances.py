import datetime
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
from ...models.sla_compliance_status_filter import SlaComplianceStatusFilter
from ...models.sla_instance_report import SlaInstanceReport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    policy_id: UUID,
    *,
    name_search_pattern: str | Unset = UNSET,
    sla_compliance_status_filter: SlaComplianceStatusFilter,
    date_from: datetime.date,
    date_to: datetime.date,
    schedule_type: ScheduleType,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["nameSearchPattern"] = name_search_pattern

    json_sla_compliance_status_filter = sla_compliance_status_filter.value
    params["SlaComplianceStatusFilter"] = json_sla_compliance_status_filter

    json_date_from = date_from.isoformat()
    params["dateFrom"] = json_date_from

    json_date_to = date_to.isoformat()
    params["dateTo"] = json_date_to

    json_schedule_type = schedule_type.value
    params["ScheduleType"] = json_schedule_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/policy/slaBased/slaInstances/{policy_id}".format(
            policy_id=quote(str(policy_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaInstanceReport | None:
    if response.status_code == 200:
        response_200 = SlaInstanceReport.from_dict(response.json())

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
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaInstanceReport]:
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
    name_search_pattern: str | Unset = UNSET,
    sla_compliance_status_filter: SlaComplianceStatusFilter,
    date_from: datetime.date,
    date_to: datetime.date,
    schedule_type: ScheduleType,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaInstanceReport]:
    """Get SLA Compliance per VM

     The HTTP GET request to the `/policy/slaBased/slaInstances/{policyId}}` endpoint retrieves SLA
    compliance information on each Azure VM protected by the SLA-based backup policy with the specified
    ID.

    Args:
        policy_id (UUID):
        name_search_pattern (str | Unset):
        sla_compliance_status_filter (SlaComplianceStatusFilter): SLA compliance status.
        date_from (datetime.date):
        date_to (datetime.date):
        schedule_type (ScheduleType): Schedule type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaInstanceReport]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        name_search_pattern=name_search_pattern,
        sla_compliance_status_filter=sla_compliance_status_filter,
        date_from=date_from,
        date_to=date_to,
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
    name_search_pattern: str | Unset = UNSET,
    sla_compliance_status_filter: SlaComplianceStatusFilter,
    date_from: datetime.date,
    date_to: datetime.date,
    schedule_type: ScheduleType,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaInstanceReport | None:
    """Get SLA Compliance per VM

     The HTTP GET request to the `/policy/slaBased/slaInstances/{policyId}}` endpoint retrieves SLA
    compliance information on each Azure VM protected by the SLA-based backup policy with the specified
    ID.

    Args:
        policy_id (UUID):
        name_search_pattern (str | Unset):
        sla_compliance_status_filter (SlaComplianceStatusFilter): SLA compliance status.
        date_from (datetime.date):
        date_to (datetime.date):
        schedule_type (ScheduleType): Schedule type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaInstanceReport
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
        name_search_pattern=name_search_pattern,
        sla_compliance_status_filter=sla_compliance_status_filter,
        date_from=date_from,
        date_to=date_to,
        schedule_type=schedule_type,
    ).parsed


async def asyncio_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    name_search_pattern: str | Unset = UNSET,
    sla_compliance_status_filter: SlaComplianceStatusFilter,
    date_from: datetime.date,
    date_to: datetime.date,
    schedule_type: ScheduleType,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaInstanceReport]:
    """Get SLA Compliance per VM

     The HTTP GET request to the `/policy/slaBased/slaInstances/{policyId}}` endpoint retrieves SLA
    compliance information on each Azure VM protected by the SLA-based backup policy with the specified
    ID.

    Args:
        policy_id (UUID):
        name_search_pattern (str | Unset):
        sla_compliance_status_filter (SlaComplianceStatusFilter): SLA compliance status.
        date_from (datetime.date):
        date_to (datetime.date):
        schedule_type (ScheduleType): Schedule type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaInstanceReport]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        name_search_pattern=name_search_pattern,
        sla_compliance_status_filter=sla_compliance_status_filter,
        date_from=date_from,
        date_to=date_to,
        schedule_type=schedule_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    name_search_pattern: str | Unset = UNSET,
    sla_compliance_status_filter: SlaComplianceStatusFilter,
    date_from: datetime.date,
    date_to: datetime.date,
    schedule_type: ScheduleType,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaInstanceReport | None:
    """Get SLA Compliance per VM

     The HTTP GET request to the `/policy/slaBased/slaInstances/{policyId}}` endpoint retrieves SLA
    compliance information on each Azure VM protected by the SLA-based backup policy with the specified
    ID.

    Args:
        policy_id (UUID):
        name_search_pattern (str | Unset):
        sla_compliance_status_filter (SlaComplianceStatusFilter): SLA compliance status.
        date_from (datetime.date):
        date_to (datetime.date):
        schedule_type (ScheduleType): Schedule type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaInstanceReport
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            name_search_pattern=name_search_pattern,
            sla_compliance_status_filter=sla_compliance_status_filter,
            date_from=date_from,
            date_to=date_to,
            schedule_type=schedule_type,
        )
    ).parsed
