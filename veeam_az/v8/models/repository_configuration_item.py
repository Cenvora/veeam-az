from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryConfigurationItem")


@_attrs_define
class RepositoryConfigurationItem:
    """Region-specific repository settings.

    Attributes:
        repository_id (UUID | Unset): System ID assigned to a region-specific repository in the Veeam Backup for
            Microsoft Azure REST API.
        repository_name (str | Unset): Name of the repository.
        repository_region_id (str | Unset): Microsoft Azure ID assigned to a region in which the repository resides.
        repository_region_name (str | Unset): Name of the region in which the repository resides.
        repository_immutability_enabled (bool | Unset): Defines whether immutability is enabled for the repository.
        repository_encryption_enabled (bool | Unset): Defines whether data encryption is enabled for the repository.
        region_resource_id (str | Unset): Resource ID assigned in Microsoft Azure to a region for which the repository
            is used.
        region_name (str | Unset): Name of the region for which the repository is used.
    """

    repository_id: UUID | Unset = UNSET
    repository_name: str | Unset = UNSET
    repository_region_id: str | Unset = UNSET
    repository_region_name: str | Unset = UNSET
    repository_immutability_enabled: bool | Unset = UNSET
    repository_encryption_enabled: bool | Unset = UNSET
    region_resource_id: str | Unset = UNSET
    region_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository_id: str | Unset = UNSET
        if not isinstance(self.repository_id, Unset):
            repository_id = str(self.repository_id)

        repository_name = self.repository_name

        repository_region_id = self.repository_region_id

        repository_region_name = self.repository_region_name

        repository_immutability_enabled = self.repository_immutability_enabled

        repository_encryption_enabled = self.repository_encryption_enabled

        region_resource_id = self.region_resource_id

        region_name = self.region_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if repository_region_id is not UNSET:
            field_dict["repositoryRegionId"] = repository_region_id
        if repository_region_name is not UNSET:
            field_dict["repositoryRegionName"] = repository_region_name
        if repository_immutability_enabled is not UNSET:
            field_dict["repositoryImmutabilityEnabled"] = repository_immutability_enabled
        if repository_encryption_enabled is not UNSET:
            field_dict["repositoryEncryptionEnabled"] = repository_encryption_enabled
        if region_resource_id is not UNSET:
            field_dict["regionResourceId"] = region_resource_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _repository_id = d.pop("repositoryId", UNSET)
        repository_id: UUID | Unset
        if isinstance(_repository_id, Unset):
            repository_id = UNSET
        else:
            repository_id = UUID(_repository_id)

        repository_name = d.pop("repositoryName", UNSET)

        repository_region_id = d.pop("repositoryRegionId", UNSET)

        repository_region_name = d.pop("repositoryRegionName", UNSET)

        repository_immutability_enabled = d.pop("repositoryImmutabilityEnabled", UNSET)

        repository_encryption_enabled = d.pop("repositoryEncryptionEnabled", UNSET)

        region_resource_id = d.pop("regionResourceId", UNSET)

        region_name = d.pop("regionName", UNSET)

        repository_configuration_item = cls(
            repository_id=repository_id,
            repository_name=repository_name,
            repository_region_id=repository_region_id,
            repository_region_name=repository_region_name,
            repository_immutability_enabled=repository_immutability_enabled,
            repository_encryption_enabled=repository_encryption_enabled,
            region_resource_id=region_resource_id,
            region_name=region_name,
        )

        repository_configuration_item.additional_properties = d
        return repository_configuration_item

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
