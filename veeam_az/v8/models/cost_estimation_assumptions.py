from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CostEstimationAssumptions")


@_attrs_define
class CostEstimationAssumptions:
    """Assumptions used to calculate the cost.

    Attributes:
        disk_occupied_size_ratio (float): Percentage of disk space occupied by data.
        daily_churn_ratio (float): Percentage of data change per day.
        data_compression_ratio (float): Ratio between the uncompressed and compressed size.
    """

    disk_occupied_size_ratio: float
    daily_churn_ratio: float
    data_compression_ratio: float

    def to_dict(self) -> dict[str, Any]:
        disk_occupied_size_ratio = self.disk_occupied_size_ratio

        daily_churn_ratio = self.daily_churn_ratio

        data_compression_ratio = self.data_compression_ratio

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "diskOccupiedSizeRatio": disk_occupied_size_ratio,
                "dailyChurnRatio": daily_churn_ratio,
                "dataCompressionRatio": data_compression_ratio,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disk_occupied_size_ratio = d.pop("diskOccupiedSizeRatio")

        daily_churn_ratio = d.pop("dailyChurnRatio")

        data_compression_ratio = d.pop("dataCompressionRatio")

        cost_estimation_assumptions = cls(
            disk_occupied_size_ratio=disk_occupied_size_ratio,
            daily_churn_ratio=daily_churn_ratio,
            data_compression_ratio=data_compression_ratio,
        )

        return cost_estimation_assumptions
