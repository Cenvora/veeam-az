from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archive_repository_configuration_from_client import ArchiveRepositoryConfigurationFromClient
    from ..models.backup_repository_configuration_from_client import BackupRepositoryConfigurationFromClient


T = TypeVar("T", bound="StorageTemplateConfigurationFromClient")


@_attrs_define
class StorageTemplateConfigurationFromClient:
    """Specifies the storage template configuration.

    Attributes:
        backup_repository (BackupRepositoryConfigurationFromClient | Unset): Specifies target locations where backups
            will be stored.
        archive_repository (ArchiveRepositoryConfigurationFromClient | Unset): Specifies target locations where archived
            backups will be stored.
    """

    backup_repository: BackupRepositoryConfigurationFromClient | Unset = UNSET
    archive_repository: ArchiveRepositoryConfigurationFromClient | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_repository, Unset):
            backup_repository = self.backup_repository.to_dict()

        archive_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.archive_repository, Unset):
            archive_repository = self.archive_repository.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_repository is not UNSET:
            field_dict["backupRepository"] = backup_repository
        if archive_repository is not UNSET:
            field_dict["archiveRepository"] = archive_repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.archive_repository_configuration_from_client import ArchiveRepositoryConfigurationFromClient
        from ..models.backup_repository_configuration_from_client import BackupRepositoryConfigurationFromClient

        d = dict(src_dict)
        _backup_repository = d.pop("backupRepository", UNSET)
        backup_repository: BackupRepositoryConfigurationFromClient | Unset
        if isinstance(_backup_repository, Unset):
            backup_repository = UNSET
        else:
            backup_repository = BackupRepositoryConfigurationFromClient.from_dict(_backup_repository)

        _archive_repository = d.pop("archiveRepository", UNSET)
        archive_repository: ArchiveRepositoryConfigurationFromClient | Unset
        if isinstance(_archive_repository, Unset):
            archive_repository = UNSET
        else:
            archive_repository = ArchiveRepositoryConfigurationFromClient.from_dict(_archive_repository)

        storage_template_configuration_from_client = cls(
            backup_repository=backup_repository,
            archive_repository=archive_repository,
        )

        storage_template_configuration_from_client.additional_properties = d
        return storage_template_configuration_from_client

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
