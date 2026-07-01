from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_operation_of_array_of_sql_connection_test_message import (
    AsyncOperationOfArrayOfSqlConnectionTestMessage,
)
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.problem_details_415 import ProblemDetails415
from ...models.sql_connection_test_message import SqlConnectionTestMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sql_server_id: str,
    *,
    sql_account_id: None | str | Unset = UNSET,
    azure_account_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sql_account_id: None | str | Unset
    if isinstance(sql_account_id, Unset):
        json_sql_account_id = UNSET
    else:
        json_sql_account_id = sql_account_id
    params["sqlAccountId"] = json_sql_account_id

    json_azure_account_id: None | str | Unset
    if isinstance(azure_account_id, Unset):
        json_azure_account_id = UNSET
    else:
        json_azure_account_id = azure_account_id
    params["azureAccountId"] = json_azure_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v8.1/cloudInfrastructure/sqlServers/testConnectivity/{sql_server_id}".format(
            sql_server_id=quote(str(sql_server_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncOperationOfArrayOfSqlConnectionTestMessage
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | list[SqlConnectionTestMessage]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SqlConnectionTestMessage.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 202:
        response_202 = AsyncOperationOfArrayOfSqlConnectionTestMessage.from_dict(response.json())

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
    AsyncOperationOfArrayOfSqlConnectionTestMessage
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | list[SqlConnectionTestMessage]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sql_server_id: str,
    *,
    client: AuthenticatedClient | Client,
    sql_account_id: None | str | Unset = UNSET,
    azure_account_id: None | str | Unset = UNSET,
) -> Response[
    AsyncOperationOfArrayOfSqlConnectionTestMessage
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | list[SqlConnectionTestMessage]
]:
    """Test Connection to SQL Server

     The HTTP POST request to the `/cloudInfrastructure/sqlServers/testConnectivity/{sqlServerId}`
    endpoint verifies connection to a SQL Server with the specified ID.

    Args:
        sql_server_id (str):
        sql_account_id (None | str | Unset):
        azure_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfArrayOfSqlConnectionTestMessage | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | list[SqlConnectionTestMessage]]
    """

    kwargs = _get_kwargs(
        sql_server_id=sql_server_id,
        sql_account_id=sql_account_id,
        azure_account_id=azure_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sql_server_id: str,
    *,
    client: AuthenticatedClient | Client,
    sql_account_id: None | str | Unset = UNSET,
    azure_account_id: None | str | Unset = UNSET,
) -> (
    AsyncOperationOfArrayOfSqlConnectionTestMessage
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | list[SqlConnectionTestMessage]
    | None
):
    """Test Connection to SQL Server

     The HTTP POST request to the `/cloudInfrastructure/sqlServers/testConnectivity/{sqlServerId}`
    endpoint verifies connection to a SQL Server with the specified ID.

    Args:
        sql_server_id (str):
        sql_account_id (None | str | Unset):
        azure_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfArrayOfSqlConnectionTestMessage | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | list[SqlConnectionTestMessage]
    """

    return sync_detailed(
        sql_server_id=sql_server_id,
        client=client,
        sql_account_id=sql_account_id,
        azure_account_id=azure_account_id,
    ).parsed


async def asyncio_detailed(
    sql_server_id: str,
    *,
    client: AuthenticatedClient | Client,
    sql_account_id: None | str | Unset = UNSET,
    azure_account_id: None | str | Unset = UNSET,
) -> Response[
    AsyncOperationOfArrayOfSqlConnectionTestMessage
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | list[SqlConnectionTestMessage]
]:
    """Test Connection to SQL Server

     The HTTP POST request to the `/cloudInfrastructure/sqlServers/testConnectivity/{sqlServerId}`
    endpoint verifies connection to a SQL Server with the specified ID.

    Args:
        sql_server_id (str):
        sql_account_id (None | str | Unset):
        azure_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncOperationOfArrayOfSqlConnectionTestMessage | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | list[SqlConnectionTestMessage]]
    """

    kwargs = _get_kwargs(
        sql_server_id=sql_server_id,
        sql_account_id=sql_account_id,
        azure_account_id=azure_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sql_server_id: str,
    *,
    client: AuthenticatedClient | Client,
    sql_account_id: None | str | Unset = UNSET,
    azure_account_id: None | str | Unset = UNSET,
) -> (
    AsyncOperationOfArrayOfSqlConnectionTestMessage
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | list[SqlConnectionTestMessage]
    | None
):
    """Test Connection to SQL Server

     The HTTP POST request to the `/cloudInfrastructure/sqlServers/testConnectivity/{sqlServerId}`
    endpoint verifies connection to a SQL Server with the specified ID.

    Args:
        sql_server_id (str):
        sql_account_id (None | str | Unset):
        azure_account_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncOperationOfArrayOfSqlConnectionTestMessage | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | list[SqlConnectionTestMessage]
    """

    return (
        await asyncio_detailed(
            sql_server_id=sql_server_id,
            client=client,
            sql_account_id=sql_account_id,
            azure_account_id=azure_account_id,
        )
    ).parsed
