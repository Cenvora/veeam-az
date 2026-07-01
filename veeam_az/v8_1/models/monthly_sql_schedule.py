from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.day_of_week_nullable import DayOfWeekNullable
from ..models.monthly_type_nullable import MonthlyTypeNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monthly_backup_schedule import MonthlyBackupSchedule


T = TypeVar("T", bound="MonthlySqlSchedule")


@_attrs_define
class MonthlySqlSchedule:
    r"""Specifies monthly schedule settings for the backup policy.

    Attributes:
        start_time (int | None | Unset): Specifies the time when the backup policy will run.
        type_ (MonthlyTypeNullable | Unset): Specifies the day of the month when the backup policy will run.
        day_of_week (DayOfWeekNullable | Unset): \[Applies if one of the *First*, *Second*, *Third*, *Fourth* or *Last*
            values is specified for the `type` parameter] Specifies the days of the week when the backup policy will run.
        day_of_month (int | None | Unset): Specifies ordinal number of the day of the month when the backup policy will
            run.
        monthly_last_day (bool | None | Unset): Defines whether the backup policy will always run on the last day of the
            month.
        backup_schedule (MonthlyBackupSchedule | Unset): Specifies the monthly schedule settings for image-level
            backups.
    """

    start_time: int | None | Unset = UNSET
    type_: MonthlyTypeNullable | Unset = UNSET
    day_of_week: DayOfWeekNullable | Unset = UNSET
    day_of_month: int | None | Unset = UNSET
    monthly_last_day: bool | None | Unset = UNSET
    backup_schedule: MonthlyBackupSchedule | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_time: int | None | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        day_of_week: str | Unset = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        day_of_month: int | None | Unset
        if isinstance(self.day_of_month, Unset):
            day_of_month = UNSET
        else:
            day_of_month = self.day_of_month

        monthly_last_day: bool | None | Unset
        if isinstance(self.monthly_last_day, Unset):
            monthly_last_day = UNSET
        else:
            monthly_last_day = self.monthly_last_day

        backup_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_schedule, Unset):
            backup_schedule = self.backup_schedule.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if type_ is not UNSET:
            field_dict["type"] = type_
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if monthly_last_day is not UNSET:
            field_dict["monthlyLastDay"] = monthly_last_day
        if backup_schedule is not UNSET:
            field_dict["backupSchedule"] = backup_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monthly_backup_schedule import MonthlyBackupSchedule

        d = dict(src_dict)

        def _parse_start_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: MonthlyTypeNullable | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MonthlyTypeNullable(_type_)

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: DayOfWeekNullable | Unset
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = DayOfWeekNullable(_day_of_week)

        def _parse_day_of_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day_of_month = _parse_day_of_month(d.pop("dayOfMonth", UNSET))

        def _parse_monthly_last_day(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        monthly_last_day = _parse_monthly_last_day(d.pop("monthlyLastDay", UNSET))

        _backup_schedule = d.pop("backupSchedule", UNSET)
        backup_schedule: MonthlyBackupSchedule | Unset
        if isinstance(_backup_schedule, Unset):
            backup_schedule = UNSET
        else:
            backup_schedule = MonthlyBackupSchedule.from_dict(_backup_schedule)

        monthly_sql_schedule = cls(
            start_time=start_time,
            type_=type_,
            day_of_week=day_of_week,
            day_of_month=day_of_month,
            monthly_last_day=monthly_last_day,
            backup_schedule=backup_schedule,
        )

        return monthly_sql_schedule
