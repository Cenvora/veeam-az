from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_type_nullable import BackupTypeNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_region_from_client import PolicyRegionFromClient
    from ..models.sql_policy_backup_items_from_client import SqlPolicyBackupItemsFromClient
    from ..models.sql_policy_excluded_items_from_client import SqlPolicyExcludedItemsFromClient


T = TypeVar("T", bound="ValidateSyncDatabasesSqlPolicyFromClient")


@_attrs_define
class ValidateSyncDatabasesSqlPolicyFromClient:
    r"""
    Attributes:
        tenant_id (str):
        service_account_id (UUID):
        backup_type (BackupTypeNullable | Unset): Defines whether you want to include to the backup scope all resources
            residing in the specified Azure regions and to which the specified service account has access.
        regions (list[PolicyRegionFromClient] | None | Unset):
        selected_items (SqlPolicyBackupItemsFromClient | Unset): \[Applies if the *SelectedItems* value is specified for
            the `backupType` parameter] Specifies information on Azure resources to protect by the backup policy.
        excluded_items (SqlPolicyExcludedItemsFromClient | Unset): Specifies Azure resources to exclude from the backup
            scope.
    """

    tenant_id: str
    service_account_id: UUID
    backup_type: BackupTypeNullable | Unset = UNSET
    regions: list[PolicyRegionFromClient] | None | Unset = UNSET
    selected_items: SqlPolicyBackupItemsFromClient | Unset = UNSET
    excluded_items: SqlPolicyExcludedItemsFromClient | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        service_account_id = str(self.service_account_id)

        backup_type: str | Unset = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value

        regions: list[dict[str, Any]] | None | Unset
        if isinstance(self.regions, Unset):
            regions = UNSET
        elif isinstance(self.regions, list):
            regions = []
            for regions_type_0_item_data in self.regions:
                regions_type_0_item = regions_type_0_item_data.to_dict()
                regions.append(regions_type_0_item)

        else:
            regions = self.regions

        selected_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selected_items, Unset):
            selected_items = self.selected_items.to_dict()

        excluded_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.excluded_items, Unset):
            excluded_items = self.excluded_items.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tenantId": tenant_id,
                "serviceAccountId": service_account_id,
            }
        )
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
        if regions is not UNSET:
            field_dict["regions"] = regions
        if selected_items is not UNSET:
            field_dict["selectedItems"] = selected_items
        if excluded_items is not UNSET:
            field_dict["excludedItems"] = excluded_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_region_from_client import PolicyRegionFromClient
        from ..models.sql_policy_backup_items_from_client import SqlPolicyBackupItemsFromClient
        from ..models.sql_policy_excluded_items_from_client import SqlPolicyExcludedItemsFromClient

        d = dict(src_dict)
        tenant_id = d.pop("tenantId")

        service_account_id = UUID(d.pop("serviceAccountId"))

        _backup_type = d.pop("backupType", UNSET)
        backup_type: BackupTypeNullable | Unset
        if isinstance(_backup_type, Unset):
            backup_type = UNSET
        else:
            backup_type = BackupTypeNullable(_backup_type)

        def _parse_regions(data: object) -> list[PolicyRegionFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                regions_type_0 = []
                _regions_type_0 = data
                for regions_type_0_item_data in _regions_type_0:
                    regions_type_0_item = PolicyRegionFromClient.from_dict(regions_type_0_item_data)

                    regions_type_0.append(regions_type_0_item)

                return regions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PolicyRegionFromClient] | None | Unset, data)

        regions = _parse_regions(d.pop("regions", UNSET))

        _selected_items = d.pop("selectedItems", UNSET)
        selected_items: SqlPolicyBackupItemsFromClient | Unset
        if isinstance(_selected_items, Unset):
            selected_items = UNSET
        else:
            selected_items = SqlPolicyBackupItemsFromClient.from_dict(_selected_items)

        _excluded_items = d.pop("excludedItems", UNSET)
        excluded_items: SqlPolicyExcludedItemsFromClient | Unset
        if isinstance(_excluded_items, Unset):
            excluded_items = UNSET
        else:
            excluded_items = SqlPolicyExcludedItemsFromClient.from_dict(_excluded_items)

        validate_sync_databases_sql_policy_from_client = cls(
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            backup_type=backup_type,
            regions=regions,
            selected_items=selected_items,
            excluded_items=excluded_items,
        )

        return validate_sync_databases_sql_policy_from_client
