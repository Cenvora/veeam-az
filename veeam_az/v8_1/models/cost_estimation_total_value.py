from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimation_warning import CostEstimationWarning
    from ..models.price_per_month import PricePerMonth


T = TypeVar("T", bound="CostEstimationTotalValue")


@_attrs_define
class CostEstimationTotalValue:
    """Information on the estimated total cost value.

    Attributes:
        price_per_month (PricePerMonth | Unset): Information on the monthly price for creating and maintaining snapshots
            by the backup policy.
        warnings (list[CostEstimationWarning] | None | Unset): Information on cost estimation warnings.
    """

    price_per_month: PricePerMonth | Unset = UNSET
    warnings: list[CostEstimationWarning] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        price_per_month: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price_per_month, Unset):
            price_per_month = self.price_per_month.to_dict()

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
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_estimation_warning import CostEstimationWarning
        from ..models.price_per_month import PricePerMonth

        d = dict(src_dict)
        _price_per_month = d.pop("pricePerMonth", UNSET)
        price_per_month: PricePerMonth | Unset
        if isinstance(_price_per_month, Unset):
            price_per_month = UNSET
        else:
            price_per_month = PricePerMonth.from_dict(_price_per_month)

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

        cost_estimation_total_value = cls(
            price_per_month=price_per_month,
            warnings=warnings,
        )

        return cost_estimation_total_value
