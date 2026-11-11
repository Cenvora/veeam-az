from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.login import Login
from ...models.login_from_client import LoginFromClient
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_trace_id import ProblemDetailsTraceId
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LoginFromClient | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/oauth2/token",
    }

    if not isinstance(body, Unset):
        _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Login | ProblemDetails400 | ProblemDetailsTraceId | None:
    if response.status_code == 200:
        response_200 = Login.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetailsTraceId.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Login | ProblemDetails400 | ProblemDetailsTraceId]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoginFromClient | Unset = UNSET,
) -> Response[Login | ProblemDetails400 | ProblemDetailsTraceId]:
    """Request Authorization Tokens

     The HTTP POST request to the `/api/oauth2/token` endpoint allows you to authorize your access to the
    Veeam Backup for Microsoft Azure REST API.

    Args:
        body (LoginFromClient | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Login | ProblemDetails400 | ProblemDetailsTraceId]
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
    body: LoginFromClient | Unset = UNSET,
) -> Login | ProblemDetails400 | ProblemDetailsTraceId | None:
    """Request Authorization Tokens

     The HTTP POST request to the `/api/oauth2/token` endpoint allows you to authorize your access to the
    Veeam Backup for Microsoft Azure REST API.

    Args:
        body (LoginFromClient | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Login | ProblemDetails400 | ProblemDetailsTraceId
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoginFromClient | Unset = UNSET,
) -> Response[Login | ProblemDetails400 | ProblemDetailsTraceId]:
    """Request Authorization Tokens

     The HTTP POST request to the `/api/oauth2/token` endpoint allows you to authorize your access to the
    Veeam Backup for Microsoft Azure REST API.

    Args:
        body (LoginFromClient | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Login | ProblemDetails400 | ProblemDetailsTraceId]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LoginFromClient | Unset = UNSET,
) -> Login | ProblemDetails400 | ProblemDetailsTraceId | None:
    """Request Authorization Tokens

     The HTTP POST request to the `/api/oauth2/token` endpoint allows you to authorize your access to the
    Veeam Backup for Microsoft Azure REST API.

    Args:
        body (LoginFromClient | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Login | ProblemDetails400 | ProblemDetailsTraceId
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
