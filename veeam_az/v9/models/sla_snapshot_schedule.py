from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_sla_schedule import DailySlaSchedule
    from ..models.monthly_sla_schedule import MonthlySlaSchedule
    from ..models.time_window_sla_schedule import TimeWindowSlaSchedule
    from ..models.weekly_sla_schedule import WeeklySlaSchedule


T = TypeVar("T", bound="SlaSnapshotSchedule")


@_attrs_define
class SlaSnapshotSchedule:
    """Specifies scheduling and retention settings for snapshots.

    Attributes:
        daily (DailySlaSchedule | Unset): Specifies the daily schedule settings.
        weekly (WeeklySlaSchedule | Unset): Specifies the weekly schedule settings.
        monthly (MonthlySlaSchedule | Unset): Specifies the monthly schedule settings.
        execution_window (TimeWindowSlaSchedule | Unset): Specifies a snapshot or a backup window during which the
            restore points will be created.
    """

    daily: DailySlaSchedule | Unset = UNSET
    weekly: WeeklySlaSchedule | Unset = UNSET
    monthly: MonthlySlaSchedule | Unset = UNSET
    execution_window: TimeWindowSlaSchedule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily, Unset):
            daily = self.daily.to_dict()

        weekly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weekly, Unset):
            weekly = self.weekly.to_dict()

        monthly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        execution_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_window, Unset):
            execution_window = self.execution_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily is not UNSET:
            field_dict["daily"] = daily
        if weekly is not UNSET:
            field_dict["weekly"] = weekly
        if monthly is not UNSET:
            field_dict["monthly"] = monthly
        if execution_window is not UNSET:
            field_dict["executionWindow"] = execution_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_sla_schedule import DailySlaSchedule
        from ..models.monthly_sla_schedule import MonthlySlaSchedule
        from ..models.time_window_sla_schedule import TimeWindowSlaSchedule
        from ..models.weekly_sla_schedule import WeeklySlaSchedule

        d = dict(src_dict)
        _daily = d.pop("daily", UNSET)
        daily: DailySlaSchedule | Unset
        if isinstance(_daily, Unset):
            daily = UNSET
        else:
            daily = DailySlaSchedule.from_dict(_daily)

        _weekly = d.pop("weekly", UNSET)
        weekly: WeeklySlaSchedule | Unset
        if isinstance(_weekly, Unset):
            weekly = UNSET
        else:
            weekly = WeeklySlaSchedule.from_dict(_weekly)

        _monthly = d.pop("monthly", UNSET)
        monthly: MonthlySlaSchedule | Unset
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = MonthlySlaSchedule.from_dict(_monthly)

        _execution_window = d.pop("executionWindow", UNSET)
        execution_window: TimeWindowSlaSchedule | Unset
        if isinstance(_execution_window, Unset):
            execution_window = UNSET
        else:
            execution_window = TimeWindowSlaSchedule.from_dict(_execution_window)

        sla_snapshot_schedule = cls(
            daily=daily,
            weekly=weekly,
            monthly=monthly,
            execution_window=execution_window,
        )

        sla_snapshot_schedule.additional_properties = d
        return sla_snapshot_schedule

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
