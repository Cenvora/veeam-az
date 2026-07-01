from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_provider_configuration import ServiceProviderConfiguration
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/settings/saml2/sp",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceProviderConfiguration | None:
    if response.status_code == 200:
        response_200 = ServiceProviderConfiguration.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServiceProviderConfiguration]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ServiceProviderConfiguration]:
    """Get Service Provider Settings

     The HTTP GET request to the `/settings/saml2/sp` endpoint retrieves service provider authentication
    settings that must be forwarded to the identity provider.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceProviderConfiguration]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ServiceProviderConfiguration | None:
    """Get Service Provider Settings

     The HTTP GET request to the `/settings/saml2/sp` endpoint retrieves service provider authentication
    settings that must be forwarded to the identity provider.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceProviderConfiguration
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ServiceProviderConfiguration]:
    """Get Service Provider Settings

     The HTTP GET request to the `/settings/saml2/sp` endpoint retrieves service provider authentication
    settings that must be forwarded to the identity provider.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceProviderConfiguration]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ServiceProviderConfiguration | None:
    """Get Service Provider Settings

     The HTTP GET request to the `/settings/saml2/sp` endpoint retrieves service provider authentication
    settings that must be forwarded to the identity provider.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceProviderConfiguration
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
