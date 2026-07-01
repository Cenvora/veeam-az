from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.protected_workloads_report import ProtectedWorkloadsReport
from ...models.report_period import ReportPeriod
from ...types import UNSET, Response


def _get_kwargs(
    *,
    period_flag: ReportPeriod,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period_flag = period_flag.value
    params["PeriodFlag"] = json_period_flag

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/overview/protectedWorkloads",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedWorkloadsReport | None:
    if response.status_code == 200:
        response_200 = ProtectedWorkloadsReport.from_dict(response.json())

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
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedWorkloadsReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    period_flag: ReportPeriod,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedWorkloadsReport]:
    """Get Protected Resources Report

     The HTTP GET request to the `/overview/protectedWorkloads` endpoint retrieves statistics on the
    number of available Azure resources that got protected by Veeam Backup for Microsoft Azure during a
    specific time period.

    Args:
        period_flag (ReportPeriod):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedWorkloadsReport]
    """

    kwargs = _get_kwargs(
        period_flag=period_flag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    period_flag: ReportPeriod,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedWorkloadsReport | None:
    """Get Protected Resources Report

     The HTTP GET request to the `/overview/protectedWorkloads` endpoint retrieves statistics on the
    number of available Azure resources that got protected by Veeam Backup for Microsoft Azure during a
    specific time period.

    Args:
        period_flag (ReportPeriod):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedWorkloadsReport
    """

    return sync_detailed(
        client=client,
        period_flag=period_flag,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    period_flag: ReportPeriod,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedWorkloadsReport]:
    """Get Protected Resources Report

     The HTTP GET request to the `/overview/protectedWorkloads` endpoint retrieves statistics on the
    number of available Azure resources that got protected by Veeam Backup for Microsoft Azure during a
    specific time period.

    Args:
        period_flag (ReportPeriod):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedWorkloadsReport]
    """

    kwargs = _get_kwargs(
        period_flag=period_flag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    period_flag: ReportPeriod,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedWorkloadsReport | None:
    """Get Protected Resources Report

     The HTTP GET request to the `/overview/protectedWorkloads` endpoint retrieves statistics on the
    number of available Azure resources that got protected by Veeam Backup for Microsoft Azure during a
    specific time period.

    Args:
        period_flag (ReportPeriod):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProtectedWorkloadsReport
    """

    return (
        await asyncio_detailed(
            client=client,
            period_flag=period_flag,
        )
    ).parsed
