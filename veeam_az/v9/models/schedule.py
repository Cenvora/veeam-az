from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.daily_type_nullable import DailyTypeNullable
from ..models.day_of_week import DayOfWeek
from ..models.day_of_week_nullable import DayOfWeekNullable
from ..models.frequency_type import FrequencyType
from ..models.month import Month
from ..models.monthly_type_nullable import MonthlyTypeNullable
from ..models.periodically_type import PeriodicallyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_window_settings import BackupWindowSettings
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="Schedule")


@_attrs_define
class Schedule:
    r"""Specifies the schedule for the backup policy.

    Attributes:
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
        frequency_type (FrequencyType | Unset): Specifies the frequency type.
        daily_time (None | str | Unset): Specifies the time when the backup policy will run.
        daily_type (DailyTypeNullable | Unset): Specifies the days when the backup policy will run.
        selected_days (list[DayOfWeek] | None | Unset): \[Applies if the *SelectedDays* value is specified for the
            `DailyType` parameter] Specifies the days of the week when the backup policy will run.
        monthly_time (None | str | Unset): Date when the backup policy will run.
        monthly_type (MonthlyTypeNullable | Unset): Specifies the day of the month when the backup policy will run.
        monthly_day_of_week (DayOfWeekNullable | Unset): \[Applies if one of the *First*, *Second*, *Third*, *Fourth* or
            *Last* values is specified for the `type` parameter] Specifies the days of the week when the backup policy will
            run.
        monthly_day (int | None | Unset): Specifies the ordinal number of the day of the month when the backup policy
            will run.
        monthly_last_day (bool | None | Unset): Defines whether the backup policy will run on the last day of every
            month.
        selected_months (list[Month] | None | Unset): Months when the backup policy will run.
        periodically_type (PeriodicallyType | Unset): Type of the intervals at which the backup policy will run.
        interval (int | None | Unset): Ordinal number of minutes or hours when the backup policy will run.
        periodical_schedule_window (BackupWindowSettings | Unset): Specifies the periodical schedule for the backup
            policy.
    """

    field_links: LinksDictionaryType0 | None | Unset = UNSET
    frequency_type: FrequencyType | Unset = UNSET
    daily_time: None | str | Unset = UNSET
    daily_type: DailyTypeNullable | Unset = UNSET
    selected_days: list[DayOfWeek] | None | Unset = UNSET
    monthly_time: None | str | Unset = UNSET
    monthly_type: MonthlyTypeNullable | Unset = UNSET
    monthly_day_of_week: DayOfWeekNullable | Unset = UNSET
    monthly_day: int | None | Unset = UNSET
    monthly_last_day: bool | None | Unset = UNSET
    selected_months: list[Month] | None | Unset = UNSET
    periodically_type: PeriodicallyType | Unset = UNSET
    interval: int | None | Unset = UNSET
    periodical_schedule_window: BackupWindowSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        frequency_type: str | Unset = UNSET
        if not isinstance(self.frequency_type, Unset):
            frequency_type = self.frequency_type.value

        daily_time: None | str | Unset
        if isinstance(self.daily_time, Unset):
            daily_time = UNSET
        else:
            daily_time = self.daily_time

        daily_type: str | Unset = UNSET
        if not isinstance(self.daily_type, Unset):
            daily_type = self.daily_type.value

        selected_days: list[str] | None | Unset
        if isinstance(self.selected_days, Unset):
            selected_days = UNSET
        elif isinstance(self.selected_days, list):
            selected_days = []
            for selected_days_type_0_item_data in self.selected_days:
                selected_days_type_0_item = selected_days_type_0_item_data.value
                selected_days.append(selected_days_type_0_item)

        else:
            selected_days = self.selected_days

        monthly_time: None | str | Unset
        if isinstance(self.monthly_time, Unset):
            monthly_time = UNSET
        else:
            monthly_time = self.monthly_time

        monthly_type: str | Unset = UNSET
        if not isinstance(self.monthly_type, Unset):
            monthly_type = self.monthly_type.value

        monthly_day_of_week: str | Unset = UNSET
        if not isinstance(self.monthly_day_of_week, Unset):
            monthly_day_of_week = self.monthly_day_of_week.value

        monthly_day: int | None | Unset
        if isinstance(self.monthly_day, Unset):
            monthly_day = UNSET
        else:
            monthly_day = self.monthly_day

        monthly_last_day: bool | None | Unset
        if isinstance(self.monthly_last_day, Unset):
            monthly_last_day = UNSET
        else:
            monthly_last_day = self.monthly_last_day

        selected_months: list[str] | None | Unset
        if isinstance(self.selected_months, Unset):
            selected_months = UNSET
        elif isinstance(self.selected_months, list):
            selected_months = []
            for selected_months_type_0_item_data in self.selected_months:
                selected_months_type_0_item = selected_months_type_0_item_data.value
                selected_months.append(selected_months_type_0_item)

        else:
            selected_months = self.selected_months

        periodically_type: str | Unset = UNSET
        if not isinstance(self.periodically_type, Unset):
            periodically_type = self.periodically_type.value

        interval: int | None | Unset
        if isinstance(self.interval, Unset):
            interval = UNSET
        else:
            interval = self.interval

        periodical_schedule_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.periodical_schedule_window, Unset):
            periodical_schedule_window = self.periodical_schedule_window.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if frequency_type is not UNSET:
            field_dict["frequencyType"] = frequency_type
        if daily_time is not UNSET:
            field_dict["dailyTime"] = daily_time
        if daily_type is not UNSET:
            field_dict["dailyType"] = daily_type
        if selected_days is not UNSET:
            field_dict["selectedDays"] = selected_days
        if monthly_time is not UNSET:
            field_dict["monthlyTime"] = monthly_time
        if monthly_type is not UNSET:
            field_dict["monthlyType"] = monthly_type
        if monthly_day_of_week is not UNSET:
            field_dict["monthlyDayOfWeek"] = monthly_day_of_week
        if monthly_day is not UNSET:
            field_dict["monthlyDay"] = monthly_day
        if monthly_last_day is not UNSET:
            field_dict["monthlyLastDay"] = monthly_last_day
        if selected_months is not UNSET:
            field_dict["selectedMonths"] = selected_months
        if periodically_type is not UNSET:
            field_dict["periodicallyType"] = periodically_type
        if interval is not UNSET:
            field_dict["interval"] = interval
        if periodical_schedule_window is not UNSET:
            field_dict["periodicalScheduleWindow"] = periodical_schedule_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_window_settings import BackupWindowSettings
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)

        def _parse_field_links(data: object) -> LinksDictionaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_links_dictionary_type_0 = LinksDictionaryType0.from_dict(data)

                return componentsschemas_links_dictionary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinksDictionaryType0 | None | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        _frequency_type = d.pop("frequencyType", UNSET)
        frequency_type: FrequencyType | Unset
        if isinstance(_frequency_type, Unset):
            frequency_type = UNSET
        else:
            frequency_type = FrequencyType(_frequency_type)

        def _parse_daily_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        daily_time = _parse_daily_time(d.pop("dailyTime", UNSET))

        _daily_type = d.pop("dailyType", UNSET)
        daily_type: DailyTypeNullable | Unset
        if isinstance(_daily_type, Unset):
            daily_type = UNSET
        else:
            daily_type = DailyTypeNullable(_daily_type)

        def _parse_selected_days(data: object) -> list[DayOfWeek] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_days_type_0 = []
                _selected_days_type_0 = data
                for selected_days_type_0_item_data in _selected_days_type_0:
                    selected_days_type_0_item = DayOfWeek(selected_days_type_0_item_data)

                    selected_days_type_0.append(selected_days_type_0_item)

                return selected_days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DayOfWeek] | None | Unset, data)

        selected_days = _parse_selected_days(d.pop("selectedDays", UNSET))

        def _parse_monthly_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        monthly_time = _parse_monthly_time(d.pop("monthlyTime", UNSET))

        _monthly_type = d.pop("monthlyType", UNSET)
        monthly_type: MonthlyTypeNullable | Unset
        if isinstance(_monthly_type, Unset):
            monthly_type = UNSET
        else:
            monthly_type = MonthlyTypeNullable(_monthly_type)

        _monthly_day_of_week = d.pop("monthlyDayOfWeek", UNSET)
        monthly_day_of_week: DayOfWeekNullable | Unset
        if isinstance(_monthly_day_of_week, Unset):
            monthly_day_of_week = UNSET
        else:
            monthly_day_of_week = DayOfWeekNullable(_monthly_day_of_week)

        def _parse_monthly_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        monthly_day = _parse_monthly_day(d.pop("monthlyDay", UNSET))

        def _parse_monthly_last_day(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        monthly_last_day = _parse_monthly_last_day(d.pop("monthlyLastDay", UNSET))

        def _parse_selected_months(data: object) -> list[Month] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_months_type_0 = []
                _selected_months_type_0 = data
                for selected_months_type_0_item_data in _selected_months_type_0:
                    selected_months_type_0_item = Month(selected_months_type_0_item_data)

                    selected_months_type_0.append(selected_months_type_0_item)

                return selected_months_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Month] | None | Unset, data)

        selected_months = _parse_selected_months(d.pop("selectedMonths", UNSET))

        _periodically_type = d.pop("periodicallyType", UNSET)
        periodically_type: PeriodicallyType | Unset
        if isinstance(_periodically_type, Unset):
            periodically_type = UNSET
        else:
            periodically_type = PeriodicallyType(_periodically_type)

        def _parse_interval(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        interval = _parse_interval(d.pop("interval", UNSET))

        _periodical_schedule_window = d.pop("periodicalScheduleWindow", UNSET)
        periodical_schedule_window: BackupWindowSettings | Unset
        if isinstance(_periodical_schedule_window, Unset):
            periodical_schedule_window = UNSET
        else:
            periodical_schedule_window = BackupWindowSettings.from_dict(_periodical_schedule_window)

        schedule = cls(
            field_links=field_links,
            frequency_type=frequency_type,
            daily_time=daily_time,
            daily_type=daily_type,
            selected_days=selected_days,
            monthly_time=monthly_time,
            monthly_type=monthly_type,
            monthly_day_of_week=monthly_day_of_week,
            monthly_day=monthly_day,
            monthly_last_day=monthly_last_day,
            selected_months=selected_months,
            periodically_type=periodically_type,
            interval=interval,
            periodical_schedule_window=periodical_schedule_window,
        )

        return schedule
