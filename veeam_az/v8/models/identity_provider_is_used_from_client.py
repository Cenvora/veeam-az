from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="IdentityProviderIsUsedFromClient")


@_attrs_define
class IdentityProviderIsUsedFromClient:
    """
    Attributes:
        entity_id (str): System ID assigned to the identity provider in the Veeam Backup for Microsoft Azure REST API.
        enabled (bool): Defines whether using an external identity provider for authentication is enabled.
    """

    entity_id: str
    enabled: bool

    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entityId": entity_id,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_id = d.pop("entityId")

        enabled = d.pop("enabled")

        identity_provider_is_used_from_client = cls(
            entity_id=entity_id,
            enabled=enabled,
        )

        return identity_provider_is_used_from_client
