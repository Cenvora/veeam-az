from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_retrieval_status import DataRetrievalStatus
from ...models.page_of_cosmos_db_continuous_restore_point import PageOfCosmosDbContinuousRestorePoint
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cosmos_db_account_id: None | str | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_cosmos_db_account_id: None | str | Unset
    if isinstance(cosmos_db_account_id, Unset):
        json_cosmos_db_account_id = UNSET
    else:
        json_cosmos_db_account_id = cosmos_db_account_id
    params["CosmosDbAccountId"] = json_cosmos_db_account_id

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

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/restorePoints/cosmosDb/continuous",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfCosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    if response.status_code == 200:
        response_200 = PageOfCosmosDbContinuousRestorePoint.from_dict(response.json())

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
) -> Response[PageOfCosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cosmos_db_account_id: None | str | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfCosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Cosmos DB Restorable Timestamps

     The HTTP GET request to the `/restorePoints/cosmosDb/continuous` endpoint retrieves a list of
    restorable timestamps created by Veeam Backup for Microsoft Azure for Cosmos DB accounts protected
    using the *Continuous backup* option.

    Args:
        cosmos_db_account_id (None | str | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfCosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        data_retrieval_statuses=data_retrieval_statuses,
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
    cosmos_db_account_id: None | str | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfCosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Cosmos DB Restorable Timestamps

     The HTTP GET request to the `/restorePoints/cosmosDb/continuous` endpoint retrieves a list of
    restorable timestamps created by Veeam Backup for Microsoft Azure for Cosmos DB accounts protected
    using the *Continuous backup* option.

    Args:
        cosmos_db_account_id (None | str | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfCosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return sync_detailed(
        client=client,
        cosmos_db_account_id=cosmos_db_account_id,
        data_retrieval_statuses=data_retrieval_statuses,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cosmos_db_account_id: None | str | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfCosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]:
    """Get Cosmos DB Restorable Timestamps

     The HTTP GET request to the `/restorePoints/cosmosDb/continuous` endpoint retrieves a list of
    restorable timestamps created by Veeam Backup for Microsoft Azure for Cosmos DB accounts protected
    using the *Continuous backup* option.

    Args:
        cosmos_db_account_id (None | str | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfCosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403]
    """

    kwargs = _get_kwargs(
        cosmos_db_account_id=cosmos_db_account_id,
        data_retrieval_statuses=data_retrieval_statuses,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cosmos_db_account_id: None | str | Unset = UNSET,
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfCosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | None:
    """Get Cosmos DB Restorable Timestamps

     The HTTP GET request to the `/restorePoints/cosmosDb/continuous` endpoint retrieves a list of
    restorable timestamps created by Veeam Backup for Microsoft Azure for Cosmos DB accounts protected
    using the *Continuous backup* option.

    Args:
        cosmos_db_account_id (None | str | Unset):
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfCosmosDbContinuousRestorePoint | ProblemDetails400 | ProblemDetails401 | ProblemDetails403
    """

    return (
        await asyncio_detailed(
            client=client,
            cosmos_db_account_id=cosmos_db_account_id,
            data_retrieval_statuses=data_retrieval_statuses,
            offset=offset,
            limit=limit,
        )
    ).parsed
