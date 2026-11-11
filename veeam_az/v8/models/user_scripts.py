from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_scripts_settings import UserScriptsSettings


T = TypeVar("T", bound="UserScripts")


@_attrs_define
class UserScripts:
    """Specifies script settings to be applied before and after the snapshot creating operation.

    Attributes:
        windows (UserScriptsSettings | Unset): Specifies guest scripting settings for Linux and Windows-based Azure VMs.
        linux (UserScriptsSettings | Unset): Specifies guest scripting settings for Linux and Windows-based Azure VMs.
    """

    windows: UserScriptsSettings | Unset = UNSET
    linux: UserScriptsSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        windows: dict[str, Any] | Unset = UNSET
        if not isinstance(self.windows, Unset):
            windows = self.windows.to_dict()

        linux: dict[str, Any] | Unset = UNSET
        if not isinstance(self.linux, Unset):
            linux = self.linux.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if windows is not UNSET:
            field_dict["windows"] = windows
        if linux is not UNSET:
            field_dict["linux"] = linux

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_scripts_settings import UserScriptsSettings

        d = dict(src_dict)
        _windows = d.pop("windows", UNSET)
        windows: UserScriptsSettings | Unset
        if isinstance(_windows, Unset):
            windows = UNSET
        else:
            windows = UserScriptsSettings.from_dict(_windows)

        _linux = d.pop("linux", UNSET)
        linux: UserScriptsSettings | Unset
        if isinstance(_linux, Unset):
            linux = UNSET
        else:
            linux = UserScriptsSettings.from_dict(_linux)

        user_scripts = cls(
            windows=windows,
            linux=linux,
        )

        return user_scripts
