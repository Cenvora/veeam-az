from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identity_provider_metadata import IdentityProviderMetadata
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_409 import ProblemDetails409
from ...models.problem_details_415 import ProblemDetails415
from ...types import Response


def _get_kwargs(
    *,
    body: IdentityProviderMetadata,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/settings/saml2/idp/register",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | ProblemDetails415 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails403.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ProblemDetails409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = ProblemDetails415.from_dict(response.json())

        return response_415

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | ProblemDetails415]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderMetadata,
) -> Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | ProblemDetails415]:
    """Import Identity Provider Metadata

     The HTTP POST request to the `/settings/saml2/idp/register` endpoint allows you to import to Veeam
    Backup for Microsoft Azure the metadata file with the identity provider settings.

    Args:
        body (IdentityProviderMetadata):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderMetadata,
) -> Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | ProblemDetails415 | None:
    """Import Identity Provider Metadata

     The HTTP POST request to the `/settings/saml2/idp/register` endpoint allows you to import to Veeam
    Backup for Microsoft Azure the metadata file with the identity provider settings.

    Args:
        body (IdentityProviderMetadata):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | ProblemDetails415
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderMetadata,
) -> Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | ProblemDetails415]:
    """Import Identity Provider Metadata

     The HTTP POST request to the `/settings/saml2/idp/register` endpoint allows you to import to Veeam
    Backup for Microsoft Azure the metadata file with the identity provider settings.

    Args:
        body (IdentityProviderMetadata):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderMetadata,
) -> Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | ProblemDetails415 | None:
    """Import Identity Provider Metadata

     The HTTP POST request to the `/settings/saml2/idp/register` endpoint allows you to import to Veeam
    Backup for Microsoft Azure the metadata file with the identity provider settings.

    Args:
        body (IdentityProviderMetadata):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails409 | ProblemDetails415
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
