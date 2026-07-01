from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_licensed_resource import PageOfLicensedResource
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["SearchPattern"] = json_search_pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/license/resources",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfLicensedResource | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfLicensedResource.from_dict(response.json())

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
) -> Response[PageOfLicensedResource | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
) -> Response[PageOfLicensedResource | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Azure Resources Consuming License Units

     The HTTP GET request to the `/license/resources` endpoint retrieves information on Azure resources
    that are currently protected by backup policies.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfLicensedResource | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
) -> PageOfLicensedResource | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Azure Resources Consuming License Units

     The HTTP GET request to the `/license/resources` endpoint retrieves information on Azure resources
    that are currently protected by backup policies.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfLicensedResource | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
) -> Response[PageOfLicensedResource | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Azure Resources Consuming License Units

     The HTTP GET request to the `/license/resources` endpoint retrieves information on Azure resources
    that are currently protected by backup policies.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfLicensedResource | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
) -> PageOfLicensedResource | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Azure Resources Consuming License Units

     The HTTP GET request to the `/license/resources` endpoint retrieves information on Azure resources
    that are currently protected by backup policies.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfLicensedResource | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            search_pattern=search_pattern,
        )
    ).parsed
