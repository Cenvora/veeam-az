from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlaStatisticReport")


@_attrs_define
class SlaStatisticReport:
    """Information on SLA compliance for all Azure VMs included into the backup scope of the policy.

    Attributes:
        met_target_sla (float | Unset): Number of VMs whose protection complies with the target SLA value.
        missed_target_sla (float | Unset): Number of VMs for which the target SLA value was missed.
        removed (float | Unset): Number of VMs that were removed from the backup scope during the selected period.
    """

    met_target_sla: float | Unset = UNSET
    missed_target_sla: float | Unset = UNSET
    removed: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        met_target_sla = self.met_target_sla

        missed_target_sla = self.missed_target_sla

        removed = self.removed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if met_target_sla is not UNSET:
            field_dict["metTargetSla"] = met_target_sla
        if missed_target_sla is not UNSET:
            field_dict["missedTargetSla"] = missed_target_sla
        if removed is not UNSET:
            field_dict["removed"] = removed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        met_target_sla = d.pop("metTargetSla", UNSET)

        missed_target_sla = d.pop("missedTargetSla", UNSET)

        removed = d.pop("removed", UNSET)

        sla_statistic_report = cls(
            met_target_sla=met_target_sla,
            missed_target_sla=missed_target_sla,
            removed=removed,
        )

        sla_statistic_report.additional_properties = d
        return sla_statistic_report

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
