from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataRetrievalExtendOptions")


@_attrs_define
class DataRetrievalExtendOptions:
    """
    Attributes:
        number_of_days (int | Unset): Specifies the number of days for which the data availability period will be
            extended.
    """

    number_of_days: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        number_of_days = self.number_of_days

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if number_of_days is not UNSET:
            field_dict["numberOfDays"] = number_of_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number_of_days = d.pop("numberOfDays", UNSET)

        data_retrieval_extend_options = cls(
            number_of_days=number_of_days,
        )

        return data_retrieval_extend_options
