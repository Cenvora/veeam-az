from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestoreJobInfo")


@_attrs_define
class RestoreJobInfo:
    r"""\[Applies only if restore operation is performed for the backup policy] Restore settings configured for the backup
    policy.

        Attributes:
            reason (None | str | Unset): Reason for performing the restore operation.
            backup_policy_display_name (None | str | Unset): Name of the backup policy.
    """

    reason: None | str | Unset = UNSET
    backup_policy_display_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        backup_policy_display_name: None | str | Unset
        if isinstance(self.backup_policy_display_name, Unset):
            backup_policy_display_name = UNSET
        else:
            backup_policy_display_name = self.backup_policy_display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if backup_policy_display_name is not UNSET:
            field_dict["backupPolicyDisplayName"] = backup_policy_display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_backup_policy_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_policy_display_name = _parse_backup_policy_display_name(d.pop("backupPolicyDisplayName", UNSET))

        restore_job_info = cls(
            reason=reason,
            backup_policy_display_name=backup_policy_display_name,
        )

        return restore_job_info
