from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_worker_profile_deletion_result import AsyncOperationOfWorkerProfileDeletionResult
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import Response


def _get_kwargs(
    region_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v8.1/workers/profiles/{region_id}".format(
            region_id=quote(str(region_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfWorkerProfileDeletionResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    if response.status_code == 202:
        response_202 = AsyncOperationOfWorkerProfileDeletionResult.from_dict(response.json())

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
    AsyncOperationOfWorkerProfileDeletionResult
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
) -> Response[
    AsyncOperationOfWorkerProfileDeletionResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
]:
    """Remove Worker Profiles

     The HTTP DELETE request to the `/workers/profiles/{regionId}` endpoint removes a set of worker
    profiles for a specific Azure region.

    Args:
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfWorkerProfileDeletionResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AsyncOperationOfWorkerProfileDeletionResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Remove Worker Profiles

     The HTTP DELETE request to the `/workers/profiles/{regionId}` endpoint removes a set of worker
    profiles for a specific Azure region.

    Args:
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfWorkerProfileDeletionResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        region_id=region_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    region_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AsyncOperationOfWorkerProfileDeletionResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
]:
    """Remove Worker Profiles

     The HTTP DELETE request to the `/workers/profiles/{regionId}` endpoint removes a set of worker
    profiles for a specific Azure region.

    Args:
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfWorkerProfileDeletionResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AsyncOperationOfWorkerProfileDeletionResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Remove Worker Profiles

     The HTTP DELETE request to the `/workers/profiles/{regionId}` endpoint removes a set of worker
    profiles for a specific Azure region.

    Args:
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfWorkerProfileDeletionResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
        )
    ).parsed
