from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    azure_account_id: None | Unset | UUID = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    resource_group_name: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_azure_account_id: None | str | Unset
    if isinstance(azure_account_id, Unset):
        json_azure_account_id = UNSET
    elif isinstance(azure_account_id, UUID):
        json_azure_account_id = str(azure_account_id)
    else:
        json_azure_account_id = azure_account_id
    params["azureAccountId"] = json_azure_account_id

    json_subscription_id: None | str | Unset
    if isinstance(subscription_id, Unset):
        json_subscription_id = UNSET
    elif isinstance(subscription_id, UUID):
        json_subscription_id = str(subscription_id)
    else:
        json_subscription_id = subscription_id
    params["subscriptionId"] = json_subscription_id

    json_resource_group_name: None | str | Unset
    if isinstance(resource_group_name, Unset):
        json_resource_group_name = UNSET
    else:
        json_resource_group_name = resource_group_name
    params["resourceGroupName"] = json_resource_group_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/workers/networkConfiguration/setWorkerDeploymentOptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    azure_account_id: None | Unset | UUID = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    resource_group_name: None | str | Unset = UNSET,
) -> Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    """Specify Worker Location and Service Account

     The HTTP POST request to the `/workers/networkConfiguration/setWorkerDeploymentOptions` endpoint
    allows you to specify a service account that will be used to launch worker instances, and also a
    subscription and a resource group in which the worker instances will be launched.

    Args:
        azure_account_id (None | Unset | UUID):
        subscription_id (None | Unset | UUID):
        resource_group_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        azure_account_id=azure_account_id,
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    azure_account_id: None | Unset | UUID = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    resource_group_name: None | str | Unset = UNSET,
) -> Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    """Specify Worker Location and Service Account

     The HTTP POST request to the `/workers/networkConfiguration/setWorkerDeploymentOptions` endpoint
    allows you to specify a service account that will be used to launch worker instances, and also a
    subscription and a resource group in which the worker instances will be launched.

    Args:
        azure_account_id (None | Unset | UUID):
        subscription_id (None | Unset | UUID):
        resource_group_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        client=client,
        azure_account_id=azure_account_id,
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    azure_account_id: None | Unset | UUID = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    resource_group_name: None | str | Unset = UNSET,
) -> Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]:
    """Specify Worker Location and Service Account

     The HTTP POST request to the `/workers/networkConfiguration/setWorkerDeploymentOptions` endpoint
    allows you to specify a service account that will be used to launch worker instances, and also a
    subscription and a resource group in which the worker instances will be launched.

    Args:
        azure_account_id (None | Unset | UUID):
        subscription_id (None | Unset | UUID):
        resource_group_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        azure_account_id=azure_account_id,
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    azure_account_id: None | Unset | UUID = UNSET,
    subscription_id: None | Unset | UUID = UNSET,
    resource_group_name: None | str | Unset = UNSET,
) -> Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    """Specify Worker Location and Service Account

     The HTTP POST request to the `/workers/networkConfiguration/setWorkerDeploymentOptions` endpoint
    allows you to specify a service account that will be used to launch worker instances, and also a
    subscription and a resource group in which the worker instances will be launched.

    Args:
        azure_account_id (None | Unset | UUID):
        subscription_id (None | Unset | UUID):
        resource_group_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            client=client,
            azure_account_id=azure_account_id,
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
        )
    ).parsed
