from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityProviderConfiguration")


@_attrs_define
class IdentityProviderConfiguration:
    """
    Attributes:
        entity_id (None | str | Unset): System ID assigned to the identity provider in the Veeam Backup for Microsoft
            Azure REST API.
        login_url (None | str | Unset): URL that will be used to log in to the identity provider.
        enabled (bool | None | Unset): Defines whether using an external identity provider for authentication is
            enabled.
    """

    entity_id: None | str | Unset = UNSET
    login_url: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        entity_id: None | str | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = self.entity_id

        login_url: None | str | Unset
        if isinstance(self.login_url, Unset):
            login_url = UNSET
        else:
            login_url = self.login_url

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if login_url is not UNSET:
            field_dict["loginUrl"] = login_url
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_entity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_id = _parse_entity_id(d.pop("entityId", UNSET))

        def _parse_login_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        login_url = _parse_login_url(d.pop("loginUrl", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        identity_provider_configuration = cls(
            entity_id=entity_id,
            login_url=login_url,
            enabled=enabled,
        )

        return identity_provider_configuration
