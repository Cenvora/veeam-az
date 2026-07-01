from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RegionCpuCoreResource")


@_attrs_define
class RegionCpuCoreResource:
    """
    Attributes:
        region (str):
        cpu_core_resource (int): TBD cpu core consumption in given region;
    """

    region: str
    cpu_core_resource: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region

        cpu_core_resource = self.cpu_core_resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
                "cpuCoreResource": cpu_core_resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        region = d.pop("region")

        cpu_core_resource = d.pop("cpuCoreResource")

        region_cpu_core_resource = cls(
            region=region,
            cpu_core_resource=cpu_core_resource,
        )

        region_cpu_core_resource.additional_properties = d
        return region_cpu_core_resource

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
