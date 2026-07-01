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
from ...models.virtual_network import VirtualNetwork
from ...types import UNSET, Response, Unset


def _get_kwargs(
    network_id: str,
    *,
    account_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountId"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/virtualNetworks/{network_id}".format(
            network_id=quote(str(network_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | VirtualNetwork | None:
    if response.status_code == 200:
        response_200 = VirtualNetwork.from_dict(response.json())

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
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | VirtualNetwork]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    network_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | VirtualNetwork]:
    """Get Virtual Network Data

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks/{networkId}` endpoint retrieves
    information on a virtual network with the specified ID.

    Args:
        network_id (str):
        account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | VirtualNetwork]
    """

    kwargs = _get_kwargs(
        network_id=network_id,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    network_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | VirtualNetwork | None:
    """Get Virtual Network Data

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks/{networkId}` endpoint retrieves
    information on a virtual network with the specified ID.

    Args:
        network_id (str):
        account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | VirtualNetwork
    """

    return sync_detailed(
        network_id=network_id,
        client=client,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    network_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | VirtualNetwork]:
    """Get Virtual Network Data

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks/{networkId}` endpoint retrieves
    information on a virtual network with the specified ID.

    Args:
        network_id (str):
        account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | VirtualNetwork]
    """

    kwargs = _get_kwargs(
        network_id=network_id,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    network_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | VirtualNetwork | None:
    """Get Virtual Network Data

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks/{networkId}` endpoint retrieves
    information on a virtual network with the specified ID.

    Args:
        network_id (str):
        account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | VirtualNetwork
    """

    return (
        await asyncio_detailed(
            network_id=network_id,
            client=client,
            account_id=account_id,
        )
    ).parsed
