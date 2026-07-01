from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserScriptsSettings")


@_attrs_define
class UserScriptsSettings:
    """Specifies guest scripting settings for Linux and Windows-based Azure VMs.

    Attributes:
        scripts_enabled (bool | Unset): Defines whether to run custom scripts on Azure VMs.
        pre_script_path (None | str | Unset): Specifies a path to the directory on a protected Azure VM where the pre-
            snapshot script resides.
        pre_script_arguments (None | str | Unset): Specifies arguments to be passed to the pre-snapshot script when the
            script is executed.
        post_script_path (None | str | Unset): Specifies a path to the directory on a protected Azure VM where the post-
            snapshot script resides.
        post_script_arguments (None | str | Unset): Specifies arguments to be passed to the post-snapshot script when
            the script is executed.
        repository_snapshots_only (bool | Unset): Defines whether to run scripts only when performing a snapshot for the
            image-level backup operation.
        ignore_exit_codes (bool | Unset): Defines whether to continue performing backup if script execution failed with
            errors.
        ignore_missing_scripts (bool | Unset): Defines whether to continue performing backup if scripts are missing on
            the Azure VM.
    """

    scripts_enabled: bool | Unset = UNSET
    pre_script_path: None | str | Unset = UNSET
    pre_script_arguments: None | str | Unset = UNSET
    post_script_path: None | str | Unset = UNSET
    post_script_arguments: None | str | Unset = UNSET
    repository_snapshots_only: bool | Unset = UNSET
    ignore_exit_codes: bool | Unset = UNSET
    ignore_missing_scripts: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scripts_enabled = self.scripts_enabled

        pre_script_path: None | str | Unset
        if isinstance(self.pre_script_path, Unset):
            pre_script_path = UNSET
        else:
            pre_script_path = self.pre_script_path

        pre_script_arguments: None | str | Unset
        if isinstance(self.pre_script_arguments, Unset):
            pre_script_arguments = UNSET
        else:
            pre_script_arguments = self.pre_script_arguments

        post_script_path: None | str | Unset
        if isinstance(self.post_script_path, Unset):
            post_script_path = UNSET
        else:
            post_script_path = self.post_script_path

        post_script_arguments: None | str | Unset
        if isinstance(self.post_script_arguments, Unset):
            post_script_arguments = UNSET
        else:
            post_script_arguments = self.post_script_arguments

        repository_snapshots_only = self.repository_snapshots_only

        ignore_exit_codes = self.ignore_exit_codes

        ignore_missing_scripts = self.ignore_missing_scripts

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scripts_enabled is not UNSET:
            field_dict["scriptsEnabled"] = scripts_enabled
        if pre_script_path is not UNSET:
            field_dict["preScriptPath"] = pre_script_path
        if pre_script_arguments is not UNSET:
            field_dict["preScriptArguments"] = pre_script_arguments
        if post_script_path is not UNSET:
            field_dict["postScriptPath"] = post_script_path
        if post_script_arguments is not UNSET:
            field_dict["postScriptArguments"] = post_script_arguments
        if repository_snapshots_only is not UNSET:
            field_dict["repositorySnapshotsOnly"] = repository_snapshots_only
        if ignore_exit_codes is not UNSET:
            field_dict["ignoreExitCodes"] = ignore_exit_codes
        if ignore_missing_scripts is not UNSET:
            field_dict["ignoreMissingScripts"] = ignore_missing_scripts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scripts_enabled = d.pop("scriptsEnabled", UNSET)

        def _parse_pre_script_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pre_script_path = _parse_pre_script_path(d.pop("preScriptPath", UNSET))

        def _parse_pre_script_arguments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pre_script_arguments = _parse_pre_script_arguments(d.pop("preScriptArguments", UNSET))

        def _parse_post_script_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_script_path = _parse_post_script_path(d.pop("postScriptPath", UNSET))

        def _parse_post_script_arguments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_script_arguments = _parse_post_script_arguments(d.pop("postScriptArguments", UNSET))

        repository_snapshots_only = d.pop("repositorySnapshotsOnly", UNSET)

        ignore_exit_codes = d.pop("ignoreExitCodes", UNSET)

        ignore_missing_scripts = d.pop("ignoreMissingScripts", UNSET)

        user_scripts_settings = cls(
            scripts_enabled=scripts_enabled,
            pre_script_path=pre_script_path,
            pre_script_arguments=pre_script_arguments,
            post_script_path=post_script_path,
            post_script_arguments=post_script_arguments,
            repository_snapshots_only=repository_snapshots_only,
            ignore_exit_codes=ignore_exit_codes,
            ignore_missing_scripts=ignore_missing_scripts,
        )

        return user_scripts_settings
