from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_estimation_policy_from_client import CostEstimationPolicyFromClient
from ...models.page_of_cost_estimation_item import PageOfCostEstimationItem
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_415 import ProblemDetails415
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CostEstimationPolicyFromClient,
    virtual_machine_name_filter: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_virtual_machine_name_filter: None | str | Unset
    if isinstance(virtual_machine_name_filter, Unset):
        json_virtual_machine_name_filter = UNSET
    else:
        json_virtual_machine_name_filter = virtual_machine_name_filter
    params["VirtualMachineNameFilter"] = json_virtual_machine_name_filter

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/policies/virtualMachines/estimateCost",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfCostEstimationItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | None:
    if response.status_code == 200:
        response_200 = PageOfCostEstimationItem.from_dict(response.json())

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

    if response.status_code == 415:
        response_415 = ProblemDetails415.from_dict(response.json())

        return response_415

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfCostEstimationItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CostEstimationPolicyFromClient,
    virtual_machine_name_filter: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfCostEstimationItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]:
    """Calculate Estimated Cost of Azure VM Schedule-Based Backup Policy

     The HTTP POST request to the `/policies/virtualMachines/estimateCost` endpoint calculates the
    estimated monthly cost for protecting resources by a backup policy per Azure VM.

    Args:
        virtual_machine_name_filter (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        body (CostEstimationPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfCostEstimationItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        body=body,
        virtual_machine_name_filter=virtual_machine_name_filter,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CostEstimationPolicyFromClient,
    virtual_machine_name_filter: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfCostEstimationItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | None:
    """Calculate Estimated Cost of Azure VM Schedule-Based Backup Policy

     The HTTP POST request to the `/policies/virtualMachines/estimateCost` endpoint calculates the
    estimated monthly cost for protecting resources by a backup policy per Azure VM.

    Args:
        virtual_machine_name_filter (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        body (CostEstimationPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfCostEstimationItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415
    """

    return sync_detailed(
        client=client,
        body=body,
        virtual_machine_name_filter=virtual_machine_name_filter,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CostEstimationPolicyFromClient,
    virtual_machine_name_filter: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfCostEstimationItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]:
    """Calculate Estimated Cost of Azure VM Schedule-Based Backup Policy

     The HTTP POST request to the `/policies/virtualMachines/estimateCost` endpoint calculates the
    estimated monthly cost for protecting resources by a backup policy per Azure VM.

    Args:
        virtual_machine_name_filter (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        body (CostEstimationPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfCostEstimationItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415]
    """

    kwargs = _get_kwargs(
        body=body,
        virtual_machine_name_filter=virtual_machine_name_filter,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CostEstimationPolicyFromClient,
    virtual_machine_name_filter: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfCostEstimationItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | None:
    """Calculate Estimated Cost of Azure VM Schedule-Based Backup Policy

     The HTTP POST request to the `/policies/virtualMachines/estimateCost` endpoint calculates the
    estimated monthly cost for protecting resources by a backup policy per Azure VM.

    Args:
        virtual_machine_name_filter (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        body (CostEstimationPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfCostEstimationItem | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            virtual_machine_name_filter=virtual_machine_name_filter,
            offset=offset,
            limit=limit,
        )
    ).parsed
