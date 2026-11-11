from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_window_settings_window import BackupWindowSettingsWindow


T = TypeVar("T", bound="BackupWindowSettings")


@_attrs_define
class BackupWindowSettings:
    """Specifies the periodical schedule for the backup policy.

    Attributes:
        window (BackupWindowSettingsWindow | Unset): Specifies the days and hours when the auto-backup session will run.
        minute_offset (int | None | Unset): Specifies a time interval (in minutes) by which the snapshot creation will
            be postponed.
    """

    window: BackupWindowSettingsWindow | Unset = UNSET
    minute_offset: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.to_dict()

        minute_offset: int | None | Unset
        if isinstance(self.minute_offset, Unset):
            minute_offset = UNSET
        else:
            minute_offset = self.minute_offset

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if window is not UNSET:
            field_dict["window"] = window
        if minute_offset is not UNSET:
            field_dict["minuteOffset"] = minute_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_window_settings_window import BackupWindowSettingsWindow

        d = dict(src_dict)
        _window = d.pop("window", UNSET)
        window: BackupWindowSettingsWindow | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = BackupWindowSettingsWindow.from_dict(_window)

        def _parse_minute_offset(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        minute_offset = _parse_minute_offset(d.pop("minuteOffset", UNSET))

        backup_window_settings = cls(
            window=window,
            minute_offset=minute_offset,
        )

        return backup_window_settings
