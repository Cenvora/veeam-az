from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.backup_destination import BackupDestination
from ..models.data_retrieval_status import DataRetrievalStatus
from ..models.repository_restore_point_state import RepositoryRestorePointState
from ..models.restore_point_type import RestorePointType
from ..models.storage_access_tier import StorageAccessTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="VirtualMachineRestorePoint")


@_attrs_define
class VirtualMachineRestorePoint:
    r"""Information on each restore point.

    Attributes:
        id (UUID): System ID assigned to a restore point in the Veeam Backup for Microsoft Azure REST API.
        backup_destination (BackupDestination): Type of the backup destination.
        type_ (RestorePointType | Unset): Type of the restore point.
        vbr_id (None | str | Unset): System ID assigned to a restore point in Veeam Backup & Replication.
        point_in_time (datetime.datetime | Unset): Date and time when the restore point was created.
        point_in_time_local_time (datetime.datetime | None | Unset): Date and time when the restore point was created,
            it contains timezone offset of protected VM.
        backup_size_bytes (int | Unset): Size of the restore point file (in bytes).
        is_corrupted (bool | None | Unset): Defines whether the restore point is corrupted. Note that the corrupted
            restore points cannot be used for restore operations.
        vm_name (str | Unset): Name of an Azure VM the restore point belongs to.
        resource_hash_id (str | Unset): Internal ID assigned to the restore point in the Veeam Backup for Microsoft
            Azure REST API.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region where the restore point resides.
        region_name (None | str | Unset): Name of the Azure region where the restore point resides.
        state (RepositoryRestorePointState | Unset):
        gfs_flags (str | Unset): Retention period configured for the restore point.
        job_session_id (None | str | Unset): System ID assigned to the session in the Veeam Backup for Microsoft Azure
            REST API.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
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
    """

    id: UUID
    backup_destination: BackupDestination
    type_: RestorePointType | Unset = UNSET
    vbr_id: None | str | Unset = UNSET
    point_in_time: datetime.datetime | Unset = UNSET
    point_in_time_local_time: datetime.datetime | None | Unset = UNSET
    backup_size_bytes: int | Unset = UNSET
    is_corrupted: bool | None | Unset = UNSET
    vm_name: str | Unset = UNSET
    resource_hash_id: str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    state: RepositoryRestorePointState | Unset = UNSET
    gfs_flags: str | Unset = UNSET
    job_session_id: None | str | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET
    data_retrieval_status: DataRetrievalStatus | Unset = UNSET
    retrieved_data_expiration_date: datetime.datetime | None | Unset = UNSET
    notify_before_retrieved_data_expiration_hours: int | None | Unset = UNSET
    immutable_till: datetime.datetime | None | Unset = UNSET
    access_tier: StorageAccessTier | Unset = UNSET
    latest_chain_size_bytes: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id = str(self.id)

        backup_destination = self.backup_destination.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        vbr_id: None | str | Unset
        if isinstance(self.vbr_id, Unset):
            vbr_id = UNSET
        else:
            vbr_id = self.vbr_id

        point_in_time: str | Unset = UNSET
        if not isinstance(self.point_in_time, Unset):
            point_in_time = self.point_in_time.isoformat()

        point_in_time_local_time: None | str | Unset
        if isinstance(self.point_in_time_local_time, Unset):
            point_in_time_local_time = UNSET
        elif isinstance(self.point_in_time_local_time, datetime.datetime):
            point_in_time_local_time = self.point_in_time_local_time.isoformat()
        else:
            point_in_time_local_time = self.point_in_time_local_time

        backup_size_bytes = self.backup_size_bytes

        is_corrupted: bool | None | Unset
        if isinstance(self.is_corrupted, Unset):
            is_corrupted = UNSET
        else:
            is_corrupted = self.is_corrupted

        vm_name = self.vm_name

        resource_hash_id = self.resource_hash_id

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

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        gfs_flags = self.gfs_flags

        job_session_id: None | str | Unset
        if isinstance(self.job_session_id, Unset):
            job_session_id = UNSET
        else:
            job_session_id = self.job_session_id

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "backupDestination": backup_destination,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vbr_id is not UNSET:
            field_dict["vbrId"] = vbr_id
        if point_in_time is not UNSET:
            field_dict["pointInTime"] = point_in_time
        if point_in_time_local_time is not UNSET:
            field_dict["pointInTimeLocalTime"] = point_in_time_local_time
        if backup_size_bytes is not UNSET:
            field_dict["backupSizeBytes"] = backup_size_bytes
        if is_corrupted is not UNSET:
            field_dict["isCorrupted"] = is_corrupted
        if vm_name is not UNSET:
            field_dict["vmName"] = vm_name
        if resource_hash_id is not UNSET:
            field_dict["resourceHashId"] = resource_hash_id
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if state is not UNSET:
            field_dict["state"] = state
        if gfs_flags is not UNSET:
            field_dict["gfsFlags"] = gfs_flags
        if job_session_id is not UNSET:
            field_dict["jobSessionId"] = job_session_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        backup_destination = BackupDestination(d.pop("backupDestination"))

        _type_ = d.pop("type", UNSET)
        type_: RestorePointType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestorePointType(_type_)

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

        def _parse_point_in_time_local_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                point_in_time_local_time_type_0 = isoparse(data)

                return point_in_time_local_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        point_in_time_local_time = _parse_point_in_time_local_time(d.pop("pointInTimeLocalTime", UNSET))

        backup_size_bytes = d.pop("backupSizeBytes", UNSET)

        def _parse_is_corrupted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_corrupted = _parse_is_corrupted(d.pop("isCorrupted", UNSET))

        vm_name = d.pop("vmName", UNSET)

        resource_hash_id = d.pop("resourceHashId", UNSET)

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

        _state = d.pop("state", UNSET)
        state: RepositoryRestorePointState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RepositoryRestorePointState(_state)

        gfs_flags = d.pop("gfsFlags", UNSET)

        def _parse_job_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_session_id = _parse_job_session_id(d.pop("jobSessionId", UNSET))

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

        virtual_machine_restore_point = cls(
            id=id,
            backup_destination=backup_destination,
            type_=type_,
            vbr_id=vbr_id,
            point_in_time=point_in_time,
            point_in_time_local_time=point_in_time_local_time,
            backup_size_bytes=backup_size_bytes,
            is_corrupted=is_corrupted,
            vm_name=vm_name,
            resource_hash_id=resource_hash_id,
            region_id=region_id,
            region_name=region_name,
            state=state,
            gfs_flags=gfs_flags,
            job_session_id=job_session_id,
            field_links=field_links,
            data_retrieval_status=data_retrieval_status,
            retrieved_data_expiration_date=retrieved_data_expiration_date,
            notify_before_retrieved_data_expiration_hours=notify_before_retrieved_data_expiration_hours,
            immutable_till=immutable_till,
            access_tier=access_tier,
            latest_chain_size_bytes=latest_chain_size_bytes,
        )

        return virtual_machine_restore_point
