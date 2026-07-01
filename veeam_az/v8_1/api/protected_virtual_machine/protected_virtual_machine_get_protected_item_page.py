from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_page_of_protected_virtual_machine import AsyncOperationOfPageOfProtectedVirtualMachine
from ...models.data_retrieval_status import DataRetrievalStatus
from ...models.page_of_protected_virtual_machine import PageOfProtectedVirtualMachine
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    flr_session: bool | None | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["SearchPattern"] = json_search_pattern

    json_sync: bool | None | Unset
    if isinstance(sync, Unset):
        json_sync = UNSET
    else:
        json_sync = sync
    params["Sync"] = json_sync

    json_flr_session: bool | None | Unset
    if isinstance(flr_session, Unset):
        json_flr_session = UNSET
    else:
        json_flr_session = flr_session
    params["FlrSession"] = json_flr_session

    json_data_retrieval_statuses: list[str] | None | Unset
    if isinstance(data_retrieval_statuses, Unset):
        json_data_retrieval_statuses = UNSET
    elif isinstance(data_retrieval_statuses, list):
        json_data_retrieval_statuses = []
        for data_retrieval_statuses_type_0_item_data in data_retrieval_statuses:
            data_retrieval_statuses_type_0_item = data_retrieval_statuses_type_0_item_data.value
            json_data_retrieval_statuses.append(data_retrieval_statuses_type_0_item)

    else:
        json_data_retrieval_statuses = data_retrieval_statuses
    params["DataRetrievalStatuses"] = json_data_retrieval_statuses

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/protectedItem/virtualMachines",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfPageOfProtectedVirtualMachine
    | PageOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    if response.status_code == 200:
        response_200 = PageOfProtectedVirtualMachine.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfPageOfProtectedVirtualMachine.from_dict(response.json())

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
    AsyncOperationOfPageOfProtectedVirtualMachine
    | PageOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
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
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    flr_session: bool | None | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfProtectedVirtualMachine
    | PageOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
]:
    """Get Collection of Protected Azure VMs

     The HTTP GET request to the `/protectedItem/virtualMachines` endpoint retrieves a list of Azure VMs
    protected by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        flr_session (bool | None | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfProtectedVirtualMachine | PageOfProtectedVirtualMachine | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
        sync=sync,
        flr_session=flr_session,
        data_retrieval_statuses=data_retrieval_statuses,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    flr_session: bool | None | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfProtectedVirtualMachine
    | PageOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Collection of Protected Azure VMs

     The HTTP GET request to the `/protectedItem/virtualMachines` endpoint retrieves a list of Azure VMs
    protected by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        flr_session (bool | None | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfProtectedVirtualMachine | PageOfProtectedVirtualMachine | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
        sync=sync,
        flr_session=flr_session,
        data_retrieval_statuses=data_retrieval_statuses,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    flr_session: bool | None | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
) -> Response[
    AsyncOperationOfPageOfProtectedVirtualMachine
    | PageOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
]:
    """Get Collection of Protected Azure VMs

     The HTTP GET request to the `/protectedItem/virtualMachines` endpoint retrieves a list of Azure VMs
    protected by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        flr_session (bool | None | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfPageOfProtectedVirtualMachine | PageOfProtectedVirtualMachine | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        search_pattern=search_pattern,
        sync=sync,
        flr_session=flr_session,
        data_retrieval_statuses=data_retrieval_statuses,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    sync: bool | None | Unset = UNSET,
    flr_session: bool | None | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
) -> (
    AsyncOperationOfPageOfProtectedVirtualMachine
    | PageOfProtectedVirtualMachine
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | None
):
    """Get Collection of Protected Azure VMs

     The HTTP GET request to the `/protectedItem/virtualMachines` endpoint retrieves a list of Azure VMs
    protected by Veeam Backup for Microsoft Azure.

    Args:
        offset (int | Unset):
        limit (int | Unset):
        search_pattern (None | str | Unset):
        sync (bool | None | Unset):
        flr_session (bool | None | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfPageOfProtectedVirtualMachine | PageOfProtectedVirtualMachine | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            search_pattern=search_pattern,
            sync=sync,
            flr_session=flr_session,
            data_retrieval_statuses=data_retrieval_statuses,
        )
    ).parsed
