from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.job_status_nullable import JobStatusNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configuration_backup_schedule import ConfigurationBackupSchedule
    from ..models.repository_retention_settings import RepositoryRetentionSettings


T = TypeVar("T", bound="ConfigurationBackupSettings")


@_attrs_define
class ConfigurationBackupSettings:
    r"""
    Attributes:
        is_enabled (bool): Defines whether the configuration backup is enabled.
        schedule_options (ConfigurationBackupSchedule): Schedule for the backup policy.
        repository_id (None | Unset | UUID): System ID assigned in the Veeam backup for Microsoft Azure REST API to a
            backup repository where configuration backup files are stored.
        repository_name (None | str | Unset): Name of the repository.
        retention (RepositoryRetentionSettings | Unset): Specifies period of time to keep restore points in a backup
            chain.
        modified_by (None | str | Unset): Name of the user who last modified the configuration backup settings.
        modification_time_utc (datetime.datetime | None | Unset): Date and time when the configuration backup settings
            were last modified.
        last_backup_session_start_time_utc (datetime.datetime | None | Unset): Date and time when the last configuration
            backup session started.
        last_backup_restore_point_id (None | Unset | UUID): System ID assigned in the Veeam Backup for Microsoft Azure
            REST API to the restore point to which the last configuration backup was made.
        last_backup_session_status (JobStatusNullable | Unset): Specifies the status of the last configuration backup
            session.
        vbr_server_name (None | str | Unset): \[Applies if the backup appliance is managed by a Veeam Backup &
            Replication server] Name of the Veeam Backup & Replication server to which the backup appliance is connected.
        vbr_repository_name (None | str | Unset): \[Applies if the backup appliance is managed by a Veeam Backup &
            Replication server] Name of the repository where configuration backups must be stored.
        vbr_restore_point_count (int | None | Unset): \[Applies if the backup appliance is managed by a Veeam Backup &
            Replication server] Number of restore points created for the backup appliance.
    """

    is_enabled: bool
    schedule_options: ConfigurationBackupSchedule
    repository_id: None | Unset | UUID = UNSET
    repository_name: None | str | Unset = UNSET
    retention: RepositoryRetentionSettings | Unset = UNSET
    modified_by: None | str | Unset = UNSET
    modification_time_utc: datetime.datetime | None | Unset = UNSET
    last_backup_session_start_time_utc: datetime.datetime | None | Unset = UNSET
    last_backup_restore_point_id: None | Unset | UUID = UNSET
    last_backup_session_status: JobStatusNullable | Unset = UNSET
    vbr_server_name: None | str | Unset = UNSET
    vbr_repository_name: None | str | Unset = UNSET
    vbr_restore_point_count: int | None | Unset = UNSET

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

        repository_name: None | str | Unset
        if isinstance(self.repository_name, Unset):
            repository_name = UNSET
        else:
            repository_name = self.repository_name

        retention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention, Unset):
            retention = self.retention.to_dict()

        modified_by: None | str | Unset
        if isinstance(self.modified_by, Unset):
            modified_by = UNSET
        else:
            modified_by = self.modified_by

        modification_time_utc: None | str | Unset
        if isinstance(self.modification_time_utc, Unset):
            modification_time_utc = UNSET
        elif isinstance(self.modification_time_utc, datetime.datetime):
            modification_time_utc = self.modification_time_utc.isoformat()
        else:
            modification_time_utc = self.modification_time_utc

        last_backup_session_start_time_utc: None | str | Unset
        if isinstance(self.last_backup_session_start_time_utc, Unset):
            last_backup_session_start_time_utc = UNSET
        elif isinstance(self.last_backup_session_start_time_utc, datetime.datetime):
            last_backup_session_start_time_utc = self.last_backup_session_start_time_utc.isoformat()
        else:
            last_backup_session_start_time_utc = self.last_backup_session_start_time_utc

        last_backup_restore_point_id: None | str | Unset
        if isinstance(self.last_backup_restore_point_id, Unset):
            last_backup_restore_point_id = UNSET
        elif isinstance(self.last_backup_restore_point_id, UUID):
            last_backup_restore_point_id = str(self.last_backup_restore_point_id)
        else:
            last_backup_restore_point_id = self.last_backup_restore_point_id

        last_backup_session_status: str | Unset = UNSET
        if not isinstance(self.last_backup_session_status, Unset):
            last_backup_session_status = self.last_backup_session_status.value

        vbr_server_name: None | str | Unset
        if isinstance(self.vbr_server_name, Unset):
            vbr_server_name = UNSET
        else:
            vbr_server_name = self.vbr_server_name

        vbr_repository_name: None | str | Unset
        if isinstance(self.vbr_repository_name, Unset):
            vbr_repository_name = UNSET
        else:
            vbr_repository_name = self.vbr_repository_name

        vbr_restore_point_count: int | None | Unset
        if isinstance(self.vbr_restore_point_count, Unset):
            vbr_restore_point_count = UNSET
        else:
            vbr_restore_point_count = self.vbr_restore_point_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isEnabled": is_enabled,
                "scheduleOptions": schedule_options,
            }
        )
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if retention is not UNSET:
            field_dict["retention"] = retention
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if modification_time_utc is not UNSET:
            field_dict["modificationTimeUtc"] = modification_time_utc
        if last_backup_session_start_time_utc is not UNSET:
            field_dict["lastBackupSessionStartTimeUtc"] = last_backup_session_start_time_utc
        if last_backup_restore_point_id is not UNSET:
            field_dict["lastBackupRestorePointId"] = last_backup_restore_point_id
        if last_backup_session_status is not UNSET:
            field_dict["lastBackupSessionStatus"] = last_backup_session_status
        if vbr_server_name is not UNSET:
            field_dict["vbrServerName"] = vbr_server_name
        if vbr_repository_name is not UNSET:
            field_dict["vbrRepositoryName"] = vbr_repository_name
        if vbr_restore_point_count is not UNSET:
            field_dict["vbrRestorePointCount"] = vbr_restore_point_count

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

        def _parse_repository_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_name = _parse_repository_name(d.pop("repositoryName", UNSET))

        _retention = d.pop("retention", UNSET)
        retention: RepositoryRetentionSettings | Unset
        if isinstance(_retention, Unset):
            retention = UNSET
        else:
            retention = RepositoryRetentionSettings.from_dict(_retention)

        def _parse_modified_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        modified_by = _parse_modified_by(d.pop("modifiedBy", UNSET))

        def _parse_modification_time_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modification_time_utc_type_0 = isoparse(data)

                return modification_time_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        modification_time_utc = _parse_modification_time_utc(d.pop("modificationTimeUtc", UNSET))

        def _parse_last_backup_session_start_time_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_session_start_time_utc_type_0 = isoparse(data)

                return last_backup_session_start_time_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_backup_session_start_time_utc = _parse_last_backup_session_start_time_utc(
            d.pop("lastBackupSessionStartTimeUtc", UNSET)
        )

        def _parse_last_backup_restore_point_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_restore_point_id_type_0 = UUID(data)

                return last_backup_restore_point_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        last_backup_restore_point_id = _parse_last_backup_restore_point_id(d.pop("lastBackupRestorePointId", UNSET))

        _last_backup_session_status = d.pop("lastBackupSessionStatus", UNSET)
        last_backup_session_status: JobStatusNullable | Unset
        if isinstance(_last_backup_session_status, Unset):
            last_backup_session_status = UNSET
        else:
            last_backup_session_status = JobStatusNullable(_last_backup_session_status)

        def _parse_vbr_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vbr_server_name = _parse_vbr_server_name(d.pop("vbrServerName", UNSET))

        def _parse_vbr_repository_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vbr_repository_name = _parse_vbr_repository_name(d.pop("vbrRepositoryName", UNSET))

        def _parse_vbr_restore_point_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vbr_restore_point_count = _parse_vbr_restore_point_count(d.pop("vbrRestorePointCount", UNSET))

        configuration_backup_settings = cls(
            is_enabled=is_enabled,
            schedule_options=schedule_options,
            repository_id=repository_id,
            repository_name=repository_name,
            retention=retention,
            modified_by=modified_by,
            modification_time_utc=modification_time_utc,
            last_backup_session_start_time_utc=last_backup_session_start_time_utc,
            last_backup_restore_point_id=last_backup_restore_point_id,
            last_backup_session_status=last_backup_session_status,
            vbr_server_name=vbr_server_name,
            vbr_repository_name=vbr_repository_name,
            vbr_restore_point_count=vbr_restore_point_count,
        )

        return configuration_backup_settings
