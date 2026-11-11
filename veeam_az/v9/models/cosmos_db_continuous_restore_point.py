from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.data_retrieval_status import DataRetrievalStatus
from ..models.restore_point_type import RestorePointType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="CosmosDbContinuousRestorePoint")


@_attrs_define
class CosmosDbContinuousRestorePoint:
    r"""
    Attributes:
        id (UUID | Unset): System ID assigned to the restore point in the Veeam Backup for Microsoft Azure REST API.
        type_ (RestorePointType | Unset): Type of the restore point.
        account_name (None | str | Unset): Name of a Cosmos DB account for which the restorable timastamp was created.
        account_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the
            Cosmos DB account for which the restorable timastamp was created.
        point_in_time (datetime.datetime | Unset): Date and time when the restore point was created.
        backup_size_bytes (int | Unset): Size of the restore point file (in bytes).
        is_corrupted (bool | None | Unset): Defines whether the restore point is corrupted. Note that the corrupted
            restore points cannot be used for restore operations.
        gfs_flags (str | Unset): Retention period configured for the restore point.
        job_session_id (None | str | Unset): System ID assigned to the backup session in the Veeam Backup for Microsoft
            Azure REST API.
        data_retrieval_status (DataRetrievalStatus | Unset): State of the data retrieval process.
        retrieved_data_expiration_date (datetime.datetime | None | Unset): Date and time when the retrieval period
            exceeds.
        notify_before_retrieved_data_expiration_hours (int | None | Unset): \[Applies if a user wants to be notified
            when data availability period is about to expire] Time when a notification will be sent (in hours remaining
            until the expiration).
        latest_chain_size_bytes (int | None | Unset): Size of the latest backup in an incremental backup chain.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: UUID | Unset = UNSET
    type_: RestorePointType | Unset = UNSET
    account_name: None | str | Unset = UNSET
    account_id: None | str | Unset = UNSET
    point_in_time: datetime.datetime | Unset = UNSET
    backup_size_bytes: int | Unset = UNSET
    is_corrupted: bool | None | Unset = UNSET
    gfs_flags: str | Unset = UNSET
    job_session_id: None | str | Unset = UNSET
    data_retrieval_status: DataRetrievalStatus | Unset = UNSET
    retrieved_data_expiration_date: datetime.datetime | None | Unset = UNSET
    notify_before_retrieved_data_expiration_hours: int | None | Unset = UNSET
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

        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

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
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
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
        if data_retrieval_status is not UNSET:
            field_dict["dataRetrievalStatus"] = data_retrieval_status
        if retrieved_data_expiration_date is not UNSET:
            field_dict["retrievedDataExpirationDate"] = retrieved_data_expiration_date
        if notify_before_retrieved_data_expiration_hours is not UNSET:
            field_dict["notifyBeforeRetrievedDataExpirationHours"] = notify_before_retrieved_data_expiration_hours
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

        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))

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

        cosmos_db_continuous_restore_point = cls(
            id=id,
            type_=type_,
            account_name=account_name,
            account_id=account_id,
            point_in_time=point_in_time,
            backup_size_bytes=backup_size_bytes,
            is_corrupted=is_corrupted,
            gfs_flags=gfs_flags,
            job_session_id=job_session_id,
            data_retrieval_status=data_retrieval_status,
            retrieved_data_expiration_date=retrieved_data_expiration_date,
            notify_before_retrieved_data_expiration_hours=notify_before_retrieved_data_expiration_hours,
            latest_chain_size_bytes=latest_chain_size_bytes,
            field_links=field_links,
        )

        return cosmos_db_continuous_restore_point
