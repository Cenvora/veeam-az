from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.o_auth_2_mail_service_kind import OAuth2MailServiceKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatedOauth2AccountFromClient")


@_attrs_define
class UpdatedOauth2AccountFromClient:
    """
    Attributes:
        name (str): Specifies a name for the account.
        application_id (str): Specifies an application identifier that will be used by Veeam Backup for Microsoft Azure
            to authenticate against the Server.
        application_secret (str): Specifies a application secret that will be used by Veeam Backup for Microsoft Azure
            to authenticate against the Server.
        tenant_id (str): Specifies a tenant identifier that will be used by Veeam Backup for Microsoft Azure to
            authenticate against the Server.
        kind (OAuth2MailServiceKind | Unset): Specifies the type of the mail server that you want to use to send email
            notifications.
        description (None | str | Unset): Specifies a description for the account.
    """

    name: str
    application_id: str
    application_secret: str
    tenant_id: str
    kind: OAuth2MailServiceKind | Unset = UNSET
    description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        application_id = self.application_id

        application_secret = self.application_secret

        tenant_id = self.tenant_id

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "applicationId": application_id,
                "applicationSecret": application_secret,
                "tenantId": tenant_id,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        application_id = d.pop("applicationId")

        application_secret = d.pop("applicationSecret")

        tenant_id = d.pop("tenantId")

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

        updated_oauth_2_account_from_client = cls(
            name=name,
            application_id=application_id,
            application_secret=application_secret,
            tenant_id=tenant_id,
            kind=kind,
            description=description,
        )

        return updated_oauth_2_account_from_client
