from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    subnet_mask: int,
    subscription_id: None | Unset | UUID = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["subnetMask"] = subnet_mask

    json_subscription_id: None | str | Unset
    if isinstance(subscription_id, Unset):
        json_subscription_id = UNSET
    elif isinstance(subscription_id, UUID):
        json_subscription_id = str(subscription_id)
    else:
        json_subscription_id = subscription_id
    params["subscriptionId"] = json_subscription_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/virtualNetworks/firstFreeAddressSpace",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    subnet_mask: int,
    subscription_id: None | Unset | UUID = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | str]:
    """Get First Free Address Range

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks/firstFreeAddressSpace` endpoint
    retrieves free adress range that can be used to create a new virtual network.

    Args:
        subnet_mask (int):
        subscription_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | str]
    """

    kwargs = _get_kwargs(
        subnet_mask=subnet_mask,
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    subnet_mask: int,
    subscription_id: None | Unset | UUID = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | str | None:
    """Get First Free Address Range

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks/firstFreeAddressSpace` endpoint
    retrieves free adress range that can be used to create a new virtual network.

    Args:
        subnet_mask (int):
        subscription_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | str
    """

    return sync_detailed(
        client=client,
        subnet_mask=subnet_mask,
        subscription_id=subscription_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    subnet_mask: int,
    subscription_id: None | Unset | UUID = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | str]:
    """Get First Free Address Range

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks/firstFreeAddressSpace` endpoint
    retrieves free adress range that can be used to create a new virtual network.

    Args:
        subnet_mask (int):
        subscription_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | str]
    """

    kwargs = _get_kwargs(
        subnet_mask=subnet_mask,
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    subnet_mask: int,
    subscription_id: None | Unset | UUID = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | str | None:
    """Get First Free Address Range

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks/firstFreeAddressSpace` endpoint
    retrieves free adress range that can be used to create a new virtual network.

    Args:
        subnet_mask (int):
        subscription_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            subnet_mask=subnet_mask,
            subscription_id=subscription_id,
        )
    ).parsed
