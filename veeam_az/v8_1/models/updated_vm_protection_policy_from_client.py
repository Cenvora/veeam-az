from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_type_nullable import BackupTypeNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_backup_items_from_client import PolicyBackupItemsFromClient
    from ..models.policy_excluded_items_from_client import PolicyExcludedItemsFromClient
    from ..models.policy_notification_settings import PolicyNotificationSettings
    from ..models.policy_region_from_client import PolicyRegionFromClient
    from ..models.retry_settings import RetrySettings
    from ..models.sla_policy_notification_settings import SlaPolicyNotificationSettings
    from ..models.snapshot_destination import SnapshotDestination
    from ..models.snapshot_settings import SnapshotSettings


T = TypeVar("T", bound="UpdatedVmProtectionPolicyFromClient")


@_attrs_define
class UpdatedVmProtectionPolicyFromClient:
    r"""
    Attributes:
        regions (list[PolicyRegionFromClient]): Specifies a list of regions where the backed-up Azure VM reside.
        name (str): Specifies a name for the backup policy.
        is_enabled (bool | None): Defines whether to enable the policy.
        snapshot_settings (SnapshotSettings): Specifies cloud-native snapshot settings for the backup policy.
        tenant_id (None | str | Unset): Specifies the tenant ID to which the resources protected by the policy belong.
        service_account_id (None | Unset | UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft
            Azure REST API to the service account whose permissions will be used to perform backups of Azure VMs.
        selected_items (PolicyBackupItemsFromClient | Unset): \[Applies if the *SelectedItems* value is specified for
            the `backupType` parameter] Specifies Azure resources to protect by the backup policy.
        excluded_items (PolicyExcludedItemsFromClient | Unset): Specifies Azure tags to identify the resources that
            should be excluded from the backup scope.
        description (None | str | Unset): Specifies a description for the policy.
        retry_settings (RetrySettings | Unset): Specifies the retry settings for the backup policy.
        policy_notification_settings (PolicyNotificationSettings | Unset): Specifies the notification settings for the
            backup policy.
        sla_policy_notification_settings (SlaPolicyNotificationSettings | Unset):
        backup_type (BackupTypeNullable | Unset): Defines whether you want to include to the backup scope all resources
            residing in the specified Azure regions and to which the specified service account has access.
        sla_policy_template_id (UUID | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure
            REST API to the SLA template that will be assigned to the policy.
        storage_policy_template_id (None | Unset | UUID): Specifies the system ID assigned in the Veeam Backup for
            Microsoft Azure REST API to the storage template that will be assigned to the policy.
        snapshot_destinations (list[SnapshotDestination] | None | Unset): Specifies the target location settings for
            cloud-native snapshots.
    """

    regions: list[PolicyRegionFromClient]
    name: str
    is_enabled: bool | None
    snapshot_settings: SnapshotSettings
    tenant_id: None | str | Unset = UNSET
    service_account_id: None | Unset | UUID = UNSET
    selected_items: PolicyBackupItemsFromClient | Unset = UNSET
    excluded_items: PolicyExcludedItemsFromClient | Unset = UNSET
    description: None | str | Unset = UNSET
    retry_settings: RetrySettings | Unset = UNSET
    policy_notification_settings: PolicyNotificationSettings | Unset = UNSET
    sla_policy_notification_settings: SlaPolicyNotificationSettings | Unset = UNSET
    backup_type: BackupTypeNullable | Unset = UNSET
    sla_policy_template_id: UUID | Unset = UNSET
    storage_policy_template_id: None | Unset | UUID = UNSET
    snapshot_destinations: list[SnapshotDestination] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()
            regions.append(regions_item)

        name = self.name

        is_enabled: bool | None
        is_enabled = self.is_enabled

        snapshot_settings = self.snapshot_settings.to_dict()

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        service_account_id: None | str | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        elif isinstance(self.service_account_id, UUID):
            service_account_id = str(self.service_account_id)
        else:
            service_account_id = self.service_account_id

        selected_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selected_items, Unset):
            selected_items = self.selected_items.to_dict()

        excluded_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.excluded_items, Unset):
            excluded_items = self.excluded_items.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        retry_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_settings, Unset):
            retry_settings = self.retry_settings.to_dict()

        policy_notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy_notification_settings, Unset):
            policy_notification_settings = self.policy_notification_settings.to_dict()

        sla_policy_notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sla_policy_notification_settings, Unset):
            sla_policy_notification_settings = self.sla_policy_notification_settings.to_dict()

        backup_type: str | Unset = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value

        sla_policy_template_id: str | Unset = UNSET
        if not isinstance(self.sla_policy_template_id, Unset):
            sla_policy_template_id = str(self.sla_policy_template_id)

        storage_policy_template_id: None | str | Unset
        if isinstance(self.storage_policy_template_id, Unset):
            storage_policy_template_id = UNSET
        elif isinstance(self.storage_policy_template_id, UUID):
            storage_policy_template_id = str(self.storage_policy_template_id)
        else:
            storage_policy_template_id = self.storage_policy_template_id

        snapshot_destinations: list[dict[str, Any]] | None | Unset
        if isinstance(self.snapshot_destinations, Unset):
            snapshot_destinations = UNSET
        elif isinstance(self.snapshot_destinations, list):
            snapshot_destinations = []
            for snapshot_destinations_type_0_item_data in self.snapshot_destinations:
                snapshot_destinations_type_0_item = snapshot_destinations_type_0_item_data.to_dict()
                snapshot_destinations.append(snapshot_destinations_type_0_item)

        else:
            snapshot_destinations = self.snapshot_destinations

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "regions": regions,
                "name": name,
                "isEnabled": is_enabled,
                "snapshotSettings": snapshot_settings,
            }
        )
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if selected_items is not UNSET:
            field_dict["selectedItems"] = selected_items
        if excluded_items is not UNSET:
            field_dict["excludedItems"] = excluded_items
        if description is not UNSET:
            field_dict["description"] = description
        if retry_settings is not UNSET:
            field_dict["retrySettings"] = retry_settings
        if policy_notification_settings is not UNSET:
            field_dict["policyNotificationSettings"] = policy_notification_settings
        if sla_policy_notification_settings is not UNSET:
            field_dict["slaPolicyNotificationSettings"] = sla_policy_notification_settings
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
        if sla_policy_template_id is not UNSET:
            field_dict["slaPolicyTemplateId"] = sla_policy_template_id
        if storage_policy_template_id is not UNSET:
            field_dict["storagePolicyTemplateId"] = storage_policy_template_id
        if snapshot_destinations is not UNSET:
            field_dict["snapshotDestinations"] = snapshot_destinations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_backup_items_from_client import PolicyBackupItemsFromClient
        from ..models.policy_excluded_items_from_client import PolicyExcludedItemsFromClient
        from ..models.policy_notification_settings import PolicyNotificationSettings
        from ..models.policy_region_from_client import PolicyRegionFromClient
        from ..models.retry_settings import RetrySettings
        from ..models.sla_policy_notification_settings import SlaPolicyNotificationSettings
        from ..models.snapshot_destination import SnapshotDestination
        from ..models.snapshot_settings import SnapshotSettings

        d = dict(src_dict)
        regions = []
        _regions = d.pop("regions")
        for regions_item_data in _regions:
            regions_item = PolicyRegionFromClient.from_dict(regions_item_data)

            regions.append(regions_item)

        name = d.pop("name")

        def _parse_is_enabled(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled"))

        snapshot_settings = SnapshotSettings.from_dict(d.pop("snapshotSettings"))

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

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

        _selected_items = d.pop("selectedItems", UNSET)
        selected_items: PolicyBackupItemsFromClient | Unset
        if isinstance(_selected_items, Unset):
            selected_items = UNSET
        else:
            selected_items = PolicyBackupItemsFromClient.from_dict(_selected_items)

        _excluded_items = d.pop("excludedItems", UNSET)
        excluded_items: PolicyExcludedItemsFromClient | Unset
        if isinstance(_excluded_items, Unset):
            excluded_items = UNSET
        else:
            excluded_items = PolicyExcludedItemsFromClient.from_dict(_excluded_items)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _retry_settings = d.pop("retrySettings", UNSET)
        retry_settings: RetrySettings | Unset
        if isinstance(_retry_settings, Unset):
            retry_settings = UNSET
        else:
            retry_settings = RetrySettings.from_dict(_retry_settings)

        _policy_notification_settings = d.pop("policyNotificationSettings", UNSET)
        policy_notification_settings: PolicyNotificationSettings | Unset
        if isinstance(_policy_notification_settings, Unset):
            policy_notification_settings = UNSET
        else:
            policy_notification_settings = PolicyNotificationSettings.from_dict(_policy_notification_settings)

        _sla_policy_notification_settings = d.pop("slaPolicyNotificationSettings", UNSET)
        sla_policy_notification_settings: SlaPolicyNotificationSettings | Unset
        if isinstance(_sla_policy_notification_settings, Unset):
            sla_policy_notification_settings = UNSET
        else:
            sla_policy_notification_settings = SlaPolicyNotificationSettings.from_dict(
                _sla_policy_notification_settings
            )

        _backup_type = d.pop("backupType", UNSET)
        backup_type: BackupTypeNullable | Unset
        if isinstance(_backup_type, Unset):
            backup_type = UNSET
        else:
            backup_type = BackupTypeNullable(_backup_type)

        _sla_policy_template_id = d.pop("slaPolicyTemplateId", UNSET)
        sla_policy_template_id: UUID | Unset
        if isinstance(_sla_policy_template_id, Unset):
            sla_policy_template_id = UNSET
        else:
            sla_policy_template_id = UUID(_sla_policy_template_id)

        def _parse_storage_policy_template_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_policy_template_id_type_0 = UUID(data)

                return storage_policy_template_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        storage_policy_template_id = _parse_storage_policy_template_id(d.pop("storagePolicyTemplateId", UNSET))

        def _parse_snapshot_destinations(data: object) -> list[SnapshotDestination] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                snapshot_destinations_type_0 = []
                _snapshot_destinations_type_0 = data
                for snapshot_destinations_type_0_item_data in _snapshot_destinations_type_0:
                    snapshot_destinations_type_0_item = SnapshotDestination.from_dict(
                        snapshot_destinations_type_0_item_data
                    )

                    snapshot_destinations_type_0.append(snapshot_destinations_type_0_item)

                return snapshot_destinations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SnapshotDestination] | None | Unset, data)

        snapshot_destinations = _parse_snapshot_destinations(d.pop("snapshotDestinations", UNSET))

        updated_vm_protection_policy_from_client = cls(
            regions=regions,
            name=name,
            is_enabled=is_enabled,
            snapshot_settings=snapshot_settings,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            selected_items=selected_items,
            excluded_items=excluded_items,
            description=description,
            retry_settings=retry_settings,
            policy_notification_settings=policy_notification_settings,
            sla_policy_notification_settings=sla_policy_notification_settings,
            backup_type=backup_type,
            sla_policy_template_id=sla_policy_template_id,
            storage_policy_template_id=storage_policy_template_id,
            snapshot_destinations=snapshot_destinations,
        )

        return updated_vm_protection_policy_from_client
