from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_configuration_item_from_client import RepositoryConfigurationItemFromClient


T = TypeVar("T", bound="ArchiveRepositoryConfigurationFromClient")


@_attrs_define
class ArchiveRepositoryConfigurationFromClient:
    """Specifies target locations where archived backups will be stored.

    Attributes:
        default_repository_id (UUID | Unset): Specifies a system ID assigned to the default archive repository in the
            Veeam Backup for Microsoft Azure REST API.
        items (list[RepositoryConfigurationItemFromClient] | Unset): Specifies region-specific archive repository
            settings. If not provided, the default archive repository will be used for all regions.
    """

    default_repository_id: UUID | Unset = UNSET
    items: list[RepositoryConfigurationItemFromClient] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_repository_id: str | Unset = UNSET
        if not isinstance(self.default_repository_id, Unset):
            default_repository_id = str(self.default_repository_id)

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_repository_id is not UNSET:
            field_dict["defaultRepositoryId"] = default_repository_id
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_configuration_item_from_client import RepositoryConfigurationItemFromClient

        d = dict(src_dict)
        _default_repository_id = d.pop("defaultRepositoryId", UNSET)
        default_repository_id: UUID | Unset
        if isinstance(_default_repository_id, Unset):
            default_repository_id = UNSET
        else:
            default_repository_id = UUID(_default_repository_id)

        _items = d.pop("items", UNSET)
        items: list[RepositoryConfigurationItemFromClient] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RepositoryConfigurationItemFromClient.from_dict(items_item_data)

                items.append(items_item)

        archive_repository_configuration_from_client = cls(
            default_repository_id=default_repository_id,
            items=items,
        )

        archive_repository_configuration_from_client.additional_properties = d
        return archive_repository_configuration_from_client

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
