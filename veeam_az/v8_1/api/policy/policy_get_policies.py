from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.job_status import JobStatus
from ...models.page_of_policy import PageOfPolicy
from ...models.policy_status import PolicyStatus
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    policy_name: None | str | Unset = UNSET,
    last_job_status: list[JobStatus] | None | Unset = UNSET,
    policy_status: list[PolicyStatus] | None | Unset = UNSET,
    virtual_machine_id: None | str | Unset = UNSET,
    repository_id: None | str | Unset = UNSET,
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

    json_last_job_status: list[str] | None | Unset
    if isinstance(last_job_status, Unset):
        json_last_job_status = UNSET
    elif isinstance(last_job_status, list):
        json_last_job_status = []
        for last_job_status_type_0_item_data in last_job_status:
            last_job_status_type_0_item = last_job_status_type_0_item_data.value
            json_last_job_status.append(last_job_status_type_0_item)

    else:
        json_last_job_status = last_job_status
    params["LastJobStatus"] = json_last_job_status

    json_policy_status: list[str] | None | Unset
    if isinstance(policy_status, Unset):
        json_policy_status = UNSET
    elif isinstance(policy_status, list):
        json_policy_status = []
        for policy_status_type_0_item_data in policy_status:
            policy_status_type_0_item = policy_status_type_0_item_data.value
            json_policy_status.append(policy_status_type_0_item)

    else:
        json_policy_status = policy_status
    params["PolicyStatus"] = json_policy_status

    json_virtual_machine_id: None | str | Unset
    if isinstance(virtual_machine_id, Unset):
        json_virtual_machine_id = UNSET
    else:
        json_virtual_machine_id = virtual_machine_id
    params["VirtualMachineId"] = json_virtual_machine_id

    json_repository_id: None | str | Unset
    if isinstance(repository_id, Unset):
        json_repository_id = UNSET
    else:
        json_repository_id = repository_id
    params["RepositoryId"] = json_repository_id

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/policies/virtualMachines",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfPolicy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfPolicy.from_dict(response.json())

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
) -> Response[PageOfPolicy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
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
    last_job_status: list[JobStatus] | None | Unset = UNSET,
    policy_status: list[PolicyStatus] | None | Unset = UNSET,
    virtual_machine_id: None | str | Unset = UNSET,
    repository_id: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfPolicy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Azure VM Schedule-Based Backup Policies

     The HTTP GET request to the `/policies/virtualMachines` endpoint retrieves a list of Azure VM
    schedule-based backup policies configured in Veeam Backup for Microsoft Azure.

    Args:
        policy_name (None | str | Unset): Returns a backup policy with the specified name.
        last_job_status (list[JobStatus] | None | Unset): Returns only backup policies with the
            specified most recent backup session status.
        policy_status (list[PolicyStatus] | None | Unset): Returns only enabled or disabled backup
            policies.
        virtual_machine_id (None | str | Unset): Returns only backup policies that protect an
            Azure VM with the specified ID.
        repository_id (None | str | Unset): Returns only backup policies that store backup files
            in a backup repository with the specified ID.
        offset (int | Unset): Specifies the first N items of a resource collection that will be
            excluded from the response.
        limit (int | Unset): Specifies the maximum number of items of a resource collection that
            will be returned in the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfPolicy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        policy_name=policy_name,
        last_job_status=last_job_status,
        policy_status=policy_status,
        virtual_machine_id=virtual_machine_id,
        repository_id=repository_id,
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
    last_job_status: list[JobStatus] | None | Unset = UNSET,
    policy_status: list[PolicyStatus] | None | Unset = UNSET,
    virtual_machine_id: None | str | Unset = UNSET,
    repository_id: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfPolicy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Azure VM Schedule-Based Backup Policies

     The HTTP GET request to the `/policies/virtualMachines` endpoint retrieves a list of Azure VM
    schedule-based backup policies configured in Veeam Backup for Microsoft Azure.

    Args:
        policy_name (None | str | Unset): Returns a backup policy with the specified name.
        last_job_status (list[JobStatus] | None | Unset): Returns only backup policies with the
            specified most recent backup session status.
        policy_status (list[PolicyStatus] | None | Unset): Returns only enabled or disabled backup
            policies.
        virtual_machine_id (None | str | Unset): Returns only backup policies that protect an
            Azure VM with the specified ID.
        repository_id (None | str | Unset): Returns only backup policies that store backup files
            in a backup repository with the specified ID.
        offset (int | Unset): Specifies the first N items of a resource collection that will be
            excluded from the response.
        limit (int | Unset): Specifies the maximum number of items of a resource collection that
            will be returned in the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfPolicy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        policy_name=policy_name,
        last_job_status=last_job_status,
        policy_status=policy_status,
        virtual_machine_id=virtual_machine_id,
        repository_id=repository_id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    policy_name: None | str | Unset = UNSET,
    last_job_status: list[JobStatus] | None | Unset = UNSET,
    policy_status: list[PolicyStatus] | None | Unset = UNSET,
    virtual_machine_id: None | str | Unset = UNSET,
    repository_id: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfPolicy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Collection of Azure VM Schedule-Based Backup Policies

     The HTTP GET request to the `/policies/virtualMachines` endpoint retrieves a list of Azure VM
    schedule-based backup policies configured in Veeam Backup for Microsoft Azure.

    Args:
        policy_name (None | str | Unset): Returns a backup policy with the specified name.
        last_job_status (list[JobStatus] | None | Unset): Returns only backup policies with the
            specified most recent backup session status.
        policy_status (list[PolicyStatus] | None | Unset): Returns only enabled or disabled backup
            policies.
        virtual_machine_id (None | str | Unset): Returns only backup policies that protect an
            Azure VM with the specified ID.
        repository_id (None | str | Unset): Returns only backup policies that store backup files
            in a backup repository with the specified ID.
        offset (int | Unset): Specifies the first N items of a resource collection that will be
            excluded from the response.
        limit (int | Unset): Specifies the maximum number of items of a resource collection that
            will be returned in the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfPolicy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        policy_name=policy_name,
        last_job_status=last_job_status,
        policy_status=policy_status,
        virtual_machine_id=virtual_machine_id,
        repository_id=repository_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    policy_name: None | str | Unset = UNSET,
    last_job_status: list[JobStatus] | None | Unset = UNSET,
    policy_status: list[PolicyStatus] | None | Unset = UNSET,
    virtual_machine_id: None | str | Unset = UNSET,
    repository_id: None | str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfPolicy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Collection of Azure VM Schedule-Based Backup Policies

     The HTTP GET request to the `/policies/virtualMachines` endpoint retrieves a list of Azure VM
    schedule-based backup policies configured in Veeam Backup for Microsoft Azure.

    Args:
        policy_name (None | str | Unset): Returns a backup policy with the specified name.
        last_job_status (list[JobStatus] | None | Unset): Returns only backup policies with the
            specified most recent backup session status.
        policy_status (list[PolicyStatus] | None | Unset): Returns only enabled or disabled backup
            policies.
        virtual_machine_id (None | str | Unset): Returns only backup policies that protect an
            Azure VM with the specified ID.
        repository_id (None | str | Unset): Returns only backup policies that store backup files
            in a backup repository with the specified ID.
        offset (int | Unset): Specifies the first N items of a resource collection that will be
            excluded from the response.
        limit (int | Unset): Specifies the maximum number of items of a resource collection that
            will be returned in the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfPolicy | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            policy_name=policy_name,
            last_job_status=last_job_status,
            policy_status=policy_status,
            virtual_machine_id=virtual_machine_id,
            repository_id=repository_id,
            offset=offset,
            limit=limit,
        )
    ).parsed
