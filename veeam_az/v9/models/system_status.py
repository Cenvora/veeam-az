from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.system_state import SystemState
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemStatus")


@_attrs_define
class SystemStatus:
    """
    Attributes:
        state (SystemState | Unset): Status of backup appliance after update.
        server_time (datetime.datetime | Unset): Current date and time of the server in the UTC time zone.
    """

    state: SystemState | Unset = UNSET
    server_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        server_time: str | Unset = UNSET
        if not isinstance(self.server_time, Unset):
            server_time = self.server_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if server_time is not UNSET:
            field_dict["serverTime"] = server_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: SystemState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = SystemState(_state)

        _server_time = d.pop("serverTime", UNSET)
        server_time: datetime.datetime | Unset
        if isinstance(_server_time, Unset):
            server_time = UNSET
        else:
            server_time = isoparse(_server_time)

        system_status = cls(
            state=state,
            server_time=server_time,
        )

        return system_status
