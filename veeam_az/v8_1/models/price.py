from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Price")


@_attrs_define
class Price:
    """Information on the price per hour for the Azure VM size.

    Attributes:
        value (float | Unset): Price value.
        currency (None | str | Unset): Price currency.
    """

    value: float | Unset = UNSET
    currency: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        price = cls(
            value=value,
            currency=currency,
        )

        return price
