from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identity_provider_configuration import IdentityProviderConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_disabled: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeDisabled"] = include_disabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/settings/saml2/idp",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IdentityProviderConfiguration | None:
    if response.status_code == 200:
        response_200 = IdentityProviderConfiguration.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IdentityProviderConfiguration]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_disabled: bool | Unset = False,
) -> Response[IdentityProviderConfiguration]:
    """Get Identity Provider Settings

     The HTTP GET request to the `/settings/saml2/idp` endpoint retrieves identity provider settings
    configured in Veeam Backup for Microsoft Azure.

    Args:
        include_disabled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityProviderConfiguration]
    """

    kwargs = _get_kwargs(
        include_disabled=include_disabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include_disabled: bool | Unset = False,
) -> IdentityProviderConfiguration | None:
    """Get Identity Provider Settings

     The HTTP GET request to the `/settings/saml2/idp` endpoint retrieves identity provider settings
    configured in Veeam Backup for Microsoft Azure.

    Args:
        include_disabled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityProviderConfiguration
    """

    return sync_detailed(
        client=client,
        include_disabled=include_disabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_disabled: bool | Unset = False,
) -> Response[IdentityProviderConfiguration]:
    """Get Identity Provider Settings

     The HTTP GET request to the `/settings/saml2/idp` endpoint retrieves identity provider settings
    configured in Veeam Backup for Microsoft Azure.

    Args:
        include_disabled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityProviderConfiguration]
    """

    kwargs = _get_kwargs(
        include_disabled=include_disabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_disabled: bool | Unset = False,
) -> IdentityProviderConfiguration | None:
    """Get Identity Provider Settings

     The HTTP GET request to the `/settings/saml2/idp` endpoint retrieves identity provider settings
    configured in Veeam Backup for Microsoft Azure.

    Args:
        include_disabled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityProviderConfiguration
    """

    return (
        await asyncio_detailed(
            client=client,
            include_disabled=include_disabled,
        )
    ).parsed
