from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configuration_backup_schedule import ConfigurationBackupSchedule
    from ..models.repository_retention_settings import RepositoryRetentionSettings


T = TypeVar("T", bound="ConfigurationBackupSettingsFromClient")


@_attrs_define
class ConfigurationBackupSettingsFromClient:
    """
    Attributes:
        is_enabled (bool): Defines whether the configuration backup is enabled.
        schedule_options (ConfigurationBackupSchedule): Schedule for the backup policy.
        repository_id (None | Unset | UUID): Specifies the system ID assigned in the Veeam backup for Microsoft Azure
            REST API to a backup repository where configuration backup files are stored.
        retention (RepositoryRetentionSettings | Unset): Specifies period of time to keep restore points in a backup
            chain.
    """

    is_enabled: bool
    schedule_options: ConfigurationBackupSchedule
    repository_id: None | Unset | UUID = UNSET
    retention: RepositoryRetentionSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        schedule_options = self.schedule_options.to_dict()

        repository_id: None | str | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        elif isinstance(self.repository_id, UUID):
            repository_id = str(self.repository_id)
        else:
            repository_id = self.repository_id

        retention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention, Unset):
            retention = self.retention.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isEnabled": is_enabled,
                "scheduleOptions": schedule_options,
            }
        )
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if retention is not UNSET:
            field_dict["retention"] = retention

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration_backup_schedule import ConfigurationBackupSchedule
        from ..models.repository_retention_settings import RepositoryRetentionSettings

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        schedule_options = ConfigurationBackupSchedule.from_dict(d.pop("scheduleOptions"))

        def _parse_repository_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_id_type_0 = UUID(data)

                return repository_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        repository_id = _parse_repository_id(d.pop("repositoryId", UNSET))

        _retention = d.pop("retention", UNSET)
        retention: RepositoryRetentionSettings | Unset
        if isinstance(_retention, Unset):
            retention = UNSET
        else:
            retention = RepositoryRetentionSettings.from_dict(_retention)

        configuration_backup_settings_from_client = cls(
            is_enabled=is_enabled,
            schedule_options=schedule_options,
            repository_id=repository_id,
            retention=retention,
        )

        return configuration_backup_settings_from_client
