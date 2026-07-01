from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.region import Region
from ...types import Response


def _get_kwargs(
    region_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/regions/{region_id}".format(
            region_id=quote(str(region_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | Region | None:
    if response.status_code == 200:
        response_200 = Region.from_dict(response.json())

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
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | Region]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    region_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | Region]:
    """Get Azure Region Data

     The HTTP GET request to the `/cloudInfrastructure/regions/{regionId}` endpoint retrieves information
    on an Azure region with the specified ID.

    Args:
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | Region]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | Region | None:
    """Get Azure Region Data

     The HTTP GET request to the `/cloudInfrastructure/regions/{regionId}` endpoint retrieves information
    on an Azure region with the specified ID.

    Args:
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | Region
    """

    return sync_detailed(
        region_id=region_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    region_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | Region]:
    """Get Azure Region Data

     The HTTP GET request to the `/cloudInfrastructure/regions/{regionId}` endpoint retrieves information
    on an Azure region with the specified ID.

    Args:
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | Region]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | Region | None:
    """Get Azure Region Data

     The HTTP GET request to the `/cloudInfrastructure/regions/{regionId}` endpoint retrieves information
    on an Azure region with the specified ID.

    Args:
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | Region
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
        )
    ).parsed
