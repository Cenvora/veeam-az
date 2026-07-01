from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.certificate_info import CertificateInfo
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/settings/certificates",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails401 | ProblemDetails403 | list[CertificateInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CertificateInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

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
) -> Response[ProblemDetails401 | ProblemDetails403 | list[CertificateInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails401 | ProblemDetails403 | list[CertificateInfo]]:
    """Get Collection of Certificates

     The HTTP GET request to the `/settings/certificates` endpoint retrieves TLS certificates used to
    establish secure communication between the web browser and the backup appliance or worker instances.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails401 | ProblemDetails403 | list[CertificateInfo]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails401 | ProblemDetails403 | list[CertificateInfo] | None:
    """Get Collection of Certificates

     The HTTP GET request to the `/settings/certificates` endpoint retrieves TLS certificates used to
    establish secure communication between the web browser and the backup appliance or worker instances.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails401 | ProblemDetails403 | list[CertificateInfo]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails401 | ProblemDetails403 | list[CertificateInfo]]:
    """Get Collection of Certificates

     The HTTP GET request to the `/settings/certificates` endpoint retrieves TLS certificates used to
    establish secure communication between the web browser and the backup appliance or worker instances.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails401 | ProblemDetails403 | list[CertificateInfo]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails401 | ProblemDetails403 | list[CertificateInfo] | None:
    """Get Collection of Certificates

     The HTTP GET request to the `/settings/certificates` endpoint retrieves TLS certificates used to
    establish secure communication between the web browser and the backup appliance or worker instances.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails401 | ProblemDetails403 | list[CertificateInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
