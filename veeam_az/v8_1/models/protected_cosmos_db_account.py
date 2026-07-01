from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.cosmos_db_account_status import CosmosDbAccountStatus
from ..models.cosmos_db_account_type import CosmosDbAccountType
from ..models.cosmos_db_capacity_mode import CosmosDbCapacityMode
from ..models.cosmos_db_restore_point_type import CosmosDbRestorePointType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_cosmos_db_account_state import ProtectionCosmosDbAccountState


T = TypeVar("T", bound="ProtectedCosmosDbAccount")


@_attrs_define
class ProtectedCosmosDbAccount:
    r"""Information on a Cosmos DB account protected by Veeam Backup for Microsoft Azure.

    Attributes:
        id (str | Unset): System ID assigned to the Cosmos DB account in the Veeam Backup for Microsoft Azure REST API.
        name (str | Unset): Name of the Cosmos DB account.
        status (CosmosDbAccountStatus | Unset): Status of the protected Cosmos DB account.
        account_type (CosmosDbAccountType | Unset): Kind of the protected Cosmos DB account.
        policy_name (None | str | Unset): Name of the backup policy that protects the Cosmos DB account.
        latest_restorable_timestamp (datetime.datetime | None | Unset): The most recent date and time to which the
            Cosmos DB account protected using the *Continuous backup* option can be restored.
        earliest_restorable_timestamp (datetime.datetime | None | Unset): The earliest date and time to which the Cosmos
            DB account protected using the *Continuous backup* option can be restored.
        latest_backup (datetime.datetime | None | Unset): Date and time of the most recent restore point created for the
            Cosmos DB for PostgreSQL account protected using the *Backup to repository* option.
        backup_size_bytes (int | None | Unset): Total size of the standard Cosmos DB account backups.
        archive_size_bytes (int | None | Unset): Total size of the Cosmos DB account backups stored in archive
            repositories.
        subscription_id (str | Unset): Microsoft Azure ID assigned to a subscription that manages the Cosmos DB account.
        subscription_name (None | str | Unset): Name of the subscription that manages the Cosmos DB account.
        service_account_id (None | Unset | UUID): System ID assigned in the Veeam Backup for Microsoft Azure REST API to
            the service account whose permissions are used to protect the Cosmos DB account.
        tenant_id (None | str | Unset): Microsoft Azure ID assigned to a tenant to which the Cosmos DB account belongs.
        tenant_name (None | str | Unset): Name of the tenant to which the Cosmos DB account belongs.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region in which the Cosmos DB account resides.
        region_name (None | str | Unset): Name of the region in which the Cosmos DB account resides.
        resource_group_name (str | Unset): Name of the resource group to which the Cosmos DB account belongs.
        read_regions (list[str] | None | Unset): List of the read regions available for the Cosmos DB account.
        write_regions (list[str] | None | Unset): List of the write regions available for the Cosmos DB account.
        restore_point_types (list[CosmosDbRestorePointType] | Unset): Types of restore points created for the Cosmos DB
            account.
        protection_state (ProtectionCosmosDbAccountState | Unset): Information on the backups created for the Cosmos DB
            account.
        database_name (None | str | Unset): \[Applies only to Cosmos DB for PostgreSQL accounts protected using the
            *Backup to repository* option] Name of the backed-up PostgreSQL database.
        capacity_mode (CosmosDbCapacityMode | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: CosmosDbAccountStatus | Unset = UNSET
    account_type: CosmosDbAccountType | Unset = UNSET
    policy_name: None | str | Unset = UNSET
    latest_restorable_timestamp: datetime.datetime | None | Unset = UNSET
    earliest_restorable_timestamp: datetime.datetime | None | Unset = UNSET
    latest_backup: datetime.datetime | None | Unset = UNSET
    backup_size_bytes: int | None | Unset = UNSET
    archive_size_bytes: int | None | Unset = UNSET
    subscription_id: str | Unset = UNSET
    subscription_name: None | str | Unset = UNSET
    service_account_id: None | Unset | UUID = UNSET
    tenant_id: None | str | Unset = UNSET
    tenant_name: None | str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    resource_group_name: str | Unset = UNSET
    read_regions: list[str] | None | Unset = UNSET
    write_regions: list[str] | None | Unset = UNSET
    restore_point_types: list[CosmosDbRestorePointType] | Unset = UNSET
    protection_state: ProtectionCosmosDbAccountState | Unset = UNSET
    database_name: None | str | Unset = UNSET
    capacity_mode: CosmosDbCapacityMode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        policy_name: None | str | Unset
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        latest_restorable_timestamp: None | str | Unset
        if isinstance(self.latest_restorable_timestamp, Unset):
            latest_restorable_timestamp = UNSET
        elif isinstance(self.latest_restorable_timestamp, datetime.datetime):
            latest_restorable_timestamp = self.latest_restorable_timestamp.isoformat()
        else:
            latest_restorable_timestamp = self.latest_restorable_timestamp

        earliest_restorable_timestamp: None | str | Unset
        if isinstance(self.earliest_restorable_timestamp, Unset):
            earliest_restorable_timestamp = UNSET
        elif isinstance(self.earliest_restorable_timestamp, datetime.datetime):
            earliest_restorable_timestamp = self.earliest_restorable_timestamp.isoformat()
        else:
            earliest_restorable_timestamp = self.earliest_restorable_timestamp

        latest_backup: None | str | Unset
        if isinstance(self.latest_backup, Unset):
            latest_backup = UNSET
        elif isinstance(self.latest_backup, datetime.datetime):
            latest_backup = self.latest_backup.isoformat()
        else:
            latest_backup = self.latest_backup

        backup_size_bytes: int | None | Unset
        if isinstance(self.backup_size_bytes, Unset):
            backup_size_bytes = UNSET
        else:
            backup_size_bytes = self.backup_size_bytes

        archive_size_bytes: int | None | Unset
        if isinstance(self.archive_size_bytes, Unset):
            archive_size_bytes = UNSET
        else:
            archive_size_bytes = self.archive_size_bytes

        subscription_id = self.subscription_id

        subscription_name: None | str | Unset
        if isinstance(self.subscription_name, Unset):
            subscription_name = UNSET
        else:
            subscription_name = self.subscription_name

        service_account_id: None | str | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        elif isinstance(self.service_account_id, UUID):
            service_account_id = str(self.service_account_id)
        else:
            service_account_id = self.service_account_id

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        tenant_name: None | str | Unset
        if isinstance(self.tenant_name, Unset):
            tenant_name = UNSET
        else:
            tenant_name = self.tenant_name

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

        resource_group_name = self.resource_group_name

        read_regions: list[str] | None | Unset
        if isinstance(self.read_regions, Unset):
            read_regions = UNSET
        elif isinstance(self.read_regions, list):
            read_regions = self.read_regions

        else:
            read_regions = self.read_regions

        write_regions: list[str] | None | Unset
        if isinstance(self.write_regions, Unset):
            write_regions = UNSET
        elif isinstance(self.write_regions, list):
            write_regions = self.write_regions

        else:
            write_regions = self.write_regions

        restore_point_types: list[str] | Unset = UNSET
        if not isinstance(self.restore_point_types, Unset):
            restore_point_types = []
            for restore_point_types_item_data in self.restore_point_types:
                restore_point_types_item = restore_point_types_item_data.value
                restore_point_types.append(restore_point_types_item)

        protection_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.protection_state, Unset):
            protection_state = self.protection_state.to_dict()

        database_name: None | str | Unset
        if isinstance(self.database_name, Unset):
            database_name = UNSET
        else:
            database_name = self.database_name

        capacity_mode: str | Unset = UNSET
        if not isinstance(self.capacity_mode, Unset):
            capacity_mode = self.capacity_mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if latest_restorable_timestamp is not UNSET:
            field_dict["latestRestorableTimestamp"] = latest_restorable_timestamp
        if earliest_restorable_timestamp is not UNSET:
            field_dict["earliestRestorableTimestamp"] = earliest_restorable_timestamp
        if latest_backup is not UNSET:
            field_dict["latestBackup"] = latest_backup
        if backup_size_bytes is not UNSET:
            field_dict["backupSizeBytes"] = backup_size_bytes
        if archive_size_bytes is not UNSET:
            field_dict["archiveSizeBytes"] = archive_size_bytes
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if tenant_name is not UNSET:
            field_dict["tenantName"] = tenant_name
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if read_regions is not UNSET:
            field_dict["readRegions"] = read_regions
        if write_regions is not UNSET:
            field_dict["writeRegions"] = write_regions
        if restore_point_types is not UNSET:
            field_dict["restorePointTypes"] = restore_point_types
        if protection_state is not UNSET:
            field_dict["protectionState"] = protection_state
        if database_name is not UNSET:
            field_dict["databaseName"] = database_name
        if capacity_mode is not UNSET:
            field_dict["capacityMode"] = capacity_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_cosmos_db_account_state import ProtectionCosmosDbAccountState

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: CosmosDbAccountStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CosmosDbAccountStatus(_status)

        _account_type = d.pop("accountType", UNSET)
        account_type: CosmosDbAccountType | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = CosmosDbAccountType(_account_type)

        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        def _parse_latest_restorable_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_restorable_timestamp_type_0 = isoparse(data)

                return latest_restorable_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        latest_restorable_timestamp = _parse_latest_restorable_timestamp(d.pop("latestRestorableTimestamp", UNSET))

        def _parse_earliest_restorable_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                earliest_restorable_timestamp_type_0 = isoparse(data)

                return earliest_restorable_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        earliest_restorable_timestamp = _parse_earliest_restorable_timestamp(
            d.pop("earliestRestorableTimestamp", UNSET)
        )

        def _parse_latest_backup(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_backup_type_0 = isoparse(data)

                return latest_backup_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        latest_backup = _parse_latest_backup(d.pop("latestBackup", UNSET))

        def _parse_backup_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_size_bytes = _parse_backup_size_bytes(d.pop("backupSizeBytes", UNSET))

        def _parse_archive_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archive_size_bytes = _parse_archive_size_bytes(d.pop("archiveSizeBytes", UNSET))

        subscription_id = d.pop("subscriptionId", UNSET)

        def _parse_subscription_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_name = _parse_subscription_name(d.pop("subscriptionName", UNSET))

        def _parse_service_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_account_id_type_0 = UUID(data)

                return service_account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        service_account_id = _parse_service_account_id(d.pop("serviceAccountId", UNSET))

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_tenant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_name = _parse_tenant_name(d.pop("tenantName", UNSET))

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

        resource_group_name = d.pop("resourceGroupName", UNSET)

        def _parse_read_regions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                read_regions_type_0 = cast(list[str], data)

                return read_regions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        read_regions = _parse_read_regions(d.pop("readRegions", UNSET))

        def _parse_write_regions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                write_regions_type_0 = cast(list[str], data)

                return write_regions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        write_regions = _parse_write_regions(d.pop("writeRegions", UNSET))

        _restore_point_types = d.pop("restorePointTypes", UNSET)
        restore_point_types: list[CosmosDbRestorePointType] | Unset = UNSET
        if _restore_point_types is not UNSET:
            restore_point_types = []
            for restore_point_types_item_data in _restore_point_types:
                restore_point_types_item = CosmosDbRestorePointType(restore_point_types_item_data)

                restore_point_types.append(restore_point_types_item)

        _protection_state = d.pop("protectionState", UNSET)
        protection_state: ProtectionCosmosDbAccountState | Unset
        if isinstance(_protection_state, Unset):
            protection_state = UNSET
        else:
            protection_state = ProtectionCosmosDbAccountState.from_dict(_protection_state)

        def _parse_database_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        database_name = _parse_database_name(d.pop("databaseName", UNSET))

        _capacity_mode = d.pop("capacityMode", UNSET)
        capacity_mode: CosmosDbCapacityMode | Unset
        if isinstance(_capacity_mode, Unset):
            capacity_mode = UNSET
        else:
            capacity_mode = CosmosDbCapacityMode(_capacity_mode)

        protected_cosmos_db_account = cls(
            id=id,
            name=name,
            status=status,
            account_type=account_type,
            policy_name=policy_name,
            latest_restorable_timestamp=latest_restorable_timestamp,
            earliest_restorable_timestamp=earliest_restorable_timestamp,
            latest_backup=latest_backup,
            backup_size_bytes=backup_size_bytes,
            archive_size_bytes=archive_size_bytes,
            subscription_id=subscription_id,
            subscription_name=subscription_name,
            service_account_id=service_account_id,
            tenant_id=tenant_id,
            tenant_name=tenant_name,
            region_id=region_id,
            region_name=region_name,
            resource_group_name=resource_group_name,
            read_regions=read_regions,
            write_regions=write_regions,
            restore_point_types=restore_point_types,
            protection_state=protection_state,
            database_name=database_name,
            capacity_mode=capacity_mode,
        )

        return protected_cosmos_db_account
