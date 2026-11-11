from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.month import Month
from ..models.month_magnet_type import MonthMagnetType
from ..models.sla_duration_type import SlaDurationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchiveSlaSchedule")


@_attrs_define
class ArchiveSlaSchedule:
    """Specifies the backup archival settings.

    Attributes:
        schedule_enabled (bool | Unset): Defines whether the archive schedule is enabled in the template.
        selected_months (list[Month] | Unset): Specifies months when the archives will be created.
        monthly_type (MonthMagnetType | Unset): Specifies the day on which the restore points will be created.
        store_for (int | Unset): Specifies the time period (in number of time units) during which Veeam Backup for
            Microsoft Azure will keep the created archives. **Note**&#58; For the `createUnit` parameter, you can only
            specify either *Month* or *Year*.
        store_for_unit (SlaDurationType | Unset): Specifies a time unit.
    """

    schedule_enabled: bool | Unset = UNSET
    selected_months: list[Month] | Unset = UNSET
    monthly_type: MonthMagnetType | Unset = UNSET
    store_for: int | Unset = UNSET
    store_for_unit: SlaDurationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_enabled = self.schedule_enabled

        selected_months: list[str] | Unset = UNSET
        if not isinstance(self.selected_months, Unset):
            selected_months = []
            for selected_months_item_data in self.selected_months:
                selected_months_item = selected_months_item_data.value
                selected_months.append(selected_months_item)

        monthly_type: str | Unset = UNSET
        if not isinstance(self.monthly_type, Unset):
            monthly_type = self.monthly_type.value

        store_for = self.store_for

        store_for_unit: str | Unset = UNSET
        if not isinstance(self.store_for_unit, Unset):
            store_for_unit = self.store_for_unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_enabled is not UNSET:
            field_dict["scheduleEnabled"] = schedule_enabled
        if selected_months is not UNSET:
            field_dict["selectedMonths"] = selected_months
        if monthly_type is not UNSET:
            field_dict["monthlyType"] = monthly_type
        if store_for is not UNSET:
            field_dict["storeFor"] = store_for
        if store_for_unit is not UNSET:
            field_dict["storeForUnit"] = store_for_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schedule_enabled = d.pop("scheduleEnabled", UNSET)

        _selected_months = d.pop("selectedMonths", UNSET)
        selected_months: list[Month] | Unset = UNSET
        if _selected_months is not UNSET:
            selected_months = []
            for selected_months_item_data in _selected_months:
                selected_months_item = Month(selected_months_item_data)

                selected_months.append(selected_months_item)

        _monthly_type = d.pop("monthlyType", UNSET)
        monthly_type: MonthMagnetType | Unset
        if isinstance(_monthly_type, Unset):
            monthly_type = UNSET
        else:
            monthly_type = MonthMagnetType(_monthly_type)

        store_for = d.pop("storeFor", UNSET)

        _store_for_unit = d.pop("storeForUnit", UNSET)
        store_for_unit: SlaDurationType | Unset
        if isinstance(_store_for_unit, Unset):
            store_for_unit = UNSET
        else:
            store_for_unit = SlaDurationType(_store_for_unit)

        archive_sla_schedule = cls(
            schedule_enabled=schedule_enabled,
            selected_months=selected_months,
            monthly_type=monthly_type,
            store_for=store_for,
            store_for_unit=store_for_unit,
        )

        archive_sla_schedule.additional_properties = d
        return archive_sla_schedule

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
