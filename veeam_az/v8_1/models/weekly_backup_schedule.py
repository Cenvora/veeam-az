from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.day_of_week import DayOfWeek
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_retention_settings import RepositoryRetentionSettings


T = TypeVar("T", bound="WeeklyBackupSchedule")


@_attrs_define
class WeeklyBackupSchedule:
    r"""Specifies the weekly schedule settings for backups.

    Attributes:
        selected_days (list[DayOfWeek] | Unset): \[Applies if the *SelectedDays* value is specified for the `DailyType`
            parameter] Specifies the days of the week when the backup policy will run.
        retention (RepositoryRetentionSettings | Unset): Specifies period of time to keep restore points in a backup
            chain.
        target_repository_id (None | str | Unset): Specifies the system ID assigned to the target backup repository in
            the Veeam Backup for Microsoft Azure REST API.
    """

    selected_days: list[DayOfWeek] | Unset = UNSET
    retention: RepositoryRetentionSettings | Unset = UNSET
    target_repository_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        selected_days: list[str] | Unset = UNSET
        if not isinstance(self.selected_days, Unset):
            selected_days = []
            for selected_days_item_data in self.selected_days:
                selected_days_item = selected_days_item_data.value
                selected_days.append(selected_days_item)

        retention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention, Unset):
            retention = self.retention.to_dict()

        target_repository_id: None | str | Unset
        if isinstance(self.target_repository_id, Unset):
            target_repository_id = UNSET
        else:
            target_repository_id = self.target_repository_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if selected_days is not UNSET:
            field_dict["selectedDays"] = selected_days
        if retention is not UNSET:
            field_dict["retention"] = retention
        if target_repository_id is not UNSET:
            field_dict["targetRepositoryId"] = target_repository_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_retention_settings import RepositoryRetentionSettings

        d = dict(src_dict)
        _selected_days = d.pop("selectedDays", UNSET)
        selected_days: list[DayOfWeek] | Unset = UNSET
        if _selected_days is not UNSET:
            selected_days = []
            for selected_days_item_data in _selected_days:
                selected_days_item = DayOfWeek(selected_days_item_data)

                selected_days.append(selected_days_item)

        _retention = d.pop("retention", UNSET)
        retention: RepositoryRetentionSettings | Unset
        if isinstance(_retention, Unset):
            retention = UNSET
        else:
            retention = RepositoryRetentionSettings.from_dict(_retention)

        def _parse_target_repository_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_repository_id = _parse_target_repository_id(d.pop("targetRepositoryId", UNSET))

        weekly_backup_schedule = cls(
            selected_days=selected_days,
            retention=retention,
            target_repository_id=target_repository_id,
        )

        return weekly_backup_schedule
