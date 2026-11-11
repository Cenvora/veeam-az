from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DisabledSections")


@_attrs_define
class DisabledSections:
    """Information that is not displayed in the Veeam Backup for Microsoft Azure UI.

    Attributes:
        configuration_snapshot_based (bool | Unset): Defines whether the configuration snapshot is not displayed in the
            Veeam Backup for Microsoft Azure UI.
    """

    configuration_snapshot_based: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration_snapshot_based = self.configuration_snapshot_based

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration_snapshot_based is not UNSET:
            field_dict["ConfigurationSnapshotBased"] = configuration_snapshot_based

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        configuration_snapshot_based = d.pop("ConfigurationSnapshotBased", UNSET)

        disabled_sections = cls(
            configuration_snapshot_based=configuration_snapshot_based,
        )

        disabled_sections.additional_properties = d
        return disabled_sections

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
