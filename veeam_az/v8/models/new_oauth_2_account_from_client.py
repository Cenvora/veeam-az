from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_oauth_2_account_from_client_prompt import NewOauth2AccountFromClientPrompt
from ..models.o_auth_2_mail_service_kind import OAuth2MailServiceKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewOauth2AccountFromClient")


@_attrs_define
class NewOauth2AccountFromClient:
    """
    Attributes:
        kind (OAuth2MailServiceKind): Specifies the type of the mail server that you want to use to send email
            notifications.
        name (str): Specifies a name for the account.
        client_id (str): Specifies a application identifier that will be used by Veeam Backup for Microsoft Azure to
            authenticate against the Server.
        client_secret (None | str): Specifies a application secret that will be used by Veeam Backup for Microsoft Azure
            to authenticate against the Server.
        description (None | str | Unset): Specifies a description for the account.
        tenant_id (None | str | Unset): Specifies a tenant identifier that will be used by Veeam Backup for Microsoft
            Azure to authenticate against the Server.
        redirect_url (str | Unset): Specifies an URL that will be used to redirect from authorization server to Veeam
            Backup for Microsoft Azure.
        prompt (NewOauth2AccountFromClientPrompt | Unset):
    """

    kind: OAuth2MailServiceKind
    name: str
    client_id: str
    client_secret: None | str
    description: None | str | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    redirect_url: str | Unset = UNSET
    prompt: NewOauth2AccountFromClientPrompt | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        name = self.name

        client_id = self.client_id

        client_secret: None | str
        client_secret = self.client_secret

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

        redirect_url = self.redirect_url

        prompt: str | Unset = UNSET
        if not isinstance(self.prompt, Unset):
            prompt = self.prompt.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "clientId": client_id,
                "clientSecret": client_secret,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url
        if prompt is not UNSET:
            field_dict["prompt"] = prompt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = OAuth2MailServiceKind(d.pop("kind"))

        name = d.pop("name")

        client_id = d.pop("clientId")

        def _parse_client_secret(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        client_secret = _parse_client_secret(d.pop("clientSecret"))

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

        redirect_url = d.pop("redirectUrl", UNSET)

        _prompt = d.pop("prompt", UNSET)
        prompt: NewOauth2AccountFromClientPrompt | Unset
        if isinstance(_prompt, Unset):
            prompt = UNSET
        else:
            prompt = NewOauth2AccountFromClientPrompt(_prompt)

        new_oauth_2_account_from_client = cls(
            kind=kind,
            name=name,
            client_id=client_id,
            client_secret=client_secret,
            description=description,
            tenant_id=tenant_id,
            redirect_url=redirect_url,
            prompt=prompt,
        )

        return new_oauth_2_account_from_client
