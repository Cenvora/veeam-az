from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.vnet_resource_type import VnetResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VnetRestorePointResourceTypeWithCount")


@_attrs_define
class VnetRestorePointResourceTypeWithCount:
    """
    Attributes:
        type_ (VnetResourceType | Unset):
        count (int | Unset):
    """

    type_: VnetResourceType | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: VnetResourceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VnetResourceType(_type_)

        count = d.pop("count", UNSET)

        vnet_restore_point_resource_type_with_count = cls(
            type_=type_,
            count=count,
        )

        return vnet_restore_point_resource_type_with_count
