from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileShareFlrOptions")


@_attrs_define
class FileShareFlrOptions:
    """
    Attributes:
        reason (None | str | Unset): Specifies a reason for performing the restore operation.
        target_file_share_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft
            Azure REST API to an Azure file share to which files and folders must be restored.
        service_account_id (str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure to a
            service account whose permissions will be used to access the target file share.
        source_service_account_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for
            Microsoft Azure REST API to a service account whose permissions were used to perform the backup operation.
    """

    reason: None | str | Unset = UNSET
    target_file_share_id: None | str | Unset = UNSET
    service_account_id: str | Unset = UNSET
    source_service_account_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        target_file_share_id: None | str | Unset
        if isinstance(self.target_file_share_id, Unset):
            target_file_share_id = UNSET
        else:
            target_file_share_id = self.target_file_share_id

        service_account_id = self.service_account_id

        source_service_account_id: None | str | Unset
        if isinstance(self.source_service_account_id, Unset):
            source_service_account_id = UNSET
        else:
            source_service_account_id = self.source_service_account_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if target_file_share_id is not UNSET:
            field_dict["targetFileShareId"] = target_file_share_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if source_service_account_id is not UNSET:
            field_dict["sourceServiceAccountId"] = source_service_account_id

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

        def _parse_target_file_share_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_file_share_id = _parse_target_file_share_id(d.pop("targetFileShareId", UNSET))

        service_account_id = d.pop("serviceAccountId", UNSET)

        def _parse_source_service_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_service_account_id = _parse_source_service_account_id(d.pop("sourceServiceAccountId", UNSET))

        file_share_flr_options = cls(
            reason=reason,
            target_file_share_id=target_file_share_id,
            service_account_id=service_account_id,
            source_service_account_id=source_service_account_id,
        )

        return file_share_flr_options
