from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flr_link import FlrLink


T = TypeVar("T", bound="FileShareFileLevelRestoreJobInfo")


@_attrs_define
class FileShareFileLevelRestoreJobInfo:
    r"""\[Applies only if restore operation is performed for the backup policy] File-level restore settings of a file share
    configured for the backup policy.

        Attributes:
            initiator (None | str | Unset): Name of the user that initiated the restore operation.
            reason (None | str | Unset): Reason for performing the restore operation.
            flr_link (FlrLink | Unset): Information on a File-level recovery link.
            file_share_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to an
                Azure file share to which files and folders are restored.
            file_share_name (None | str | Unset): Name of the Azure file share.
            backup_policy_display_name (None | str | Unset): Name of the backup policy for which the restore point was
                created.
            restore_point_created_date_utc (datetime.datetime | None | Unset): Date and time when the restore point was
                created.
    """

    initiator: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    flr_link: FlrLink | Unset = UNSET
    file_share_id: None | str | Unset = UNSET
    file_share_name: None | str | Unset = UNSET
    backup_policy_display_name: None | str | Unset = UNSET
    restore_point_created_date_utc: datetime.datetime | None | Unset = UNSET

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

        file_share_id: None | str | Unset
        if isinstance(self.file_share_id, Unset):
            file_share_id = UNSET
        else:
            file_share_id = self.file_share_id

        file_share_name: None | str | Unset
        if isinstance(self.file_share_name, Unset):
            file_share_name = UNSET
        else:
            file_share_name = self.file_share_name

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if reason is not UNSET:
            field_dict["reason"] = reason
        if flr_link is not UNSET:
            field_dict["flrLink"] = flr_link
        if file_share_id is not UNSET:
            field_dict["fileShareId"] = file_share_id
        if file_share_name is not UNSET:
            field_dict["fileShareName"] = file_share_name
        if backup_policy_display_name is not UNSET:
            field_dict["backupPolicyDisplayName"] = backup_policy_display_name
        if restore_point_created_date_utc is not UNSET:
            field_dict["restorePointCreatedDateUtc"] = restore_point_created_date_utc

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

        def _parse_file_share_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_share_id = _parse_file_share_id(d.pop("fileShareId", UNSET))

        def _parse_file_share_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_share_name = _parse_file_share_name(d.pop("fileShareName", UNSET))

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

        file_share_file_level_restore_job_info = cls(
            initiator=initiator,
            reason=reason,
            flr_link=flr_link,
            file_share_id=file_share_id,
            file_share_name=file_share_name,
            backup_policy_display_name=backup_policy_display_name,
            restore_point_created_date_utc=restore_point_created_date_utc,
        )

        return file_share_file_level_restore_job_info
