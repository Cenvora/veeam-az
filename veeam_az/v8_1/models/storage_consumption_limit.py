from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.storage_consumption_limit_type import StorageConsumptionLimitType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageConsumptionLimit")


@_attrs_define
class StorageConsumptionLimit:
    """
    Attributes:
        limit_value (int | Unset):
        limit_type (StorageConsumptionLimitType | Unset):
    """

    limit_value: int | Unset = UNSET
    limit_type: StorageConsumptionLimitType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit_value = self.limit_value

        limit_type: str | Unset = UNSET
        if not isinstance(self.limit_type, Unset):
            limit_type = self.limit_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if limit_value is not UNSET:
            field_dict["limitValue"] = limit_value
        if limit_type is not UNSET:
            field_dict["limitType"] = limit_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit_value = d.pop("limitValue", UNSET)

        _limit_type = d.pop("limitType", UNSET)
        limit_type: StorageConsumptionLimitType | Unset
        if isinstance(_limit_type, Unset):
            limit_type = UNSET
        else:
            limit_type = StorageConsumptionLimitType(_limit_type)

        storage_consumption_limit = cls(
            limit_value=limit_value,
            limit_type=limit_type,
        )

        return storage_consumption_limit
