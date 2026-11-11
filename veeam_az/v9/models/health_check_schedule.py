from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.day_number_in_month_health_check import DayNumberInMonthHealthCheck
from ..models.day_of_week import DayOfWeek
from ..models.month import Month
from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthCheckSchedule")


@_attrs_define
class HealthCheckSchedule:
    r"""\[Applies if backup creation is enabled for the backup policy] Specifies the health check schedule settings.

    Attributes:
        health_check_enabled (bool | Unset): Defines whether health check is enabled for the backup policy.
        local_time (datetime.datetime | Unset): Specifies the date and time when the health check will run.
        day_number_in_month (DayNumberInMonthHealthCheck | Unset): Specifies the day of the month when the health check
            will run.
        days_of_week (list[DayOfWeek] | None | Unset): Specifies the day of the week when the health check will run.
        day_of_month (int | None | Unset): \[Applies if the *OnDay* value is specified for the `dayNumberInMonth`
            parameter] Specifies the ordinal number of the day of the month when the health check will run.
        months (list[Month] | None | Unset): Specifies the months when the health check will run.
    """

    health_check_enabled: bool | Unset = UNSET
    local_time: datetime.datetime | Unset = UNSET
    day_number_in_month: DayNumberInMonthHealthCheck | Unset = UNSET
    days_of_week: list[DayOfWeek] | None | Unset = UNSET
    day_of_month: int | None | Unset = UNSET
    months: list[Month] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        health_check_enabled = self.health_check_enabled

        local_time: str | Unset = UNSET
        if not isinstance(self.local_time, Unset):
            local_time = self.local_time.isoformat()

        day_number_in_month: str | Unset = UNSET
        if not isinstance(self.day_number_in_month, Unset):
            day_number_in_month = self.day_number_in_month.value

        days_of_week: list[str] | None | Unset
        if isinstance(self.days_of_week, Unset):
            days_of_week = UNSET
        elif isinstance(self.days_of_week, list):
            days_of_week = []
            for days_of_week_type_0_item_data in self.days_of_week:
                days_of_week_type_0_item = days_of_week_type_0_item_data.value
                days_of_week.append(days_of_week_type_0_item)

        else:
            days_of_week = self.days_of_week

        day_of_month: int | None | Unset
        if isinstance(self.day_of_month, Unset):
            day_of_month = UNSET
        else:
            day_of_month = self.day_of_month

        months: list[str] | None | Unset
        if isinstance(self.months, Unset):
            months = UNSET
        elif isinstance(self.months, list):
            months = []
            for months_type_0_item_data in self.months:
                months_type_0_item = months_type_0_item_data.value
                months.append(months_type_0_item)

        else:
            months = self.months

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if health_check_enabled is not UNSET:
            field_dict["healthCheckEnabled"] = health_check_enabled
        if local_time is not UNSET:
            field_dict["localTime"] = local_time
        if day_number_in_month is not UNSET:
            field_dict["dayNumberInMonth"] = day_number_in_month
        if days_of_week is not UNSET:
            field_dict["daysOfWeek"] = days_of_week
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if months is not UNSET:
            field_dict["months"] = months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        health_check_enabled = d.pop("healthCheckEnabled", UNSET)

        _local_time = d.pop("localTime", UNSET)
        local_time: datetime.datetime | Unset
        if isinstance(_local_time, Unset):
            local_time = UNSET
        else:
            local_time = isoparse(_local_time)

        _day_number_in_month = d.pop("dayNumberInMonth", UNSET)
        day_number_in_month: DayNumberInMonthHealthCheck | Unset
        if isinstance(_day_number_in_month, Unset):
            day_number_in_month = UNSET
        else:
            day_number_in_month = DayNumberInMonthHealthCheck(_day_number_in_month)

        def _parse_days_of_week(data: object) -> list[DayOfWeek] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_of_week_type_0 = []
                _days_of_week_type_0 = data
                for days_of_week_type_0_item_data in _days_of_week_type_0:
                    days_of_week_type_0_item = DayOfWeek(days_of_week_type_0_item_data)

                    days_of_week_type_0.append(days_of_week_type_0_item)

                return days_of_week_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DayOfWeek] | None | Unset, data)

        days_of_week = _parse_days_of_week(d.pop("daysOfWeek", UNSET))

        def _parse_day_of_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day_of_month = _parse_day_of_month(d.pop("dayOfMonth", UNSET))

        def _parse_months(data: object) -> list[Month] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                months_type_0 = []
                _months_type_0 = data
                for months_type_0_item_data in _months_type_0:
                    months_type_0_item = Month(months_type_0_item_data)

                    months_type_0.append(months_type_0_item)

                return months_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Month] | None | Unset, data)

        months = _parse_months(d.pop("months", UNSET))

        health_check_schedule = cls(
            health_check_enabled=health_check_enabled,
            local_time=local_time,
            day_number_in_month=day_number_in_month,
            days_of_week=days_of_week,
            day_of_month=day_of_month,
            months=months,
        )

        return health_check_schedule
