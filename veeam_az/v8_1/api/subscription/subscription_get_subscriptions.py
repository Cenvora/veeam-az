from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_azure_subscription import PageOfAzureSubscription
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: None | str | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    search_pattern: None | str | Unset = UNSET,
    only_ids: list[str] | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_account_id: None | str | Unset
    if isinstance(account_id, Unset):
        json_account_id = UNSET
    else:
        json_account_id = account_id
    params["AccountId"] = json_account_id

    json_tenant_id: None | str | Unset
    if isinstance(tenant_id, Unset):
        json_tenant_id = UNSET
    elif isinstance(tenant_id, UUID):
        json_tenant_id = str(tenant_id)
    else:
        json_tenant_id = tenant_id
    params["TenantId"] = json_tenant_id

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["SearchPattern"] = json_search_pattern

    json_only_ids: list[str] | None | Unset
    if isinstance(only_ids, Unset):
        json_only_ids = UNSET
    elif isinstance(only_ids, list):
        json_only_ids = only_ids

    else:
        json_only_ids = only_ids
    params["OnlyIds"] = json_only_ids

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/subscriptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfAzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfAzureSubscription.from_dict(response.json())

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
) -> Response[PageOfAzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: None | str | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    search_pattern: None | str | Unset = UNSET,
    only_ids: list[str] | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfAzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Microsoft Azure Subscriptions

     The HTTP GET request to the `/cloudInfrastructure/subscriptions` endpoint retrieves a list of
    Microsoft Azure subscriptions available to the service accounts added to Veeam Backup for Microsoft
    Azure configuration.

    Args:
        account_id (None | str | Unset):
        tenant_id (None | Unset | UUID):
        search_pattern (None | str | Unset):
        only_ids (list[str] | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfAzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        tenant_id=tenant_id,
        search_pattern=search_pattern,
        only_ids=only_ids,
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
    account_id: None | str | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    search_pattern: None | str | Unset = UNSET,
    only_ids: list[str] | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfAzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Microsoft Azure Subscriptions

     The HTTP GET request to the `/cloudInfrastructure/subscriptions` endpoint retrieves a list of
    Microsoft Azure subscriptions available to the service accounts added to Veeam Backup for Microsoft
    Azure configuration.

    Args:
        account_id (None | str | Unset):
        tenant_id (None | Unset | UUID):
        search_pattern (None | str | Unset):
        only_ids (list[str] | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfAzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        tenant_id=tenant_id,
        search_pattern=search_pattern,
        only_ids=only_ids,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: None | str | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    search_pattern: None | str | Unset = UNSET,
    only_ids: list[str] | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfAzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Microsoft Azure Subscriptions

     The HTTP GET request to the `/cloudInfrastructure/subscriptions` endpoint retrieves a list of
    Microsoft Azure subscriptions available to the service accounts added to Veeam Backup for Microsoft
    Azure configuration.

    Args:
        account_id (None | str | Unset):
        tenant_id (None | Unset | UUID):
        search_pattern (None | str | Unset):
        only_ids (list[str] | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfAzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        tenant_id=tenant_id,
        search_pattern=search_pattern,
        only_ids=only_ids,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_id: None | str | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    search_pattern: None | str | Unset = UNSET,
    only_ids: list[str] | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfAzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Microsoft Azure Subscriptions

     The HTTP GET request to the `/cloudInfrastructure/subscriptions` endpoint retrieves a list of
    Microsoft Azure subscriptions available to the service accounts added to Veeam Backup for Microsoft
    Azure configuration.

    Args:
        account_id (None | str | Unset):
        tenant_id (None | Unset | UUID):
        search_pattern (None | str | Unset):
        only_ids (list[str] | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfAzureSubscription | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            tenant_id=tenant_id,
            search_pattern=search_pattern,
            only_ids=only_ids,
            offset=offset,
            limit=limit,
        )
    ).parsed
