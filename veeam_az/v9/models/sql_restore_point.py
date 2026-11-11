from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.data_retrieval_status import DataRetrievalStatus
from ..models.repository_restore_point_state import RepositoryRestorePointState
from ..models.restore_point_type import RestorePointType
from ..models.sql_backup_destination import SqlBackupDestination
from ..models.storage_access_tier import StorageAccessTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="SqlRestorePoint")


@_attrs_define
class SqlRestorePoint:
    r"""
    Attributes:
        id (UUID | Unset): System ID assigned to the restore point in the Veeam Backup for Microsoft Azure REST API.
        type_ (RestorePointType | Unset): Type of the restore point.
        database_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to an
            Azure SQL database the restore point belongs to.
        database_name (None | str | Unset): Name of an Azure SQL database the restore point belongs to.
        sql_server_id (str | Unset): Microsoft Azure ID assigned to a SQL server on which the database is hosted.
        sql_server_name (str | Unset): Name of the SQL server.
        vbr_id (None | str | Unset): System ID assigned to a restore point in Veeam Backup & Replication.
        point_in_time (datetime.datetime | Unset): Date and time when the restore point was created.
        backup_size_bytes (int | Unset): Size of the restore point file (in bytes).
        is_corrupted (bool | None | Unset): Defines whether the restore point is corrupted. Note that the corrupted
            restore points cannot be used for restore operations.
        gfs_flags (str | Unset): Retention period configured for the restore point.
        job_session_id (None | str | Unset): System ID assigned to the backup session in the Veeam Backup for Microsoft
            Azure REST API.
        backup_destination (SqlBackupDestination | Unset): Type of the backup destination.
        state (RepositoryRestorePointState | Unset):
        data_retrieval_status (DataRetrievalStatus | Unset): State of the data retrieval process.
        retrieved_data_expiration_date (datetime.datetime | None | Unset): Date and time when the retrieval period
            exceeds.
        notify_before_retrieved_data_expiration_hours (int | None | Unset): \[Applies if a user wants to be notified
            when data availability period is about to expire] Time when a notification will be sent (in hours remaining
            until the expiration).
        immutable_till (datetime.datetime | None | Unset): Date and time when immutability will be automatically
            disabled for the restore point.
        access_tier (StorageAccessTier | Unset): Specifies an access tier of a repository that stores restore points.
        latest_chain_size_bytes (int | None | Unset): Size of the latest backup in an incremental backup chain.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: UUID | Unset = UNSET
    type_: RestorePointType | Unset = UNSET
    database_id: None | str | Unset = UNSET
    database_name: None | str | Unset = UNSET
    sql_server_id: str | Unset = UNSET
    sql_server_name: str | Unset = UNSET
    vbr_id: None | str | Unset = UNSET
    point_in_time: datetime.datetime | Unset = UNSET
    backup_size_bytes: int | Unset = UNSET
    is_corrupted: bool | None | Unset = UNSET
    gfs_flags: str | Unset = UNSET
    job_session_id: None | str | Unset = UNSET
    backup_destination: SqlBackupDestination | Unset = UNSET
    state: RepositoryRestorePointState | Unset = UNSET
    data_retrieval_status: DataRetrievalStatus | Unset = UNSET
    retrieved_data_expiration_date: datetime.datetime | None | Unset = UNSET
    notify_before_retrieved_data_expiration_hours: int | None | Unset = UNSET
    immutable_till: datetime.datetime | None | Unset = UNSET
    access_tier: StorageAccessTier | Unset = UNSET
    latest_chain_size_bytes: int | None | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        database_id: None | str | Unset
        if isinstance(self.database_id, Unset):
            database_id = UNSET
        else:
            database_id = self.database_id

        database_name: None | str | Unset
        if isinstance(self.database_name, Unset):
            database_name = UNSET
        else:
            database_name = self.database_name

        sql_server_id = self.sql_server_id

        sql_server_name = self.sql_server_name

        vbr_id: None | str | Unset
        if isinstance(self.vbr_id, Unset):
            vbr_id = UNSET
        else:
            vbr_id = self.vbr_id

        point_in_time: str | Unset = UNSET
        if not isinstance(self.point_in_time, Unset):
            point_in_time = self.point_in_time.isoformat()

        backup_size_bytes = self.backup_size_bytes

        is_corrupted: bool | None | Unset
        if isinstance(self.is_corrupted, Unset):
            is_corrupted = UNSET
        else:
            is_corrupted = self.is_corrupted

        gfs_flags = self.gfs_flags

        job_session_id: None | str | Unset
        if isinstance(self.job_session_id, Unset):
            job_session_id = UNSET
        else:
            job_session_id = self.job_session_id

        backup_destination: str | Unset = UNSET
        if not isinstance(self.backup_destination, Unset):
            backup_destination = self.backup_destination.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        data_retrieval_status: str | Unset = UNSET
        if not isinstance(self.data_retrieval_status, Unset):
            data_retrieval_status = self.data_retrieval_status.value

        retrieved_data_expiration_date: None | str | Unset
        if isinstance(self.retrieved_data_expiration_date, Unset):
            retrieved_data_expiration_date = UNSET
        elif isinstance(self.retrieved_data_expiration_date, datetime.datetime):
            retrieved_data_expiration_date = self.retrieved_data_expiration_date.isoformat()
        else:
            retrieved_data_expiration_date = self.retrieved_data_expiration_date

        notify_before_retrieved_data_expiration_hours: int | None | Unset
        if isinstance(self.notify_before_retrieved_data_expiration_hours, Unset):
            notify_before_retrieved_data_expiration_hours = UNSET
        else:
            notify_before_retrieved_data_expiration_hours = self.notify_before_retrieved_data_expiration_hours

        immutable_till: None | str | Unset
        if isinstance(self.immutable_till, Unset):
            immutable_till = UNSET
        elif isinstance(self.immutable_till, datetime.datetime):
            immutable_till = self.immutable_till.isoformat()
        else:
            immutable_till = self.immutable_till

        access_tier: str | Unset = UNSET
        if not isinstance(self.access_tier, Unset):
            access_tier = self.access_tier.value

        latest_chain_size_bytes: int | None | Unset
        if isinstance(self.latest_chain_size_bytes, Unset):
            latest_chain_size_bytes = UNSET
        else:
            latest_chain_size_bytes = self.latest_chain_size_bytes

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
        if database_id is not UNSET:
            field_dict["databaseId"] = database_id
        if database_name is not UNSET:
            field_dict["databaseName"] = database_name
        if sql_server_id is not UNSET:
            field_dict["sqlServerId"] = sql_server_id
        if sql_server_name is not UNSET:
            field_dict["sqlServerName"] = sql_server_name
        if vbr_id is not UNSET:
            field_dict["vbrId"] = vbr_id
        if point_in_time is not UNSET:
            field_dict["pointInTime"] = point_in_time
        if backup_size_bytes is not UNSET:
            field_dict["backupSizeBytes"] = backup_size_bytes
        if is_corrupted is not UNSET:
            field_dict["isCorrupted"] = is_corrupted
        if gfs_flags is not UNSET:
            field_dict["gfsFlags"] = gfs_flags
        if job_session_id is not UNSET:
            field_dict["jobSessionId"] = job_session_id
        if backup_destination is not UNSET:
            field_dict["backupDestination"] = backup_destination
        if state is not UNSET:
            field_dict["state"] = state
        if data_retrieval_status is not UNSET:
            field_dict["dataRetrievalStatus"] = data_retrieval_status
        if retrieved_data_expiration_date is not UNSET:
            field_dict["retrievedDataExpirationDate"] = retrieved_data_expiration_date
        if notify_before_retrieved_data_expiration_hours is not UNSET:
            field_dict["notifyBeforeRetrievedDataExpirationHours"] = notify_before_retrieved_data_expiration_hours
        if immutable_till is not UNSET:
            field_dict["immutableTill"] = immutable_till
        if access_tier is not UNSET:
            field_dict["accessTier"] = access_tier
        if latest_chain_size_bytes is not UNSET:
            field_dict["latestChainSizeBytes"] = latest_chain_size_bytes
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

        def _parse_database_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        database_id = _parse_database_id(d.pop("databaseId", UNSET))

        def _parse_database_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        database_name = _parse_database_name(d.pop("databaseName", UNSET))

        sql_server_id = d.pop("sqlServerId", UNSET)

        sql_server_name = d.pop("sqlServerName", UNSET)

        def _parse_vbr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vbr_id = _parse_vbr_id(d.pop("vbrId", UNSET))

        _point_in_time = d.pop("pointInTime", UNSET)
        point_in_time: datetime.datetime | Unset
        if isinstance(_point_in_time, Unset):
            point_in_time = UNSET
        else:
            point_in_time = isoparse(_point_in_time)

        backup_size_bytes = d.pop("backupSizeBytes", UNSET)

        def _parse_is_corrupted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_corrupted = _parse_is_corrupted(d.pop("isCorrupted", UNSET))

        gfs_flags = d.pop("gfsFlags", UNSET)

        def _parse_job_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_session_id = _parse_job_session_id(d.pop("jobSessionId", UNSET))

        _backup_destination = d.pop("backupDestination", UNSET)
        backup_destination: SqlBackupDestination | Unset
        if isinstance(_backup_destination, Unset):
            backup_destination = UNSET
        else:
            backup_destination = SqlBackupDestination(_backup_destination)

        _state = d.pop("state", UNSET)
        state: RepositoryRestorePointState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RepositoryRestorePointState(_state)

        _data_retrieval_status = d.pop("dataRetrievalStatus", UNSET)
        data_retrieval_status: DataRetrievalStatus | Unset
        if isinstance(_data_retrieval_status, Unset):
            data_retrieval_status = UNSET
        else:
            data_retrieval_status = DataRetrievalStatus(_data_retrieval_status)

        def _parse_retrieved_data_expiration_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retrieved_data_expiration_date_type_0 = isoparse(data)

                return retrieved_data_expiration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        retrieved_data_expiration_date = _parse_retrieved_data_expiration_date(
            d.pop("retrievedDataExpirationDate", UNSET)
        )

        def _parse_notify_before_retrieved_data_expiration_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        notify_before_retrieved_data_expiration_hours = _parse_notify_before_retrieved_data_expiration_hours(
            d.pop("notifyBeforeRetrievedDataExpirationHours", UNSET)
        )

        def _parse_immutable_till(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                immutable_till_type_0 = isoparse(data)

                return immutable_till_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        immutable_till = _parse_immutable_till(d.pop("immutableTill", UNSET))

        _access_tier = d.pop("accessTier", UNSET)
        access_tier: StorageAccessTier | Unset
        if isinstance(_access_tier, Unset):
            access_tier = UNSET
        else:
            access_tier = StorageAccessTier(_access_tier)

        def _parse_latest_chain_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest_chain_size_bytes = _parse_latest_chain_size_bytes(d.pop("latestChainSizeBytes", UNSET))

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

        sql_restore_point = cls(
            id=id,
            type_=type_,
            database_id=database_id,
            database_name=database_name,
            sql_server_id=sql_server_id,
            sql_server_name=sql_server_name,
            vbr_id=vbr_id,
            point_in_time=point_in_time,
            backup_size_bytes=backup_size_bytes,
            is_corrupted=is_corrupted,
            gfs_flags=gfs_flags,
            job_session_id=job_session_id,
            backup_destination=backup_destination,
            state=state,
            data_retrieval_status=data_retrieval_status,
            retrieved_data_expiration_date=retrieved_data_expiration_date,
            notify_before_retrieved_data_expiration_hours=notify_before_retrieved_data_expiration_hours,
            immutable_till=immutable_till,
            access_tier=access_tier,
            latest_chain_size_bytes=latest_chain_size_bytes,
            field_links=field_links,
        )

        return sql_restore_point
