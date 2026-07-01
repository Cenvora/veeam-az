from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_worker_network_configuration_deletion_result import (
    AsyncOperationOfWorkerNetworkConfigurationDeletionResult,
)
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    region_id: str,
    *,
    subscription_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["subscriptionId"] = subscription_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v8.1/workers/networkConfiguration/{region_id}".format(
            region_id=quote(str(region_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfWorkerNetworkConfigurationDeletionResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    if response.status_code == 202:
        response_202 = AsyncOperationOfWorkerNetworkConfigurationDeletionResult.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AsyncOperationOfWorkerNetworkConfigurationDeletionResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    region_id: str,
    *,
    client: AuthenticatedClient | Client,
    subscription_id: str | Unset = UNSET,
) -> Response[
    AsyncOperationOfWorkerNetworkConfigurationDeletionResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
]:
    """Remove Worker Configuration

     The HTTP DELETE request to the /workers/networkConfiguration/{regionId} removes a worker
    configuration for a specific Azure region.

    Args:
        region_id (str):
        subscription_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfWorkerNetworkConfigurationDeletionResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region_id: str,
    *,
    client: AuthenticatedClient | Client,
    subscription_id: str | Unset = UNSET,
) -> (
    AsyncOperationOfWorkerNetworkConfigurationDeletionResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Remove Worker Configuration

     The HTTP DELETE request to the /workers/networkConfiguration/{regionId} removes a worker
    configuration for a specific Azure region.

    Args:
        region_id (str):
        subscription_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfWorkerNetworkConfigurationDeletionResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        region_id=region_id,
        client=client,
        subscription_id=subscription_id,
    ).parsed


async def asyncio_detailed(
    region_id: str,
    *,
    client: AuthenticatedClient | Client,
    subscription_id: str | Unset = UNSET,
) -> Response[
    AsyncOperationOfWorkerNetworkConfigurationDeletionResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
]:
    """Remove Worker Configuration

     The HTTP DELETE request to the /workers/networkConfiguration/{regionId} removes a worker
    configuration for a specific Azure region.

    Args:
        region_id (str):
        subscription_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfWorkerNetworkConfigurationDeletionResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region_id: str,
    *,
    client: AuthenticatedClient | Client,
    subscription_id: str | Unset = UNSET,
) -> (
    AsyncOperationOfWorkerNetworkConfigurationDeletionResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Remove Worker Configuration

     The HTTP DELETE request to the /workers/networkConfiguration/{regionId} removes a worker
    configuration for a specific Azure region.

    Args:
        region_id (str):
        subscription_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfWorkerNetworkConfigurationDeletionResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
            subscription_id=subscription_id,
        )
    ).parsed
