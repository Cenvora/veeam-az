from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.job_session_type import JobSessionType
from ..models.job_status import JobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_job_info import BackupJobInfo
    from ..models.file_level_restore_job_info import FileLevelRestoreJobInfo
    from ..models.file_share_file_level_restore_job_info import FileShareFileLevelRestoreJobInfo
    from ..models.health_check_job_info import HealthCheckJobInfo
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.repository_job_info import RepositoryJobInfo
    from ..models.restore_job_info import RestoreJobInfo
    from ..models.restore_point_data_retrieval_job_info import RestorePointDataRetrievalJobInfo
    from ..models.retention_job_info import RetentionJobInfo


T = TypeVar("T", bound="JobSession")


@_attrs_define
class JobSession:
    r"""
    Attributes:
        status (JobStatus): Specifies the status of the performed session.
        id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the session.
        type_ (JobSessionType | Unset): Type of the session.
        localized_type (None | str | Unset): Type of the session displayed in the Veeam Backup for Microsoft Azure UI.
        execution_start_time (datetime.datetime | None | Unset): Date and time when the session will run.
        execution_stop_time (datetime.datetime | None | Unset): Date and time when the session will stop.
        execution_duration (None | str | Unset): The duration of the session.
        backup_job_info (BackupJobInfo | Unset): Information on a backup policy.
        health_check_job_info (HealthCheckJobInfo | Unset): \[Applies only if backup creation is enabled for the backup
            policy] Health check schedule settings configured for the backup policy.
        restore_job_info (RestoreJobInfo | Unset): \[Applies only if restore operation is performed for the backup
            policy] Restore settings configured for the backup policy.
        file_level_restore_job_info (FileLevelRestoreJobInfo | Unset): \[Applies only if file-level restore operation is
            performed for the backup policy] File-level restore settings configured for the backup policy.
        file_share_file_level_restore_job_info (FileShareFileLevelRestoreJobInfo | Unset): \[Applies only if restore
            operation is performed for the backup policy] File-level restore settings of a file share configured for the
            backup policy.
        repository_job_info (RepositoryJobInfo | Unset): \[Applies only if backup creation is enabled for the backup
            policy] Information on a backup repository added to the policy.
        restore_point_data_retrieval_job_info (RestorePointDataRetrievalJobInfo | Unset): Information on retrieved
            restore points.
        retention_job_info (RetentionJobInfo | Unset): Information on the removed restore points.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    status: JobStatus
    id: None | str | Unset = UNSET
    type_: JobSessionType | Unset = UNSET
    localized_type: None | str | Unset = UNSET
    execution_start_time: datetime.datetime | None | Unset = UNSET
    execution_stop_time: datetime.datetime | None | Unset = UNSET
    execution_duration: None | str | Unset = UNSET
    backup_job_info: BackupJobInfo | Unset = UNSET
    health_check_job_info: HealthCheckJobInfo | Unset = UNSET
    restore_job_info: RestoreJobInfo | Unset = UNSET
    file_level_restore_job_info: FileLevelRestoreJobInfo | Unset = UNSET
    file_share_file_level_restore_job_info: FileShareFileLevelRestoreJobInfo | Unset = UNSET
    repository_job_info: RepositoryJobInfo | Unset = UNSET
    restore_point_data_retrieval_job_info: RestorePointDataRetrievalJobInfo | Unset = UNSET
    retention_job_info: RetentionJobInfo | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        status = self.status.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        localized_type: None | str | Unset
        if isinstance(self.localized_type, Unset):
            localized_type = UNSET
        else:
            localized_type = self.localized_type

        execution_start_time: None | str | Unset
        if isinstance(self.execution_start_time, Unset):
            execution_start_time = UNSET
        elif isinstance(self.execution_start_time, datetime.datetime):
            execution_start_time = self.execution_start_time.isoformat()
        else:
            execution_start_time = self.execution_start_time

        execution_stop_time: None | str | Unset
        if isinstance(self.execution_stop_time, Unset):
            execution_stop_time = UNSET
        elif isinstance(self.execution_stop_time, datetime.datetime):
            execution_stop_time = self.execution_stop_time.isoformat()
        else:
            execution_stop_time = self.execution_stop_time

        execution_duration: None | str | Unset
        if isinstance(self.execution_duration, Unset):
            execution_duration = UNSET
        else:
            execution_duration = self.execution_duration

        backup_job_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_job_info, Unset):
            backup_job_info = self.backup_job_info.to_dict()

        health_check_job_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.health_check_job_info, Unset):
            health_check_job_info = self.health_check_job_info.to_dict()

        restore_job_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restore_job_info, Unset):
            restore_job_info = self.restore_job_info.to_dict()

        file_level_restore_job_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_level_restore_job_info, Unset):
            file_level_restore_job_info = self.file_level_restore_job_info.to_dict()

        file_share_file_level_restore_job_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_share_file_level_restore_job_info, Unset):
            file_share_file_level_restore_job_info = self.file_share_file_level_restore_job_info.to_dict()

        repository_job_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository_job_info, Unset):
            repository_job_info = self.repository_job_info.to_dict()

        restore_point_data_retrieval_job_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restore_point_data_retrieval_job_info, Unset):
            restore_point_data_retrieval_job_info = self.restore_point_data_retrieval_job_info.to_dict()

        retention_job_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention_job_info, Unset):
            retention_job_info = self.retention_job_info.to_dict()

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
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if localized_type is not UNSET:
            field_dict["localizedType"] = localized_type
        if execution_start_time is not UNSET:
            field_dict["executionStartTime"] = execution_start_time
        if execution_stop_time is not UNSET:
            field_dict["executionStopTime"] = execution_stop_time
        if execution_duration is not UNSET:
            field_dict["executionDuration"] = execution_duration
        if backup_job_info is not UNSET:
            field_dict["backupJobInfo"] = backup_job_info
        if health_check_job_info is not UNSET:
            field_dict["healthCheckJobInfo"] = health_check_job_info
        if restore_job_info is not UNSET:
            field_dict["restoreJobInfo"] = restore_job_info
        if file_level_restore_job_info is not UNSET:
            field_dict["fileLevelRestoreJobInfo"] = file_level_restore_job_info
        if file_share_file_level_restore_job_info is not UNSET:
            field_dict["fileShareFileLevelRestoreJobInfo"] = file_share_file_level_restore_job_info
        if repository_job_info is not UNSET:
            field_dict["repositoryJobInfo"] = repository_job_info
        if restore_point_data_retrieval_job_info is not UNSET:
            field_dict["restorePointDataRetrievalJobInfo"] = restore_point_data_retrieval_job_info
        if retention_job_info is not UNSET:
            field_dict["retentionJobInfo"] = retention_job_info
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_job_info import BackupJobInfo
        from ..models.file_level_restore_job_info import FileLevelRestoreJobInfo
        from ..models.file_share_file_level_restore_job_info import FileShareFileLevelRestoreJobInfo
        from ..models.health_check_job_info import HealthCheckJobInfo
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.repository_job_info import RepositoryJobInfo
        from ..models.restore_job_info import RestoreJobInfo
        from ..models.restore_point_data_retrieval_job_info import RestorePointDataRetrievalJobInfo
        from ..models.retention_job_info import RetentionJobInfo

        d = dict(src_dict)
        status = JobStatus(d.pop("status"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: JobSessionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = JobSessionType(_type_)

        def _parse_localized_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        localized_type = _parse_localized_type(d.pop("localizedType", UNSET))

        def _parse_execution_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_start_time_type_0 = isoparse(data)

                return execution_start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        execution_start_time = _parse_execution_start_time(d.pop("executionStartTime", UNSET))

        def _parse_execution_stop_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_stop_time_type_0 = isoparse(data)

                return execution_stop_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        execution_stop_time = _parse_execution_stop_time(d.pop("executionStopTime", UNSET))

        def _parse_execution_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        execution_duration = _parse_execution_duration(d.pop("executionDuration", UNSET))

        _backup_job_info = d.pop("backupJobInfo", UNSET)
        backup_job_info: BackupJobInfo | Unset
        if isinstance(_backup_job_info, Unset):
            backup_job_info = UNSET
        else:
            backup_job_info = BackupJobInfo.from_dict(_backup_job_info)

        _health_check_job_info = d.pop("healthCheckJobInfo", UNSET)
        health_check_job_info: HealthCheckJobInfo | Unset
        if isinstance(_health_check_job_info, Unset):
            health_check_job_info = UNSET
        else:
            health_check_job_info = HealthCheckJobInfo.from_dict(_health_check_job_info)

        _restore_job_info = d.pop("restoreJobInfo", UNSET)
        restore_job_info: RestoreJobInfo | Unset
        if isinstance(_restore_job_info, Unset):
            restore_job_info = UNSET
        else:
            restore_job_info = RestoreJobInfo.from_dict(_restore_job_info)

        _file_level_restore_job_info = d.pop("fileLevelRestoreJobInfo", UNSET)
        file_level_restore_job_info: FileLevelRestoreJobInfo | Unset
        if isinstance(_file_level_restore_job_info, Unset):
            file_level_restore_job_info = UNSET
        else:
            file_level_restore_job_info = FileLevelRestoreJobInfo.from_dict(_file_level_restore_job_info)

        _file_share_file_level_restore_job_info = d.pop("fileShareFileLevelRestoreJobInfo", UNSET)
        file_share_file_level_restore_job_info: FileShareFileLevelRestoreJobInfo | Unset
        if isinstance(_file_share_file_level_restore_job_info, Unset):
            file_share_file_level_restore_job_info = UNSET
        else:
            file_share_file_level_restore_job_info = FileShareFileLevelRestoreJobInfo.from_dict(
                _file_share_file_level_restore_job_info
            )

        _repository_job_info = d.pop("repositoryJobInfo", UNSET)
        repository_job_info: RepositoryJobInfo | Unset
        if isinstance(_repository_job_info, Unset):
            repository_job_info = UNSET
        else:
            repository_job_info = RepositoryJobInfo.from_dict(_repository_job_info)

        _restore_point_data_retrieval_job_info = d.pop("restorePointDataRetrievalJobInfo", UNSET)
        restore_point_data_retrieval_job_info: RestorePointDataRetrievalJobInfo | Unset
        if isinstance(_restore_point_data_retrieval_job_info, Unset):
            restore_point_data_retrieval_job_info = UNSET
        else:
            restore_point_data_retrieval_job_info = RestorePointDataRetrievalJobInfo.from_dict(
                _restore_point_data_retrieval_job_info
            )

        _retention_job_info = d.pop("retentionJobInfo", UNSET)
        retention_job_info: RetentionJobInfo | Unset
        if isinstance(_retention_job_info, Unset):
            retention_job_info = UNSET
        else:
            retention_job_info = RetentionJobInfo.from_dict(_retention_job_info)

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

        job_session = cls(
            status=status,
            id=id,
            type_=type_,
            localized_type=localized_type,
            execution_start_time=execution_start_time,
            execution_stop_time=execution_stop_time,
            execution_duration=execution_duration,
            backup_job_info=backup_job_info,
            health_check_job_info=health_check_job_info,
            restore_job_info=restore_job_info,
            file_level_restore_job_info=file_level_restore_job_info,
            file_share_file_level_restore_job_info=file_share_file_level_restore_job_info,
            repository_job_info=repository_job_info,
            restore_point_data_retrieval_job_info=restore_point_data_retrieval_job_info,
            retention_job_info=retention_job_info,
            field_links=field_links,
        )

        return job_session
