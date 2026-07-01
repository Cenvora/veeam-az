from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimation_item_costs_data import CostEstimationItemCostsData
    from ..models.cost_estimation_total_value import CostEstimationTotalValue
    from ..models.cost_estimation_warning import CostEstimationWarning


T = TypeVar("T", bound="CostEstimationCosmosDbItem")


@_attrs_define
class CostEstimationCosmosDbItem:
    """
    Attributes:
        protected_item_hash_id (None | str | Unset):
        name (None | str | Unset):
        continuous_backup_cost (CostEstimationItemCostsData | Unset): Information on the cost estimation for Azure
            services used by the backup policy.
        backup_cost (CostEstimationItemCostsData | Unset): Information on the cost estimation for Azure services used by
            the backup policy.
        traffic_cost (CostEstimationItemCostsData | Unset): Information on the cost estimation for Azure services used
            by the backup policy.
        transaction_cost (CostEstimationItemCostsData | Unset): Information on the cost estimation for Azure services
            used by the backup policy.
        total_per_month (CostEstimationTotalValue | Unset): Information on the estimated total cost value.
        warnings (list[CostEstimationWarning] | None | Unset):
    """

    protected_item_hash_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    continuous_backup_cost: CostEstimationItemCostsData | Unset = UNSET
    backup_cost: CostEstimationItemCostsData | Unset = UNSET
    traffic_cost: CostEstimationItemCostsData | Unset = UNSET
    transaction_cost: CostEstimationItemCostsData | Unset = UNSET
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

        continuous_backup_cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.continuous_backup_cost, Unset):
            continuous_backup_cost = self.continuous_backup_cost.to_dict()

        backup_cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_cost, Unset):
            backup_cost = self.backup_cost.to_dict()

        traffic_cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic_cost, Unset):
            traffic_cost = self.traffic_cost.to_dict()

        transaction_cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transaction_cost, Unset):
            transaction_cost = self.transaction_cost.to_dict()

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
        if continuous_backup_cost is not UNSET:
            field_dict["continuousBackupCost"] = continuous_backup_cost
        if backup_cost is not UNSET:
            field_dict["backupCost"] = backup_cost
        if traffic_cost is not UNSET:
            field_dict["trafficCost"] = traffic_cost
        if transaction_cost is not UNSET:
            field_dict["transactionCost"] = transaction_cost
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

        _continuous_backup_cost = d.pop("continuousBackupCost", UNSET)
        continuous_backup_cost: CostEstimationItemCostsData | Unset
        if isinstance(_continuous_backup_cost, Unset):
            continuous_backup_cost = UNSET
        else:
            continuous_backup_cost = CostEstimationItemCostsData.from_dict(_continuous_backup_cost)

        _backup_cost = d.pop("backupCost", UNSET)
        backup_cost: CostEstimationItemCostsData | Unset
        if isinstance(_backup_cost, Unset):
            backup_cost = UNSET
        else:
            backup_cost = CostEstimationItemCostsData.from_dict(_backup_cost)

        _traffic_cost = d.pop("trafficCost", UNSET)
        traffic_cost: CostEstimationItemCostsData | Unset
        if isinstance(_traffic_cost, Unset):
            traffic_cost = UNSET
        else:
            traffic_cost = CostEstimationItemCostsData.from_dict(_traffic_cost)

        _transaction_cost = d.pop("transactionCost", UNSET)
        transaction_cost: CostEstimationItemCostsData | Unset
        if isinstance(_transaction_cost, Unset):
            transaction_cost = UNSET
        else:
            transaction_cost = CostEstimationItemCostsData.from_dict(_transaction_cost)

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

        cost_estimation_cosmos_db_item = cls(
            protected_item_hash_id=protected_item_hash_id,
            name=name,
            continuous_backup_cost=continuous_backup_cost,
            backup_cost=backup_cost,
            traffic_cost=traffic_cost,
            transaction_cost=transaction_cost,
            total_per_month=total_per_month,
            warnings=warnings,
        )

        return cost_estimation_cosmos_db_item
