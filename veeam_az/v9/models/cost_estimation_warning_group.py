from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.cost_estimation_warning_type import CostEstimationWarningType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimation_warning_with_data import CostEstimationWarningWithData


T = TypeVar("T", bound="CostEstimationWarningGroup")


@_attrs_define
class CostEstimationWarningGroup:
    """Information on the warning groups of the backup policy estimated cost.

    Attributes:
        type_ (CostEstimationWarningType | Unset): Type of the cost estimation warning.
        text (None | str | Unset): Text of the warning group message.
        warnings (list[CostEstimationWarningWithData] | None | Unset): Information on each warning.
    """

    type_: CostEstimationWarningType | Unset = UNSET
    text: None | str | Unset = UNSET
    warnings: list[CostEstimationWarningWithData] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if text is not UNSET:
            field_dict["text"] = text
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_estimation_warning_with_data import CostEstimationWarningWithData

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: CostEstimationWarningType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CostEstimationWarningType(_type_)

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_warnings(data: object) -> list[CostEstimationWarningWithData] | None | Unset:
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
                    warnings_type_0_item = CostEstimationWarningWithData.from_dict(warnings_type_0_item_data)

                    warnings_type_0.append(warnings_type_0_item)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CostEstimationWarningWithData] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

        cost_estimation_warning_group = cls(
            type_=type_,
            text=text,
            warnings=warnings,
        )

        return cost_estimation_warning_group
