from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlaThresholdSettings")


@_attrs_define
class SlaThresholdSettings:
    """Specifies the SLA threshold settings.

    Attributes:
        met_target_above (int | Unset): Specifies the SLA threshold, a percentage of successfully created restore points
            out of the total number of restore points produced by an SLA-based backup policy.
        missed_target_below (int | Unset):
    """

    met_target_above: int | Unset = UNSET
    missed_target_below: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        met_target_above = self.met_target_above

        missed_target_below = self.missed_target_below

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if met_target_above is not UNSET:
            field_dict["metTargetAbove"] = met_target_above
        if missed_target_below is not UNSET:
            field_dict["missedTargetBelow"] = missed_target_below

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        met_target_above = d.pop("metTargetAbove", UNSET)

        missed_target_below = d.pop("missedTargetBelow", UNSET)

        sla_threshold_settings = cls(
            met_target_above=met_target_above,
            missed_target_below=missed_target_below,
        )

        sla_threshold_settings.additional_properties = d
        return sla_threshold_settings

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
