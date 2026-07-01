from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_configuration_item import RepositoryConfigurationItem


T = TypeVar("T", bound="BackupRepositoryConfiguration")


@_attrs_define
class BackupRepositoryConfiguration:
    """Configuration of target locations where backups are stored.

    Attributes:
        default_repository_id (UUID | Unset): System ID assigned to the default backup repository in the Veeam Backup
            for Microsoft Azure REST API.
        default_repository_name (str | Unset): Name of the default backup repository.
        items (list[RepositoryConfigurationItem] | Unset): Region-specific backup repository settings. If not provided,
            the default backup repository is used for all regions.
    """

    default_repository_id: UUID | Unset = UNSET
    default_repository_name: str | Unset = UNSET
    items: list[RepositoryConfigurationItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_repository_id: str | Unset = UNSET
        if not isinstance(self.default_repository_id, Unset):
            default_repository_id = str(self.default_repository_id)

        default_repository_name = self.default_repository_name

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
        if default_repository_name is not UNSET:
            field_dict["defaultRepositoryName"] = default_repository_name
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_configuration_item import RepositoryConfigurationItem

        d = dict(src_dict)
        _default_repository_id = d.pop("defaultRepositoryId", UNSET)
        default_repository_id: UUID | Unset
        if isinstance(_default_repository_id, Unset):
            default_repository_id = UNSET
        else:
            default_repository_id = UUID(_default_repository_id)

        default_repository_name = d.pop("defaultRepositoryName", UNSET)

        _items = d.pop("items", UNSET)
        items: list[RepositoryConfigurationItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RepositoryConfigurationItem.from_dict(items_item_data)

                items.append(items_item)

        backup_repository_configuration = cls(
            default_repository_id=default_repository_id,
            default_repository_name=default_repository_name,
            items=items,
        )

        backup_repository_configuration.additional_properties = d
        return backup_repository_configuration

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
