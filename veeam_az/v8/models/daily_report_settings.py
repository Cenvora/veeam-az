from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DailyReportSettings")


@_attrs_define
class DailyReportSettings:
    """Specifies the settings of daily reports.

    Attributes:
        send_daily_report (bool | None | Unset): Defines whether the daily reports will be sent. The default value is
            *false*.
        daily_time (None | str | Unset): Specifies the date and time when the daily reports will be generated and sent.
            The default value is *09:00 AM*.
    """

    send_daily_report: bool | None | Unset = UNSET
    daily_time: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        send_daily_report: bool | None | Unset
        if isinstance(self.send_daily_report, Unset):
            send_daily_report = UNSET
        else:
            send_daily_report = self.send_daily_report

        daily_time: None | str | Unset
        if isinstance(self.daily_time, Unset):
            daily_time = UNSET
        else:
            daily_time = self.daily_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if send_daily_report is not UNSET:
            field_dict["sendDailyReport"] = send_daily_report
        if daily_time is not UNSET:
            field_dict["dailyTime"] = daily_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_send_daily_report(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        send_daily_report = _parse_send_daily_report(d.pop("sendDailyReport", UNSET))

        def _parse_daily_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        daily_time = _parse_daily_time(d.pop("dailyTime", UNSET))

        daily_report_settings = cls(
            send_daily_report=send_daily_report,
            daily_time=daily_time,
        )

        return daily_report_settings
