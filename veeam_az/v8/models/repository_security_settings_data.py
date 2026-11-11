from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.immutability_state import ImmutabilityState
from ..models.repository_encryption_method import RepositoryEncryptionMethod
from ..models.storage_tier_nullable import StorageTierNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositorySecuritySettingsData")


@_attrs_define
class RepositorySecuritySettingsData:
    """Information on the security settings of each repository.

    Attributes:
        repository_exists (bool | Unset): Defines whether the backup repository exists.
        storage_tier (StorageTierNullable | Unset): Specifies the access tier.
        is_encrypted (bool | Unset): Defines whether encryption is enabled for backup files stored in the repository.
        encryption_method (RepositoryEncryptionMethod | Unset): Method used for repository encryption.
        hint (None | str | Unset): Hint to the repository password.
        key_vault_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to a Key
            Vault where a cryptographic key used for repository encryption resides.
        key_name (None | str | Unset): Name of the cryptographic key.
        key_uri (None | str | Unset): URI of the cryptographic key.
        key_vault_name (None | str | Unset): Name of the Key Vault where the cryptographic key used for repository
            encryption resides.
        key_version (None | str | Unset): Current version of the cryptographic key.
        immutability (ImmutabilityState | Unset): Defines whether backups stored in the repository are immutable.
    """

    repository_exists: bool | Unset = UNSET
    storage_tier: StorageTierNullable | Unset = UNSET
    is_encrypted: bool | Unset = UNSET
    encryption_method: RepositoryEncryptionMethod | Unset = UNSET
    hint: None | str | Unset = UNSET
    key_vault_id: None | str | Unset = UNSET
    key_name: None | str | Unset = UNSET
    key_uri: None | str | Unset = UNSET
    key_vault_name: None | str | Unset = UNSET
    key_version: None | str | Unset = UNSET
    immutability: ImmutabilityState | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        repository_exists = self.repository_exists

        storage_tier: str | Unset = UNSET
        if not isinstance(self.storage_tier, Unset):
            storage_tier = self.storage_tier.value

        is_encrypted = self.is_encrypted

        encryption_method: str | Unset = UNSET
        if not isinstance(self.encryption_method, Unset):
            encryption_method = self.encryption_method.value

        hint: None | str | Unset
        if isinstance(self.hint, Unset):
            hint = UNSET
        else:
            hint = self.hint

        key_vault_id: None | str | Unset
        if isinstance(self.key_vault_id, Unset):
            key_vault_id = UNSET
        else:
            key_vault_id = self.key_vault_id

        key_name: None | str | Unset
        if isinstance(self.key_name, Unset):
            key_name = UNSET
        else:
            key_name = self.key_name

        key_uri: None | str | Unset
        if isinstance(self.key_uri, Unset):
            key_uri = UNSET
        else:
            key_uri = self.key_uri

        key_vault_name: None | str | Unset
        if isinstance(self.key_vault_name, Unset):
            key_vault_name = UNSET
        else:
            key_vault_name = self.key_vault_name

        key_version: None | str | Unset
        if isinstance(self.key_version, Unset):
            key_version = UNSET
        else:
            key_version = self.key_version

        immutability: str | Unset = UNSET
        if not isinstance(self.immutability, Unset):
            immutability = self.immutability.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository_exists is not UNSET:
            field_dict["repositoryExists"] = repository_exists
        if storage_tier is not UNSET:
            field_dict["storageTier"] = storage_tier
        if is_encrypted is not UNSET:
            field_dict["isEncrypted"] = is_encrypted
        if encryption_method is not UNSET:
            field_dict["encryptionMethod"] = encryption_method
        if hint is not UNSET:
            field_dict["hint"] = hint
        if key_vault_id is not UNSET:
            field_dict["keyVaultId"] = key_vault_id
        if key_name is not UNSET:
            field_dict["keyName"] = key_name
        if key_uri is not UNSET:
            field_dict["keyUri"] = key_uri
        if key_vault_name is not UNSET:
            field_dict["keyVaultName"] = key_vault_name
        if key_version is not UNSET:
            field_dict["keyVersion"] = key_version
        if immutability is not UNSET:
            field_dict["immutability"] = immutability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository_exists = d.pop("repositoryExists", UNSET)

        _storage_tier = d.pop("storageTier", UNSET)
        storage_tier: StorageTierNullable | Unset
        if isinstance(_storage_tier, Unset):
            storage_tier = UNSET
        else:
            storage_tier = StorageTierNullable(_storage_tier)

        is_encrypted = d.pop("isEncrypted", UNSET)

        _encryption_method = d.pop("encryptionMethod", UNSET)
        encryption_method: RepositoryEncryptionMethod | Unset
        if isinstance(_encryption_method, Unset):
            encryption_method = UNSET
        else:
            encryption_method = RepositoryEncryptionMethod(_encryption_method)

        def _parse_hint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hint = _parse_hint(d.pop("hint", UNSET))

        def _parse_key_vault_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_vault_id = _parse_key_vault_id(d.pop("keyVaultId", UNSET))

        def _parse_key_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_name = _parse_key_name(d.pop("keyName", UNSET))

        def _parse_key_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_uri = _parse_key_uri(d.pop("keyUri", UNSET))

        def _parse_key_vault_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_vault_name = _parse_key_vault_name(d.pop("keyVaultName", UNSET))

        def _parse_key_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_version = _parse_key_version(d.pop("keyVersion", UNSET))

        _immutability = d.pop("immutability", UNSET)
        immutability: ImmutabilityState | Unset
        if isinstance(_immutability, Unset):
            immutability = UNSET
        else:
            immutability = ImmutabilityState(_immutability)

        repository_security_settings_data = cls(
            repository_exists=repository_exists,
            storage_tier=storage_tier,
            is_encrypted=is_encrypted,
            encryption_method=encryption_method,
            hint=hint,
            key_vault_id=key_vault_id,
            key_name=key_name,
            key_uri=key_uri,
            key_vault_name=key_vault_name,
            key_version=key_version,
            immutability=immutability,
        )

        return repository_security_settings_data
