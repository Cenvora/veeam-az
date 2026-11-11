from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.region_cpu_core_resource import RegionCpuCoreResource


T = TypeVar("T", bound="EntraIdResource")


@_attrs_define
class EntraIdResource:
    """TBD Resource consumption; The exact number value doesn't mean anything, we care about ratio, but we need to be
    consistent so e.g. two different VBAz instances don't return different numbers for the same tenant etc.

        Attributes:
            cpu_resource (int): TBD CPU consumption; It estimates CPU usage
            ram_resource (int): TBD RAM consumption;
            item_resource (int): TBD Total number of tenant items; Just number of resources (VMs) we protect
            worker_cpu_core_resource (list[RegionCpuCoreResource]): TBD cpuCores usages per region
    """

    cpu_resource: int
    ram_resource: int
    item_resource: int
    worker_cpu_core_resource: list[RegionCpuCoreResource]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_resource = self.cpu_resource

        ram_resource = self.ram_resource

        item_resource = self.item_resource

        worker_cpu_core_resource = []
        for worker_cpu_core_resource_item_data in self.worker_cpu_core_resource:
            worker_cpu_core_resource_item = worker_cpu_core_resource_item_data.to_dict()
            worker_cpu_core_resource.append(worker_cpu_core_resource_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpuResource": cpu_resource,
                "ramResource": ram_resource,
                "itemResource": item_resource,
                "workerCpuCoreResource": worker_cpu_core_resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.region_cpu_core_resource import RegionCpuCoreResource

        d = dict(src_dict)
        cpu_resource = d.pop("cpuResource")

        ram_resource = d.pop("ramResource")

        item_resource = d.pop("itemResource")

        worker_cpu_core_resource = []
        _worker_cpu_core_resource = d.pop("workerCpuCoreResource")
        for worker_cpu_core_resource_item_data in _worker_cpu_core_resource:
            worker_cpu_core_resource_item = RegionCpuCoreResource.from_dict(worker_cpu_core_resource_item_data)

            worker_cpu_core_resource.append(worker_cpu_core_resource_item)

        entra_id_resource = cls(
            cpu_resource=cpu_resource,
            ram_resource=ram_resource,
            item_resource=item_resource,
            worker_cpu_core_resource=worker_cpu_core_resource,
        )

        entra_id_resource.additional_properties = d
        return entra_id_resource

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
