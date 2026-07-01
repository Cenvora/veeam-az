import datetime
from http import HTTPStatus
from io import BytesIO
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_logs_type import ExportLogsType
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    export_logs_type: ExportLogsType,
    days: int | None | Unset = UNSET,
    from_date_utc: datetime.datetime | None | Unset = UNSET,
    to_date_utc: datetime.datetime | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_export_logs_type = export_logs_type.value
    params["ExportLogsType"] = json_export_logs_type

    json_days: int | None | Unset
    if isinstance(days, Unset):
        json_days = UNSET
    else:
        json_days = days
    params["Days"] = json_days

    json_from_date_utc: None | str | Unset
    if isinstance(from_date_utc, Unset):
        json_from_date_utc = UNSET
    elif isinstance(from_date_utc, datetime.datetime):
        json_from_date_utc = from_date_utc.isoformat()
    else:
        json_from_date_utc = from_date_utc
    params["FromDateUtc"] = json_from_date_utc

    json_to_date_utc: None | str | Unset
    if isinstance(to_date_utc, Unset):
        json_to_date_utc = UNSET
    elif isinstance(to_date_utc, datetime.datetime):
        json_to_date_utc = to_date_utc.isoformat()
    else:
        json_to_date_utc = to_date_utc
    params["ToDateUtc"] = json_to_date_utc

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/system/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 201:
        response_201 = File(payload=BytesIO(response.content))

        return response_201

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    export_logs_type: ExportLogsType,
    days: int | None | Unset = UNSET,
    from_date_utc: datetime.datetime | None | Unset = UNSET,
    to_date_utc: datetime.datetime | None | Unset = UNSET,
) -> Response[Any | File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get System Logs

     The HTTP GET request to the `/system/logs` endpoint retrieves Veeam Backup for Microsoft Azure
    system logs.

    Args:
        export_logs_type (ExportLogsType):
        days (int | None | Unset):
        from_date_utc (datetime.datetime | None | Unset):
        to_date_utc (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        export_logs_type=export_logs_type,
        days=days,
        from_date_utc=from_date_utc,
        to_date_utc=to_date_utc,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    export_logs_type: ExportLogsType,
    days: int | None | Unset = UNSET,
    from_date_utc: datetime.datetime | None | Unset = UNSET,
    to_date_utc: datetime.datetime | None | Unset = UNSET,
) -> Any | File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get System Logs

     The HTTP GET request to the `/system/logs` endpoint retrieves Veeam Backup for Microsoft Azure
    system logs.

    Args:
        export_logs_type (ExportLogsType):
        days (int | None | Unset):
        from_date_utc (datetime.datetime | None | Unset):
        to_date_utc (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        export_logs_type=export_logs_type,
        days=days,
        from_date_utc=from_date_utc,
        to_date_utc=to_date_utc,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    export_logs_type: ExportLogsType,
    days: int | None | Unset = UNSET,
    from_date_utc: datetime.datetime | None | Unset = UNSET,
    to_date_utc: datetime.datetime | None | Unset = UNSET,
) -> Response[Any | File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get System Logs

     The HTTP GET request to the `/system/logs` endpoint retrieves Veeam Backup for Microsoft Azure
    system logs.

    Args:
        export_logs_type (ExportLogsType):
        days (int | None | Unset):
        from_date_utc (datetime.datetime | None | Unset):
        to_date_utc (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        export_logs_type=export_logs_type,
        days=days,
        from_date_utc=from_date_utc,
        to_date_utc=to_date_utc,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    export_logs_type: ExportLogsType,
    days: int | None | Unset = UNSET,
    from_date_utc: datetime.datetime | None | Unset = UNSET,
    to_date_utc: datetime.datetime | None | Unset = UNSET,
) -> Any | File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get System Logs

     The HTTP GET request to the `/system/logs` endpoint retrieves Veeam Backup for Microsoft Azure
    system logs.

    Args:
        export_logs_type (ExportLogsType):
        days (int | None | Unset):
        from_date_utc (datetime.datetime | None | Unset):
        to_date_utc (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            export_logs_type=export_logs_type,
            days=days,
            from_date_utc=from_date_utc,
            to_date_utc=to_date_utc,
        )
    ).parsed
