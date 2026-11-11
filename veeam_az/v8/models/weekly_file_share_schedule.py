from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.weekly_snapshot_schedule import WeeklySnapshotSchedule


T = TypeVar("T", bound="WeeklyFileShareSchedule")


@_attrs_define
class WeeklyFileShareSchedule:
    """Specifies weekly schedule settings for the backup policy.

    Attributes:
        start_time (int | None | Unset): Specifies the time when the backup policy will run.
        snapshot_schedule (WeeklySnapshotSchedule | Unset): Specifies the weekly schedule settings for cloud-native
            snapshots.
    """

    start_time: int | None | Unset = UNSET
    snapshot_schedule: WeeklySnapshotSchedule | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_time: int | None | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        snapshot_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot_schedule, Unset):
            snapshot_schedule = self.snapshot_schedule.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if snapshot_schedule is not UNSET:
            field_dict["snapshotSchedule"] = snapshot_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.weekly_snapshot_schedule import WeeklySnapshotSchedule

        d = dict(src_dict)

        def _parse_start_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        _snapshot_schedule = d.pop("snapshotSchedule", UNSET)
        snapshot_schedule: WeeklySnapshotSchedule | Unset
        if isinstance(_snapshot_schedule, Unset):
            snapshot_schedule = UNSET
        else:
            snapshot_schedule = WeeklySnapshotSchedule.from_dict(_snapshot_schedule)

        weekly_file_share_schedule = cls(
            start_time=start_time,
            snapshot_schedule=snapshot_schedule,
        )

        return weekly_file_share_schedule
