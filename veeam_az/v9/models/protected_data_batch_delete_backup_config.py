from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.protected_data_backup_tier_nullable import ProtectedDataBackupTierNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedDataBatchDeleteBackupConfig")


@_attrs_define
class ProtectedDataBatchDeleteBackupConfig:
    """Information on the backups that will be removed.

    Attributes:
        ids (list[str]): Specifies a comma-separated list of system IDs assigned in the Veeam Backup for Microsoft Azure
            REST API to Azure VMs whose backups will be removed.
        backup_tier (ProtectedDataBackupTierNullable | Unset): Defines whether you want to delete *Archive*, Standard
            (*NonArchive*) or *All* backups created for the specified Azure resources. By default, Veeam Backup for
            Microsoft Azure deletes all backups.
    """

    ids: list[str]
    backup_tier: ProtectedDataBackupTierNullable | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        backup_tier: str | Unset = UNSET
        if not isinstance(self.backup_tier, Unset):
            backup_tier = self.backup_tier.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ids": ids,
            }
        )
        if backup_tier is not UNSET:
            field_dict["backupTier"] = backup_tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        _backup_tier = d.pop("backupTier", UNSET)
        backup_tier: ProtectedDataBackupTierNullable | Unset
        if isinstance(_backup_tier, Unset):
            backup_tier = UNSET
        else:
            backup_tier = ProtectedDataBackupTierNullable(_backup_tier)

        protected_data_batch_delete_backup_config = cls(
            ids=ids,
            backup_tier=backup_tier,
        )

        return protected_data_batch_delete_backup_config
