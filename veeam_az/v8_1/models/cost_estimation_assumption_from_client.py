from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostEstimationAssumptionFromClient")


@_attrs_define
class CostEstimationAssumptionFromClient:
    r"""\[Optional assumptions about protected items] Specifies average daily churn and expected disk occupy ratio.

    Attributes:
        daily_churn (float | None | Unset): \[Daily churn of protected item] The portion of data which is changed during
            one day (value 0 - 1 means 0 - 100%).
        disk_occupied_size_ratio (float | None | Unset): \[Ratio of occupied disk space] valid values are between 0 and
            1. 0 means no data at disk, 1 means full disk).
        data_compression_ratio (float | None | Unset): \[Ratio how much are data on disk compressible] valid values are
            between 0 and 1. 0 means that data can be compress practically to 0 percent of original, 1 means compression
            will not make data smaller of all).
    """

    daily_churn: float | None | Unset = UNSET
    disk_occupied_size_ratio: float | None | Unset = UNSET
    data_compression_ratio: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_churn: float | None | Unset
        if isinstance(self.daily_churn, Unset):
            daily_churn = UNSET
        else:
            daily_churn = self.daily_churn

        disk_occupied_size_ratio: float | None | Unset
        if isinstance(self.disk_occupied_size_ratio, Unset):
            disk_occupied_size_ratio = UNSET
        else:
            disk_occupied_size_ratio = self.disk_occupied_size_ratio

        data_compression_ratio: float | None | Unset
        if isinstance(self.data_compression_ratio, Unset):
            data_compression_ratio = UNSET
        else:
            data_compression_ratio = self.data_compression_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily_churn is not UNSET:
            field_dict["dailyChurn"] = daily_churn
        if disk_occupied_size_ratio is not UNSET:
            field_dict["diskOccupiedSizeRatio"] = disk_occupied_size_ratio
        if data_compression_ratio is not UNSET:
            field_dict["dataCompressionRatio"] = data_compression_ratio

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_daily_churn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        daily_churn = _parse_daily_churn(d.pop("dailyChurn", UNSET))

        def _parse_disk_occupied_size_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        disk_occupied_size_ratio = _parse_disk_occupied_size_ratio(d.pop("diskOccupiedSizeRatio", UNSET))

        def _parse_data_compression_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        data_compression_ratio = _parse_data_compression_ratio(d.pop("dataCompressionRatio", UNSET))

        cost_estimation_assumption_from_client = cls(
            daily_churn=daily_churn,
            disk_occupied_size_ratio=disk_occupied_size_ratio,
            data_compression_ratio=data_compression_ratio,
        )

        cost_estimation_assumption_from_client.additional_properties = d
        return cost_estimation_assumption_from_client

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
