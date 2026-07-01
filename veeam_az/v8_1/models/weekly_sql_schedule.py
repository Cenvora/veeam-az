from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.weekly_backup_schedule import WeeklyBackupSchedule


T = TypeVar("T", bound="WeeklySqlSchedule")


@_attrs_define
class WeeklySqlSchedule:
    """Specifies weekly schedule settings for the backup policy.

    Attributes:
        start_time (int | None | Unset): Specifies the time when the backup policy will run.
        backup_schedule (WeeklyBackupSchedule | Unset): Specifies the weekly schedule settings for backups.
    """

    start_time: int | None | Unset = UNSET
    backup_schedule: WeeklyBackupSchedule | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_time: int | None | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        backup_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_schedule, Unset):
            backup_schedule = self.backup_schedule.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if backup_schedule is not UNSET:
            field_dict["backupSchedule"] = backup_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.weekly_backup_schedule import WeeklyBackupSchedule

        d = dict(src_dict)

        def _parse_start_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        _backup_schedule = d.pop("backupSchedule", UNSET)
        backup_schedule: WeeklyBackupSchedule | Unset
        if isinstance(_backup_schedule, Unset):
            backup_schedule = UNSET
        else:
            backup_schedule = WeeklyBackupSchedule.from_dict(_backup_schedule)

        weekly_sql_schedule = cls(
            start_time=start_time,
            backup_schedule=backup_schedule,
        )

        return weekly_sql_schedule
