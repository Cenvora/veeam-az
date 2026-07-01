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
from ...models.sla_template import SlaTemplate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    template_id: UUID,
    *,
    template_name: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_template_name: None | str | Unset
    if isinstance(template_name, Unset):
        json_template_name = UNSET
    else:
        json_template_name = template_name
    params["TemplateName"] = json_template_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v8.1/policyTemplates/slaTemplate/{template_id}".format(
            template_id=quote(str(template_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaTemplate | None:
    if response.status_code == 200:
        response_200 = SlaTemplate.from_dict(response.json())

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
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    template_name: None | str | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaTemplate]:
    """Get SLA Template Data

     The HTTP GET request to the `/policyTemplates/slaTemplate/{templateId}` endpoint retrieves
    information on an SLA template with the specified ID.

    Args:
        template_id (UUID):
        template_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaTemplate]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        template_name=template_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    template_name: None | str | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaTemplate | None:
    """Get SLA Template Data

     The HTTP GET request to the `/policyTemplates/slaTemplate/{templateId}` endpoint retrieves
    information on an SLA template with the specified ID.

    Args:
        template_id (UUID):
        template_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaTemplate
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
        template_name=template_name,
    ).parsed


async def asyncio_detailed(
    template_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    template_name: None | str | Unset = UNSET,
) -> Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaTemplate]:
    """Get SLA Template Data

     The HTTP GET request to the `/policyTemplates/slaTemplate/{templateId}` endpoint retrieves
    information on an SLA template with the specified ID.

    Args:
        template_id (UUID):
        template_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaTemplate]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        template_name=template_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    template_name: None | str | Unset = UNSET,
) -> ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaTemplate | None:
    """Get SLA Template Data

     The HTTP GET request to the `/policyTemplates/slaTemplate/{templateId}` endpoint retrieves
    information on an SLA template with the specified ID.

    Args:
        template_id (UUID):
        template_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | SlaTemplate
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
            template_name=template_name,
        )
    ).parsed
