from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.licensed_resource_state import LicensedResourceState
from ..models.licensed_resource_type import LicensedResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LicensedResource")


@_attrs_define
class LicensedResource:
    """
    Attributes:
        id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to a license unit
            consumed by an Azure resource.
        name (None | str | Unset): Name of the Azure resource.
        resource_type (LicensedResourceType | Unset): Type of the resource.
        licensed_state (LicensedResourceState | Unset): License state of the license unit consumed by an Azure resource.
        last_backup_time (datetime.datetime | None | Unset): Date and time of the most recent backup of the protected
            resource.
        cost (float | Unset):
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    resource_type: LicensedResourceType | Unset = UNSET
    licensed_state: LicensedResourceState | Unset = UNSET
    last_backup_time: datetime.datetime | None | Unset = UNSET
    cost: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        resource_type: str | Unset = UNSET
        if not isinstance(self.resource_type, Unset):
            resource_type = self.resource_type.value

        licensed_state: str | Unset = UNSET
        if not isinstance(self.licensed_state, Unset):
            licensed_state = self.licensed_state.value

        last_backup_time: None | str | Unset
        if isinstance(self.last_backup_time, Unset):
            last_backup_time = UNSET
        elif isinstance(self.last_backup_time, datetime.datetime):
            last_backup_time = self.last_backup_time.isoformat()
        else:
            last_backup_time = self.last_backup_time

        cost = self.cost

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if licensed_state is not UNSET:
            field_dict["licensedState"] = licensed_state
        if last_backup_time is not UNSET:
            field_dict["lastBackupTime"] = last_backup_time
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _resource_type = d.pop("resourceType", UNSET)
        resource_type: LicensedResourceType | Unset
        if isinstance(_resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = LicensedResourceType(_resource_type)

        _licensed_state = d.pop("licensedState", UNSET)
        licensed_state: LicensedResourceState | Unset
        if isinstance(_licensed_state, Unset):
            licensed_state = UNSET
        else:
            licensed_state = LicensedResourceState(_licensed_state)

        def _parse_last_backup_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_time_type_0 = isoparse(data)

                return last_backup_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_backup_time = _parse_last_backup_time(d.pop("lastBackupTime", UNSET))

        cost = d.pop("cost", UNSET)

        licensed_resource = cls(
            id=id,
            name=name,
            resource_type=resource_type,
            licensed_state=licensed_state,
            last_backup_time=last_backup_time,
            cost=cost,
        )

        return licensed_resource
