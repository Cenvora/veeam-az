from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_page_of_tenant_with_account import AsyncOperationOfPageOfTenantWithAccount
from ...models.page_of_tenant_with_account import PageOfTenantWithAccount
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["SearchPattern"] = json_search_pattern

    json_sync: bool | None | Unset
    if isinstance(sync, Unset):
        json_sync = UNSET
    else:
        json_sync = sync
    params["Sync"] = json_sync

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/tenants/withAccount",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfPageOfTenantWithAccount
    | PageOfTenantWithAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    if response.status_code == 200:
        response_200 = PageOfTenantWithAccount.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfPageOfTenantWithAccount.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AsyncOperationOfPageOfTenantWithAccount
    | PageOfTenantWithAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfTenantWithAccount
    | PageOfTenantWithAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
]:
    """Get Tenants by Service Account

     The HTTP GET request to the `/cloudInfrastructure/tenants/withAccount` endpoint retrieves tenants
    with information on service accounts linked to these tenants.

    Args:
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfTenantWithAccount | PageOfTenantWithAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        search_pattern=search_pattern,
        sync=sync,
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
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfTenantWithAccount
    | PageOfTenantWithAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Tenants by Service Account

     The HTTP GET request to the `/cloudInfrastructure/tenants/withAccount` endpoint retrieves tenants
    with information on service accounts linked to these tenants.

    Args:
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfTenantWithAccount | PageOfTenantWithAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        search_pattern=search_pattern,
        sync=sync,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfTenantWithAccount
    | PageOfTenantWithAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
]:
    """Get Tenants by Service Account

     The HTTP GET request to the `/cloudInfrastructure/tenants/withAccount` endpoint retrieves tenants
    with information on service accounts linked to these tenants.

    Args:
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfTenantWithAccount | PageOfTenantWithAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        search_pattern=search_pattern,
        sync=sync,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfTenantWithAccount
    | PageOfTenantWithAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Tenants by Service Account

     The HTTP GET request to the `/cloudInfrastructure/tenants/withAccount` endpoint retrieves tenants
    with information on service accounts linked to these tenants.

    Args:
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfTenantWithAccount | PageOfTenantWithAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            search_pattern=search_pattern,
            sync=sync,
            offset=offset,
            limit=limit,
        )
    ).parsed
