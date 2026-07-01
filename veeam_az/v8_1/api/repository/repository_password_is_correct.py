from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_nullable_boolean import AsyncOperationOfNullableBoolean
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_404 import ProblemDetails404
from ...models.problem_details_415 import ProblemDetails415
from ...models.problem_details_429 import ProblemDetails429
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repository_id: str,
    *,
    body: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/repositories/{repository_id}/checkPassword".format(
            repository_id=quote(str(repository_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfNullableBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails415
    | ProblemDetails429
    | bool
    | None
):
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfNullableBoolean.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ProblemDetails404.from_dict(response.json())

        return response_404

    if response.status_code == 415:
        response_415 = ProblemDetails415.from_dict(response.json())

        return response_415

    if response.status_code == 429:
        response_429 = ProblemDetails429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AsyncOperationOfNullableBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails415
    | ProblemDetails429
    | bool
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
) -> Response[
    AsyncOperationOfNullableBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails415
    | ProblemDetails429
    | bool
]:
    """Verify Backup Repository Password

     The HTTP POST request to the `/repositories/{repositoryId}/checkPassword` endpoint verifies if a
    password used to encrypt a specific backup repository is valid.

    Args:
        repository_id (str):
        body (str | Unset): Specifies a password used for repository encryption.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfNullableBoolean | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails415 | ProblemDetails429 | bool]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
) -> (
    AsyncOperationOfNullableBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails415
    | ProblemDetails429
    | bool
    | None
):
    """Verify Backup Repository Password

     The HTTP POST request to the `/repositories/{repositoryId}/checkPassword` endpoint verifies if a
    password used to encrypt a specific backup repository is valid.

    Args:
        repository_id (str):
        body (str | Unset): Specifies a password used for repository encryption.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfNullableBoolean | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails415 | ProblemDetails429 | bool
    """

    return sync_detailed(
        repository_id=repository_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
) -> Response[
    AsyncOperationOfNullableBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails415
    | ProblemDetails429
    | bool
]:
    """Verify Backup Repository Password

     The HTTP POST request to the `/repositories/{repositoryId}/checkPassword` endpoint verifies if a
    password used to encrypt a specific backup repository is valid.

    Args:
        repository_id (str):
        body (str | Unset): Specifies a password used for repository encryption.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfNullableBoolean | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails415 | ProblemDetails429 | bool]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
) -> (
    AsyncOperationOfNullableBoolean
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails415
    | ProblemDetails429
    | bool
    | None
):
    """Verify Backup Repository Password

     The HTTP POST request to the `/repositories/{repositoryId}/checkPassword` endpoint verifies if a
    password used to encrypt a specific backup repository is valid.

    Args:
        repository_id (str):
        body (str | Unset): Specifies a password used for repository encryption.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfNullableBoolean | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails415 | ProblemDetails429 | bool
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            client=client,
            body=body,
        )
    ).parsed
