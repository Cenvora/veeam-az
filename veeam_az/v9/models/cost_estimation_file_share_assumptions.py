from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CostEstimationFileShareAssumptions")


@_attrs_define
class CostEstimationFileShareAssumptions:
    """Assumptions used to calculate the cost.

    Attributes:
        daily_churn_ratio (float): Percentage of data change per day.
    """

    daily_churn_ratio: float

    def to_dict(self) -> dict[str, Any]:
        daily_churn_ratio = self.daily_churn_ratio

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dailyChurnRatio": daily_churn_ratio,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        daily_churn_ratio = d.pop("dailyChurnRatio")

        cost_estimation_file_share_assumptions = cls(
            daily_churn_ratio=daily_churn_ratio,
        )

        return cost_estimation_file_share_assumptions
