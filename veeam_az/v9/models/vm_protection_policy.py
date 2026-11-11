from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.backup_type_nullable import BackupTypeNullable
from ..models.job_status import JobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.policy_notification_settings import PolicyNotificationSettings
    from ..models.retry_settings import RetrySettings
    from ..models.sla_policy_notification_settings import SlaPolicyNotificationSettings
    from ..models.snapshot_destination import SnapshotDestination
    from ..models.snapshot_settings import SnapshotSettings


T = TypeVar("T", bound="VmProtectionPolicy")


@_attrs_define
class VmProtectionPolicy:
    """
    Attributes:
        id (UUID): System ID assigned to an SLA-based backup policy in the Veeam Backup for Microsoft Azure REST API.
        service_account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to
            a service account whose permissions are used to perform backups of Azure VMs.
        is_backup_configured (bool): Defines whether backups are configured for the policy.
        priority (int | Unset): Priority ordinal number of the SLA-based backup policy.
        excluded_items_count (int | Unset): Number of items excluded from the policy.
        tenant_id (None | str | Unset): Tenant ID to which the resources protected by the policy belong.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
        name (None | str | Unset): Name of the policy.
        description (None | str | Unset): Description of the policy.
        retry_settings (RetrySettings | Unset): Specifies the retry settings for the backup policy.
        policy_notification_settings (PolicyNotificationSettings | Unset): Specifies the notification settings for the
            backup policy.
        sla_policy_notification_settings (None | SlaPolicyNotificationSettings | Unset):
        is_enabled (bool | None | Unset): Defines whether the policy is enabled.
        backup_type (BackupTypeNullable | Unset): Defines whether you want to include to the backup scope all resources
            residing in the specified Azure regions and to which the specified service account has access.
        snapshot_settings (SnapshotSettings | Unset): Specifies cloud-native snapshot settings for the backup policy.
        snapshot_status (JobStatus | Unset): Specifies the status of the performed session.
        backup_status (JobStatus | Unset): Specifies the status of the performed session.
        next_execution_time (datetime.datetime | None | Unset): Date and time of the next backup session.
        sla_policy_template_id (UUID | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to
            the SLA template assigned to the policy.
        storage_policy_template_id (None | Unset | UUID): System ID assigned in the Veeam Backup for Microsoft Azure
            REST API to the storage template assigned to the policy.
        snapshot_destinations (list[SnapshotDestination] | Unset): Specifies the target location settings for cloud-
            native snapshots.
    """

    id: UUID
    service_account_id: UUID
    is_backup_configured: bool
    priority: int | Unset = UNSET
    excluded_items_count: int | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    retry_settings: RetrySettings | Unset = UNSET
    policy_notification_settings: PolicyNotificationSettings | Unset = UNSET
    sla_policy_notification_settings: None | SlaPolicyNotificationSettings | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET
    backup_type: BackupTypeNullable | Unset = UNSET
    snapshot_settings: SnapshotSettings | Unset = UNSET
    snapshot_status: JobStatus | Unset = UNSET
    backup_status: JobStatus | Unset = UNSET
    next_execution_time: datetime.datetime | None | Unset = UNSET
    sla_policy_template_id: UUID | Unset = UNSET
    storage_policy_template_id: None | Unset | UUID = UNSET
    snapshot_destinations: list[SnapshotDestination] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.sla_policy_notification_settings import SlaPolicyNotificationSettings

        id = str(self.id)

        service_account_id = str(self.service_account_id)

        is_backup_configured = self.is_backup_configured

        priority = self.priority

        excluded_items_count = self.excluded_items_count

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        sla_policy_notification_settings: dict[str, Any] | None | Unset
        if isinstance(self.sla_policy_notification_settings, Unset):
            sla_policy_notification_settings = UNSET
        elif isinstance(self.sla_policy_notification_settings, SlaPolicyNotificationSettings):
            sla_policy_notification_settings = self.sla_policy_notification_settings.to_dict()
        else:
            sla_policy_notification_settings = self.sla_policy_notification_settings

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        backup_type: str | Unset = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value

        snapshot_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot_settings, Unset):
            snapshot_settings = self.snapshot_settings.to_dict()

        snapshot_status: str | Unset = UNSET
        if not isinstance(self.snapshot_status, Unset):
            snapshot_status = self.snapshot_status.value

        backup_status: str | Unset = UNSET
        if not isinstance(self.backup_status, Unset):
            backup_status = self.backup_status.value

        next_execution_time: None | str | Unset
        if isinstance(self.next_execution_time, Unset):
            next_execution_time = UNSET
        elif isinstance(self.next_execution_time, datetime.datetime):
            next_execution_time = self.next_execution_time.isoformat()
        else:
            next_execution_time = self.next_execution_time

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

        snapshot_destinations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.snapshot_destinations, Unset):
            snapshot_destinations = []
            for snapshot_destinations_item_data in self.snapshot_destinations:
                snapshot_destinations_item = snapshot_destinations_item_data.to_dict()
                snapshot_destinations.append(snapshot_destinations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "serviceAccountId": service_account_id,
                "isBackupConfigured": is_backup_configured,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if excluded_items_count is not UNSET:
            field_dict["excludedItemsCount"] = excluded_items_count
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if retry_settings is not UNSET:
            field_dict["retrySettings"] = retry_settings
        if policy_notification_settings is not UNSET:
            field_dict["policyNotificationSettings"] = policy_notification_settings
        if sla_policy_notification_settings is not UNSET:
            field_dict["slaPolicyNotificationSettings"] = sla_policy_notification_settings
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
        if snapshot_settings is not UNSET:
            field_dict["snapshotSettings"] = snapshot_settings
        if snapshot_status is not UNSET:
            field_dict["snapshotStatus"] = snapshot_status
        if backup_status is not UNSET:
            field_dict["backupStatus"] = backup_status
        if next_execution_time is not UNSET:
            field_dict["nextExecutionTime"] = next_execution_time
        if sla_policy_template_id is not UNSET:
            field_dict["slaPolicyTemplateId"] = sla_policy_template_id
        if storage_policy_template_id is not UNSET:
            field_dict["storagePolicyTemplateId"] = storage_policy_template_id
        if snapshot_destinations is not UNSET:
            field_dict["snapshotDestinations"] = snapshot_destinations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.policy_notification_settings import PolicyNotificationSettings
        from ..models.retry_settings import RetrySettings
        from ..models.sla_policy_notification_settings import SlaPolicyNotificationSettings
        from ..models.snapshot_destination import SnapshotDestination
        from ..models.snapshot_settings import SnapshotSettings

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        service_account_id = UUID(d.pop("serviceAccountId"))

        is_backup_configured = d.pop("isBackupConfigured")

        priority = d.pop("priority", UNSET)

        excluded_items_count = d.pop("excludedItemsCount", UNSET)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_sla_policy_notification_settings(data: object) -> None | SlaPolicyNotificationSettings | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sla_policy_notification_settings_type_1 = SlaPolicyNotificationSettings.from_dict(data)

                return sla_policy_notification_settings_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SlaPolicyNotificationSettings | Unset, data)

        sla_policy_notification_settings = _parse_sla_policy_notification_settings(
            d.pop("slaPolicyNotificationSettings", UNSET)
        )

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        _backup_type = d.pop("backupType", UNSET)
        backup_type: BackupTypeNullable | Unset
        if isinstance(_backup_type, Unset):
            backup_type = UNSET
        else:
            backup_type = BackupTypeNullable(_backup_type)

        _snapshot_settings = d.pop("snapshotSettings", UNSET)
        snapshot_settings: SnapshotSettings | Unset
        if isinstance(_snapshot_settings, Unset):
            snapshot_settings = UNSET
        else:
            snapshot_settings = SnapshotSettings.from_dict(_snapshot_settings)

        _snapshot_status = d.pop("snapshotStatus", UNSET)
        snapshot_status: JobStatus | Unset
        if isinstance(_snapshot_status, Unset):
            snapshot_status = UNSET
        else:
            snapshot_status = JobStatus(_snapshot_status)

        _backup_status = d.pop("backupStatus", UNSET)
        backup_status: JobStatus | Unset
        if isinstance(_backup_status, Unset):
            backup_status = UNSET
        else:
            backup_status = JobStatus(_backup_status)

        def _parse_next_execution_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_execution_time_type_0 = isoparse(data)

                return next_execution_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_execution_time = _parse_next_execution_time(d.pop("nextExecutionTime", UNSET))

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

        _snapshot_destinations = d.pop("snapshotDestinations", UNSET)
        snapshot_destinations: list[SnapshotDestination] | Unset = UNSET
        if _snapshot_destinations is not UNSET:
            snapshot_destinations = []
            for snapshot_destinations_item_data in _snapshot_destinations:
                snapshot_destinations_item = SnapshotDestination.from_dict(snapshot_destinations_item_data)

                snapshot_destinations.append(snapshot_destinations_item)

        vm_protection_policy = cls(
            id=id,
            service_account_id=service_account_id,
            is_backup_configured=is_backup_configured,
            priority=priority,
            excluded_items_count=excluded_items_count,
            tenant_id=tenant_id,
            field_links=field_links,
            name=name,
            description=description,
            retry_settings=retry_settings,
            policy_notification_settings=policy_notification_settings,
            sla_policy_notification_settings=sla_policy_notification_settings,
            is_enabled=is_enabled,
            backup_type=backup_type,
            snapshot_settings=snapshot_settings,
            snapshot_status=snapshot_status,
            backup_status=backup_status,
            next_execution_time=next_execution_time,
            sla_policy_template_id=sla_policy_template_id,
            storage_policy_template_id=storage_policy_template_id,
            snapshot_destinations=snapshot_destinations,
        )

        return vm_protection_policy
