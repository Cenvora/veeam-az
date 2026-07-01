from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_repository_validate_delete import PageOfRepositoryValidateDelete
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    repository_id: list[UUID] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_repository_id: list[str] | Unset = UNSET
    if not isinstance(repository_id, Unset):
        json_repository_id = []
        for repository_id_item_data in repository_id:
            repository_id_item = str(repository_id_item_data)
            json_repository_id.append(repository_id_item)

    params["RepositoryId"] = json_repository_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/repositories/validateDelete",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRepositoryValidateDelete | ProblemDetails400 | ProblemDetails401 | None:
    if response.status_code == 200:
        response_200 = PageOfRepositoryValidateDelete.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRepositoryValidateDelete | ProblemDetails400 | ProblemDetails401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    repository_id: list[UUID] | Unset = UNSET,
) -> Response[PageOfRepositoryValidateDelete | ProblemDetails400 | ProblemDetails401]:
    """Validate Repository Deletion

     The HTTP GET request to the `/repositories/validateDelete` endpoint validates whether the specified
    backup repositories are not used by any backup policies or storage templates and can be deleted from
    Veeam Backup for Microsoft Azure.

    Args:
        repository_id (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRepositoryValidateDelete | ProblemDetails400 | ProblemDetails401]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    repository_id: list[UUID] | Unset = UNSET,
) -> PageOfRepositoryValidateDelete | ProblemDetails400 | ProblemDetails401 | None:
    """Validate Repository Deletion

     The HTTP GET request to the `/repositories/validateDelete` endpoint validates whether the specified
    backup repositories are not used by any backup policies or storage templates and can be deleted from
    Veeam Backup for Microsoft Azure.

    Args:
        repository_id (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRepositoryValidateDelete | ProblemDetails400 | ProblemDetails401
    """

    return sync_detailed(
        client=client,
        repository_id=repository_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    repository_id: list[UUID] | Unset = UNSET,
) -> Response[PageOfRepositoryValidateDelete | ProblemDetails400 | ProblemDetails401]:
    """Validate Repository Deletion

     The HTTP GET request to the `/repositories/validateDelete` endpoint validates whether the specified
    backup repositories are not used by any backup policies or storage templates and can be deleted from
    Veeam Backup for Microsoft Azure.

    Args:
        repository_id (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRepositoryValidateDelete | ProblemDetails400 | ProblemDetails401]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    repository_id: list[UUID] | Unset = UNSET,
) -> PageOfRepositoryValidateDelete | ProblemDetails400 | ProblemDetails401 | None:
    """Validate Repository Deletion

     The HTTP GET request to the `/repositories/validateDelete` endpoint validates whether the specified
    backup repositories are not used by any backup policies or storage templates and can be deleted from
    Veeam Backup for Microsoft Azure.

    Args:
        repository_id (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRepositoryValidateDelete | ProblemDetails400 | ProblemDetails401
    """

    return (
        await asyncio_detailed(
            client=client,
            repository_id=repository_id,
        )
    ).parsed
