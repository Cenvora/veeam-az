from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_cosmos_db_policy_excluded_item import PageOfCosmosDbPolicyExcludedItem
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    policy_id: UUID,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name_search_pattern: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    json_name_search_pattern: None | str | Unset
    if isinstance(name_search_pattern, Unset):
        json_name_search_pattern = UNSET
    else:
        json_name_search_pattern = name_search_pattern
    params["NameSearchPattern"] = json_name_search_pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/policies/cosmosDb/{policy_id}/excludedItems".format(
            policy_id=quote(str(policy_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PageOfCosmosDbPolicyExcludedItem
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    if response.status_code == 200:
        response_200 = PageOfCosmosDbPolicyExcludedItem.from_dict(response.json())

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
    PageOfCosmosDbPolicyExcludedItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name_search_pattern: None | str | Unset = UNSET,
) -> Response[
    PageOfCosmosDbPolicyExcludedItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    """Get Resources Excluded from Backup Policy

     The HTTP GET request to the `/policies/cosmosDb/{policyId}/excludedItems` endpoint retrieves a list
    of Cosmos DB accounts excluded from a Cosmos DB backup policy with the specified ID.

    Args:
        policy_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        name_search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfCosmosDbPolicyExcludedItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        offset=offset,
        limit=limit,
        name_search_pattern=name_search_pattern,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name_search_pattern: None | str | Unset = UNSET,
) -> (
    PageOfCosmosDbPolicyExcludedItem
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Get Resources Excluded from Backup Policy

     The HTTP GET request to the `/policies/cosmosDb/{policyId}/excludedItems` endpoint retrieves a list
    of Cosmos DB accounts excluded from a Cosmos DB backup policy with the specified ID.

    Args:
        policy_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        name_search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfCosmosDbPolicyExcludedItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
        offset=offset,
        limit=limit,
        name_search_pattern=name_search_pattern,
    ).parsed


async def asyncio_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name_search_pattern: None | str | Unset = UNSET,
) -> Response[
    PageOfCosmosDbPolicyExcludedItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    """Get Resources Excluded from Backup Policy

     The HTTP GET request to the `/policies/cosmosDb/{policyId}/excludedItems` endpoint retrieves a list
    of Cosmos DB accounts excluded from a Cosmos DB backup policy with the specified ID.

    Args:
        policy_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        name_search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfCosmosDbPolicyExcludedItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        offset=offset,
        limit=limit,
        name_search_pattern=name_search_pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name_search_pattern: None | str | Unset = UNSET,
) -> (
    PageOfCosmosDbPolicyExcludedItem
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | None
):
    """Get Resources Excluded from Backup Policy

     The HTTP GET request to the `/policies/cosmosDb/{policyId}/excludedItems` endpoint retrieves a list
    of Cosmos DB accounts excluded from a Cosmos DB backup policy with the specified ID.

    Args:
        policy_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        name_search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfCosmosDbPolicyExcludedItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            offset=offset,
            limit=limit,
            name_search_pattern=name_search_pattern,
        )
    ).parsed
