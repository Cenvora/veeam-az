from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_409 import ProblemDetails409
from ...models.set_deployment_mode_request import SetDeploymentModeRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SetDeploymentModeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v8.1/system/privateDeployment/state",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | None:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

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
) -> Response[Any | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetDeploymentModeRequest,
) -> Response[Any | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]:
    """Configure Deployment Mode

     The HTTP PUT request to the `/system/privateDeployment/state` allows you to choose a messaging
    service that will be used to transfer data, enable or disable the private network deployment
    functionality, and enable or disable automatic creation of service endpoints.

    Args:
        body (SetDeploymentModeRequest): Specifies the deployment mode settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]
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
    body: SetDeploymentModeRequest,
) -> Any | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | None:
    """Configure Deployment Mode

     The HTTP PUT request to the `/system/privateDeployment/state` allows you to choose a messaging
    service that will be used to transfer data, enable or disable the private network deployment
    functionality, and enable or disable automatic creation of service endpoints.

    Args:
        body (SetDeploymentModeRequest): Specifies the deployment mode settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails401 | ProblemDetails403 | ProblemDetails409
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetDeploymentModeRequest,
) -> Response[Any | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]:
    """Configure Deployment Mode

     The HTTP PUT request to the `/system/privateDeployment/state` allows you to choose a messaging
    service that will be used to transfer data, enable or disable the private network deployment
    functionality, and enable or disable automatic creation of service endpoints.

    Args:
        body (SetDeploymentModeRequest): Specifies the deployment mode settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails401 | ProblemDetails403 | ProblemDetails409]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SetDeploymentModeRequest,
) -> Any | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | None:
    """Configure Deployment Mode

     The HTTP PUT request to the `/system/privateDeployment/state` allows you to choose a messaging
    service that will be used to transfer data, enable or disable the private network deployment
    functionality, and enable or disable automatic creation of service endpoints.

    Args:
        body (SetDeploymentModeRequest): Specifies the deployment mode settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails401 | ProblemDetails403 | ProblemDetails409
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
