from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.azure_environment_nullable import AzureEnvironmentNullable
from ..models.repository_status import RepositoryStatus
from ..models.repository_type import RepositoryType
from ..models.storage_tier import StorageTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_storage_item import AzureStorageItem
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.repository_ownership import RepositoryOwnership
    from ..models.storage_consumption_limit import StorageConsumptionLimit


T = TypeVar("T", bound="Repository")


@_attrs_define
class Repository:
    """Information on a backup repository.

    Attributes:
        enable_encryption (bool): Defines whether the encryption is enabled for backup files stored in the repository.
        storage_tier (StorageTier): Storage tier of the repository.
        id (None | str | Unset): System ID assigned to the repository in the Veeam Backup for Microsoft Azure REST API.
        name (None | str | Unset): Name of the repository.
        description (None | str | Unset): Description of the repository.
        azure_storage_account_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST
            API to a storage account where a target blob container resides.
        azure_storage_account_name (None | str | Unset): Name of the storage account where the target blob container
            resides.
        azure_storage_folder (AzureStorageItem | Unset): Information on an Azure storage resource.
        azure_storage_container (AzureStorageItem | Unset): Information on an Azure storage resource.
        hint (None | str | Unset): Hint to the password of the backup repository.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region where the backup repository resides.
        region_name (None | str | Unset): Name of the Azure region where the backup repository resides.
        azure_account_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to a
            service account whose permissions were used to create the repository.
        repository_type (RepositoryType | Unset): Status of the repository.
        environment (AzureEnvironmentNullable | Unset): Specifies the type of the Microsoft Azure cloud environment.
        status (RepositoryStatus | Unset): Status of the repository.
        is_storage_tier_inferred (bool | Unset): Defines whether the storage tier of the repository is Inferred.
        immutability_enabled (bool | Unset): Defines whether immutability is enabled at the repository level.
        repository_ownership (RepositoryOwnership | Unset):
        concurrency_limit (int | None | Unset): Specifies the maximum number of concurrent connections from worker
            instances to the repository within a backup session.
        storage_consumption_limit (StorageConsumptionLimit | Unset):
        veeam_vault_id (int | None | Unset):
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    enable_encryption: bool
    storage_tier: StorageTier
    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    azure_storage_account_id: None | str | Unset = UNSET
    azure_storage_account_name: None | str | Unset = UNSET
    azure_storage_folder: AzureStorageItem | Unset = UNSET
    azure_storage_container: AzureStorageItem | Unset = UNSET
    hint: None | str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    azure_account_id: None | str | Unset = UNSET
    repository_type: RepositoryType | Unset = UNSET
    environment: AzureEnvironmentNullable | Unset = UNSET
    status: RepositoryStatus | Unset = UNSET
    is_storage_tier_inferred: bool | Unset = UNSET
    immutability_enabled: bool | Unset = UNSET
    repository_ownership: RepositoryOwnership | Unset = UNSET
    concurrency_limit: int | None | Unset = UNSET
    storage_consumption_limit: StorageConsumptionLimit | Unset = UNSET
    veeam_vault_id: int | None | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        enable_encryption = self.enable_encryption

        storage_tier = self.storage_tier.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

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

        azure_storage_account_id: None | str | Unset
        if isinstance(self.azure_storage_account_id, Unset):
            azure_storage_account_id = UNSET
        else:
            azure_storage_account_id = self.azure_storage_account_id

        azure_storage_account_name: None | str | Unset
        if isinstance(self.azure_storage_account_name, Unset):
            azure_storage_account_name = UNSET
        else:
            azure_storage_account_name = self.azure_storage_account_name

        azure_storage_folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_storage_folder, Unset):
            azure_storage_folder = self.azure_storage_folder.to_dict()

        azure_storage_container: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_storage_container, Unset):
            azure_storage_container = self.azure_storage_container.to_dict()

        hint: None | str | Unset
        if isinstance(self.hint, Unset):
            hint = UNSET
        else:
            hint = self.hint

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        azure_account_id: None | str | Unset
        if isinstance(self.azure_account_id, Unset):
            azure_account_id = UNSET
        else:
            azure_account_id = self.azure_account_id

        repository_type: str | Unset = UNSET
        if not isinstance(self.repository_type, Unset):
            repository_type = self.repository_type.value

        environment: str | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_storage_tier_inferred = self.is_storage_tier_inferred

        immutability_enabled = self.immutability_enabled

        repository_ownership: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository_ownership, Unset):
            repository_ownership = self.repository_ownership.to_dict()

        concurrency_limit: int | None | Unset
        if isinstance(self.concurrency_limit, Unset):
            concurrency_limit = UNSET
        else:
            concurrency_limit = self.concurrency_limit

        storage_consumption_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_consumption_limit, Unset):
            storage_consumption_limit = self.storage_consumption_limit.to_dict()

        veeam_vault_id: int | None | Unset
        if isinstance(self.veeam_vault_id, Unset):
            veeam_vault_id = UNSET
        else:
            veeam_vault_id = self.veeam_vault_id

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enableEncryption": enable_encryption,
                "storageTier": storage_tier,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if azure_storage_account_id is not UNSET:
            field_dict["azureStorageAccountId"] = azure_storage_account_id
        if azure_storage_account_name is not UNSET:
            field_dict["azureStorageAccountName"] = azure_storage_account_name
        if azure_storage_folder is not UNSET:
            field_dict["azureStorageFolder"] = azure_storage_folder
        if azure_storage_container is not UNSET:
            field_dict["azureStorageContainer"] = azure_storage_container
        if hint is not UNSET:
            field_dict["hint"] = hint
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if azure_account_id is not UNSET:
            field_dict["azureAccountId"] = azure_account_id
        if repository_type is not UNSET:
            field_dict["repositoryType"] = repository_type
        if environment is not UNSET:
            field_dict["environment"] = environment
        if status is not UNSET:
            field_dict["status"] = status
        if is_storage_tier_inferred is not UNSET:
            field_dict["isStorageTierInferred"] = is_storage_tier_inferred
        if immutability_enabled is not UNSET:
            field_dict["immutabilityEnabled"] = immutability_enabled
        if repository_ownership is not UNSET:
            field_dict["repositoryOwnership"] = repository_ownership
        if concurrency_limit is not UNSET:
            field_dict["concurrencyLimit"] = concurrency_limit
        if storage_consumption_limit is not UNSET:
            field_dict["storageConsumptionLimit"] = storage_consumption_limit
        if veeam_vault_id is not UNSET:
            field_dict["veeamVaultId"] = veeam_vault_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_storage_item import AzureStorageItem
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.repository_ownership import RepositoryOwnership
        from ..models.storage_consumption_limit import StorageConsumptionLimit

        d = dict(src_dict)
        enable_encryption = d.pop("enableEncryption")

        storage_tier = StorageTier(d.pop("storageTier"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

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

        def _parse_azure_storage_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_storage_account_id = _parse_azure_storage_account_id(d.pop("azureStorageAccountId", UNSET))

        def _parse_azure_storage_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_storage_account_name = _parse_azure_storage_account_name(d.pop("azureStorageAccountName", UNSET))

        _azure_storage_folder = d.pop("azureStorageFolder", UNSET)
        azure_storage_folder: AzureStorageItem | Unset
        if isinstance(_azure_storage_folder, Unset):
            azure_storage_folder = UNSET
        else:
            azure_storage_folder = AzureStorageItem.from_dict(_azure_storage_folder)

        _azure_storage_container = d.pop("azureStorageContainer", UNSET)
        azure_storage_container: AzureStorageItem | Unset
        if isinstance(_azure_storage_container, Unset):
            azure_storage_container = UNSET
        else:
            azure_storage_container = AzureStorageItem.from_dict(_azure_storage_container)

        def _parse_hint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hint = _parse_hint(d.pop("hint", UNSET))

        def _parse_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        def _parse_azure_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_account_id = _parse_azure_account_id(d.pop("azureAccountId", UNSET))

        _repository_type = d.pop("repositoryType", UNSET)
        repository_type: RepositoryType | Unset
        if isinstance(_repository_type, Unset):
            repository_type = UNSET
        else:
            repository_type = RepositoryType(_repository_type)

        _environment = d.pop("environment", UNSET)
        environment: AzureEnvironmentNullable | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = AzureEnvironmentNullable(_environment)

        _status = d.pop("status", UNSET)
        status: RepositoryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RepositoryStatus(_status)

        is_storage_tier_inferred = d.pop("isStorageTierInferred", UNSET)

        immutability_enabled = d.pop("immutabilityEnabled", UNSET)

        _repository_ownership = d.pop("repositoryOwnership", UNSET)
        repository_ownership: RepositoryOwnership | Unset
        if isinstance(_repository_ownership, Unset):
            repository_ownership = UNSET
        else:
            repository_ownership = RepositoryOwnership.from_dict(_repository_ownership)

        def _parse_concurrency_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        concurrency_limit = _parse_concurrency_limit(d.pop("concurrencyLimit", UNSET))

        _storage_consumption_limit = d.pop("storageConsumptionLimit", UNSET)
        storage_consumption_limit: StorageConsumptionLimit | Unset
        if isinstance(_storage_consumption_limit, Unset):
            storage_consumption_limit = UNSET
        else:
            storage_consumption_limit = StorageConsumptionLimit.from_dict(_storage_consumption_limit)

        def _parse_veeam_vault_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        veeam_vault_id = _parse_veeam_vault_id(d.pop("veeamVaultId", UNSET))

        def _parse_field_links(data: object) -> LinksDictionaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_links_dictionary_type_0 = LinksDictionaryType0.from_dict(data)

                return componentsschemas_links_dictionary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinksDictionaryType0 | None | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        repository = cls(
            enable_encryption=enable_encryption,
            storage_tier=storage_tier,
            id=id,
            name=name,
            description=description,
            azure_storage_account_id=azure_storage_account_id,
            azure_storage_account_name=azure_storage_account_name,
            azure_storage_folder=azure_storage_folder,
            azure_storage_container=azure_storage_container,
            hint=hint,
            region_id=region_id,
            region_name=region_name,
            azure_account_id=azure_account_id,
            repository_type=repository_type,
            environment=environment,
            status=status,
            is_storage_tier_inferred=is_storage_tier_inferred,
            immutability_enabled=immutability_enabled,
            repository_ownership=repository_ownership,
            concurrency_limit=concurrency_limit,
            storage_consumption_limit=storage_consumption_limit,
            veeam_vault_id=veeam_vault_id,
            field_links=field_links,
        )

        return repository
