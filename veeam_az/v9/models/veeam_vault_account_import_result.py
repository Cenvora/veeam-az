from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_account import StorageAccount


T = TypeVar("T", bound="VeeamVaultAccountImportResult")


@_attrs_define
class VeeamVaultAccountImportResult:
    """
    Attributes:
        azure_account_id (str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the
            service account that you can use to access Veeam Data Cloud Vault.
        azure_account_name (str | Unset):
        storage_account (StorageAccount | Unset): Specifies information on a storage account.
        storage_account_container (str | Unset): Name of the blob container in which the storage vault resides.
    """

    azure_account_id: str | Unset = UNSET
    azure_account_name: str | Unset = UNSET
    storage_account: StorageAccount | Unset = UNSET
    storage_account_container: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        azure_account_id = self.azure_account_id

        azure_account_name = self.azure_account_name

        storage_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_account, Unset):
            storage_account = self.storage_account.to_dict()

        storage_account_container = self.storage_account_container

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if azure_account_id is not UNSET:
            field_dict["azureAccountId"] = azure_account_id
        if azure_account_name is not UNSET:
            field_dict["azureAccountName"] = azure_account_name
        if storage_account is not UNSET:
            field_dict["storageAccount"] = storage_account
        if storage_account_container is not UNSET:
            field_dict["storageAccountContainer"] = storage_account_container

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_account import StorageAccount

        d = dict(src_dict)
        azure_account_id = d.pop("azureAccountId", UNSET)

        azure_account_name = d.pop("azureAccountName", UNSET)

        _storage_account = d.pop("storageAccount", UNSET)
        storage_account: StorageAccount | Unset
        if isinstance(_storage_account, Unset):
            storage_account = UNSET
        else:
            storage_account = StorageAccount.from_dict(_storage_account)

        storage_account_container = d.pop("storageAccountContainer", UNSET)

        veeam_vault_account_import_result = cls(
            azure_account_id=azure_account_id,
            azure_account_name=azure_account_name,
            storage_account=storage_account,
            storage_account_container=storage_account_container,
        )

        return veeam_vault_account_import_result
