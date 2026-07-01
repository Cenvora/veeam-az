from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimation_total_value import CostEstimationTotalValue


T = TypeVar("T", bound="CostEstimationFileShareTotals")


@_attrs_define
class CostEstimationFileShareTotals:
    """Information on the cost estimation totals.

    Attributes:
        total_costs (CostEstimationTotalValue | Unset): Information on the estimated total cost value.
        total_snapshot_costs (CostEstimationTotalValue | Unset): Information on the estimated total cost value.
    """

    total_costs: CostEstimationTotalValue | Unset = UNSET
    total_snapshot_costs: CostEstimationTotalValue | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_costs, Unset):
            total_costs = self.total_costs.to_dict()

        total_snapshot_costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_snapshot_costs, Unset):
            total_snapshot_costs = self.total_snapshot_costs.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_costs is not UNSET:
            field_dict["totalCosts"] = total_costs
        if total_snapshot_costs is not UNSET:
            field_dict["totalSnapshotCosts"] = total_snapshot_costs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_estimation_total_value import CostEstimationTotalValue

        d = dict(src_dict)
        _total_costs = d.pop("totalCosts", UNSET)
        total_costs: CostEstimationTotalValue | Unset
        if isinstance(_total_costs, Unset):
            total_costs = UNSET
        else:
            total_costs = CostEstimationTotalValue.from_dict(_total_costs)

        _total_snapshot_costs = d.pop("totalSnapshotCosts", UNSET)
        total_snapshot_costs: CostEstimationTotalValue | Unset
        if isinstance(_total_snapshot_costs, Unset):
            total_snapshot_costs = UNSET
        else:
            total_snapshot_costs = CostEstimationTotalValue.from_dict(_total_snapshot_costs)

        cost_estimation_file_share_totals = cls(
            total_costs=total_costs,
            total_snapshot_costs=total_snapshot_costs,
        )

        return cost_estimation_file_share_totals
