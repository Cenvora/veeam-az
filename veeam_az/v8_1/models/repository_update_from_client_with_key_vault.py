from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_consumption_limit import StorageConsumptionLimit


T = TypeVar("T", bound="RepositoryUpdateFromClientWithKeyVault")


@_attrs_define
class RepositoryUpdateFromClientWithKeyVault:
    r"""
    Attributes:
        key_vault_id (None | str | Unset): \[Applies if data stored in the repository must be encrypted using an Azure
            Key Vault cryptographic key] Specifies the Microsoft Azure ID assigned to a Key Vault where a cryptographic key
            that will be used for repository encryption resides.
        key_vault_key_uri (None | str | Unset): \[Applies if data stored in the repository must be encrypted using an
            Azure Key Vault cryptographic key] Specifies the URI of the cryptographic key.
        name (None | str | Unset): Specifies the repository name.
        description (None | str | Unset): Specifies the repository description.
        azure_account_id (None | str | Unset):
        concurrency_limit (int | None | Unset): Specifies the maximum number of concurrent connections from worker
            instances to the repository within a backup session.
        enable_encryption (bool | Unset): Defines whether to enable encryption for the repository.
        password (None | str | Unset): \[Applies if data stored in the repository must be encrypted using a password]
            Specifies a password to be used for repository encryption.
        hint (None | str | Unset): Specifies a hint for the password.
        storage_consumption_limit (StorageConsumptionLimit | Unset):
    """

    key_vault_id: None | str | Unset = UNSET
    key_vault_key_uri: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    azure_account_id: None | str | Unset = UNSET
    concurrency_limit: int | None | Unset = UNSET
    enable_encryption: bool | Unset = UNSET
    password: None | str | Unset = UNSET
    hint: None | str | Unset = UNSET
    storage_consumption_limit: StorageConsumptionLimit | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        azure_account_id: None | str | Unset
        if isinstance(self.azure_account_id, Unset):
            azure_account_id = UNSET
        else:
            azure_account_id = self.azure_account_id

        concurrency_limit: int | None | Unset
        if isinstance(self.concurrency_limit, Unset):
            concurrency_limit = UNSET
        else:
            concurrency_limit = self.concurrency_limit

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

        field_dict.update({})
        if key_vault_id is not UNSET:
            field_dict["keyVaultId"] = key_vault_id
        if key_vault_key_uri is not UNSET:
            field_dict["keyVaultKeyUri"] = key_vault_key_uri
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if azure_account_id is not UNSET:
            field_dict["azureAccountId"] = azure_account_id
        if concurrency_limit is not UNSET:
            field_dict["concurrencyLimit"] = concurrency_limit
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

        def _parse_azure_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_account_id = _parse_azure_account_id(d.pop("azureAccountId", UNSET))

        def _parse_concurrency_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        concurrency_limit = _parse_concurrency_limit(d.pop("concurrencyLimit", UNSET))

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

        repository_update_from_client_with_key_vault = cls(
            key_vault_id=key_vault_id,
            key_vault_key_uri=key_vault_key_uri,
            name=name,
            description=description,
            azure_account_id=azure_account_id,
            concurrency_limit=concurrency_limit,
            enable_encryption=enable_encryption,
            password=password,
            hint=hint,
            storage_consumption_limit=storage_consumption_limit,
        )

        return repository_update_from_client_with_key_vault
