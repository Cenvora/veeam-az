from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_array_of_sql_policy_configuration_test_result import (
    AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult,
)
from ...models.new_sql_policy_from_client import NewSqlPolicyFromClient
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_415 import ProblemDetails415
from ...models.sql_policy_configuration_test_result import SqlPolicyConfigurationTestResult
from ...types import Response


def _get_kwargs(
    *,
    body: NewSqlPolicyFromClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/policies/sql/testConfiguration",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails415
    | list[SqlPolicyConfigurationTestResult]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SqlPolicyConfigurationTestResult.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult.from_dict(response.json())

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
    AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails415
    | list[SqlPolicyConfigurationTestResult]
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
    body: NewSqlPolicyFromClient,
) -> Response[
    AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails415
    | list[SqlPolicyConfigurationTestResult]
]:
    """Check Configuration of Backup Policy

     The HTTP POST request to the `/policies/sql/testConfiguration` endpoint verifies whether the SQL
    policy settings are configured properly.

    Args:
        body (NewSqlPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[SqlPolicyConfigurationTestResult]]
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
    body: NewSqlPolicyFromClient,
) -> (
    AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails415
    | list[SqlPolicyConfigurationTestResult]
    | None
):
    """Check Configuration of Backup Policy

     The HTTP POST request to the `/policies/sql/testConfiguration` endpoint verifies whether the SQL
    policy settings are configured properly.

    Args:
        body (NewSqlPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[SqlPolicyConfigurationTestResult]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewSqlPolicyFromClient,
) -> Response[
    AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails415
    | list[SqlPolicyConfigurationTestResult]
]:
    """Check Configuration of Backup Policy

     The HTTP POST request to the `/policies/sql/testConfiguration` endpoint verifies whether the SQL
    policy settings are configured properly.

    Args:
        body (NewSqlPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[SqlPolicyConfigurationTestResult]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewSqlPolicyFromClient,
) -> (
    AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails415
    | list[SqlPolicyConfigurationTestResult]
    | None
):
    """Check Configuration of Backup Policy

     The HTTP POST request to the `/policies/sql/testConfiguration` endpoint verifies whether the SQL
    policy settings are configured properly.

    Args:
        body (NewSqlPolicyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfArrayOfSqlPolicyConfigurationTestResult | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails415 | list[SqlPolicyConfigurationTestResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
