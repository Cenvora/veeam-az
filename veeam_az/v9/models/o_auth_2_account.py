from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.o_auth_2_mail_service_kind import OAuth2MailServiceKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2Account")


@_attrs_define
class OAuth2Account:
    r"""
    Attributes:
        id (UUID): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the account used to send email
            notifications.
        name (str): Name of the account.
        application_id (str): Client ID obtained for the application upon registration in the Google Cloud Console or
            Microsoft Azure portal used by Veeam Backup for Microsoft Azure to authenticate against an OAuth 2.0 server.
        kind (OAuth2MailServiceKind | Unset): Specifies the type of the mail server that you want to use to send email
            notifications.
        description (None | str | Unset): Description of the account.
        tenant_id (None | str | Unset): \[Applies only if the *Microsoft* value is specified for the
            `OAuth2MailServiceKind` parameter] Tenant ID obtained for the application upon registration in the Microsoft
            Azure portal.
        is_refresh_token_expired (bool | Unset): Defines whether the refresh token is expired for specified account.
    """

    id: UUID
    name: str
    application_id: str
    kind: OAuth2MailServiceKind | Unset = UNSET
    description: None | str | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    is_refresh_token_expired: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        application_id = self.application_id

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        is_refresh_token_expired = self.is_refresh_token_expired

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "applicationId": application_id,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if description is not UNSET:
            field_dict["description"] = description
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if is_refresh_token_expired is not UNSET:
            field_dict["isRefreshTokenExpired"] = is_refresh_token_expired

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        application_id = d.pop("applicationId")

        _kind = d.pop("kind", UNSET)
        kind: OAuth2MailServiceKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = OAuth2MailServiceKind(_kind)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        is_refresh_token_expired = d.pop("isRefreshTokenExpired", UNSET)

        o_auth_2_account = cls(
            id=id,
            name=name,
            application_id=application_id,
            kind=kind,
            description=description,
            tenant_id=tenant_id,
            is_refresh_token_expired=is_refresh_token_expired,
        )

        return o_auth_2_account
