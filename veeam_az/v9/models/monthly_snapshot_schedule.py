from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.month import Month
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonthlySnapshotSchedule")


@_attrs_define
class MonthlySnapshotSchedule:
    """Specifies the monthly schedule settings for cloud-native snapshots.

    Attributes:
        selected_months (list[Month] | None | Unset): Specifies the months when the backup policy must start creating
            cloud-native snapshots.
        snapshots_to_keep (int | None | Unset): Specifies the number of restore points to keep in a backup chain.
    """

    selected_months: list[Month] | None | Unset = UNSET
    snapshots_to_keep: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        snapshots_to_keep: int | None | Unset
        if isinstance(self.snapshots_to_keep, Unset):
            snapshots_to_keep = UNSET
        else:
            snapshots_to_keep = self.snapshots_to_keep

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if selected_months is not UNSET:
            field_dict["selectedMonths"] = selected_months
        if snapshots_to_keep is not UNSET:
            field_dict["snapshotsToKeep"] = snapshots_to_keep

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_snapshots_to_keep(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        snapshots_to_keep = _parse_snapshots_to_keep(d.pop("snapshotsToKeep", UNSET))

        monthly_snapshot_schedule = cls(
            selected_months=selected_months,
            snapshots_to_keep=snapshots_to_keep,
        )

        return monthly_snapshot_schedule
