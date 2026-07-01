from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DailySnapshotSchedule")


@_attrs_define
class DailySnapshotSchedule:
    """Specifies the daily schedule settings for cloud-native snapshots.

    Attributes:
        hours (list[int] | None | Unset): Specifies hours when the backup policy must start creating cloud-native
            snapshots.
        snapshots_to_keep (int | None | Unset): Specifies the number of restore points to keep in a backup chain.
    """

    hours: list[int] | None | Unset = UNSET
    snapshots_to_keep: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        hours: list[int] | None | Unset
        if isinstance(self.hours, Unset):
            hours = UNSET
        elif isinstance(self.hours, list):
            hours = self.hours

        else:
            hours = self.hours

        snapshots_to_keep: int | None | Unset
        if isinstance(self.snapshots_to_keep, Unset):
            snapshots_to_keep = UNSET
        else:
            snapshots_to_keep = self.snapshots_to_keep

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if hours is not UNSET:
            field_dict["hours"] = hours
        if snapshots_to_keep is not UNSET:
            field_dict["snapshotsToKeep"] = snapshots_to_keep

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_hours(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hours_type_0 = cast(list[int], data)

                return hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        hours = _parse_hours(d.pop("hours", UNSET))

        def _parse_snapshots_to_keep(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        snapshots_to_keep = _parse_snapshots_to_keep(d.pop("snapshotsToKeep", UNSET))

        daily_snapshot_schedule = cls(
            hours=hours,
            snapshots_to_keep=snapshots_to_keep,
        )

        return daily_snapshot_schedule
