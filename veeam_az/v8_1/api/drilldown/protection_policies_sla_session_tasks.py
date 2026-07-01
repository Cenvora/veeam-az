from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.sla_session_task_report import SlaSessionTaskReport
from ...types import Response


def _get_kwargs(
    instance_id: str,
    session_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/policy/slaBased/slaSessionTasks/{instance_id}/{session_id}".format(
            instance_id=quote(str(instance_id), safe=""),
            session_id=quote(str(session_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaSessionTaskReport | None:
    if response.status_code == 200:
        response_200 = SlaSessionTaskReport.from_dict(response.json())

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
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaSessionTaskReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    instance_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaSessionTaskReport]:
    """Get SLA-Based Backup Policy Session Tasks

     The HTTP GET request to the `/policy/slaBased/slaSessionTasks/{instanceId}/{sessionID}` endpoint
    retrieves information on each task of the session with the specified ID.

    Args:
        instance_id (str):
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaSessionTaskReport]
    """

    kwargs = _get_kwargs(
        instance_id=instance_id,
        session_id=session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    instance_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaSessionTaskReport | None:
    """Get SLA-Based Backup Policy Session Tasks

     The HTTP GET request to the `/policy/slaBased/slaSessionTasks/{instanceId}/{sessionID}` endpoint
    retrieves information on each task of the session with the specified ID.

    Args:
        instance_id (str):
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaSessionTaskReport
    """

    return sync_detailed(
        instance_id=instance_id,
        session_id=session_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    instance_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaSessionTaskReport]:
    """Get SLA-Based Backup Policy Session Tasks

     The HTTP GET request to the `/policy/slaBased/slaSessionTasks/{instanceId}/{sessionID}` endpoint
    retrieves information on each task of the session with the specified ID.

    Args:
        instance_id (str):
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaSessionTaskReport]
    """

    kwargs = _get_kwargs(
        instance_id=instance_id,
        session_id=session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    instance_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaSessionTaskReport | None:
    """Get SLA-Based Backup Policy Session Tasks

     The HTTP GET request to the `/policy/slaBased/slaSessionTasks/{instanceId}/{sessionID}` endpoint
    retrieves information on each task of the session with the specified ID.

    Args:
        instance_id (str):
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaSessionTaskReport
    """

    return (
        await asyncio_detailed(
            instance_id=instance_id,
            session_id=session_id,
            client=client,
        )
    ).parsed
