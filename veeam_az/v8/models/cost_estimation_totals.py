from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimation_total_value import CostEstimationTotalValue


T = TypeVar("T", bound="CostEstimationTotals")


@_attrs_define
class CostEstimationTotals:
    """Information on the cost estimation totals.

    Attributes:
        total_costs (CostEstimationTotalValue | Unset): Information on the estimated total cost value.
        total_snapshot_costs (CostEstimationTotalValue | Unset): Information on the estimated total cost value.
        total_backup_costs (CostEstimationTotalValue | Unset): Information on the estimated total cost value.
        total_archive_costs (CostEstimationTotalValue | Unset): Information on the estimated total cost value.
        total_traffic_costs (CostEstimationTotalValue | Unset): Information on the estimated total cost value.
        total_transaction_costs (CostEstimationTotalValue | Unset): Information on the estimated total cost value.
    """

    total_costs: CostEstimationTotalValue | Unset = UNSET
    total_snapshot_costs: CostEstimationTotalValue | Unset = UNSET
    total_backup_costs: CostEstimationTotalValue | Unset = UNSET
    total_archive_costs: CostEstimationTotalValue | Unset = UNSET
    total_traffic_costs: CostEstimationTotalValue | Unset = UNSET
    total_transaction_costs: CostEstimationTotalValue | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_costs, Unset):
            total_costs = self.total_costs.to_dict()

        total_snapshot_costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_snapshot_costs, Unset):
            total_snapshot_costs = self.total_snapshot_costs.to_dict()

        total_backup_costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_backup_costs, Unset):
            total_backup_costs = self.total_backup_costs.to_dict()

        total_archive_costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_archive_costs, Unset):
            total_archive_costs = self.total_archive_costs.to_dict()

        total_traffic_costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_traffic_costs, Unset):
            total_traffic_costs = self.total_traffic_costs.to_dict()

        total_transaction_costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_transaction_costs, Unset):
            total_transaction_costs = self.total_transaction_costs.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_costs is not UNSET:
            field_dict["totalCosts"] = total_costs
        if total_snapshot_costs is not UNSET:
            field_dict["totalSnapshotCosts"] = total_snapshot_costs
        if total_backup_costs is not UNSET:
            field_dict["totalBackupCosts"] = total_backup_costs
        if total_archive_costs is not UNSET:
            field_dict["totalArchiveCosts"] = total_archive_costs
        if total_traffic_costs is not UNSET:
            field_dict["totalTrafficCosts"] = total_traffic_costs
        if total_transaction_costs is not UNSET:
            field_dict["totalTransactionCosts"] = total_transaction_costs

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

        _total_backup_costs = d.pop("totalBackupCosts", UNSET)
        total_backup_costs: CostEstimationTotalValue | Unset
        if isinstance(_total_backup_costs, Unset):
            total_backup_costs = UNSET
        else:
            total_backup_costs = CostEstimationTotalValue.from_dict(_total_backup_costs)

        _total_archive_costs = d.pop("totalArchiveCosts", UNSET)
        total_archive_costs: CostEstimationTotalValue | Unset
        if isinstance(_total_archive_costs, Unset):
            total_archive_costs = UNSET
        else:
            total_archive_costs = CostEstimationTotalValue.from_dict(_total_archive_costs)

        _total_traffic_costs = d.pop("totalTrafficCosts", UNSET)
        total_traffic_costs: CostEstimationTotalValue | Unset
        if isinstance(_total_traffic_costs, Unset):
            total_traffic_costs = UNSET
        else:
            total_traffic_costs = CostEstimationTotalValue.from_dict(_total_traffic_costs)

        _total_transaction_costs = d.pop("totalTransactionCosts", UNSET)
        total_transaction_costs: CostEstimationTotalValue | Unset
        if isinstance(_total_transaction_costs, Unset):
            total_transaction_costs = UNSET
        else:
            total_transaction_costs = CostEstimationTotalValue.from_dict(_total_transaction_costs)

        cost_estimation_totals = cls(
            total_costs=total_costs,
            total_snapshot_costs=total_snapshot_costs,
            total_backup_costs=total_backup_costs,
            total_archive_costs=total_archive_costs,
            total_traffic_costs=total_traffic_costs,
            total_transaction_costs=total_transaction_costs,
        )

        return cost_estimation_totals
