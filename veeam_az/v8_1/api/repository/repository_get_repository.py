from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_404 import ProblemDetails404
from ...models.repository import Repository
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repository_id: str,
    *,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_tenant_id: None | str | Unset
    if isinstance(tenant_id, Unset):
        json_tenant_id = UNSET
    elif isinstance(tenant_id, UUID):
        json_tenant_id = str(tenant_id)
    else:
        json_tenant_id = tenant_id
    params["TenantId"] = json_tenant_id

    params["ServiceAccountId"] = service_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/repositories/{repository_id}".format(
            repository_id=quote(str(repository_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | Repository | None:
    if response.status_code == 200:
        response_200 = Repository.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ProblemDetails404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | Repository]:
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
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | Repository]:
    """Get Backup Repository Data

     The HTTP GET request to the `/repositories/{repositoryId}` endpoint retrieves information on a
    backup repository with the specified ID.

    Args:
        repository_id (str):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | Repository]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | Repository | None:
    """Get Backup Repository Data

     The HTTP GET request to the `/repositories/{repositoryId}` endpoint retrieves information on a
    backup repository with the specified ID.

    Args:
        repository_id (str):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | Repository
    """

    return sync_detailed(
        repository_id=repository_id,
        client=client,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
    ).parsed


async def asyncio_detailed(
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | Repository]:
    """Get Backup Repository Data

     The HTTP GET request to the `/repositories/{repositoryId}` endpoint retrieves information on a
    backup repository with the specified ID.

    Args:
        repository_id (str):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | Repository]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        tenant_id=tenant_id,
        service_account_id=service_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    tenant_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | Repository | None:
    """Get Backup Repository Data

     The HTTP GET request to the `/repositories/{repositoryId}` endpoint retrieves information on a
    backup repository with the specified ID.

    Args:
        repository_id (str):
        tenant_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails404 | Repository
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            client=client,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
        )
    ).parsed
