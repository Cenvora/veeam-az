from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimation_item_costs_meter import CostEstimationItemCostsMeter
    from ..models.cost_estimation_warning import CostEstimationWarning
    from ..models.price_per_month import PricePerMonth


T = TypeVar("T", bound="CostEstimationItemCostsData")


@_attrs_define
class CostEstimationItemCostsData:
    """Information on the cost estimation for Azure services used by the backup policy.

    Attributes:
        price_per_month (PricePerMonth | Unset): Information on the monthly price for creating and maintaining snapshots
            by the backup policy.
        meters (list[CostEstimationItemCostsMeter] | None | Unset): Information on the Azure billing meters used for
            cost estimation.
        warnings (list[CostEstimationWarning] | None | Unset): Information on cost estimation warnings.
    """

    price_per_month: PricePerMonth | Unset = UNSET
    meters: list[CostEstimationItemCostsMeter] | None | Unset = UNSET
    warnings: list[CostEstimationWarning] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        price_per_month: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price_per_month, Unset):
            price_per_month = self.price_per_month.to_dict()

        meters: list[dict[str, Any]] | None | Unset
        if isinstance(self.meters, Unset):
            meters = UNSET
        elif isinstance(self.meters, list):
            meters = []
            for meters_type_0_item_data in self.meters:
                meters_type_0_item = meters_type_0_item_data.to_dict()
                meters.append(meters_type_0_item)

        else:
            meters = self.meters

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
        if price_per_month is not UNSET:
            field_dict["pricePerMonth"] = price_per_month
        if meters is not UNSET:
            field_dict["meters"] = meters
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_estimation_item_costs_meter import CostEstimationItemCostsMeter
        from ..models.cost_estimation_warning import CostEstimationWarning
        from ..models.price_per_month import PricePerMonth

        d = dict(src_dict)
        _price_per_month = d.pop("pricePerMonth", UNSET)
        price_per_month: PricePerMonth | Unset
        if isinstance(_price_per_month, Unset):
            price_per_month = UNSET
        else:
            price_per_month = PricePerMonth.from_dict(_price_per_month)

        def _parse_meters(data: object) -> list[CostEstimationItemCostsMeter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                meters_type_0 = []
                _meters_type_0 = data
                for meters_type_0_item_data in _meters_type_0:
                    meters_type_0_item = CostEstimationItemCostsMeter.from_dict(meters_type_0_item_data)

                    meters_type_0.append(meters_type_0_item)

                return meters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CostEstimationItemCostsMeter] | None | Unset, data)

        meters = _parse_meters(d.pop("meters", UNSET))

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

        cost_estimation_item_costs_data = cls(
            price_per_month=price_per_month,
            meters=meters,
            warnings=warnings,
        )

        return cost_estimation_item_costs_data
