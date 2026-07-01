from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ad_group_listing_result import AdGroupListingResult
from ...models.async_operation_of_ad_group_listing_result import AsyncOperationOfAdGroupListingResult
from ...models.list_ad_group_request import ListAdGroupRequest
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.problem_details_409 import ProblemDetails409
from ...models.problem_details_415 import ProblemDetails415
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ListAdGroupRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/accounts/azure/service/listAdGroups",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AdGroupListingResult
    | AsyncOperationOfAdGroupListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | None
):
    if response.status_code == 200:
        response_200 = AdGroupListingResult.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfAdGroupListingResult.from_dict(response.json())

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
    AdGroupListingResult
    | AsyncOperationOfAdGroupListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
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
    body: ListAdGroupRequest | Unset = UNSET,
) -> Response[
    AdGroupListingResult
    | AsyncOperationOfAdGroupListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
]:
    r"""Get List of Microsoft Entra Groups

     The HTTP POST request to the `/accounts/azure/service/listAdGroups` endpoint retrieves a list of
    Microsoft Entra groups available in the Microsoft Azure environment.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        body (ListAdGroupRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdGroupListingResult | AsyncOperationOfAdGroupListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415]
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
    body: ListAdGroupRequest | Unset = UNSET,
) -> (
    AdGroupListingResult
    | AsyncOperationOfAdGroupListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | None
):
    r"""Get List of Microsoft Entra Groups

     The HTTP POST request to the `/accounts/azure/service/listAdGroups` endpoint retrieves a list of
    Microsoft Entra groups available in the Microsoft Azure environment.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        body (ListAdGroupRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdGroupListingResult | AsyncOperationOfAdGroupListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListAdGroupRequest | Unset = UNSET,
) -> Response[
    AdGroupListingResult
    | AsyncOperationOfAdGroupListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
]:
    r"""Get List of Microsoft Entra Groups

     The HTTP POST request to the `/accounts/azure/service/listAdGroups` endpoint retrieves a list of
    Microsoft Entra groups available in the Microsoft Azure environment.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        body (ListAdGroupRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdGroupListingResult | AsyncOperationOfAdGroupListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListAdGroupRequest | Unset = UNSET,
) -> (
    AdGroupListingResult
    | AsyncOperationOfAdGroupListingResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails409
    | ProblemDetails415
    | None
):
    r"""Get List of Microsoft Entra Groups

     The HTTP POST request to the `/accounts/azure/service/listAdGroups` endpoint retrieves a list of
    Microsoft Entra groups available in the Microsoft Azure environment.<br> <div
    class=\"note\"><strong>NOTE</strong> <br>This operation requires authentication to the Microsoft
    Azure Cross-platform Command Line Interface (Azure CLI). That is why to complete the operation, you
    must obtain the value of the `accessTokenCache` parameter.</div>

    Args:
        body (ListAdGroupRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdGroupListingResult | AsyncOperationOfAdGroupListingResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails409 | ProblemDetails415
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
