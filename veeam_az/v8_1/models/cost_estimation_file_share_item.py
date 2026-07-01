from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimation_item_costs_data import CostEstimationItemCostsData
    from ..models.cost_estimation_total_value import CostEstimationTotalValue
    from ..models.cost_estimation_warning import CostEstimationWarning


T = TypeVar("T", bound="CostEstimationFileShareItem")


@_attrs_define
class CostEstimationFileShareItem:
    """Information on cost estimation of each protected resource.

    Attributes:
        protected_item_hash_id (None | str | Unset): System ID assigned to the protected resource in the Veeam Backup
            for Microsoft Azure REST API.
        name (None | str | Unset): Name of the protected resource.
        snapshot_cost (CostEstimationItemCostsData | Unset): Information on the cost estimation for Azure services used
            by the backup policy.
        total_per_month (CostEstimationTotalValue | Unset): Information on the estimated total cost value.
        warnings (list[CostEstimationWarning] | None | Unset): Information on cost estimation warnings.
    """

    protected_item_hash_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    snapshot_cost: CostEstimationItemCostsData | Unset = UNSET
    total_per_month: CostEstimationTotalValue | Unset = UNSET
    warnings: list[CostEstimationWarning] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        protected_item_hash_id: None | str | Unset
        if isinstance(self.protected_item_hash_id, Unset):
            protected_item_hash_id = UNSET
        else:
            protected_item_hash_id = self.protected_item_hash_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        snapshot_cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot_cost, Unset):
            snapshot_cost = self.snapshot_cost.to_dict()

        total_per_month: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_per_month, Unset):
            total_per_month = self.total_per_month.to_dict()

        warnings: list[dict[str, Any]] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = []
            for warnings_type_0_item_data in self.warnings:
                warnings_type_0_item = warnings_type_0_item_data.to_dict()
                warnings.append(warnings_type_0_item)

        else:
            warnings = self.warnings

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if protected_item_hash_id is not UNSET:
            field_dict["protectedItemHashId"] = protected_item_hash_id
        if name is not UNSET:
            field_dict["name"] = name
        if snapshot_cost is not UNSET:
            field_dict["snapshotCost"] = snapshot_cost
        if total_per_month is not UNSET:
            field_dict["totalPerMonth"] = total_per_month
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_estimation_item_costs_data import CostEstimationItemCostsData
        from ..models.cost_estimation_total_value import CostEstimationTotalValue
        from ..models.cost_estimation_warning import CostEstimationWarning

        d = dict(src_dict)

        def _parse_protected_item_hash_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        protected_item_hash_id = _parse_protected_item_hash_id(d.pop("protectedItemHashId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _snapshot_cost = d.pop("snapshotCost", UNSET)
        snapshot_cost: CostEstimationItemCostsData | Unset
        if isinstance(_snapshot_cost, Unset):
            snapshot_cost = UNSET
        else:
            snapshot_cost = CostEstimationItemCostsData.from_dict(_snapshot_cost)

        _total_per_month = d.pop("totalPerMonth", UNSET)
        total_per_month: CostEstimationTotalValue | Unset
        if isinstance(_total_per_month, Unset):
            total_per_month = UNSET
        else:
            total_per_month = CostEstimationTotalValue.from_dict(_total_per_month)

        def _parse_warnings(data: object) -> list[CostEstimationWarning] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = []
                _warnings_type_0 = data
                for warnings_type_0_item_data in _warnings_type_0:
                    warnings_type_0_item = CostEstimationWarning.from_dict(warnings_type_0_item_data)

                    warnings_type_0.append(warnings_type_0_item)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CostEstimationWarning] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

        cost_estimation_file_share_item = cls(
            protected_item_hash_id=protected_item_hash_id,
            name=name,
            snapshot_cost=snapshot_cost,
            total_per_month=total_per_month,
            warnings=warnings,
        )

        return cost_estimation_file_share_item
