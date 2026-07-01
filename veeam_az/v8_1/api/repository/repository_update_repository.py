from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.job_session import JobSession
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_404 import ProblemDetails404
from ...models.problem_details_409 import ProblemDetails409
from ...models.problem_details_415 import ProblemDetails415
from ...models.problem_details_429 import ProblemDetails429
from ...models.repository_update_from_client_with_key_vault import RepositoryUpdateFromClientWithKeyVault
from ...types import Response


def _get_kwargs(
    repository_id: str,
    *,
    body: RepositoryUpdateFromClientWithKeyVault,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v8.1/repositories/{repository_id}".format(
            repository_id=quote(str(repository_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    JobSession
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | ProblemDetails429
    | None
):
    if response.status_code == 202:
        response_202 = JobSession.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ProblemDetails409.from_dict(response.json())

        return response_409

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
    JobSession
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | ProblemDetails429
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
    body: RepositoryUpdateFromClientWithKeyVault,
) -> Response[
    JobSession
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | ProblemDetails429
]:
    """Modify Backup Repository Settings

     The HTTP PUT request to the `/repositories/{repositoryId}` endpoint updates settings of a backup
    repository with the specified ID.

    Args:
        repository_id (str):
        body (RepositoryUpdateFromClientWithKeyVault):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | ProblemDetails429]
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
    body: RepositoryUpdateFromClientWithKeyVault,
) -> (
    JobSession
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | ProblemDetails429
    | None
):
    """Modify Backup Repository Settings

     The HTTP PUT request to the `/repositories/{repositoryId}` endpoint updates settings of a backup
    repository with the specified ID.

    Args:
        repository_id (str):
        body (RepositoryUpdateFromClientWithKeyVault):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | ProblemDetails429
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
    body: RepositoryUpdateFromClientWithKeyVault,
) -> Response[
    JobSession
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | ProblemDetails429
]:
    """Modify Backup Repository Settings

     The HTTP PUT request to the `/repositories/{repositoryId}` endpoint updates settings of a backup
    repository with the specified ID.

    Args:
        repository_id (str):
        body (RepositoryUpdateFromClientWithKeyVault):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | ProblemDetails429]
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
    body: RepositoryUpdateFromClientWithKeyVault,
) -> (
    JobSession
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | ProblemDetails429
    | None
):
    """Modify Backup Repository Settings

     The HTTP PUT request to the `/repositories/{repositoryId}` endpoint updates settings of a backup
    repository with the specified ID.

    Args:
        repository_id (str):
        body (RepositoryUpdateFromClientWithKeyVault):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobSession | ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | ProblemDetails429
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            client=client,
            body=body,
        )
    ).parsed
