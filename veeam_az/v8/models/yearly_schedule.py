from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.day_of_week_nullable import DayOfWeekNullable
from ..models.month_nullable import MonthNullable
from ..models.yearly_type_nullable import YearlyTypeNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="YearlySchedule")


@_attrs_define
class YearlySchedule:
    r"""Specifies the yearly schedule settings for the backup policy.

    Attributes:
        start_time (int | None | Unset): Specifies the time when the backup policy will run.
        month (MonthNullable | Unset): \[Applies if the *SelectedDay* value is specified for the `type` parameter]
            Specifies the ordinal number of the day of the month when the backup policy will run.
        type_ (YearlyTypeNullable | Unset): Specifies the day of the month when the backup policy will run.
        day_of_week (DayOfWeekNullable | Unset): \[Applies if one of the *First*, *Second*, *Third*, *Fourth* or *Last*
            values is specified for the `type` parameter] Specifies the days of the week when the backup policy will run.
        day_of_month (int | None | Unset): \[Applies if the *SelectedDay* value is specified for the `type` parameter]
            Specifies the ordinal number of the day of the month when the backup policy will run.
        yearly_last_day (bool | None | Unset): Defines whether the backup policy must run always on last day of the
            year.
        retention_years_count (int | None | Unset): Specifies the number of years to keep restore points in a backup
            chain.
        target_repository_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft
            Azure REST API to the target backup repository.
    """

    start_time: int | None | Unset = UNSET
    month: MonthNullable | Unset = UNSET
    type_: YearlyTypeNullable | Unset = UNSET
    day_of_week: DayOfWeekNullable | Unset = UNSET
    day_of_month: int | None | Unset = UNSET
    yearly_last_day: bool | None | Unset = UNSET
    retention_years_count: int | None | Unset = UNSET
    target_repository_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_time: int | None | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        month: str | Unset = UNSET
        if not isinstance(self.month, Unset):
            month = self.month.value

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

        yearly_last_day: bool | None | Unset
        if isinstance(self.yearly_last_day, Unset):
            yearly_last_day = UNSET
        else:
            yearly_last_day = self.yearly_last_day

        retention_years_count: int | None | Unset
        if isinstance(self.retention_years_count, Unset):
            retention_years_count = UNSET
        else:
            retention_years_count = self.retention_years_count

        target_repository_id: None | str | Unset
        if isinstance(self.target_repository_id, Unset):
            target_repository_id = UNSET
        else:
            target_repository_id = self.target_repository_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if month is not UNSET:
            field_dict["month"] = month
        if type_ is not UNSET:
            field_dict["type"] = type_
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if yearly_last_day is not UNSET:
            field_dict["yearlyLastDay"] = yearly_last_day
        if retention_years_count is not UNSET:
            field_dict["retentionYearsCount"] = retention_years_count
        if target_repository_id is not UNSET:
            field_dict["targetRepositoryId"] = target_repository_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_start_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        _month = d.pop("month", UNSET)
        month: MonthNullable | Unset
        if isinstance(_month, Unset):
            month = UNSET
        else:
            month = MonthNullable(_month)

        _type_ = d.pop("type", UNSET)
        type_: YearlyTypeNullable | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = YearlyTypeNullable(_type_)

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

        def _parse_yearly_last_day(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        yearly_last_day = _parse_yearly_last_day(d.pop("yearlyLastDay", UNSET))

        def _parse_retention_years_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_years_count = _parse_retention_years_count(d.pop("retentionYearsCount", UNSET))

        def _parse_target_repository_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_repository_id = _parse_target_repository_id(d.pop("targetRepositoryId", UNSET))

        yearly_schedule = cls(
            start_time=start_time,
            month=month,
            type_=type_,
            day_of_week=day_of_week,
            day_of_month=day_of_month,
            yearly_last_day=yearly_last_day,
            retention_years_count=retention_years_count,
            target_repository_id=target_repository_id,
        )

        return yearly_schedule
