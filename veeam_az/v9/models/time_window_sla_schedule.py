from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeWindowSlaSchedule")


@_attrs_define
class TimeWindowSlaSchedule:
    """Specifies a snapshot or a backup window during which the restore points will be created.

    Attributes:
        window_opening (None | str | Unset): Specifies the time (in the format HH:MM:SS) at which the window starts.
        window_closing (None | str | Unset): Specifies the time (in the format HH:MM:SS) at which the window ends.
    """

    window_opening: None | str | Unset = UNSET
    window_closing: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        window_opening: None | str | Unset
        if isinstance(self.window_opening, Unset):
            window_opening = UNSET
        else:
            window_opening = self.window_opening

        window_closing: None | str | Unset
        if isinstance(self.window_closing, Unset):
            window_closing = UNSET
        else:
            window_closing = self.window_closing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if window_opening is not UNSET:
            field_dict["windowOpening"] = window_opening
        if window_closing is not UNSET:
            field_dict["windowClosing"] = window_closing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_window_opening(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        window_opening = _parse_window_opening(d.pop("windowOpening", UNSET))

        def _parse_window_closing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        window_closing = _parse_window_closing(d.pop("windowClosing", UNSET))

        time_window_sla_schedule = cls(
            window_opening=window_opening,
            window_closing=window_closing,
        )

        time_window_sla_schedule.additional_properties = d
        return time_window_sla_schedule

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
