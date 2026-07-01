from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.price_per_month_type import PricePerMonthType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PricePerMonth")


@_attrs_define
class PricePerMonth:
    """Information on the monthly price for creating and maintaining snapshots by the backup policy.

    Attributes:
        value (float | Unset): Monthly price for creating and maintaining the snapshot by the backup policy.
        type_ (PricePerMonthType | Unset): Type of the monthly price for creating and maintaining the snapshot by the
            backup policy.
    """

    value: float | Unset = UNSET
    type_: PricePerMonthType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PricePerMonthType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PricePerMonthType(_type_)

        price_per_month = cls(
            value=value,
            type_=type_,
        )

        return price_per_month
