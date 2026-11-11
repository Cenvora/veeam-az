from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagementGroup")


@_attrs_define
class ManagementGroup:
    """Information on each management group.

    Attributes:
        id (str | Unset): Specifies the Microsoft Azure ID assigned to the management group
        name (str | Unset): Specifies the name of the management group
        subscription_count (float | Unset): Specifies the number of subscriptions inside the management group
        readonly (bool | Unset): Defines whether the user can modify the management group or not
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    subscription_count: float | Unset = UNSET
    readonly: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        subscription_count = self.subscription_count

        readonly = self.readonly

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if subscription_count is not UNSET:
            field_dict["subscriptionCount"] = subscription_count
        if readonly is not UNSET:
            field_dict["readonly"] = readonly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        subscription_count = d.pop("subscriptionCount", UNSET)

        readonly = d.pop("readonly", UNSET)

        management_group = cls(
            id=id,
            name=name,
            subscription_count=subscription_count,
            readonly=readonly,
        )

        return management_group
