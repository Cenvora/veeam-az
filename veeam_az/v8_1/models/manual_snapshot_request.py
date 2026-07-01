from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_items import BackupItems
    from ..models.manual_snapshot_settings import ManualSnapshotSettings


T = TypeVar("T", bound="ManualSnapshotRequest")


@_attrs_define
class ManualSnapshotRequest:
    """
    Attributes:
        azure_account_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure
            REST API to a repository or service account whose permissions will be used to create the snapshots.
        snapshot_settings (ManualSnapshotSettings | Unset): Specifies Azure tags that will be assigned to the snapshots.
        backup_items (BackupItems | Unset): Specifies a list of Azure VMs for which snapshots must be created.
    """

    azure_account_id: None | str | Unset = UNSET
    snapshot_settings: ManualSnapshotSettings | Unset = UNSET
    backup_items: BackupItems | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        azure_account_id: None | str | Unset
        if isinstance(self.azure_account_id, Unset):
            azure_account_id = UNSET
        else:
            azure_account_id = self.azure_account_id

        snapshot_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot_settings, Unset):
            snapshot_settings = self.snapshot_settings.to_dict()

        backup_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_items, Unset):
            backup_items = self.backup_items.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if azure_account_id is not UNSET:
            field_dict["azureAccountId"] = azure_account_id
        if snapshot_settings is not UNSET:
            field_dict["snapshotSettings"] = snapshot_settings
        if backup_items is not UNSET:
            field_dict["backupItems"] = backup_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_items import BackupItems
        from ..models.manual_snapshot_settings import ManualSnapshotSettings

        d = dict(src_dict)

        def _parse_azure_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_account_id = _parse_azure_account_id(d.pop("azureAccountId", UNSET))

        _snapshot_settings = d.pop("snapshotSettings", UNSET)
        snapshot_settings: ManualSnapshotSettings | Unset
        if isinstance(_snapshot_settings, Unset):
            snapshot_settings = UNSET
        else:
            snapshot_settings = ManualSnapshotSettings.from_dict(_snapshot_settings)

        _backup_items = d.pop("backupItems", UNSET)
        backup_items: BackupItems | Unset
        if isinstance(_backup_items, Unset):
            backup_items = UNSET
        else:
            backup_items = BackupItems.from_dict(_backup_items)

        manual_snapshot_request = cls(
            azure_account_id=azure_account_id,
            snapshot_settings=snapshot_settings,
            backup_items=backup_items,
        )

        return manual_snapshot_request
