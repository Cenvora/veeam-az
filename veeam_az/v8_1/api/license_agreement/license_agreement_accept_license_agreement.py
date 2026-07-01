from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_checksum import DocumentChecksum
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[DocumentChecksum] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/licenseAgreement/accept",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails400 | ProblemDetails401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ProblemDetails400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails400 | ProblemDetails401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[DocumentChecksum] | Unset = UNSET,
) -> Response[Any | ProblemDetails400 | ProblemDetails401]:
    r"""Accept License Agreements

     The HTTP POST request to the `/licenseAgreement/accept` endpoint allows you to accept terms of the
    license agreements.<br> <div class=\"note\"><strong>NOTE</strong> <br>To read the specific agreement
    and get the parameters `checksum` and `type` required for accepting that agreement, send the HTTP
    GET request to the [Get License
    Agreements](#tag/LicenseAgreement/operation/LicenseAgreement_GetLicenseAgreement) endpoint.</div>

    Args:
        body (list[DocumentChecksum] | Unset): Specifies a list of documents to be accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails400 | ProblemDetails401]
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
    body: list[DocumentChecksum] | Unset = UNSET,
) -> Any | ProblemDetails400 | ProblemDetails401 | None:
    r"""Accept License Agreements

     The HTTP POST request to the `/licenseAgreement/accept` endpoint allows you to accept terms of the
    license agreements.<br> <div class=\"note\"><strong>NOTE</strong> <br>To read the specific agreement
    and get the parameters `checksum` and `type` required for accepting that agreement, send the HTTP
    GET request to the [Get License
    Agreements](#tag/LicenseAgreement/operation/LicenseAgreement_GetLicenseAgreement) endpoint.</div>

    Args:
        body (list[DocumentChecksum] | Unset): Specifies a list of documents to be accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails400 | ProblemDetails401
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[DocumentChecksum] | Unset = UNSET,
) -> Response[Any | ProblemDetails400 | ProblemDetails401]:
    r"""Accept License Agreements

     The HTTP POST request to the `/licenseAgreement/accept` endpoint allows you to accept terms of the
    license agreements.<br> <div class=\"note\"><strong>NOTE</strong> <br>To read the specific agreement
    and get the parameters `checksum` and `type` required for accepting that agreement, send the HTTP
    GET request to the [Get License
    Agreements](#tag/LicenseAgreement/operation/LicenseAgreement_GetLicenseAgreement) endpoint.</div>

    Args:
        body (list[DocumentChecksum] | Unset): Specifies a list of documents to be accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails400 | ProblemDetails401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[DocumentChecksum] | Unset = UNSET,
) -> Any | ProblemDetails400 | ProblemDetails401 | None:
    r"""Accept License Agreements

     The HTTP POST request to the `/licenseAgreement/accept` endpoint allows you to accept terms of the
    license agreements.<br> <div class=\"note\"><strong>NOTE</strong> <br>To read the specific agreement
    and get the parameters `checksum` and `type` required for accepting that agreement, send the HTTP
    GET request to the [Get License
    Agreements](#tag/LicenseAgreement/operation/LicenseAgreement_GetLicenseAgreement) endpoint.</div>

    Args:
        body (list[DocumentChecksum] | Unset): Specifies a list of documents to be accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails400 | ProblemDetails401
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
