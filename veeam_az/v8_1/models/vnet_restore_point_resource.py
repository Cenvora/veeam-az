from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.vnet_resource_state import VnetResourceState
from ..models.vnet_resource_type import VnetResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VnetRestorePointResource")


@_attrs_define
class VnetRestorePointResource:
    """
    Attributes:
        resource_id (str | Unset):
        resource_name (str | Unset):
        type_ (VnetResourceType | Unset):
        modification_date (datetime.datetime | Unset):
        state (VnetResourceState | Unset):
        region_name (str | Unset):
    """

    resource_id: str | Unset = UNSET
    resource_name: str | Unset = UNSET
    type_: VnetResourceType | Unset = UNSET
    modification_date: datetime.datetime | Unset = UNSET
    state: VnetResourceState | Unset = UNSET
    region_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        resource_name = self.resource_name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        modification_date: str | Unset = UNSET
        if not isinstance(self.modification_date, Unset):
            modification_date = self.modification_date.isoformat()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        region_name = self.region_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if resource_name is not UNSET:
            field_dict["resourceName"] = resource_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if modification_date is not UNSET:
            field_dict["modificationDate"] = modification_date
        if state is not UNSET:
            field_dict["state"] = state
        if region_name is not UNSET:
            field_dict["regionName"] = region_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_id = d.pop("resourceId", UNSET)

        resource_name = d.pop("resourceName", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: VnetResourceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VnetResourceType(_type_)

        _modification_date = d.pop("modificationDate", UNSET)
        modification_date: datetime.datetime | Unset
        if isinstance(_modification_date, Unset):
            modification_date = UNSET
        else:
            modification_date = isoparse(_modification_date)

        _state = d.pop("state", UNSET)
        state: VnetResourceState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = VnetResourceState(_state)

        region_name = d.pop("regionName", UNSET)

        vnet_restore_point_resource = cls(
            resource_id=resource_id,
            resource_name=resource_name,
            type_=type_,
            modification_date=modification_date,
            state=state,
            region_name=region_name,
        )

        return vnet_restore_point_resource
