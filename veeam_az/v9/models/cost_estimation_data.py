from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimation_assumptions import CostEstimationAssumptions
    from ..models.cost_estimation_totals import CostEstimationTotals
    from ..models.cost_estimation_warning_group import CostEstimationWarningGroup


T = TypeVar("T", bound="CostEstimationData")


@_attrs_define
class CostEstimationData:
    """Information on total estimated costs per month, assumptions and warnings.

    Attributes:
        totals (CostEstimationTotals | Unset): Information on the cost estimation totals.
        assumptions (CostEstimationAssumptions | Unset): Assumptions used to calculate the cost.
        warning_groups (list[CostEstimationWarningGroup] | None | Unset): Information on the warning groups of the
            backup policy estimated cost.
        currency_iso_code (None | str | Unset): ISO code of the used currency.
    """

    totals: CostEstimationTotals | Unset = UNSET
    assumptions: CostEstimationAssumptions | Unset = UNSET
    warning_groups: list[CostEstimationWarningGroup] | None | Unset = UNSET
    currency_iso_code: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        assumptions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assumptions, Unset):
            assumptions = self.assumptions.to_dict()

        warning_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.warning_groups, Unset):
            warning_groups = UNSET
        elif isinstance(self.warning_groups, list):
            warning_groups = []
            for warning_groups_type_0_item_data in self.warning_groups:
                warning_groups_type_0_item = warning_groups_type_0_item_data.to_dict()
                warning_groups.append(warning_groups_type_0_item)

        else:
            warning_groups = self.warning_groups

        currency_iso_code: None | str | Unset
        if isinstance(self.currency_iso_code, Unset):
            currency_iso_code = UNSET
        else:
            currency_iso_code = self.currency_iso_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if totals is not UNSET:
            field_dict["totals"] = totals
        if assumptions is not UNSET:
            field_dict["assumptions"] = assumptions
        if warning_groups is not UNSET:
            field_dict["warningGroups"] = warning_groups
        if currency_iso_code is not UNSET:
            field_dict["currencyIsoCode"] = currency_iso_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_estimation_assumptions import CostEstimationAssumptions
        from ..models.cost_estimation_totals import CostEstimationTotals
        from ..models.cost_estimation_warning_group import CostEstimationWarningGroup

        d = dict(src_dict)
        _totals = d.pop("totals", UNSET)
        totals: CostEstimationTotals | Unset
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = CostEstimationTotals.from_dict(_totals)

        _assumptions = d.pop("assumptions", UNSET)
        assumptions: CostEstimationAssumptions | Unset
        if isinstance(_assumptions, Unset):
            assumptions = UNSET
        else:
            assumptions = CostEstimationAssumptions.from_dict(_assumptions)

        def _parse_warning_groups(data: object) -> list[CostEstimationWarningGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warning_groups_type_0 = []
                _warning_groups_type_0 = data
                for warning_groups_type_0_item_data in _warning_groups_type_0:
                    warning_groups_type_0_item = CostEstimationWarningGroup.from_dict(warning_groups_type_0_item_data)

                    warning_groups_type_0.append(warning_groups_type_0_item)

                return warning_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CostEstimationWarningGroup] | None | Unset, data)

        warning_groups = _parse_warning_groups(d.pop("warningGroups", UNSET))

        def _parse_currency_iso_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_iso_code = _parse_currency_iso_code(d.pop("currencyIsoCode", UNSET))

        cost_estimation_data = cls(
            totals=totals,
            assumptions=assumptions,
            warning_groups=warning_groups,
            currency_iso_code=currency_iso_code,
        )

        return cost_estimation_data
