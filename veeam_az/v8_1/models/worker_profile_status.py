from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.worker_configuration_status_result import WorkerConfigurationStatusResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerProfileStatus")


@_attrs_define
class WorkerProfileStatus:
    """
    Attributes:
        is_virtual_machine_type_available (bool | Unset):
        minimum_memory_requirement_fulfilled (bool | Unset):
        has_recommended_memory (bool | Unset):
        summary (WorkerConfigurationStatusResult | Unset):
    """

    is_virtual_machine_type_available: bool | Unset = UNSET
    minimum_memory_requirement_fulfilled: bool | Unset = UNSET
    has_recommended_memory: bool | Unset = UNSET
    summary: WorkerConfigurationStatusResult | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_virtual_machine_type_available = self.is_virtual_machine_type_available

        minimum_memory_requirement_fulfilled = self.minimum_memory_requirement_fulfilled

        has_recommended_memory = self.has_recommended_memory

        summary: str | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_virtual_machine_type_available is not UNSET:
            field_dict["isVirtualMachineTypeAvailable"] = is_virtual_machine_type_available
        if minimum_memory_requirement_fulfilled is not UNSET:
            field_dict["minimumMemoryRequirementFulfilled"] = minimum_memory_requirement_fulfilled
        if has_recommended_memory is not UNSET:
            field_dict["hasRecommendedMemory"] = has_recommended_memory
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_virtual_machine_type_available = d.pop("isVirtualMachineTypeAvailable", UNSET)

        minimum_memory_requirement_fulfilled = d.pop("minimumMemoryRequirementFulfilled", UNSET)

        has_recommended_memory = d.pop("hasRecommendedMemory", UNSET)

        _summary = d.pop("summary", UNSET)
        summary: WorkerConfigurationStatusResult | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = WorkerConfigurationStatusResult(_summary)

        worker_profile_status = cls(
            is_virtual_machine_type_available=is_virtual_machine_type_available,
            minimum_memory_requirement_fulfilled=minimum_memory_requirement_fulfilled,
            has_recommended_memory=has_recommended_memory,
            summary=summary,
        )

        return worker_profile_status
