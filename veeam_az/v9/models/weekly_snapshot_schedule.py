from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.day_of_week import DayOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="WeeklySnapshotSchedule")


@_attrs_define
class WeeklySnapshotSchedule:
    r"""Specifies the weekly schedule settings for cloud-native snapshots.

    Attributes:
        selected_days (list[DayOfWeek] | Unset): \[Applies if the *SelectedDays* value is specified for the `DailyType`
            parameter] Specifies the days of the week when the backup policy will run.
        snapshots_to_keep (int | None | Unset): Specifies the number of restore points to keep in cloud-native snapshot
            chains.
    """

    selected_days: list[DayOfWeek] | Unset = UNSET
    snapshots_to_keep: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        selected_days: list[str] | Unset = UNSET
        if not isinstance(self.selected_days, Unset):
            selected_days = []
            for selected_days_item_data in self.selected_days:
                selected_days_item = selected_days_item_data.value
                selected_days.append(selected_days_item)

        snapshots_to_keep: int | None | Unset
        if isinstance(self.snapshots_to_keep, Unset):
            snapshots_to_keep = UNSET
        else:
            snapshots_to_keep = self.snapshots_to_keep

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if selected_days is not UNSET:
            field_dict["selectedDays"] = selected_days
        if snapshots_to_keep is not UNSET:
            field_dict["snapshotsToKeep"] = snapshots_to_keep

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _selected_days = d.pop("selectedDays", UNSET)
        selected_days: list[DayOfWeek] | Unset = UNSET
        if _selected_days is not UNSET:
            selected_days = []
            for selected_days_item_data in _selected_days:
                selected_days_item = DayOfWeek(selected_days_item_data)

                selected_days.append(selected_days_item)

        def _parse_snapshots_to_keep(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        snapshots_to_keep = _parse_snapshots_to_keep(d.pop("snapshotsToKeep", UNSET))

        weekly_snapshot_schedule = cls(
            selected_days=selected_days,
            snapshots_to_keep=snapshots_to_keep,
        )

        return weekly_snapshot_schedule
