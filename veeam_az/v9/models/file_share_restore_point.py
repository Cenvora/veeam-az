from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.file_share_backup_destination import FileShareBackupDestination
from ..models.repository_restore_point_state import RepositoryRestorePointState
from ..models.restore_point_type import RestorePointType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="FileShareRestorePoint")


@_attrs_define
class FileShareRestorePoint:
    """
    Attributes:
        id (UUID | Unset): System ID assigned to a restore point in the Veeam Backup for Microsoft Azure REST API.
        type_ (RestorePointType | Unset): Type of the restore point.
        indexed (bool | None | Unset): Defines whether the Azure file share for which the restore point was created is
            indexed.
        file_share_id (None | str | Unset): System ID assigned to the file share in the Veeam Backup for Microsoft Azure
            REST API.
        file_share_name (None | str | Unset): Name of the file share.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region where the restore point resides.
        region_name (None | str | Unset): Name of the region.
        point_in_time (datetime.datetime | Unset): Date and time when the restore point was created.
        gfs_flags (str | Unset): Retention period configured for the restore point.
        state (RepositoryRestorePointState | Unset):
        job_session_id (None | str | Unset): System ID assigned to the session in the Veeam Backup for Microsoft Azure
            REST API.
        backup_destination (FileShareBackupDestination | Unset): Type of the backup destination.
        size_in_bytes (int | Unset): Size of the restore point file (in bytes).
        is_corrupted (bool | None | Unset): Defines whether the restore point was corrupted.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: UUID | Unset = UNSET
    type_: RestorePointType | Unset = UNSET
    indexed: bool | None | Unset = UNSET
    file_share_id: None | str | Unset = UNSET
    file_share_name: None | str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    point_in_time: datetime.datetime | Unset = UNSET
    gfs_flags: str | Unset = UNSET
    state: RepositoryRestorePointState | Unset = UNSET
    job_session_id: None | str | Unset = UNSET
    backup_destination: FileShareBackupDestination | Unset = UNSET
    size_in_bytes: int | Unset = UNSET
    is_corrupted: bool | None | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        indexed: bool | None | Unset
        if isinstance(self.indexed, Unset):
            indexed = UNSET
        else:
            indexed = self.indexed

        file_share_id: None | str | Unset
        if isinstance(self.file_share_id, Unset):
            file_share_id = UNSET
        else:
            file_share_id = self.file_share_id

        file_share_name: None | str | Unset
        if isinstance(self.file_share_name, Unset):
            file_share_name = UNSET
        else:
            file_share_name = self.file_share_name

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

        point_in_time: str | Unset = UNSET
        if not isinstance(self.point_in_time, Unset):
            point_in_time = self.point_in_time.isoformat()

        gfs_flags = self.gfs_flags

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        job_session_id: None | str | Unset
        if isinstance(self.job_session_id, Unset):
            job_session_id = UNSET
        else:
            job_session_id = self.job_session_id

        backup_destination: str | Unset = UNSET
        if not isinstance(self.backup_destination, Unset):
            backup_destination = self.backup_destination.value

        size_in_bytes = self.size_in_bytes

        is_corrupted: bool | None | Unset
        if isinstance(self.is_corrupted, Unset):
            is_corrupted = UNSET
        else:
            is_corrupted = self.is_corrupted

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if indexed is not UNSET:
            field_dict["indexed"] = indexed
        if file_share_id is not UNSET:
            field_dict["fileShareId"] = file_share_id
        if file_share_name is not UNSET:
            field_dict["fileShareName"] = file_share_name
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if point_in_time is not UNSET:
            field_dict["pointInTime"] = point_in_time
        if gfs_flags is not UNSET:
            field_dict["gfsFlags"] = gfs_flags
        if state is not UNSET:
            field_dict["state"] = state
        if job_session_id is not UNSET:
            field_dict["jobSessionId"] = job_session_id
        if backup_destination is not UNSET:
            field_dict["backupDestination"] = backup_destination
        if size_in_bytes is not UNSET:
            field_dict["sizeInBytes"] = size_in_bytes
        if is_corrupted is not UNSET:
            field_dict["isCorrupted"] = is_corrupted
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _type_ = d.pop("type", UNSET)
        type_: RestorePointType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestorePointType(_type_)

        def _parse_indexed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        indexed = _parse_indexed(d.pop("indexed", UNSET))

        def _parse_file_share_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_share_id = _parse_file_share_id(d.pop("fileShareId", UNSET))

        def _parse_file_share_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_share_name = _parse_file_share_name(d.pop("fileShareName", UNSET))

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

        _point_in_time = d.pop("pointInTime", UNSET)
        point_in_time: datetime.datetime | Unset
        if isinstance(_point_in_time, Unset):
            point_in_time = UNSET
        else:
            point_in_time = isoparse(_point_in_time)

        gfs_flags = d.pop("gfsFlags", UNSET)

        _state = d.pop("state", UNSET)
        state: RepositoryRestorePointState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RepositoryRestorePointState(_state)

        def _parse_job_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_session_id = _parse_job_session_id(d.pop("jobSessionId", UNSET))

        _backup_destination = d.pop("backupDestination", UNSET)
        backup_destination: FileShareBackupDestination | Unset
        if isinstance(_backup_destination, Unset):
            backup_destination = UNSET
        else:
            backup_destination = FileShareBackupDestination(_backup_destination)

        size_in_bytes = d.pop("sizeInBytes", UNSET)

        def _parse_is_corrupted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_corrupted = _parse_is_corrupted(d.pop("isCorrupted", UNSET))

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

        file_share_restore_point = cls(
            id=id,
            type_=type_,
            indexed=indexed,
            file_share_id=file_share_id,
            file_share_name=file_share_name,
            region_id=region_id,
            region_name=region_name,
            point_in_time=point_in_time,
            gfs_flags=gfs_flags,
            state=state,
            job_session_id=job_session_id,
            backup_destination=backup_destination,
            size_in_bytes=size_in_bytes,
            is_corrupted=is_corrupted,
            field_links=field_links,
        )

        return file_share_restore_point
