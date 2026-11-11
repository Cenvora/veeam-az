from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateTimeInfo")


@_attrs_define
class DateTimeInfo:
    """
    Attributes:
        utc_date_time (datetime.datetime | Unset): Current date and time of the server in the UTC time zone.
        time_zone (None | str | Unset): Time zone used on the server.
    """

    utc_date_time: datetime.datetime | Unset = UNSET
    time_zone: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        utc_date_time: str | Unset = UNSET
        if not isinstance(self.utc_date_time, Unset):
            utc_date_time = self.utc_date_time.isoformat()

        time_zone: None | str | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if utc_date_time is not UNSET:
            field_dict["utcDateTime"] = utc_date_time
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _utc_date_time = d.pop("utcDateTime", UNSET)
        utc_date_time: datetime.datetime | Unset
        if isinstance(_utc_date_time, Unset):
            utc_date_time = UNSET
        else:
            utc_date_time = isoparse(_utc_date_time)

        def _parse_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))

        date_time_info = cls(
            utc_date_time=utc_date_time,
            time_zone=time_zone,
        )

        return date_time_info
