from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.vm_size import VmSize
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    region: str,
    name_search_pattern: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["region"] = region

    json_name_search_pattern: None | str | Unset
    if isinstance(name_search_pattern, Unset):
        json_name_search_pattern = UNSET
    else:
        json_name_search_pattern = name_search_pattern
    params["NameSearchPattern"] = json_name_search_pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/virtualMachineWorkerSizes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[VmSize] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VmSize.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[VmSize]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    region: str,
    name_search_pattern: None | str | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[VmSize]]:
    """Get Collection of Worker VM Sizes

     The HTTP GET request to the `/cloudInfrastructure/virtualMachineWorkerSizes` endpoint retrieves a
    list of Azure VM sizes that can be used to launch worker instances.

    Args:
        region (str):
        name_search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[VmSize]]
    """

    kwargs = _get_kwargs(
        region=region,
        name_search_pattern=name_search_pattern,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    region: str,
    name_search_pattern: None | str | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[VmSize] | None:
    """Get Collection of Worker VM Sizes

     The HTTP GET request to the `/cloudInfrastructure/virtualMachineWorkerSizes` endpoint retrieves a
    list of Azure VM sizes that can be used to launch worker instances.

    Args:
        region (str):
        name_search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[VmSize]
    """

    return sync_detailed(
        client=client,
        region=region,
        name_search_pattern=name_search_pattern,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    region: str,
    name_search_pattern: None | str | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[VmSize]]:
    """Get Collection of Worker VM Sizes

     The HTTP GET request to the `/cloudInfrastructure/virtualMachineWorkerSizes` endpoint retrieves a
    list of Azure VM sizes that can be used to launch worker instances.

    Args:
        region (str):
        name_search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[VmSize]]
    """

    kwargs = _get_kwargs(
        region=region,
        name_search_pattern=name_search_pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    region: str,
    name_search_pattern: None | str | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[VmSize] | None:
    """Get Collection of Worker VM Sizes

     The HTTP GET request to the `/cloudInfrastructure/virtualMachineWorkerSizes` endpoint retrieves a
    list of Azure VM sizes that can be used to launch worker instances.

    Args:
        region (str):
        name_search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | list[VmSize]
    """

    return (
        await asyncio_detailed(
            client=client,
            region=region,
            name_search_pattern=name_search_pattern,
        )
    ).parsed
