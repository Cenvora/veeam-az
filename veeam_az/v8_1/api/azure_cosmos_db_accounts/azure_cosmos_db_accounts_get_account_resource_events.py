import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cosmos_db_resource_event_type import CosmosDbResourceEventType
from ...models.page_of_cosmos_db_resource_event import PageOfCosmosDbResourceEvent
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cosmos_db_account_id: str,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    service_account_id: UUID,
    event_type: list[CosmosDbResourceEventType] | None | Unset = UNSET,
    database_rid: str | Unset = UNSET,
    from_time: datetime.datetime | Unset = UNSET,
    to_time: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    json_service_account_id = str(service_account_id)
    params["ServiceAccountId"] = json_service_account_id

    json_event_type: list[str] | None | Unset
    if isinstance(event_type, Unset):
        json_event_type = UNSET
    elif isinstance(event_type, list):
        json_event_type = []
        for event_type_type_0_item_data in event_type:
            event_type_type_0_item = event_type_type_0_item_data.value
            json_event_type.append(event_type_type_0_item)

    else:
        json_event_type = event_type
    params["EventType"] = json_event_type

    params["databaseRid"] = database_rid

    json_from_time: str | Unset = UNSET
    if not isinstance(from_time, Unset):
        json_from_time = from_time.isoformat()
    params["FromTime"] = json_from_time

    json_to_time: str | Unset = UNSET
    if not isinstance(to_time, Unset):
        json_to_time = to_time.isoformat()
    params["ToTime"] = json_to_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/cloudInfrastructure/cosmosDb/{cosmos_db_account_id}/resourceEvents".format(
            cosmos_db_account_id=quote(str(cosmos_db_account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfCosmosDbResourceEvent | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    if response.status_code == 200:
        response_200 = PageOfCosmosDbResourceEvent.from_dict(response.json())

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
    PageOfCosmosDbResourceEvent | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    service_account_id: UUID,
    event_type: list[CosmosDbResourceEventType] | None | Unset = UNSET,
    database_rid: str | Unset = UNSET,
    from_time: datetime.datetime | Unset = UNSET,
    to_time: datetime.datetime | Unset = UNSET,
) -> Response[
    PageOfCosmosDbResourceEvent | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    r"""Get Cosmos DB Account Events

     The HTTP GET request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/databases/{databaseRid}/resourceEvents` endpoint
    retrieves a list of create, replace and delete events for a specific database of a Cosmos DB account
    with the specified ID. <br> <div class=\"note\"><strong>NOTE</strong> <br>This operation can only be
    performed to Cosmos DB accounts of the following kinds&#58; NoSQL, MongoDB, Apache Gremlin and
    Table.</div>

    Args:
        cosmos_db_account_id (str):
        offset (int | Unset):
        limit (int | Unset):
        service_account_id (UUID):
        event_type (list[CosmosDbResourceEventType] | None | Unset):
        database_rid (str | Unset):
        from_time (datetime.datetime | Unset):
        to_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfCosmosDbResourceEvent | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        offset=offset,
        limit=limit,
        service_account_id=service_account_id,
        event_type=event_type,
        database_rid=database_rid,
        from_time=from_time,
        to_time=to_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    service_account_id: UUID,
    event_type: list[CosmosDbResourceEventType] | None | Unset = UNSET,
    database_rid: str | Unset = UNSET,
    from_time: datetime.datetime | Unset = UNSET,
    to_time: datetime.datetime | Unset = UNSET,
) -> PageOfCosmosDbResourceEvent | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    r"""Get Cosmos DB Account Events

     The HTTP GET request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/databases/{databaseRid}/resourceEvents` endpoint
    retrieves a list of create, replace and delete events for a specific database of a Cosmos DB account
    with the specified ID. <br> <div class=\"note\"><strong>NOTE</strong> <br>This operation can only be
    performed to Cosmos DB accounts of the following kinds&#58; NoSQL, MongoDB, Apache Gremlin and
    Table.</div>

    Args:
        cosmos_db_account_id (str):
        offset (int | Unset):
        limit (int | Unset):
        service_account_id (UUID):
        event_type (list[CosmosDbResourceEventType] | None | Unset):
        database_rid (str | Unset):
        from_time (datetime.datetime | Unset):
        to_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfCosmosDbResourceEvent | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return sync_detailed(
        cosmos_db_account_id=cosmos_db_account_id,
        client=client,
        offset=offset,
        limit=limit,
        service_account_id=service_account_id,
        event_type=event_type,
        database_rid=database_rid,
        from_time=from_time,
        to_time=to_time,
    ).parsed


async def asyncio_detailed(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    service_account_id: UUID,
    event_type: list[CosmosDbResourceEventType] | None | Unset = UNSET,
    database_rid: str | Unset = UNSET,
    from_time: datetime.datetime | Unset = UNSET,
    to_time: datetime.datetime | Unset = UNSET,
) -> Response[
    PageOfCosmosDbResourceEvent | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
]:
    r"""Get Cosmos DB Account Events

     The HTTP GET request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/databases/{databaseRid}/resourceEvents` endpoint
    retrieves a list of create, replace and delete events for a specific database of a Cosmos DB account
    with the specified ID. <br> <div class=\"note\"><strong>NOTE</strong> <br>This operation can only be
    performed to Cosmos DB accounts of the following kinds&#58; NoSQL, MongoDB, Apache Gremlin and
    Table.</div>

    Args:
        cosmos_db_account_id (str):
        offset (int | Unset):
        limit (int | Unset):
        service_account_id (UUID):
        event_type (list[CosmosDbResourceEventType] | None | Unset):
        database_rid (str | Unset):
        from_time (datetime.datetime | Unset):
        to_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfCosmosDbResourceEvent | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        offset=offset,
        limit=limit,
        service_account_id=service_account_id,
        event_type=event_type,
        database_rid=database_rid,
        from_time=from_time,
        to_time=to_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cosmos_db_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    service_account_id: UUID,
    event_type: list[CosmosDbResourceEventType] | None | Unset = UNSET,
    database_rid: str | Unset = UNSET,
    from_time: datetime.datetime | Unset = UNSET,
    to_time: datetime.datetime | Unset = UNSET,
) -> PageOfCosmosDbResourceEvent | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | None:
    r"""Get Cosmos DB Account Events

     The HTTP GET request to the
    `/cloudInfrastructure/cosmosDb/{cosmosDbAccountId}/databases/{databaseRid}/resourceEvents` endpoint
    retrieves a list of create, replace and delete events for a specific database of a Cosmos DB account
    with the specified ID. <br> <div class=\"note\"><strong>NOTE</strong> <br>This operation can only be
    performed to Cosmos DB accounts of the following kinds&#58; NoSQL, MongoDB, Apache Gremlin and
    Table.</div>

    Args:
        cosmos_db_account_id (str):
        offset (int | Unset):
        limit (int | Unset):
        service_account_id (UUID):
        event_type (list[CosmosDbResourceEventType] | None | Unset):
        database_rid (str | Unset):
        from_time (datetime.datetime | Unset):
        to_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfCosmosDbResourceEvent | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404
    """

    return (
        await asyncio_detailed(
            cosmos_db_account_id=cosmos_db_account_id,
            client=client,
            offset=offset,
            limit=limit,
            service_account_id=service_account_id,
            event_type=event_type,
            database_rid=database_rid,
            from_time=from_time,
            to_time=to_time,
        )
    ).parsed
