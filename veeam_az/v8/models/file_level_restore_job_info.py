from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flr_link import FlrLink


T = TypeVar("T", bound="FileLevelRestoreJobInfo")


@_attrs_define
class FileLevelRestoreJobInfo:
    r"""\[Applies only if file-level restore operation is performed for the backup policy] File-level restore settings
    configured for the backup policy.

        Attributes:
            initiator (None | str | Unset): Name of the user that initiated the restore operation.
            reason (None | str | Unset): Reason for performing the restore operation.
            flr_link (FlrLink | Unset): Information on a File-level recovery link.
            vm_id (None | str | Unset): System ID assigned to the protected Azure VM in the Veeam Backup for Microsoft Azure
                REST API.
            vm_name (None | str | Unset): Name of the protected Azure VM.
            backup_policy_display_name (None | str | Unset): Name of the backup policy.
            restore_point_created_date_utc (datetime.datetime | None | Unset): Date and time when the restore point was
                created.
            is_flr_session_ready (bool | Unset):
    """

    initiator: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    flr_link: FlrLink | Unset = UNSET
    vm_id: None | str | Unset = UNSET
    vm_name: None | str | Unset = UNSET
    backup_policy_display_name: None | str | Unset = UNSET
    restore_point_created_date_utc: datetime.datetime | None | Unset = UNSET
    is_flr_session_ready: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        initiator: None | str | Unset
        if isinstance(self.initiator, Unset):
            initiator = UNSET
        else:
            initiator = self.initiator

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        flr_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flr_link, Unset):
            flr_link = self.flr_link.to_dict()

        vm_id: None | str | Unset
        if isinstance(self.vm_id, Unset):
            vm_id = UNSET
        else:
            vm_id = self.vm_id

        vm_name: None | str | Unset
        if isinstance(self.vm_name, Unset):
            vm_name = UNSET
        else:
            vm_name = self.vm_name

        backup_policy_display_name: None | str | Unset
        if isinstance(self.backup_policy_display_name, Unset):
            backup_policy_display_name = UNSET
        else:
            backup_policy_display_name = self.backup_policy_display_name

        restore_point_created_date_utc: None | str | Unset
        if isinstance(self.restore_point_created_date_utc, Unset):
            restore_point_created_date_utc = UNSET
        elif isinstance(self.restore_point_created_date_utc, datetime.datetime):
            restore_point_created_date_utc = self.restore_point_created_date_utc.isoformat()
        else:
            restore_point_created_date_utc = self.restore_point_created_date_utc

        is_flr_session_ready = self.is_flr_session_ready

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if reason is not UNSET:
            field_dict["reason"] = reason
        if flr_link is not UNSET:
            field_dict["flrLink"] = flr_link
        if vm_id is not UNSET:
            field_dict["vmId"] = vm_id
        if vm_name is not UNSET:
            field_dict["vmName"] = vm_name
        if backup_policy_display_name is not UNSET:
            field_dict["backupPolicyDisplayName"] = backup_policy_display_name
        if restore_point_created_date_utc is not UNSET:
            field_dict["restorePointCreatedDateUtc"] = restore_point_created_date_utc
        if is_flr_session_ready is not UNSET:
            field_dict["isFlrSessionReady"] = is_flr_session_ready

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flr_link import FlrLink

        d = dict(src_dict)

        def _parse_initiator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initiator = _parse_initiator(d.pop("initiator", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        _flr_link = d.pop("flrLink", UNSET)
        flr_link: FlrLink | Unset
        if isinstance(_flr_link, Unset):
            flr_link = UNSET
        else:
            flr_link = FlrLink.from_dict(_flr_link)

        def _parse_vm_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vm_id = _parse_vm_id(d.pop("vmId", UNSET))

        def _parse_vm_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vm_name = _parse_vm_name(d.pop("vmName", UNSET))

        def _parse_backup_policy_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_policy_display_name = _parse_backup_policy_display_name(d.pop("backupPolicyDisplayName", UNSET))

        def _parse_restore_point_created_date_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restore_point_created_date_utc_type_0 = isoparse(data)

                return restore_point_created_date_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        restore_point_created_date_utc = _parse_restore_point_created_date_utc(
            d.pop("restorePointCreatedDateUtc", UNSET)
        )

        is_flr_session_ready = d.pop("isFlrSessionReady", UNSET)

        file_level_restore_job_info = cls(
            initiator=initiator,
            reason=reason,
            flr_link=flr_link,
            vm_id=vm_id,
            vm_name=vm_name,
            backup_policy_display_name=backup_policy_display_name,
            restore_point_created_date_utc=restore_point_created_date_utc,
            is_flr_session_ready=is_flr_session_ready,
        )

        return file_level_restore_job_info
