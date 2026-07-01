from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_400 import ProblemDetails400
from ...models.problem_details_401 import ProblemDetails401
from ...models.problem_details_403 import ProblemDetails403
from ...models.problem_details_404 import ProblemDetails404
from ...models.problem_details_415 import ProblemDetails415
from ...models.sla_template import SlaTemplate
from ...models.updated_sla_template_from_client import UpdatedSlaTemplateFromClient
from ...types import Response


def _get_kwargs(
    template_id: UUID,
    *,
    body: UpdatedSlaTemplateFromClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v8.1/policyTemplates/slaTemplate/{template_id}".format(
            template_id=quote(str(template_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SlaTemplate
    | None
):
    if response.status_code == 200:
        response_200 = SlaTemplate.from_dict(response.json())

        return response_200

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
    Any
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SlaTemplate
]:
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
    body: UpdatedSlaTemplateFromClient,
) -> Response[
    Any
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SlaTemplate
]:
    """Modify SLA Template

     The HTTP PUT request to the `/policyTemplates/slaTemplate/{templateId}` endpoint updates settings of
    an SLA template with the specified ID.

    Args:
        template_id (UUID):
        body (UpdatedSlaTemplateFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | SlaTemplate]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatedSlaTemplateFromClient,
) -> (
    Any
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SlaTemplate
    | None
):
    """Modify SLA Template

     The HTTP PUT request to the `/policyTemplates/slaTemplate/{templateId}` endpoint updates settings of
    an SLA template with the specified ID.

    Args:
        template_id (UUID):
        body (UpdatedSlaTemplateFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | SlaTemplate
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    template_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatedSlaTemplateFromClient,
) -> Response[
    Any
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SlaTemplate
]:
    """Modify SLA Template

     The HTTP PUT request to the `/policyTemplates/slaTemplate/{templateId}` endpoint updates settings of
    an SLA template with the specified ID.

    Args:
        template_id (UUID):
        body (UpdatedSlaTemplateFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | SlaTemplate]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatedSlaTemplateFromClient,
) -> (
    Any
    | ProblemDetails400
    | ProblemDetails401
    | ProblemDetails403
    | ProblemDetails404
    | ProblemDetails415
    | SlaTemplate
    | None
):
    """Modify SLA Template

     The HTTP PUT request to the `/policyTemplates/slaTemplate/{templateId}` endpoint updates settings of
    an SLA template with the specified ID.

    Args:
        template_id (UUID):
        body (UpdatedSlaTemplateFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails400 | ProblemDetails401 | ProblemDetails403 | ProblemDetails404 | ProblemDetails415 | SlaTemplate
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
            body=body,
        )
    ).parsed
