from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_storage_template import PageOfStorageTemplate
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: None | str | Unset = UNSET,
    repository_id: None | Unset | UUID = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_name: None | str | Unset
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["Name"] = json_name

    json_repository_id: None | str | Unset
    if isinstance(repository_id, Unset):
        json_repository_id = UNSET
    elif isinstance(repository_id, UUID):
        json_repository_id = str(repository_id)
    else:
        json_repository_id = repository_id
    params["RepositoryId"] = json_repository_id

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/policyTemplates/storageTemplate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfStorageTemplate | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfStorageTemplate.from_dict(response.json())

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
) -> Response[PageOfStorageTemplate | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    repository_id: None | Unset | UUID = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfStorageTemplate | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Storage Templates

     The HTTP GET request to the `/policyTemplates/storageTemplate` endpoint retrieves a list of storage
    templates configured in Veeam Backup for Microsoft Azure.

    Args:
        name (None | str | Unset):
        repository_id (None | Unset | UUID): Returns only storage templates that use a repository
            with the specified ID.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfStorageTemplate | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        name=name,
        repository_id=repository_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    repository_id: None | Unset | UUID = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfStorageTemplate | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Storage Templates

     The HTTP GET request to the `/policyTemplates/storageTemplate` endpoint retrieves a list of storage
    templates configured in Veeam Backup for Microsoft Azure.

    Args:
        name (None | str | Unset):
        repository_id (None | Unset | UUID): Returns only storage templates that use a repository
            with the specified ID.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfStorageTemplate | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        name=name,
        repository_id=repository_id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    repository_id: None | Unset | UUID = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfStorageTemplate | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Storage Templates

     The HTTP GET request to the `/policyTemplates/storageTemplate` endpoint retrieves a list of storage
    templates configured in Veeam Backup for Microsoft Azure.

    Args:
        name (None | str | Unset):
        repository_id (None | Unset | UUID): Returns only storage templates that use a repository
            with the specified ID.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfStorageTemplate | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        name=name,
        repository_id=repository_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    repository_id: None | Unset | UUID = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfStorageTemplate | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Storage Templates

     The HTTP GET request to the `/policyTemplates/storageTemplate` endpoint retrieves a list of storage
    templates configured in Veeam Backup for Microsoft Azure.

    Args:
        name (None | str | Unset):
        repository_id (None | Unset | UUID): Returns only storage templates that use a repository
            with the specified ID.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfStorageTemplate | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            repository_id=repository_id,
            offset=offset,
            limit=limit,
        )
    ).parsed
