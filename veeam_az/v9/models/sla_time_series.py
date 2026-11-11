from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sla_time_series_point import SlaTimeSeriesPoint


T = TypeVar("T", bound="SlaTimeSeries")


@_attrs_define
class SlaTimeSeries:
    """
    Attributes:
        sla_time_series_point (list[SlaTimeSeriesPoint] | Unset):
    """

    sla_time_series_point: list[SlaTimeSeriesPoint] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sla_time_series_point: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sla_time_series_point, Unset):
            sla_time_series_point = []
            for sla_time_series_point_item_data in self.sla_time_series_point:
                sla_time_series_point_item = sla_time_series_point_item_data.to_dict()
                sla_time_series_point.append(sla_time_series_point_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sla_time_series_point is not UNSET:
            field_dict["SlaTimeSeriesPoint"] = sla_time_series_point

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sla_time_series_point import SlaTimeSeriesPoint

        d = dict(src_dict)
        _sla_time_series_point = d.pop("SlaTimeSeriesPoint", UNSET)
        sla_time_series_point: list[SlaTimeSeriesPoint] | Unset = UNSET
        if _sla_time_series_point is not UNSET:
            sla_time_series_point = []
            for sla_time_series_point_item_data in _sla_time_series_point:
                sla_time_series_point_item = SlaTimeSeriesPoint.from_dict(sla_time_series_point_item_data)

                sla_time_series_point.append(sla_time_series_point_item)

        sla_time_series = cls(
            sla_time_series_point=sla_time_series_point,
        )

        sla_time_series.additional_properties = d
        return sla_time_series

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
