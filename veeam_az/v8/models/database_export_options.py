from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.credentials_state_filter_options import CredentialsStateFilterOptions
from ..models.protection_status import ProtectionStatus
from ..models.sql_backup_destination_filter_options import SqlBackupDestinationFilterOptions
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseExportOptions")


@_attrs_define
class DatabaseExportOptions:
    """
    Attributes:
        database_ids (list[str] | None | Unset): Specifies the system IDs assigned in the Veeam Backup for Microsoft
            Azure REST API to the Azure SQL databases whose data will be exported.
        subscription_id (None | Unset | UUID): Returns only SQL databases available in a subscription with the specified
            ID.
        tenant_id (None | Unset | UUID): Returns only SQL databases available for a tenant with the specified ID.
        service_account_id (None | str | Unset): Returns only SQL databases to which a service account with the
            specified ID has access.
        search_pattern (None | str | Unset): Returns only those items of a resource collection whose names match the
            specified search pattern in the parameter value.
        credentials_state (CredentialsStateFilterOptions | Unset):
        assignable_by_sql_account_id (int | None | Unset): Returns only SQL databases that are associated with an Azure
            SQL account with the specified ID.
        region_ids (list[str] | None | Unset): Returns only SQL databases that reside in Azure regions with the
            specified IDs.
        protection_status (list[ProtectionStatus] | None | Unset): Returns only SQL databases with the specified
            protection status.
        backup_destination (list[SqlBackupDestinationFilterOptions] | None | Unset): Returns only SQL databases with the
            specified backup type.
        db_from_protected_regions (bool | Unset): Defines whether Veeam Backup for Microsoft Azure must return only SQL
            databases that reside in regions protected by backup policies.
    """

    database_ids: list[str] | None | Unset = UNSET
    subscription_id: None | Unset | UUID = UNSET
    tenant_id: None | Unset | UUID = UNSET
    service_account_id: None | str | Unset = UNSET
    search_pattern: None | str | Unset = UNSET
    credentials_state: CredentialsStateFilterOptions | Unset = UNSET
    assignable_by_sql_account_id: int | None | Unset = UNSET
    region_ids: list[str] | None | Unset = UNSET
    protection_status: list[ProtectionStatus] | None | Unset = UNSET
    backup_destination: list[SqlBackupDestinationFilterOptions] | None | Unset = UNSET
    db_from_protected_regions: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        database_ids: list[str] | None | Unset
        if isinstance(self.database_ids, Unset):
            database_ids = UNSET
        elif isinstance(self.database_ids, list):
            database_ids = self.database_ids

        else:
            database_ids = self.database_ids

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        elif isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        elif isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        service_account_id: None | str | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        else:
            service_account_id = self.service_account_id

        search_pattern: None | str | Unset
        if isinstance(self.search_pattern, Unset):
            search_pattern = UNSET
        else:
            search_pattern = self.search_pattern

        credentials_state: str | Unset = UNSET
        if not isinstance(self.credentials_state, Unset):
            credentials_state = self.credentials_state.value

        assignable_by_sql_account_id: int | None | Unset
        if isinstance(self.assignable_by_sql_account_id, Unset):
            assignable_by_sql_account_id = UNSET
        else:
            assignable_by_sql_account_id = self.assignable_by_sql_account_id

        region_ids: list[str] | None | Unset
        if isinstance(self.region_ids, Unset):
            region_ids = UNSET
        elif isinstance(self.region_ids, list):
            region_ids = self.region_ids

        else:
            region_ids = self.region_ids

        protection_status: list[str] | None | Unset
        if isinstance(self.protection_status, Unset):
            protection_status = UNSET
        elif isinstance(self.protection_status, list):
            protection_status = []
            for protection_status_type_0_item_data in self.protection_status:
                protection_status_type_0_item = protection_status_type_0_item_data.value
                protection_status.append(protection_status_type_0_item)

        else:
            protection_status = self.protection_status

        backup_destination: list[str] | None | Unset
        if isinstance(self.backup_destination, Unset):
            backup_destination = UNSET
        elif isinstance(self.backup_destination, list):
            backup_destination = []
            for backup_destination_type_0_item_data in self.backup_destination:
                backup_destination_type_0_item = backup_destination_type_0_item_data.value
                backup_destination.append(backup_destination_type_0_item)

        else:
            backup_destination = self.backup_destination

        db_from_protected_regions = self.db_from_protected_regions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if database_ids is not UNSET:
            field_dict["databaseIds"] = database_ids
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern
        if credentials_state is not UNSET:
            field_dict["credentialsState"] = credentials_state
        if assignable_by_sql_account_id is not UNSET:
            field_dict["assignableBySqlAccountId"] = assignable_by_sql_account_id
        if region_ids is not UNSET:
            field_dict["regionIds"] = region_ids
        if protection_status is not UNSET:
            field_dict["protectionStatus"] = protection_status
        if backup_destination is not UNSET:
            field_dict["backupDestination"] = backup_destination
        if db_from_protected_regions is not UNSET:
            field_dict["dbFromProtectedRegions"] = db_from_protected_regions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_database_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                database_ids_type_0 = cast(list[str], data)

                return database_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        database_ids = _parse_database_ids(d.pop("databaseIds", UNSET))

        def _parse_subscription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_type_0 = UUID(data)

                return subscription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        def _parse_tenant_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_id_type_0 = UUID(data)

                return tenant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_service_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_account_id = _parse_service_account_id(d.pop("serviceAccountId", UNSET))

        def _parse_search_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_pattern = _parse_search_pattern(d.pop("searchPattern", UNSET))

        _credentials_state = d.pop("credentialsState", UNSET)
        credentials_state: CredentialsStateFilterOptions | Unset
        if isinstance(_credentials_state, Unset):
            credentials_state = UNSET
        else:
            credentials_state = CredentialsStateFilterOptions(_credentials_state)

        def _parse_assignable_by_sql_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assignable_by_sql_account_id = _parse_assignable_by_sql_account_id(d.pop("assignableBySqlAccountId", UNSET))

        def _parse_region_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                region_ids_type_0 = cast(list[str], data)

                return region_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        region_ids = _parse_region_ids(d.pop("regionIds", UNSET))

        def _parse_protection_status(data: object) -> list[ProtectionStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protection_status_type_0 = []
                _protection_status_type_0 = data
                for protection_status_type_0_item_data in _protection_status_type_0:
                    protection_status_type_0_item = ProtectionStatus(protection_status_type_0_item_data)

                    protection_status_type_0.append(protection_status_type_0_item)

                return protection_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProtectionStatus] | None | Unset, data)

        protection_status = _parse_protection_status(d.pop("protectionStatus", UNSET))

        def _parse_backup_destination(data: object) -> list[SqlBackupDestinationFilterOptions] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                backup_destination_type_0 = []
                _backup_destination_type_0 = data
                for backup_destination_type_0_item_data in _backup_destination_type_0:
                    backup_destination_type_0_item = SqlBackupDestinationFilterOptions(
                        backup_destination_type_0_item_data
                    )

                    backup_destination_type_0.append(backup_destination_type_0_item)

                return backup_destination_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SqlBackupDestinationFilterOptions] | None | Unset, data)

        backup_destination = _parse_backup_destination(d.pop("backupDestination", UNSET))

        db_from_protected_regions = d.pop("dbFromProtectedRegions", UNSET)

        database_export_options = cls(
            database_ids=database_ids,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            search_pattern=search_pattern,
            credentials_state=credentials_state,
            assignable_by_sql_account_id=assignable_by_sql_account_id,
            region_ids=region_ids,
            protection_status=protection_status,
            backup_destination=backup_destination,
            db_from_protected_regions=db_from_protected_regions,
        )

        return database_export_options
