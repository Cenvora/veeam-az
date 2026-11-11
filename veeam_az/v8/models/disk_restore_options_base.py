from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_group import ResourceGroup
    from ..models.storage_account import StorageAccount


T = TypeVar("T", bound="DiskRestoreOptionsBase")


@_attrs_define
class DiskRestoreOptionsBase:
    """Specifies information on OS and data disks attached to the restored Azure VM.

    Attributes:
        disk_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API
            to the restored virtual disk.
        name (None | str | Unset): Specifies the name of the restored virtual disk.
        resource_group (ResourceGroup | Unset): Specifies information on a resource group.
        storage_account (StorageAccount | Unset): Specifies information on a storage account.
    """

    disk_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    resource_group: ResourceGroup | Unset = UNSET
    storage_account: StorageAccount | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        disk_id: None | str | Unset
        if isinstance(self.disk_id, Unset):
            disk_id = UNSET
        else:
            disk_id = self.disk_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        resource_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_group, Unset):
            resource_group = self.resource_group.to_dict()

        storage_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_account, Unset):
            storage_account = self.storage_account.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if disk_id is not UNSET:
            field_dict["diskId"] = disk_id
        if name is not UNSET:
            field_dict["name"] = name
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if storage_account is not UNSET:
            field_dict["storageAccount"] = storage_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_group import ResourceGroup
        from ..models.storage_account import StorageAccount

        d = dict(src_dict)

        def _parse_disk_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disk_id = _parse_disk_id(d.pop("diskId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _resource_group = d.pop("resourceGroup", UNSET)
        resource_group: ResourceGroup | Unset
        if isinstance(_resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = ResourceGroup.from_dict(_resource_group)

        _storage_account = d.pop("storageAccount", UNSET)
        storage_account: StorageAccount | Unset
        if isinstance(_storage_account, Unset):
            storage_account = UNSET
        else:
            storage_account = StorageAccount.from_dict(_storage_account)

        disk_restore_options_base = cls(
            disk_id=disk_id,
            name=name,
            resource_group=resource_group,
            storage_account=storage_account,
        )

        return disk_restore_options_base
