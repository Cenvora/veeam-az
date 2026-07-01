from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_string import AsyncOperationOfString
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.problem_details_409 import ProblemDetails409
from ...models.problem_details_415 import ProblemDetails415
from ...models.save_azure_account_info import SaveAzureAccountInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: SaveAzureAccountInfo | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v8.1/accounts/azure/service/updateByApp/{account_id}".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfString
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | str
    | None
):
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfString.from_dict(response.json())

        return response_202

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
) -> Response[
    AsyncOperationOfString
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | str
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SaveAzureAccountInfo | Unset = UNSET,
) -> Response[
    AsyncOperationOfString
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | str
]:
    """Edit Service Account Created Using Existing Application

     The HTTP PUT request to the `/accounts/azure/service/updateByApp/{accountId}` endpoint updates a
    specific service account created using an existing Entra ID application.

    Args:
        account_id (str):
        body (SaveAzureAccountInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfString | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | str]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SaveAzureAccountInfo | Unset = UNSET,
) -> (
    AsyncOperationOfString
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | str
    | None
):
    """Edit Service Account Created Using Existing Application

     The HTTP PUT request to the `/accounts/azure/service/updateByApp/{accountId}` endpoint updates a
    specific service account created using an existing Entra ID application.

    Args:
        account_id (str):
        body (SaveAzureAccountInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfString | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | str
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SaveAzureAccountInfo | Unset = UNSET,
) -> Response[
    AsyncOperationOfString
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | str
]:
    """Edit Service Account Created Using Existing Application

     The HTTP PUT request to the `/accounts/azure/service/updateByApp/{accountId}` endpoint updates a
    specific service account created using an existing Entra ID application.

    Args:
        account_id (str):
        body (SaveAzureAccountInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfString | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | str]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SaveAzureAccountInfo | Unset = UNSET,
) -> (
    AsyncOperationOfString
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | str
    | None
):
    """Edit Service Account Created Using Existing Application

     The HTTP PUT request to the `/accounts/azure/service/updateByApp/{accountId}` endpoint updates a
    specific service account created using an existing Entra ID application.

    Args:
        account_id (str):
        body (SaveAzureAccountInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfString | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415 | str
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
