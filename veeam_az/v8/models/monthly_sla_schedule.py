from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.day_of_week import DayOfWeek
from ..models.month import Month
from ..models.monthly_type import MonthlyType
from ..models.sla_duration_type import SlaDurationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonthlySlaSchedule")


@_attrs_define
class MonthlySlaSchedule:
    r"""Specifies the monthly schedule settings.

    Attributes:
        schedule_enabled (bool | Unset): Defines whether the monthly schedule is enabled in the template.
        monthly_type (MonthlyType | Unset): Specifies the day of the month when the sessions will run.
        exact_day (int | None | Unset): Specifies the ordinal number of the day of the month when the restore points
            will be created.
        day_of_week (DayOfWeek | Unset): \[Applies if the *SelectedDays* value is specified for the `DailyType`
            parameter] Specifies the days of the week when the backup policy will run.
        selected_months (list[Month] | None | Unset): Specifies months when the restore points will be created.
        store_for (int | Unset): Specifies the time period (in number of time units) during which Veeam Backup for
            Microsoft Azure will keep the created restore points. **Note**&#58; For the `createUnit` parameter, you can only
            specify either *Month* or *Year*.
        store_for_unit (SlaDurationType | Unset): Specifies a time unit.
    """

    schedule_enabled: bool | Unset = UNSET
    monthly_type: MonthlyType | Unset = UNSET
    exact_day: int | None | Unset = UNSET
    day_of_week: DayOfWeek | Unset = UNSET
    selected_months: list[Month] | None | Unset = UNSET
    store_for: int | Unset = UNSET
    store_for_unit: SlaDurationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_enabled = self.schedule_enabled

        monthly_type: str | Unset = UNSET
        if not isinstance(self.monthly_type, Unset):
            monthly_type = self.monthly_type.value

        exact_day: int | None | Unset
        if isinstance(self.exact_day, Unset):
            exact_day = UNSET
        else:
            exact_day = self.exact_day

        day_of_week: str | Unset = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

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

        store_for = self.store_for

        store_for_unit: str | Unset = UNSET
        if not isinstance(self.store_for_unit, Unset):
            store_for_unit = self.store_for_unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_enabled is not UNSET:
            field_dict["scheduleEnabled"] = schedule_enabled
        if monthly_type is not UNSET:
            field_dict["monthlyType"] = monthly_type
        if exact_day is not UNSET:
            field_dict["exactDay"] = exact_day
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if selected_months is not UNSET:
            field_dict["selectedMonths"] = selected_months
        if store_for is not UNSET:
            field_dict["storeFor"] = store_for
        if store_for_unit is not UNSET:
            field_dict["storeForUnit"] = store_for_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schedule_enabled = d.pop("scheduleEnabled", UNSET)

        _monthly_type = d.pop("monthlyType", UNSET)
        monthly_type: MonthlyType | Unset
        if isinstance(_monthly_type, Unset):
            monthly_type = UNSET
        else:
            monthly_type = MonthlyType(_monthly_type)

        def _parse_exact_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exact_day = _parse_exact_day(d.pop("exactDay", UNSET))

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: DayOfWeek | Unset
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = DayOfWeek(_day_of_week)

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

        store_for = d.pop("storeFor", UNSET)

        _store_for_unit = d.pop("storeForUnit", UNSET)
        store_for_unit: SlaDurationType | Unset
        if isinstance(_store_for_unit, Unset):
            store_for_unit = UNSET
        else:
            store_for_unit = SlaDurationType(_store_for_unit)

        monthly_sla_schedule = cls(
            schedule_enabled=schedule_enabled,
            monthly_type=monthly_type,
            exact_day=exact_day,
            day_of_week=day_of_week,
            selected_months=selected_months,
            store_for=store_for,
            store_for_unit=store_for_unit,
        )

        monthly_sla_schedule.additional_properties = d
        return monthly_sla_schedule

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
