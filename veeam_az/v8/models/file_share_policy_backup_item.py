from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_share import FileShare
    from ..models.file_share_policy_item_deleted_from_azure import FileSharePolicyItemDeletedFromAzure
    from ..models.resource_group import ResourceGroup
    from ..models.storage_account import StorageAccount


T = TypeVar("T", bound="FileSharePolicyBackupItem")


@_attrs_define
class FileSharePolicyBackupItem:
    """
    Attributes:
        file_share (FileShare | Unset): Specifies information on a file share.
        storage_account (StorageAccount | Unset): Specifies information on a storage account.
        resource_group (ResourceGroup | Unset): Specifies information on a resource group.
        deleted_item (FileSharePolicyItemDeletedFromAzure | Unset): Specifies information on a resource deleted from the
            Microsoft Azure infrastructure.
    """

    file_share: FileShare | Unset = UNSET
    storage_account: StorageAccount | Unset = UNSET
    resource_group: ResourceGroup | Unset = UNSET
    deleted_item: FileSharePolicyItemDeletedFromAzure | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_share: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_share, Unset):
            file_share = self.file_share.to_dict()

        storage_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_account, Unset):
            storage_account = self.storage_account.to_dict()

        resource_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_group, Unset):
            resource_group = self.resource_group.to_dict()

        deleted_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deleted_item, Unset):
            deleted_item = self.deleted_item.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_share is not UNSET:
            field_dict["fileShare"] = file_share
        if storage_account is not UNSET:
            field_dict["storageAccount"] = storage_account
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if deleted_item is not UNSET:
            field_dict["deletedItem"] = deleted_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_share import FileShare
        from ..models.file_share_policy_item_deleted_from_azure import FileSharePolicyItemDeletedFromAzure
        from ..models.resource_group import ResourceGroup
        from ..models.storage_account import StorageAccount

        d = dict(src_dict)
        _file_share = d.pop("fileShare", UNSET)
        file_share: FileShare | Unset
        if isinstance(_file_share, Unset):
            file_share = UNSET
        else:
            file_share = FileShare.from_dict(_file_share)

        _storage_account = d.pop("storageAccount", UNSET)
        storage_account: StorageAccount | Unset
        if isinstance(_storage_account, Unset):
            storage_account = UNSET
        else:
            storage_account = StorageAccount.from_dict(_storage_account)

        _resource_group = d.pop("resourceGroup", UNSET)
        resource_group: ResourceGroup | Unset
        if isinstance(_resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = ResourceGroup.from_dict(_resource_group)

        _deleted_item = d.pop("deletedItem", UNSET)
        deleted_item: FileSharePolicyItemDeletedFromAzure | Unset
        if isinstance(_deleted_item, Unset):
            deleted_item = UNSET
        else:
            deleted_item = FileSharePolicyItemDeletedFromAzure.from_dict(_deleted_item)

        file_share_policy_backup_item = cls(
            file_share=file_share,
            storage_account=storage_account,
            resource_group=resource_group,
            deleted_item=deleted_item,
        )

        return file_share_policy_backup_item
