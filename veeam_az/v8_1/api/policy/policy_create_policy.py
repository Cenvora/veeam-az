from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.new_policy_from_client import NewPolicyFromClient
from ...models.policy import Policy
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_415 import ProblemDetails415
from ...types import Response


def _get_kwargs(
    *,
    body: NewPolicyFromClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/policies/virtualMachines",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Policy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | None:
    if response.status_code == 201:
        response_201 = Policy.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails403.from_dict(response.json())

        return response_403

    if response.status_code == 415:
        response_415 = ProblemDetails415.from_dict(response.json())

        return response_415

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Policy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewPolicyFromClient,
) -> Response[Policy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]:
    """Create Backup Policy

     The HTTP POST request to the `/policies/virtualMachines` endpoint creates a new Azure VM schedule-
    based backup policy.

    Args:
        body (NewPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Policy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]
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
    body: NewPolicyFromClient,
) -> Policy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | None:
    """Create Backup Policy

     The HTTP POST request to the `/policies/virtualMachines` endpoint creates a new Azure VM schedule-
    based backup policy.

    Args:
        body (NewPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Policy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewPolicyFromClient,
) -> Response[Policy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]:
    """Create Backup Policy

     The HTTP POST request to the `/policies/virtualMachines` endpoint creates a new Azure VM schedule-
    based backup policy.

    Args:
        body (NewPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Policy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewPolicyFromClient,
) -> Policy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | None:
    """Create Backup Policy

     The HTTP POST request to the `/policies/virtualMachines` endpoint creates a new Azure VM schedule-
    based backup policy.

    Args:
        body (NewPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Policy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
