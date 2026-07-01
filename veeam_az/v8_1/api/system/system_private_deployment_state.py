from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.private_deployment_state import PrivateDeploymentState
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_409 import ProblemDetails409
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/system/privateDeployment/state",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PrivateDeploymentState | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | None:
    if response.status_code == 200:
        response_200 = PrivateDeploymentState.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails403.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ProblemDetails409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PrivateDeploymentState | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[PrivateDeploymentState | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]:
    """Get Deployment Mode

     The HTTP GET request to the `/system/privateDeployment/state` endpoint retrieves the state of the
    private network deployment functionality as well as other Deployment Mode settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrivateDeploymentState | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> PrivateDeploymentState | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | None:
    """Get Deployment Mode

     The HTTP GET request to the `/system/privateDeployment/state` endpoint retrieves the state of the
    private network deployment functionality as well as other Deployment Mode settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PrivateDeploymentState | ProblemDetails401 | ProblemDetails403 | ProblemDetails409
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[PrivateDeploymentState | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]:
    """Get Deployment Mode

     The HTTP GET request to the `/system/privateDeployment/state` endpoint retrieves the state of the
    private network deployment functionality as well as other Deployment Mode settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrivateDeploymentState | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> PrivateDeploymentState | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | None:
    """Get Deployment Mode

     The HTTP GET request to the `/system/privateDeployment/state` endpoint retrieves the state of the
    private network deployment functionality as well as other Deployment Mode settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PrivateDeploymentState | ProblemDetails401 | ProblemDetails403 | ProblemDetails409
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
