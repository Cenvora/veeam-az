from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.vnet_comparison_result import VnetComparisonResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_point_id: UUID,
    *,
    only_different: bool | Unset = UNSET,
    region_id: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["OnlyDifferent"] = only_different

    json_region_id: None | str | Unset
    if isinstance(region_id, Unset):
        json_region_id = UNSET
    else:
        json_region_id = region_id
    params["RegionId"] = json_region_id

    json_resource_id: None | str | Unset
    if isinstance(resource_id, Unset):
        json_resource_id = UNSET
    else:
        json_resource_id = resource_id
    params["ResourceId"] = json_resource_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/restorePoints/vnets/{restore_point_id}/compareWithProduction".format(
            restore_point_id=quote(str(restore_point_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | list[VnetComparisonResult] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VnetComparisonResult.from_dict(response_200_item_data)

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

    if response.status_code == 404:
        response_404 = ProblemDetails404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | list[VnetComparisonResult]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    only_different: bool | Unset = UNSET,
    region_id: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
) -> Response[
    ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | list[VnetComparisonResult]
]:
    """Compare Virtual Network Configuration Restore Point Backups

     The HTTP GET request to the `/restorePoints/vnets/{restorePointId}/compareWithProduction` endpoint
    allows you to compare the current Azure virtual network configuration to the backed-up virtual
    network configuration data from the restore point with the specified ID.

    Args:
        restore_point_id (UUID):
        only_different (bool | Unset):
        region_id (None | str | Unset):
        resource_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | list[VnetComparisonResult]]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
        only_different=only_different,
        region_id=region_id,
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    only_different: bool | Unset = UNSET,
    region_id: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | list[VnetComparisonResult] | None:
    """Compare Virtual Network Configuration Restore Point Backups

     The HTTP GET request to the `/restorePoints/vnets/{restorePointId}/compareWithProduction` endpoint
    allows you to compare the current Azure virtual network configuration to the backed-up virtual
    network configuration data from the restore point with the specified ID.

    Args:
        restore_point_id (UUID):
        only_different (bool | Unset):
        region_id (None | str | Unset):
        resource_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | list[VnetComparisonResult]
    """

    return sync_detailed(
        restore_point_id=restore_point_id,
        client=client,
        only_different=only_different,
        region_id=region_id,
        resource_id=resource_id,
    ).parsed


async def asyncio_detailed(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    only_different: bool | Unset = UNSET,
    region_id: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
) -> Response[
    ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | list[VnetComparisonResult]
]:
    """Compare Virtual Network Configuration Restore Point Backups

     The HTTP GET request to the `/restorePoints/vnets/{restorePointId}/compareWithProduction` endpoint
    allows you to compare the current Azure virtual network configuration to the backed-up virtual
    network configuration data from the restore point with the specified ID.

    Args:
        restore_point_id (UUID):
        only_different (bool | Unset):
        region_id (None | str | Unset):
        resource_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | list[VnetComparisonResult]]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
        only_different=only_different,
        region_id=region_id,
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_point_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    only_different: bool | Unset = UNSET,
    region_id: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | list[VnetComparisonResult] | None:
    """Compare Virtual Network Configuration Restore Point Backups

     The HTTP GET request to the `/restorePoints/vnets/{restorePointId}/compareWithProduction` endpoint
    allows you to compare the current Azure virtual network configuration to the backed-up virtual
    network configuration data from the restore point with the specified ID.

    Args:
        restore_point_id (UUID):
        only_different (bool | Unset):
        region_id (None | str | Unset):
        resource_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | list[VnetComparisonResult]
    """

    return (
        await asyncio_detailed(
            restore_point_id=restore_point_id,
            client=client,
            only_different=only_different,
            region_id=region_id,
            resource_id=resource_id,
        )
    ).parsed
