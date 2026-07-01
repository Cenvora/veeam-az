from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupWindowSettingsWindow")


@_attrs_define
class BackupWindowSettingsWindow:
    """Specifies the days and hours when the auto-backup session will run.

    Attributes:
        sunday (list[int] | Unset):
        monday (list[int] | Unset):
        tuesday (list[int] | Unset):
        wednesday (list[int] | Unset):
        thursday (list[int] | Unset):
        friday (list[int] | Unset):
        saturday (list[int] | Unset):
    """

    sunday: list[int] | Unset = UNSET
    monday: list[int] | Unset = UNSET
    tuesday: list[int] | Unset = UNSET
    wednesday: list[int] | Unset = UNSET
    thursday: list[int] | Unset = UNSET
    friday: list[int] | Unset = UNSET
    saturday: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sunday: list[int] | Unset = UNSET
        if not isinstance(self.sunday, Unset):
            sunday = self.sunday

        monday: list[int] | Unset = UNSET
        if not isinstance(self.monday, Unset):
            monday = self.monday

        tuesday: list[int] | Unset = UNSET
        if not isinstance(self.tuesday, Unset):
            tuesday = self.tuesday

        wednesday: list[int] | Unset = UNSET
        if not isinstance(self.wednesday, Unset):
            wednesday = self.wednesday

        thursday: list[int] | Unset = UNSET
        if not isinstance(self.thursday, Unset):
            thursday = self.thursday

        friday: list[int] | Unset = UNSET
        if not isinstance(self.friday, Unset):
            friday = self.friday

        saturday: list[int] | Unset = UNSET
        if not isinstance(self.saturday, Unset):
            saturday = self.saturday

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sunday is not UNSET:
            field_dict["Sunday"] = sunday
        if monday is not UNSET:
            field_dict["Monday"] = monday
        if tuesday is not UNSET:
            field_dict["Tuesday"] = tuesday
        if wednesday is not UNSET:
            field_dict["Wednesday"] = wednesday
        if thursday is not UNSET:
            field_dict["Thursday"] = thursday
        if friday is not UNSET:
            field_dict["Friday"] = friday
        if saturday is not UNSET:
            field_dict["Saturday"] = saturday

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sunday = cast(list[int], d.pop("Sunday", UNSET))

        monday = cast(list[int], d.pop("Monday", UNSET))

        tuesday = cast(list[int], d.pop("Tuesday", UNSET))

        wednesday = cast(list[int], d.pop("Wednesday", UNSET))

        thursday = cast(list[int], d.pop("Thursday", UNSET))

        friday = cast(list[int], d.pop("Friday", UNSET))

        saturday = cast(list[int], d.pop("Saturday", UNSET))

        backup_window_settings_window = cls(
            sunday=sunday,
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
        )

        return backup_window_settings_window
