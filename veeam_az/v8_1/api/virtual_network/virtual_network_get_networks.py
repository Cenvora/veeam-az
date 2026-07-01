from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_virtual_network import PageOfVirtualNetwork
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    region_id: None | str | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    json_region_id: None | str | Unset
    if isinstance(region_id, Unset):
        json_region_id = UNSET
    else:
        json_region_id = region_id
    params["RegionId"] = json_region_id

    json_subscription_id: None | str | Unset
    if isinstance(subscription_id, Unset):
        json_subscription_id = UNSET
    elif isinstance(subscription_id, UUID):
        json_subscription_id = str(subscription_id)
    else:
        json_subscription_id = subscription_id
    params["SubscriptionId"] = json_subscription_id

    params["ServiceAccountId"] = service_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/virtualNetworks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfVirtualNetwork | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfVirtualNetwork.from_dict(response.json())

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
) -> Response[PageOfVirtualNetwork | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
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
    region_id: None | str | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> Response[PageOfVirtualNetwork | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Virtual Networks

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks` endpoint retrieves a list of all
    virtual networks created in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        region_id (None | str | Unset):
        subscription_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfVirtualNetwork | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        region_id=region_id,
        subscription_id=subscription_id,
        service_account_id=service_account_id,
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
    region_id: None | str | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> PageOfVirtualNetwork | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Virtual Networks

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks` endpoint retrieves a list of all
    virtual networks created in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        region_id (None | str | Unset):
        subscription_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfVirtualNetwork | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        region_id=region_id,
        subscription_id=subscription_id,
        service_account_id=service_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    region_id: None | str | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> Response[PageOfVirtualNetwork | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Virtual Networks

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks` endpoint retrieves a list of all
    virtual networks created in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        region_id (None | str | Unset):
        subscription_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfVirtualNetwork | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        region_id=region_id,
        subscription_id=subscription_id,
        service_account_id=service_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    region_id: None | str | Unset = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    service_account_id: str | Unset = UNSET,
) -> PageOfVirtualNetwork | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Virtual Networks

     The HTTP GET request to the `/cloudInfrastructure/virtualNetworks` endpoint retrieves a list of all
    virtual networks created in the Microsoft Azure environment.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        region_id (None | str | Unset):
        subscription_id (None | Unset | UUID):
        service_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfVirtualNetwork | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            region_id=region_id,
            subscription_id=subscription_id,
            service_account_id=service_account_id,
        )
    ).parsed
