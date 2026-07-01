from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sla_duration_type import SlaDurationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DailySlaSchedule")


@_attrs_define
class DailySlaSchedule:
    """Specifies the daily schedule settings.

    Attributes:
        schedule_enabled (bool | Unset): Defines whether the daily schedule is enabled in the template.
        create_every (int | Unset): Specifies the interval (in number of time units) at which the restore points will be
            created. **Note**&#58; For the `createUnit` parameter, you can only specify either *Minute* or *Hour*. If you
            specify *Minute* for the `createUnit` parameter, you can only use either of the following values for the
            `createEvery` parameter&#58; 5, 10, 15, 20, 30; if you specify *Hour* for the `createUnit` parameter, you can
            only use either of the following values for the `createEvery` parameter&#58; 1, 2, 3, 4, 6, 8, 12, 24.
        create_unit (SlaDurationType | Unset): Specifies a time unit.
        store_for (int | Unset): Specifies the time period (in number of time units) during which Veeam Backup for
            Microsoft Azure will keep the created restore points. **Note**&#58; For the `createUnit` parameter, you can
            specify the following values only&#58; either *Day* or *Month* for a snapshot schedule, and *Hour* for a backup
            schedule.
        store_for_unit (SlaDurationType | Unset): Specifies a time unit.
    """

    schedule_enabled: bool | Unset = UNSET
    create_every: int | Unset = UNSET
    create_unit: SlaDurationType | Unset = UNSET
    store_for: int | Unset = UNSET
    store_for_unit: SlaDurationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_enabled = self.schedule_enabled

        create_every = self.create_every

        create_unit: str | Unset = UNSET
        if not isinstance(self.create_unit, Unset):
            create_unit = self.create_unit.value

        store_for = self.store_for

        store_for_unit: str | Unset = UNSET
        if not isinstance(self.store_for_unit, Unset):
            store_for_unit = self.store_for_unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_enabled is not UNSET:
            field_dict["scheduleEnabled"] = schedule_enabled
        if create_every is not UNSET:
            field_dict["createEvery"] = create_every
        if create_unit is not UNSET:
            field_dict["createUnit"] = create_unit
        if store_for is not UNSET:
            field_dict["storeFor"] = store_for
        if store_for_unit is not UNSET:
            field_dict["storeForUnit"] = store_for_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schedule_enabled = d.pop("scheduleEnabled", UNSET)

        create_every = d.pop("createEvery", UNSET)

        _create_unit = d.pop("createUnit", UNSET)
        create_unit: SlaDurationType | Unset
        if isinstance(_create_unit, Unset):
            create_unit = UNSET
        else:
            create_unit = SlaDurationType(_create_unit)

        store_for = d.pop("storeFor", UNSET)

        _store_for_unit = d.pop("storeForUnit", UNSET)
        store_for_unit: SlaDurationType | Unset
        if isinstance(_store_for_unit, Unset):
            store_for_unit = UNSET
        else:
            store_for_unit = SlaDurationType(_store_for_unit)

        daily_sla_schedule = cls(
            schedule_enabled=schedule_enabled,
            create_every=create_every,
            create_unit=create_unit,
            store_for=store_for,
            store_for_unit=store_for_unit,
        )

        daily_sla_schedule.additional_properties = d
        return daily_sla_schedule

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
