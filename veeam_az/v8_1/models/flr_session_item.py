from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.flr_session_item_type import FlrSessionItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrSessionItem")


@_attrs_define
class FlrSessionItem:
    """
    Attributes:
        item_path (str | Unset): The path to the directory on the Azure VM where the item is located.
        name (str | Unset): The name of the item.
        type_ (FlrSessionItemType | Unset): The type of the item.
        size (int | Unset): The size of the item.
        last_modification_time (datetime.datetime | Unset): Date and time when the item was last modified.
    """

    item_path: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: FlrSessionItemType | Unset = UNSET
    size: int | Unset = UNSET
    last_modification_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_path = self.item_path

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        size = self.size

        last_modification_time: str | Unset = UNSET
        if not isinstance(self.last_modification_time, Unset):
            last_modification_time = self.last_modification_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if item_path is not UNSET:
            field_dict["itemPath"] = item_path
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if size is not UNSET:
            field_dict["size"] = size
        if last_modification_time is not UNSET:
            field_dict["lastModificationTime"] = last_modification_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_path = d.pop("itemPath", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: FlrSessionItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FlrSessionItemType(_type_)

        size = d.pop("size", UNSET)

        _last_modification_time = d.pop("lastModificationTime", UNSET)
        last_modification_time: datetime.datetime | Unset
        if isinstance(_last_modification_time, Unset):
            last_modification_time = UNSET
        else:
            last_modification_time = isoparse(_last_modification_time)

        flr_session_item = cls(
            item_path=item_path,
            name=name,
            type_=type_,
            size=size,
            last_modification_time=last_modification_time,
        )

        return flr_session_item
