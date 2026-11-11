from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.standard_account_kind import StandardAccountKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standard_account_sql_options_from_client import StandardAccountSqlOptionsFromClient


T = TypeVar("T", bound="NewStandardAccountFromClient")


@_attrs_define
class NewStandardAccountFromClient:
    """
    Attributes:
        name (str): Specifies a name for the account.
        kind (StandardAccountKind | Unset): Specifies the type of the account.
        description (None | str | Unset): Specifies a description for the account.
        username (None | str | Unset): Specifies a user name that will be used by Veeam Backup for Microsoft Azure to
            authenticate against a protected Azure database or an SMTP server used for sending email notifications.
        password (None | str | Unset): Specifies a password that will be used by Veeam Backup for Microsoft Azure to
            authenticate against a protected Azure database or an SMTP server used for sending email notifications.
        sql_options_from_client (StandardAccountSqlOptionsFromClient | Unset): Specifies SQL options for the account.
    """

    name: str
    kind: StandardAccountKind | Unset = UNSET
    description: None | str | Unset = UNSET
    username: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    sql_options_from_client: StandardAccountSqlOptionsFromClient | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        sql_options_from_client: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sql_options_from_client, Unset):
            sql_options_from_client = self.sql_options_from_client.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if description is not UNSET:
            field_dict["description"] = description
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if sql_options_from_client is not UNSET:
            field_dict["sqlOptionsFromClient"] = sql_options_from_client

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.standard_account_sql_options_from_client import StandardAccountSqlOptionsFromClient

        d = dict(src_dict)
        name = d.pop("name")

        _kind = d.pop("kind", UNSET)
        kind: StandardAccountKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = StandardAccountKind(_kind)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        _sql_options_from_client = d.pop("sqlOptionsFromClient", UNSET)
        sql_options_from_client: StandardAccountSqlOptionsFromClient | Unset
        if isinstance(_sql_options_from_client, Unset):
            sql_options_from_client = UNSET
        else:
            sql_options_from_client = StandardAccountSqlOptionsFromClient.from_dict(_sql_options_from_client)

        new_standard_account_from_client = cls(
            name=name,
            kind=kind,
            description=description,
            username=username,
            password=password,
            sql_options_from_client=sql_options_from_client,
        )

        return new_standard_account_from_client
