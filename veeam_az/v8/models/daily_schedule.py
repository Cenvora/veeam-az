from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.daily_type_nullable import DailyTypeNullable
from ..models.day_of_week import DayOfWeek
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_backup_schedule import DailyBackupSchedule
    from ..models.daily_snapshot_schedule import DailySnapshotSchedule


T = TypeVar("T", bound="DailySchedule")


@_attrs_define
class DailySchedule:
    r"""Specifies the daily schedule settings for the backup policy.

    Attributes:
        daily_type (DailyTypeNullable | Unset): Specifies the days when the backup policy will run.
        selected_days (list[DayOfWeek] | None | Unset): \[Applies if the *SelectedDays* value is specified for the
            `DailyType` parameter] Specifies the days of the week when the backup policy will run.
        runs_per_hour (int | None | Unset): \[Applies to cloud-native snapshots only] Specifies the number of times for
            the backup policy to run within an hour. The minimum value is 1.
        snapshot_schedule (DailySnapshotSchedule | Unset): Specifies the daily schedule settings for cloud-native
            snapshots.
        backup_schedule (DailyBackupSchedule | Unset): Specifies the daily schedule settings for the backup policy.
    """

    daily_type: DailyTypeNullable | Unset = UNSET
    selected_days: list[DayOfWeek] | None | Unset = UNSET
    runs_per_hour: int | None | Unset = UNSET
    snapshot_schedule: DailySnapshotSchedule | Unset = UNSET
    backup_schedule: DailyBackupSchedule | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        runs_per_hour: int | None | Unset
        if isinstance(self.runs_per_hour, Unset):
            runs_per_hour = UNSET
        else:
            runs_per_hour = self.runs_per_hour

        snapshot_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot_schedule, Unset):
            snapshot_schedule = self.snapshot_schedule.to_dict()

        backup_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_schedule, Unset):
            backup_schedule = self.backup_schedule.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if daily_type is not UNSET:
            field_dict["dailyType"] = daily_type
        if selected_days is not UNSET:
            field_dict["selectedDays"] = selected_days
        if runs_per_hour is not UNSET:
            field_dict["runsPerHour"] = runs_per_hour
        if snapshot_schedule is not UNSET:
            field_dict["snapshotSchedule"] = snapshot_schedule
        if backup_schedule is not UNSET:
            field_dict["backupSchedule"] = backup_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_backup_schedule import DailyBackupSchedule
        from ..models.daily_snapshot_schedule import DailySnapshotSchedule

        d = dict(src_dict)
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

        def _parse_runs_per_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        runs_per_hour = _parse_runs_per_hour(d.pop("runsPerHour", UNSET))

        _snapshot_schedule = d.pop("snapshotSchedule", UNSET)
        snapshot_schedule: DailySnapshotSchedule | Unset
        if isinstance(_snapshot_schedule, Unset):
            snapshot_schedule = UNSET
        else:
            snapshot_schedule = DailySnapshotSchedule.from_dict(_snapshot_schedule)

        _backup_schedule = d.pop("backupSchedule", UNSET)
        backup_schedule: DailyBackupSchedule | Unset
        if isinstance(_backup_schedule, Unset):
            backup_schedule = UNSET
        else:
            backup_schedule = DailyBackupSchedule.from_dict(_backup_schedule)

        daily_schedule = cls(
            daily_type=daily_type,
            selected_days=selected_days,
            runs_per_hour=runs_per_hour,
            snapshot_schedule=snapshot_schedule,
            backup_schedule=backup_schedule,
        )

        return daily_schedule
