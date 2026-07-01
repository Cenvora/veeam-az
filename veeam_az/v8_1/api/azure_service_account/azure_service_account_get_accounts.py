from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_page_of_azure_account import AsyncOperationOfPageOfAzureAccount
from ...models.azure_account_purpose import AzureAccountPurpose
from ...models.page_of_azure_account import PageOfAzureAccount
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    purpose: list[AzureAccountPurpose] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filter_: None | str | Unset
    if isinstance(filter_, Unset):
        json_filter_ = UNSET
    else:
        json_filter_ = filter_
    params["Filter"] = json_filter_

    params["Offset"] = offset

    params["Limit"] = limit

    json_purpose: list[str] | None | Unset
    if isinstance(purpose, Unset):
        json_purpose = UNSET
    elif isinstance(purpose, list):
        json_purpose = []
        for purpose_type_0_item_data in purpose:
            purpose_type_0_item = purpose_type_0_item_data.value
            json_purpose.append(purpose_type_0_item)

    else:
        json_purpose = purpose
    params["Purpose"] = json_purpose

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/accounts/azure/service",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfPageOfAzureAccount
    | PageOfAzureAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    if response.status_code == 200:
        response_200 = PageOfAzureAccount.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfPageOfAzureAccount.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AsyncOperationOfPageOfAzureAccount | PageOfAzureAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    purpose: list[AzureAccountPurpose] | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfAzureAccount | PageOfAzureAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
]:
    """Get Collection of Service Accounts

     The HTTP GET request to the `/accounts/azure/service` endpoint retrieves a list of service accounts
    added to the Veeam Backup for Microsoft Azure configuration database.

    Args:
        filter_ (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        purpose (list[AzureAccountPurpose] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfAzureAccount | PageOfAzureAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        offset=offset,
        limit=limit,
        purpose=purpose,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filter_: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    purpose: list[AzureAccountPurpose] | None | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfAzureAccount
    | PageOfAzureAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Collection of Service Accounts

     The HTTP GET request to the `/accounts/azure/service` endpoint retrieves a list of service accounts
    added to the Veeam Backup for Microsoft Azure configuration database.

    Args:
        filter_ (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        purpose (list[AzureAccountPurpose] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfAzureAccount | PageOfAzureAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        offset=offset,
        limit=limit,
        purpose=purpose,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    purpose: list[AzureAccountPurpose] | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfAzureAccount | PageOfAzureAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
]:
    """Get Collection of Service Accounts

     The HTTP GET request to the `/accounts/azure/service` endpoint retrieves a list of service accounts
    added to the Veeam Backup for Microsoft Azure configuration database.

    Args:
        filter_ (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        purpose (list[AzureAccountPurpose] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfAzureAccount | PageOfAzureAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        offset=offset,
        limit=limit,
        purpose=purpose,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filter_: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    purpose: list[AzureAccountPurpose] | None | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfAzureAccount
    | PageOfAzureAccount
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Collection of Service Accounts

     The HTTP GET request to the `/accounts/azure/service` endpoint retrieves a list of service accounts
    added to the Veeam Backup for Microsoft Azure configuration database.

    Args:
        filter_ (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        purpose (list[AzureAccountPurpose] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfAzureAccount | PageOfAzureAccount | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            offset=offset,
            limit=limit,
            purpose=purpose,
        )
    ).parsed
