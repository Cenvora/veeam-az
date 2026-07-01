from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.repository_restore_point_state import RepositoryRestorePointState
from ..models.restore_point_type import RestorePointType
from ..models.vnet_backup_destination import VnetBackupDestination
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="VnetRestorePoint")


@_attrs_define
class VnetRestorePoint:
    """
    Attributes:
        id (UUID | Unset): System ID assigned to the restore point in the Veeam Backup for Microsoft Azure REST API.
        type_ (RestorePointType | Unset): Type of the restore point.
        vbr_id (None | str | Unset): System ID assigned to a restore point in Veeam Backup & Replication.
        azure_account_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to a
            service account whose permissions were used to create the restore point.
        subscription_id (None | str | Unset): Microsoft Azure ID assigned to a subscription for which the restore point
            was created.
        subscription_name (None | str | Unset): Name of the subscription for which the restore point was created.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region where the restore point was created.
        region_name (None | str | Unset): Name of the Azure region where the restore point was created.
        point_in_time (datetime.datetime | Unset): Date and time when the restore point was created.
        gfs_flags (str | Unset): Retention period configured for the restore point.
        job_session_id (None | str | Unset): System ID assigned to the backup session in the Veeam Backup for Microsoft
            Azure REST API.
        backup_destination (VnetBackupDestination | Unset): Type of the backup destination.
        state (RepositoryRestorePointState | Unset):
        size_in_bytes (int | Unset): Size of the restore point file (in bytes).
        is_corrupted (bool | None | Unset): Defines whether the restore point is corrupted. Note that the corrupted
            restore points cannot be used for restore operations.
        latest_chain_size_bytes (int | None | Unset): Size of the latest backup in an incremental backup chain.
        changes (None | str | Unset): List containing data on the virtual network configuration items that were recently
            added to the backup scope or deleted from it.
        immutable_till (datetime.datetime | None | Unset): Date and time when immutability will be automatically
            disabled for the restore point.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: UUID | Unset = UNSET
    type_: RestorePointType | Unset = UNSET
    vbr_id: None | str | Unset = UNSET
    azure_account_id: None | str | Unset = UNSET
    subscription_id: None | str | Unset = UNSET
    subscription_name: None | str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    point_in_time: datetime.datetime | Unset = UNSET
    gfs_flags: str | Unset = UNSET
    job_session_id: None | str | Unset = UNSET
    backup_destination: VnetBackupDestination | Unset = UNSET
    state: RepositoryRestorePointState | Unset = UNSET
    size_in_bytes: int | Unset = UNSET
    is_corrupted: bool | None | Unset = UNSET
    latest_chain_size_bytes: int | None | Unset = UNSET
    changes: None | str | Unset = UNSET
    immutable_till: datetime.datetime | None | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        vbr_id: None | str | Unset
        if isinstance(self.vbr_id, Unset):
            vbr_id = UNSET
        else:
            vbr_id = self.vbr_id

        azure_account_id: None | str | Unset
        if isinstance(self.azure_account_id, Unset):
            azure_account_id = UNSET
        else:
            azure_account_id = self.azure_account_id

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = self.subscription_id

        subscription_name: None | str | Unset
        if isinstance(self.subscription_name, Unset):
            subscription_name = UNSET
        else:
            subscription_name = self.subscription_name

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

        size_in_bytes = self.size_in_bytes

        is_corrupted: bool | None | Unset
        if isinstance(self.is_corrupted, Unset):
            is_corrupted = UNSET
        else:
            is_corrupted = self.is_corrupted

        latest_chain_size_bytes: int | None | Unset
        if isinstance(self.latest_chain_size_bytes, Unset):
            latest_chain_size_bytes = UNSET
        else:
            latest_chain_size_bytes = self.latest_chain_size_bytes

        changes: None | str | Unset
        if isinstance(self.changes, Unset):
            changes = UNSET
        else:
            changes = self.changes

        immutable_till: None | str | Unset
        if isinstance(self.immutable_till, Unset):
            immutable_till = UNSET
        elif isinstance(self.immutable_till, datetime.datetime):
            immutable_till = self.immutable_till.isoformat()
        else:
            immutable_till = self.immutable_till

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
        if vbr_id is not UNSET:
            field_dict["vbrId"] = vbr_id
        if azure_account_id is not UNSET:
            field_dict["azureAccountId"] = azure_account_id
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if point_in_time is not UNSET:
            field_dict["pointInTime"] = point_in_time
        if gfs_flags is not UNSET:
            field_dict["gfsFlags"] = gfs_flags
        if job_session_id is not UNSET:
            field_dict["jobSessionId"] = job_session_id
        if backup_destination is not UNSET:
            field_dict["backupDestination"] = backup_destination
        if state is not UNSET:
            field_dict["state"] = state
        if size_in_bytes is not UNSET:
            field_dict["sizeInBytes"] = size_in_bytes
        if is_corrupted is not UNSET:
            field_dict["isCorrupted"] = is_corrupted
        if latest_chain_size_bytes is not UNSET:
            field_dict["latestChainSizeBytes"] = latest_chain_size_bytes
        if changes is not UNSET:
            field_dict["changes"] = changes
        if immutable_till is not UNSET:
            field_dict["immutableTill"] = immutable_till
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

        def _parse_vbr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vbr_id = _parse_vbr_id(d.pop("vbrId", UNSET))

        def _parse_azure_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_account_id = _parse_azure_account_id(d.pop("azureAccountId", UNSET))

        def _parse_subscription_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        def _parse_subscription_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_name = _parse_subscription_name(d.pop("subscriptionName", UNSET))

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

        def _parse_job_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_session_id = _parse_job_session_id(d.pop("jobSessionId", UNSET))

        _backup_destination = d.pop("backupDestination", UNSET)
        backup_destination: VnetBackupDestination | Unset
        if isinstance(_backup_destination, Unset):
            backup_destination = UNSET
        else:
            backup_destination = VnetBackupDestination(_backup_destination)

        _state = d.pop("state", UNSET)
        state: RepositoryRestorePointState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RepositoryRestorePointState(_state)

        size_in_bytes = d.pop("sizeInBytes", UNSET)

        def _parse_is_corrupted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_corrupted = _parse_is_corrupted(d.pop("isCorrupted", UNSET))

        def _parse_latest_chain_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest_chain_size_bytes = _parse_latest_chain_size_bytes(d.pop("latestChainSizeBytes", UNSET))

        def _parse_changes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        changes = _parse_changes(d.pop("changes", UNSET))

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

        vnet_restore_point = cls(
            id=id,
            type_=type_,
            vbr_id=vbr_id,
            azure_account_id=azure_account_id,
            subscription_id=subscription_id,
            subscription_name=subscription_name,
            region_id=region_id,
            region_name=region_name,
            point_in_time=point_in_time,
            gfs_flags=gfs_flags,
            job_session_id=job_session_id,
            backup_destination=backup_destination,
            state=state,
            size_in_bytes=size_in_bytes,
            is_corrupted=is_corrupted,
            latest_chain_size_bytes=latest_chain_size_bytes,
            changes=changes,
            immutable_till=immutable_till,
            field_links=field_links,
        )

        return vnet_restore_point
