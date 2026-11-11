from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_type_nullable import BackupTypeNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cosmos_db_policy_backup_items_from_client import CosmosDbPolicyBackupItemsFromClient
    from ..models.cosmos_db_policy_excluded_items_from_client import CosmosDbPolicyExcludedItemsFromClient


T = TypeVar("T", bound="ExpandToCosmosDbAccountOptions")


@_attrs_define
class ExpandToCosmosDbAccountOptions:
    """
    Attributes:
        tenant_id (UUID):
        service_account_id (UUID):
        region_ids (list[str]):
        backup_type (BackupTypeNullable): Defines whether you want to include to the backup scope all resources residing
            in the specified Azure regions and to which the specified service account has access.
        selected_items (CosmosDbPolicyBackupItemsFromClient | Unset): Specifies information on Azure resources to
            protect by the backup policy.
        excluded_items (CosmosDbPolicyExcludedItemsFromClient | Unset): Specifies Azure resources to exclude from the
            backup scope.
    """

    tenant_id: UUID
    service_account_id: UUID
    region_ids: list[str]
    backup_type: BackupTypeNullable
    selected_items: CosmosDbPolicyBackupItemsFromClient | Unset = UNSET
    excluded_items: CosmosDbPolicyExcludedItemsFromClient | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tenant_id = str(self.tenant_id)

        service_account_id = str(self.service_account_id)

        region_ids = self.region_ids

        backup_type = self.backup_type.value

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
                "regionIds": region_ids,
                "backupType": backup_type,
            }
        )
        if selected_items is not UNSET:
            field_dict["selectedItems"] = selected_items
        if excluded_items is not UNSET:
            field_dict["excludedItems"] = excluded_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cosmos_db_policy_backup_items_from_client import CosmosDbPolicyBackupItemsFromClient
        from ..models.cosmos_db_policy_excluded_items_from_client import CosmosDbPolicyExcludedItemsFromClient

        d = dict(src_dict)
        tenant_id = UUID(d.pop("tenantId"))

        service_account_id = UUID(d.pop("serviceAccountId"))

        region_ids = cast(list[str], d.pop("regionIds"))

        backup_type = BackupTypeNullable(d.pop("backupType"))

        _selected_items = d.pop("selectedItems", UNSET)
        selected_items: CosmosDbPolicyBackupItemsFromClient | Unset
        if isinstance(_selected_items, Unset):
            selected_items = UNSET
        else:
            selected_items = CosmosDbPolicyBackupItemsFromClient.from_dict(_selected_items)

        _excluded_items = d.pop("excludedItems", UNSET)
        excluded_items: CosmosDbPolicyExcludedItemsFromClient | Unset
        if isinstance(_excluded_items, Unset):
            excluded_items = UNSET
        else:
            excluded_items = CosmosDbPolicyExcludedItemsFromClient.from_dict(_excluded_items)

        expand_to_cosmos_db_account_options = cls(
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            region_ids=region_ids,
            backup_type=backup_type,
            selected_items=selected_items,
            excluded_items=excluded_items,
        )

        return expand_to_cosmos_db_account_options
