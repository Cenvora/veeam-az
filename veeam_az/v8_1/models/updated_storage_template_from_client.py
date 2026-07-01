from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_template_configuration_from_client import StorageTemplateConfigurationFromClient


T = TypeVar("T", bound="UpdatedStorageTemplateFromClient")


@_attrs_define
class UpdatedStorageTemplateFromClient:
    """
    Attributes:
        name (str | Unset): Specifies a name for the storage template.
        description (str | Unset): Specifies a description for the storage template.
        storage_configuration (StorageTemplateConfigurationFromClient | Unset): Specifies the storage template
            configuration.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    storage_configuration: StorageTemplateConfigurationFromClient | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        storage_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_configuration, Unset):
            storage_configuration = self.storage_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if storage_configuration is not UNSET:
            field_dict["storageConfiguration"] = storage_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_template_configuration_from_client import StorageTemplateConfigurationFromClient

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _storage_configuration = d.pop("storageConfiguration", UNSET)
        storage_configuration: StorageTemplateConfigurationFromClient | Unset
        if isinstance(_storage_configuration, Unset):
            storage_configuration = UNSET
        else:
            storage_configuration = StorageTemplateConfigurationFromClient.from_dict(_storage_configuration)

        updated_storage_template_from_client = cls(
            name=name,
            description=description,
            storage_configuration=storage_configuration,
        )

        updated_storage_template_from_client.additional_properties = d
        return updated_storage_template_from_client

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
