from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_of_vm_protection_policy_with_sla import PageOfVmProtectionPolicyWithSla
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    policy_name: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_policy_name: None | str | Unset
    if isinstance(policy_name, Unset):
        json_policy_name = UNSET
    else:
        json_policy_name = policy_name
    params["PolicyName"] = json_policy_name

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/policy/slaBased/virtualMachines/slaReport",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfVmProtectionPolicyWithSla | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfVmProtectionPolicyWithSla.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfVmProtectionPolicyWithSla | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    policy_name: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfVmProtectionPolicyWithSla | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get SLA Compliance Information

     The HTTP GET request to the `/policy/slaBased/virtualMachines/slaReport` endpoint retrieves a list
    of SLA-based backup policies configured in Veeam Backup for Microsoft Azure and their SLA compliance
    information.

    Args:
        policy_name (None | str | Unset): Returns an SLA-based backup policy with the specified
            name.
        offset (int | Unset): Specifies the first N items of a resource collection that will be
            excluded from the response.
        limit (int | Unset): Specifies the maximum number of items of a resource collection that
            will be returned in the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfVmProtectionPolicyWithSla | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        policy_name=policy_name,
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
    policy_name: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfVmProtectionPolicyWithSla | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get SLA Compliance Information

     The HTTP GET request to the `/policy/slaBased/virtualMachines/slaReport` endpoint retrieves a list
    of SLA-based backup policies configured in Veeam Backup for Microsoft Azure and their SLA compliance
    information.

    Args:
        policy_name (None | str | Unset): Returns an SLA-based backup policy with the specified
            name.
        offset (int | Unset): Specifies the first N items of a resource collection that will be
            excluded from the response.
        limit (int | Unset): Specifies the maximum number of items of a resource collection that
            will be returned in the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfVmProtectionPolicyWithSla | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        policy_name=policy_name,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    policy_name: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfVmProtectionPolicyWithSla | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get SLA Compliance Information

     The HTTP GET request to the `/policy/slaBased/virtualMachines/slaReport` endpoint retrieves a list
    of SLA-based backup policies configured in Veeam Backup for Microsoft Azure and their SLA compliance
    information.

    Args:
        policy_name (None | str | Unset): Returns an SLA-based backup policy with the specified
            name.
        offset (int | Unset): Specifies the first N items of a resource collection that will be
            excluded from the response.
        limit (int | Unset): Specifies the maximum number of items of a resource collection that
            will be returned in the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfVmProtectionPolicyWithSla | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        policy_name=policy_name,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    policy_name: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfVmProtectionPolicyWithSla | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get SLA Compliance Information

     The HTTP GET request to the `/policy/slaBased/virtualMachines/slaReport` endpoint retrieves a list
    of SLA-based backup policies configured in Veeam Backup for Microsoft Azure and their SLA compliance
    information.

    Args:
        policy_name (None | str | Unset): Returns an SLA-based backup policy with the specified
            name.
        offset (int | Unset): Specifies the first N items of a resource collection that will be
            excluded from the response.
        limit (int | Unset): Specifies the maximum number of items of a resource collection that
            will be returned in the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfVmProtectionPolicyWithSla | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            policy_name=policy_name,
            offset=offset,
            limit=limit,
        )
    ).parsed
