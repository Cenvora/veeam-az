from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_worker_profile import PageOfWorkerProfile
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    region_id: None | str | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_region_id: None | str | Unset
    if isinstance(region_id, Unset):
        json_region_id = UNSET
    else:
        json_region_id = region_id
    params["RegionId"] = json_region_id

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["SearchPattern"] = json_search_pattern

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/workers/profiles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfWorkerProfile | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfWorkerProfile.from_dict(response.json())

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
) -> Response[PageOfWorkerProfile | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    region_id: None | str | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfWorkerProfile | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Worker Profiles

     The HTTP GET request to the `/workers/profiles` endpoint retrieves a list of worker profiles added
    to Veeam Backup for Microsoft Azure.

    Args:
        region_id (None | str | Unset):
        search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfWorkerProfile | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        search_pattern=search_pattern,
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
    region_id: None | str | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfWorkerProfile | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Worker Profiles

     The HTTP GET request to the `/workers/profiles` endpoint retrieves a list of worker profiles added
    to Veeam Backup for Microsoft Azure.

    Args:
        region_id (None | str | Unset):
        search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfWorkerProfile | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        region_id=region_id,
        search_pattern=search_pattern,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    region_id: None | str | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfWorkerProfile | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Worker Profiles

     The HTTP GET request to the `/workers/profiles` endpoint retrieves a list of worker profiles added
    to Veeam Backup for Microsoft Azure.

    Args:
        region_id (None | str | Unset):
        search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfWorkerProfile | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        search_pattern=search_pattern,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    region_id: None | str | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfWorkerProfile | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Worker Profiles

     The HTTP GET request to the `/workers/profiles` endpoint retrieves a list of worker profiles added
    to Veeam Backup for Microsoft Azure.

    Args:
        region_id (None | str | Unset):
        search_pattern (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfWorkerProfile | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            region_id=region_id,
            search_pattern=search_pattern,
            offset=offset,
            limit=limit,
        )
    ).parsed
