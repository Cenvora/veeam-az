from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mongo_db_throughput_scaling_type import MongoDbThroughputScalingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MongoDbThroughputSettings")


@_attrs_define
class MongoDbThroughputSettings:
    """
    Attributes:
        max_throughput (int | Unset):
        type_ (MongoDbThroughputScalingType | Unset):
    """

    max_throughput: int | Unset = UNSET
    type_: MongoDbThroughputScalingType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_throughput = self.max_throughput

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_throughput is not UNSET:
            field_dict["MaxThroughput"] = max_throughput
        if type_ is not UNSET:
            field_dict["Type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_throughput = d.pop("MaxThroughput", UNSET)

        _type_ = d.pop("Type", UNSET)
        type_: MongoDbThroughputScalingType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MongoDbThroughputScalingType(_type_)

        mongo_db_throughput_settings = cls(
            max_throughput=max_throughput,
            type_=type_,
        )

        mongo_db_throughput_settings.additional_properties = d
        return mongo_db_throughput_settings

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
