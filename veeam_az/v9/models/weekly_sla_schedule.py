from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.daily_type import DailyType
from ..models.day_of_week import DayOfWeek
from ..models.sla_duration_type import SlaDurationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WeeklySlaSchedule")


@_attrs_define
class WeeklySlaSchedule:
    r"""Specifies the weekly schedule settings.

    Attributes:
        schedule_enabled (bool | Unset): Defines whether the weekly schedule is enabled in the template.
        daily_type (DailyType | Unset): Specifies the frequency type.
        selected_days (list[DayOfWeek] | None | Unset): \[Applies if the *SelectedDays* value is specified for the
            `DailyType` parameter] Specifies the days of the week on which the restore points will be created.
        store_for (int | Unset): Specifies the time period (in number of time units) during which Veeam Backup for
            Microsoft Azure will keep the created restore points. **Note**&#58; For the `createUnit` parameter, you can only
            specify either *Day* or *Month*.
        store_for_unit (SlaDurationType | Unset): Specifies a time unit.
    """

    schedule_enabled: bool | Unset = UNSET
    daily_type: DailyType | Unset = UNSET
    selected_days: list[DayOfWeek] | None | Unset = UNSET
    store_for: int | Unset = UNSET
    store_for_unit: SlaDurationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_enabled = self.schedule_enabled

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

        store_for = self.store_for

        store_for_unit: str | Unset = UNSET
        if not isinstance(self.store_for_unit, Unset):
            store_for_unit = self.store_for_unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_enabled is not UNSET:
            field_dict["scheduleEnabled"] = schedule_enabled
        if daily_type is not UNSET:
            field_dict["dailyType"] = daily_type
        if selected_days is not UNSET:
            field_dict["selectedDays"] = selected_days
        if store_for is not UNSET:
            field_dict["storeFor"] = store_for
        if store_for_unit is not UNSET:
            field_dict["storeForUnit"] = store_for_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schedule_enabled = d.pop("scheduleEnabled", UNSET)

        _daily_type = d.pop("dailyType", UNSET)
        daily_type: DailyType | Unset
        if isinstance(_daily_type, Unset):
            daily_type = UNSET
        else:
            daily_type = DailyType(_daily_type)

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

        store_for = d.pop("storeFor", UNSET)

        _store_for_unit = d.pop("storeForUnit", UNSET)
        store_for_unit: SlaDurationType | Unset
        if isinstance(_store_for_unit, Unset):
            store_for_unit = UNSET
        else:
            store_for_unit = SlaDurationType(_store_for_unit)

        weekly_sla_schedule = cls(
            schedule_enabled=schedule_enabled,
            daily_type=daily_type,
            selected_days=selected_days,
            store_for=store_for,
            store_for_unit=store_for_unit,
        )

        weekly_sla_schedule.additional_properties = d
        return weekly_sla_schedule

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
