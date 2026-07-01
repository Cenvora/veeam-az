from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_share_policy_file_share_from_client import FileSharePolicyFileShareFromClient
    from ..models.file_share_policy_resource_group_from_client import FileSharePolicyResourceGroupFromClient
    from ..models.file_share_policy_storage_account_from_client import FileSharePolicyStorageAccountFromClient


T = TypeVar("T", bound="FileSharePolicyBackupItemsFromClient")


@_attrs_define
class FileSharePolicyBackupItemsFromClient:
    r"""\[Applies if the *SelectedItems* value is specified for the `backupType` parameter] Specifies information on Azure
    resources to protect by the backup policy.

        Attributes:
            file_shares (list[FileSharePolicyFileShareFromClient] | None | Unset): List of file shares.
            storage_accounts (list[FileSharePolicyStorageAccountFromClient] | None | Unset): List of storage accounts where
                protected file shares reside.
            resource_groups (list[FileSharePolicyResourceGroupFromClient] | None | Unset): List of resource groups where
                protected file shares belong.
    """

    file_shares: list[FileSharePolicyFileShareFromClient] | None | Unset = UNSET
    storage_accounts: list[FileSharePolicyStorageAccountFromClient] | None | Unset = UNSET
    resource_groups: list[FileSharePolicyResourceGroupFromClient] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_shares: list[dict[str, Any]] | None | Unset
        if isinstance(self.file_shares, Unset):
            file_shares = UNSET
        elif isinstance(self.file_shares, list):
            file_shares = []
            for file_shares_type_0_item_data in self.file_shares:
                file_shares_type_0_item = file_shares_type_0_item_data.to_dict()
                file_shares.append(file_shares_type_0_item)

        else:
            file_shares = self.file_shares

        storage_accounts: list[dict[str, Any]] | None | Unset
        if isinstance(self.storage_accounts, Unset):
            storage_accounts = UNSET
        elif isinstance(self.storage_accounts, list):
            storage_accounts = []
            for storage_accounts_type_0_item_data in self.storage_accounts:
                storage_accounts_type_0_item = storage_accounts_type_0_item_data.to_dict()
                storage_accounts.append(storage_accounts_type_0_item)

        else:
            storage_accounts = self.storage_accounts

        resource_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.resource_groups, Unset):
            resource_groups = UNSET
        elif isinstance(self.resource_groups, list):
            resource_groups = []
            for resource_groups_type_0_item_data in self.resource_groups:
                resource_groups_type_0_item = resource_groups_type_0_item_data.to_dict()
                resource_groups.append(resource_groups_type_0_item)

        else:
            resource_groups = self.resource_groups

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_shares is not UNSET:
            field_dict["fileShares"] = file_shares
        if storage_accounts is not UNSET:
            field_dict["storageAccounts"] = storage_accounts
        if resource_groups is not UNSET:
            field_dict["resourceGroups"] = resource_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_share_policy_file_share_from_client import FileSharePolicyFileShareFromClient
        from ..models.file_share_policy_resource_group_from_client import FileSharePolicyResourceGroupFromClient
        from ..models.file_share_policy_storage_account_from_client import FileSharePolicyStorageAccountFromClient

        d = dict(src_dict)

        def _parse_file_shares(data: object) -> list[FileSharePolicyFileShareFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_shares_type_0 = []
                _file_shares_type_0 = data
                for file_shares_type_0_item_data in _file_shares_type_0:
                    file_shares_type_0_item = FileSharePolicyFileShareFromClient.from_dict(file_shares_type_0_item_data)

                    file_shares_type_0.append(file_shares_type_0_item)

                return file_shares_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileSharePolicyFileShareFromClient] | None | Unset, data)

        file_shares = _parse_file_shares(d.pop("fileShares", UNSET))

        def _parse_storage_accounts(data: object) -> list[FileSharePolicyStorageAccountFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                storage_accounts_type_0 = []
                _storage_accounts_type_0 = data
                for storage_accounts_type_0_item_data in _storage_accounts_type_0:
                    storage_accounts_type_0_item = FileSharePolicyStorageAccountFromClient.from_dict(
                        storage_accounts_type_0_item_data
                    )

                    storage_accounts_type_0.append(storage_accounts_type_0_item)

                return storage_accounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileSharePolicyStorageAccountFromClient] | None | Unset, data)

        storage_accounts = _parse_storage_accounts(d.pop("storageAccounts", UNSET))

        def _parse_resource_groups(data: object) -> list[FileSharePolicyResourceGroupFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resource_groups_type_0 = []
                _resource_groups_type_0 = data
                for resource_groups_type_0_item_data in _resource_groups_type_0:
                    resource_groups_type_0_item = FileSharePolicyResourceGroupFromClient.from_dict(
                        resource_groups_type_0_item_data
                    )

                    resource_groups_type_0.append(resource_groups_type_0_item)

                return resource_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileSharePolicyResourceGroupFromClient] | None | Unset, data)

        resource_groups = _parse_resource_groups(d.pop("resourceGroups", UNSET))

        file_share_policy_backup_items_from_client = cls(
            file_shares=file_shares,
            storage_accounts=storage_accounts,
            resource_groups=resource_groups,
        )

        return file_share_policy_backup_items_from_client
