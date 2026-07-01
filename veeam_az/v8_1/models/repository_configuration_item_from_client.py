from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryConfigurationItemFromClient")


@_attrs_define
class RepositoryConfigurationItemFromClient:
    """Specifies region-specific repository settings.

    Attributes:
        repository_id (UUID | Unset): Specifies a system ID assigned to a region-specific repository in the Veeam Backup
            for Microsoft Azure REST API.
        region_resource_id (str | Unset): Specifies a resource ID assigned in Microsoft Azure to a region for which the
            repository will be used.
    """

    repository_id: UUID | Unset = UNSET
    region_resource_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository_id: str | Unset = UNSET
        if not isinstance(self.repository_id, Unset):
            repository_id = str(self.repository_id)

        region_resource_id = self.region_resource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if region_resource_id is not UNSET:
            field_dict["regionResourceId"] = region_resource_id

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

        region_resource_id = d.pop("regionResourceId", UNSET)

        repository_configuration_item_from_client = cls(
            repository_id=repository_id,
            region_resource_id=region_resource_id,
        )

        repository_configuration_item_from_client.additional_properties = d
        return repository_configuration_item_from_client

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
