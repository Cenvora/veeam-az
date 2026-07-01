from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.configuration_override_ownership_request import ConfigurationOverrideOwnershipRequest
from ...models.job_session import JobSession
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ConfigurationOverrideOwnershipRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/configuration/overrideOwnership",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | list[JobSession] | None:
    if response.status_code == 202:
        response_202 = []
        _response_202 = response.json()
        for response_202_item_data in _response_202:
            response_202_item = JobSession.from_dict(response_202_item_data)

            response_202.append(response_202_item)

        return response_202

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
) -> Response[ProblemDetails400 | ProblemDetails401 | list[JobSession]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfigurationOverrideOwnershipRequest | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | list[JobSession]]:
    r"""Override Repository Owner

     The HTTP POST request to the `/configuration/overrideOwnership` endpoint allows you to override the
    owner for the backup repositories with the specified IDs to the current backup appliance. To be able
    to override the owner for a backup repository, you must first add this repository to the current
    backup appliance by sending the HTTP POST request to the [Add Backup
    Repository](#tag/Repository/operation/Repository_CreateRepository) endpoint.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>As soon as you override a repository owner, backup policies
    configured on the backup appliance to which the repository previously belonged will start
    failing.</div>

    Args:
        body (ConfigurationOverrideOwnershipRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | list[JobSession]]
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
    body: ConfigurationOverrideOwnershipRequest | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | list[JobSession] | None:
    r"""Override Repository Owner

     The HTTP POST request to the `/configuration/overrideOwnership` endpoint allows you to override the
    owner for the backup repositories with the specified IDs to the current backup appliance. To be able
    to override the owner for a backup repository, you must first add this repository to the current
    backup appliance by sending the HTTP POST request to the [Add Backup
    Repository](#tag/Repository/operation/Repository_CreateRepository) endpoint.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>As soon as you override a repository owner, backup policies
    configured on the backup appliance to which the repository previously belonged will start
    failing.</div>

    Args:
        body (ConfigurationOverrideOwnershipRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | list[JobSession]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfigurationOverrideOwnershipRequest | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | list[JobSession]]:
    r"""Override Repository Owner

     The HTTP POST request to the `/configuration/overrideOwnership` endpoint allows you to override the
    owner for the backup repositories with the specified IDs to the current backup appliance. To be able
    to override the owner for a backup repository, you must first add this repository to the current
    backup appliance by sending the HTTP POST request to the [Add Backup
    Repository](#tag/Repository/operation/Repository_CreateRepository) endpoint.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>As soon as you override a repository owner, backup policies
    configured on the backup appliance to which the repository previously belonged will start
    failing.</div>

    Args:
        body (ConfigurationOverrideOwnershipRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | list[JobSession]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ConfigurationOverrideOwnershipRequest | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | list[JobSession] | None:
    r"""Override Repository Owner

     The HTTP POST request to the `/configuration/overrideOwnership` endpoint allows you to override the
    owner for the backup repositories with the specified IDs to the current backup appliance. To be able
    to override the owner for a backup repository, you must first add this repository to the current
    backup appliance by sending the HTTP POST request to the [Add Backup
    Repository](#tag/Repository/operation/Repository_CreateRepository) endpoint.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>As soon as you override a repository owner, backup policies
    configured on the backup appliance to which the repository previously belonged will start
    failing.</div>

    Args:
        body (ConfigurationOverrideOwnershipRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | list[JobSession]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
