from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.daily_type_nullable import DailyTypeNullable
from ..models.day_of_week import DayOfWeek
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_backup_schedule import DailyBackupSchedule


T = TypeVar("T", bound="DailyCosmosDbSchedule")


@_attrs_define
class DailyCosmosDbSchedule:
    r"""/[Applies only to backup policies that have the *Backup to repository* option enabled] Specifies daily schedule
    settings for the backup policy.

        Attributes:
            daily_type (DailyTypeNullable | Unset): Specifies the days when the backup policy will run.
            selected_days (list[DayOfWeek] | None | Unset): \[Applies if the *SelectedDays* value is specified for the
                `DailyType` parameter] Specifies days of the week when the backup policy will run.
            backup_schedule (DailyBackupSchedule | Unset): Specifies the daily schedule settings for the backup policy.
    """

    daily_type: DailyTypeNullable | Unset = UNSET
    selected_days: list[DayOfWeek] | None | Unset = UNSET
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

        backup_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_schedule, Unset):
            backup_schedule = self.backup_schedule.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if daily_type is not UNSET:
            field_dict["dailyType"] = daily_type
        if selected_days is not UNSET:
            field_dict["selectedDays"] = selected_days
        if backup_schedule is not UNSET:
            field_dict["backupSchedule"] = backup_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_backup_schedule import DailyBackupSchedule

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

        _backup_schedule = d.pop("backupSchedule", UNSET)
        backup_schedule: DailyBackupSchedule | Unset
        if isinstance(_backup_schedule, Unset):
            backup_schedule = UNSET
        else:
            backup_schedule = DailyBackupSchedule.from_dict(_backup_schedule)

        daily_cosmos_db_schedule = cls(
            daily_type=daily_type,
            selected_days=selected_days,
            backup_schedule=backup_schedule,
        )

        return daily_cosmos_db_schedule
