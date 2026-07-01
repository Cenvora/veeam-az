from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_type import BackupType

if TYPE_CHECKING:
    from ..models.policy_backup_items_from_client import PolicyBackupItemsFromClient


T = TypeVar("T", bound="SlaPolicyProtectionInfo")


@_attrs_define
class SlaPolicyProtectionInfo:
    r"""
    Attributes:
        tenant_id (UUID):
        service_account_id (UUID):
        selected_items (PolicyBackupItemsFromClient): \[Applies if the *SelectedItems* value is specified for the
            `backupType` parameter] Specifies Azure resources to protect by the backup policy.
        backup_type (BackupType):
    """

    tenant_id: UUID
    service_account_id: UUID
    selected_items: PolicyBackupItemsFromClient
    backup_type: BackupType

    def to_dict(self) -> dict[str, Any]:
        tenant_id = str(self.tenant_id)

        service_account_id = str(self.service_account_id)

        selected_items = self.selected_items.to_dict()

        backup_type = self.backup_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tenantId": tenant_id,
                "serviceAccountId": service_account_id,
                "selectedItems": selected_items,
                "backupType": backup_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_backup_items_from_client import PolicyBackupItemsFromClient

        d = dict(src_dict)
        tenant_id = UUID(d.pop("tenantId"))

        service_account_id = UUID(d.pop("serviceAccountId"))

        selected_items = PolicyBackupItemsFromClient.from_dict(d.pop("selectedItems"))

        backup_type = BackupType(d.pop("backupType"))

        sla_policy_protection_info = cls(
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            selected_items=selected_items,
            backup_type=backup_type,
        )

        return sla_policy_protection_info
