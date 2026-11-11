from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.storage_tier_nullable import StorageTierNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_consumption_limit import StorageConsumptionLimit


T = TypeVar("T", bound="RepositoryCreateFromClientWithKeyVault")


@_attrs_define
class RepositoryCreateFromClientWithKeyVault:
    """
    Attributes:
        azure_storage_account_id (str): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST
            API to a storage account where a target blob container resides.
        azure_storage_folder (str): Specifies a name of the folder in the selected container that will be used to store
            backups.
        azure_storage_container (str): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API
            to the blob container that will be used as a target location for backups of Azure resources.
        azure_account_id (str): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to a
            repository or service account whose permissions were used to create the repository.
        key_vault_id (None | str | Unset): /[Applies if data stored in the repository must be encrypted using an Azure
            Key Vault cryptographic key/] Specifies the Microsoft Azure ID assigned to a Key Vault where a cryptographic key
            that will be used for repository encryption resides.
        key_vault_key_uri (None | str | Unset): /[Applies if data stored in the repository must be encrypted using an
            Azure Key Vault cryptographic key/] Specifies the URI of the cryptographic key.
        storage_tier (StorageTierNullable | Unset): Specifies the access tier.
        concurrency_limit (int | None | Unset): Specifies the maximum number of concurrent connections from worker
            instances to the repository within a backup session.
        import_if_folder_has_backup (bool | None | Unset): Defines whether to import to the backup appliance backup
            files that are already stored in the specified folder.
        auto_create_tiers (bool | None | Unset): Defines whether to automatically create 3 separate repositories for
            Hot, Cool and Archive access tiers.
        name (None | str | Unset): Specifies a name for the repository.
        description (None | str | Unset): Specifies a description for the repository.
        enable_encryption (bool | Unset): Defines whether the encryption must be enabled for backup files stored in the
            repository.
        password (None | str | Unset): /[Applies if data stored in the repository must be encrypted using a password/]
            Specifies a password that will be used for repository encryption.
        hint (None | str | Unset): Specifies a hint to the password.
        storage_consumption_limit (StorageConsumptionLimit | Unset):
    """

    azure_storage_account_id: str
    azure_storage_folder: str
    azure_storage_container: str
    azure_account_id: str
    key_vault_id: None | str | Unset = UNSET
    key_vault_key_uri: None | str | Unset = UNSET
    storage_tier: StorageTierNullable | Unset = UNSET
    concurrency_limit: int | None | Unset = UNSET
    import_if_folder_has_backup: bool | None | Unset = UNSET
    auto_create_tiers: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    enable_encryption: bool | Unset = UNSET
    password: None | str | Unset = UNSET
    hint: None | str | Unset = UNSET
    storage_consumption_limit: StorageConsumptionLimit | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        azure_storage_account_id = self.azure_storage_account_id

        azure_storage_folder = self.azure_storage_folder

        azure_storage_container = self.azure_storage_container

        azure_account_id = self.azure_account_id

        key_vault_id: None | str | Unset
        if isinstance(self.key_vault_id, Unset):
            key_vault_id = UNSET
        else:
            key_vault_id = self.key_vault_id

        key_vault_key_uri: None | str | Unset
        if isinstance(self.key_vault_key_uri, Unset):
            key_vault_key_uri = UNSET
        else:
            key_vault_key_uri = self.key_vault_key_uri

        storage_tier: str | Unset = UNSET
        if not isinstance(self.storage_tier, Unset):
            storage_tier = self.storage_tier.value

        concurrency_limit: int | None | Unset
        if isinstance(self.concurrency_limit, Unset):
            concurrency_limit = UNSET
        else:
            concurrency_limit = self.concurrency_limit

        import_if_folder_has_backup: bool | None | Unset
        if isinstance(self.import_if_folder_has_backup, Unset):
            import_if_folder_has_backup = UNSET
        else:
            import_if_folder_has_backup = self.import_if_folder_has_backup

        auto_create_tiers: bool | None | Unset
        if isinstance(self.auto_create_tiers, Unset):
            auto_create_tiers = UNSET
        else:
            auto_create_tiers = self.auto_create_tiers

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enable_encryption = self.enable_encryption

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        hint: None | str | Unset
        if isinstance(self.hint, Unset):
            hint = UNSET
        else:
            hint = self.hint

        storage_consumption_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_consumption_limit, Unset):
            storage_consumption_limit = self.storage_consumption_limit.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "azureStorageAccountId": azure_storage_account_id,
                "azureStorageFolder": azure_storage_folder,
                "azureStorageContainer": azure_storage_container,
                "azureAccountId": azure_account_id,
            }
        )
        if key_vault_id is not UNSET:
            field_dict["keyVaultId"] = key_vault_id
        if key_vault_key_uri is not UNSET:
            field_dict["keyVaultKeyUri"] = key_vault_key_uri
        if storage_tier is not UNSET:
            field_dict["storageTier"] = storage_tier
        if concurrency_limit is not UNSET:
            field_dict["concurrencyLimit"] = concurrency_limit
        if import_if_folder_has_backup is not UNSET:
            field_dict["importIfFolderHasBackup"] = import_if_folder_has_backup
        if auto_create_tiers is not UNSET:
            field_dict["autoCreateTiers"] = auto_create_tiers
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if enable_encryption is not UNSET:
            field_dict["enableEncryption"] = enable_encryption
        if password is not UNSET:
            field_dict["password"] = password
        if hint is not UNSET:
            field_dict["hint"] = hint
        if storage_consumption_limit is not UNSET:
            field_dict["storageConsumptionLimit"] = storage_consumption_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_consumption_limit import StorageConsumptionLimit

        d = dict(src_dict)
        azure_storage_account_id = d.pop("azureStorageAccountId")

        azure_storage_folder = d.pop("azureStorageFolder")

        azure_storage_container = d.pop("azureStorageContainer")

        azure_account_id = d.pop("azureAccountId")

        def _parse_key_vault_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_vault_id = _parse_key_vault_id(d.pop("keyVaultId", UNSET))

        def _parse_key_vault_key_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_vault_key_uri = _parse_key_vault_key_uri(d.pop("keyVaultKeyUri", UNSET))

        _storage_tier = d.pop("storageTier", UNSET)
        storage_tier: StorageTierNullable | Unset
        if isinstance(_storage_tier, Unset):
            storage_tier = UNSET
        else:
            storage_tier = StorageTierNullable(_storage_tier)

        def _parse_concurrency_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        concurrency_limit = _parse_concurrency_limit(d.pop("concurrencyLimit", UNSET))

        def _parse_import_if_folder_has_backup(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        import_if_folder_has_backup = _parse_import_if_folder_has_backup(d.pop("importIfFolderHasBackup", UNSET))

        def _parse_auto_create_tiers(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_create_tiers = _parse_auto_create_tiers(d.pop("autoCreateTiers", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        enable_encryption = d.pop("enableEncryption", UNSET)

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_hint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hint = _parse_hint(d.pop("hint", UNSET))

        _storage_consumption_limit = d.pop("storageConsumptionLimit", UNSET)
        storage_consumption_limit: StorageConsumptionLimit | Unset
        if isinstance(_storage_consumption_limit, Unset):
            storage_consumption_limit = UNSET
        else:
            storage_consumption_limit = StorageConsumptionLimit.from_dict(_storage_consumption_limit)

        repository_create_from_client_with_key_vault = cls(
            azure_storage_account_id=azure_storage_account_id,
            azure_storage_folder=azure_storage_folder,
            azure_storage_container=azure_storage_container,
            azure_account_id=azure_account_id,
            key_vault_id=key_vault_id,
            key_vault_key_uri=key_vault_key_uri,
            storage_tier=storage_tier,
            concurrency_limit=concurrency_limit,
            import_if_folder_has_backup=import_if_folder_has_backup,
            auto_create_tiers=auto_create_tiers,
            name=name,
            description=description,
            enable_encryption=enable_encryption,
            password=password,
            hint=hint,
            storage_consumption_limit=storage_consumption_limit,
        )

        return repository_create_from_client_with_key_vault
