from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CosmosDbResourceEvent")


@_attrs_define
class CosmosDbResourceEvent:
    """Information on an event.

    Attributes:
        event_description (str | Unset): Description of the event.
        event_time (datetime.datetime | Unset): Date and time when the event occurred.
    """

    event_description: str | Unset = UNSET
    event_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        event_description = self.event_description

        event_time: str | Unset = UNSET
        if not isinstance(self.event_time, Unset):
            event_time = self.event_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if event_description is not UNSET:
            field_dict["EventDescription"] = event_description
        if event_time is not UNSET:
            field_dict["EventTime"] = event_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_description = d.pop("EventDescription", UNSET)

        _event_time = d.pop("EventTime", UNSET)
        event_time: datetime.datetime | Unset
        if isinstance(_event_time, Unset):
            event_time = UNSET
        else:
            event_time = isoparse(_event_time)

        cosmos_db_resource_event = cls(
            event_description=event_description,
            event_time=event_time,
        )

        return cosmos_db_resource_event
