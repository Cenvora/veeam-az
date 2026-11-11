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
    from ..models.daily_schedule import DailySchedule
    from ..models.health_check_schedule import HealthCheckSchedule
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.monthly_schedule import MonthlySchedule
    from ..models.policy_notification_settings import PolicyNotificationSettings
    from ..models.retry_settings import RetrySettings
    from ..models.snapshot_settings import SnapshotSettings
    from ..models.weekly_schedule import WeeklySchedule
    from ..models.yearly_schedule import YearlySchedule


T = TypeVar("T", bound="Policy")


@_attrs_define
class Policy:
    r"""
    Attributes:
        id (UUID): System ID assigned to a backup policy in the Veeam Backup for Microsoft Azure REST API.
        is_backup_configured (bool): Defines whether the backup policy creates backups of the processed Azure VMs.
        service_account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to
            a service account whose permissions are used to perform backups of Azure VMs.
        priority (int | Unset): Priority number of the backup policy.
        excluded_items_count (int | Unset): Number of items excluded from the backup policy.
        tenant_id (None | str | Unset): Tenant ID for which the backup policy is created.
        snapshot_status (JobStatus | Unset): Specifies the status of the performed session.
        backup_status (JobStatus | Unset): Specifies the status of the performed session.
        archive_status (JobStatus | Unset): Specifies the status of the performed session.
        health_check_status (JobStatus | Unset): Specifies the status of the performed session.
        next_execution_time (datetime.datetime | None | Unset): Date and time of the next backup session.
        converted_with_loss (bool | None | Unset): Defines whether the schedule of the backup policy is impossible to
            convert to the new format.
        is_archive_backup_configured (bool | Unset): Defines whether the backup policy creates archive backups of the
            processed Azure VMs.
        is_schedule_configured (bool | Unset): Defines whether the schedule is enabled for the backup policy.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
        name (None | str | Unset): Name of the backup policy.
        description (None | str | Unset): Description of the backup policy.
        retry_settings (RetrySettings | Unset): Specifies the retry settings for the backup policy.
        policy_notification_settings (PolicyNotificationSettings | Unset): Specifies the notification settings for the
            backup policy.
        is_enabled (bool | None | Unset): Defines whether the policy is enabled.
        backup_type (BackupTypeNullable | Unset): Defines whether you want to include to the backup scope all resources
            residing in the specified Azure regions and to which the specified service account has access.
        snapshot_settings (SnapshotSettings | Unset): Specifies cloud-native snapshot settings for the backup policy.
        daily_schedule (DailySchedule | Unset): Specifies the daily schedule settings for the backup policy.
        weekly_schedule (WeeklySchedule | Unset): Specifies the weekly schedule settings for the backup policy.
        monthly_schedule (MonthlySchedule | Unset): Specifies the monthly schedule settings for the backup policy.
        yearly_schedule (YearlySchedule | Unset): Specifies the yearly schedule settings for the backup policy.
        health_check_schedule (HealthCheckSchedule | Unset): \[Applies if backup creation is enabled for the backup
            policy] Specifies the health check schedule settings.
        cbt_reset_time_utc (datetime.datetime | None | Unset): Date and time when the changed block tracking (CBT)
            mechanism was last reset for the backup policy.
    """

    id: UUID
    is_backup_configured: bool
    service_account_id: UUID
    priority: int | Unset = UNSET
    excluded_items_count: int | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    snapshot_status: JobStatus | Unset = UNSET
    backup_status: JobStatus | Unset = UNSET
    archive_status: JobStatus | Unset = UNSET
    health_check_status: JobStatus | Unset = UNSET
    next_execution_time: datetime.datetime | None | Unset = UNSET
    converted_with_loss: bool | None | Unset = UNSET
    is_archive_backup_configured: bool | Unset = UNSET
    is_schedule_configured: bool | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    retry_settings: RetrySettings | Unset = UNSET
    policy_notification_settings: PolicyNotificationSettings | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET
    backup_type: BackupTypeNullable | Unset = UNSET
    snapshot_settings: SnapshotSettings | Unset = UNSET
    daily_schedule: DailySchedule | Unset = UNSET
    weekly_schedule: WeeklySchedule | Unset = UNSET
    monthly_schedule: MonthlySchedule | Unset = UNSET
    yearly_schedule: YearlySchedule | Unset = UNSET
    health_check_schedule: HealthCheckSchedule | Unset = UNSET
    cbt_reset_time_utc: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id = str(self.id)

        is_backup_configured = self.is_backup_configured

        service_account_id = str(self.service_account_id)

        priority = self.priority

        excluded_items_count = self.excluded_items_count

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        snapshot_status: str | Unset = UNSET
        if not isinstance(self.snapshot_status, Unset):
            snapshot_status = self.snapshot_status.value

        backup_status: str | Unset = UNSET
        if not isinstance(self.backup_status, Unset):
            backup_status = self.backup_status.value

        archive_status: str | Unset = UNSET
        if not isinstance(self.archive_status, Unset):
            archive_status = self.archive_status.value

        health_check_status: str | Unset = UNSET
        if not isinstance(self.health_check_status, Unset):
            health_check_status = self.health_check_status.value

        next_execution_time: None | str | Unset
        if isinstance(self.next_execution_time, Unset):
            next_execution_time = UNSET
        elif isinstance(self.next_execution_time, datetime.datetime):
            next_execution_time = self.next_execution_time.isoformat()
        else:
            next_execution_time = self.next_execution_time

        converted_with_loss: bool | None | Unset
        if isinstance(self.converted_with_loss, Unset):
            converted_with_loss = UNSET
        else:
            converted_with_loss = self.converted_with_loss

        is_archive_backup_configured = self.is_archive_backup_configured

        is_schedule_configured = self.is_schedule_configured

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

        daily_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily_schedule, Unset):
            daily_schedule = self.daily_schedule.to_dict()

        weekly_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weekly_schedule, Unset):
            weekly_schedule = self.weekly_schedule.to_dict()

        monthly_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly_schedule, Unset):
            monthly_schedule = self.monthly_schedule.to_dict()

        yearly_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.yearly_schedule, Unset):
            yearly_schedule = self.yearly_schedule.to_dict()

        health_check_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.health_check_schedule, Unset):
            health_check_schedule = self.health_check_schedule.to_dict()

        cbt_reset_time_utc: None | str | Unset
        if isinstance(self.cbt_reset_time_utc, Unset):
            cbt_reset_time_utc = UNSET
        elif isinstance(self.cbt_reset_time_utc, datetime.datetime):
            cbt_reset_time_utc = self.cbt_reset_time_utc.isoformat()
        else:
            cbt_reset_time_utc = self.cbt_reset_time_utc

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "isBackupConfigured": is_backup_configured,
                "serviceAccountId": service_account_id,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if excluded_items_count is not UNSET:
            field_dict["excludedItemsCount"] = excluded_items_count
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if snapshot_status is not UNSET:
            field_dict["snapshotStatus"] = snapshot_status
        if backup_status is not UNSET:
            field_dict["backupStatus"] = backup_status
        if archive_status is not UNSET:
            field_dict["archiveStatus"] = archive_status
        if health_check_status is not UNSET:
            field_dict["healthCheckStatus"] = health_check_status
        if next_execution_time is not UNSET:
            field_dict["nextExecutionTime"] = next_execution_time
        if converted_with_loss is not UNSET:
            field_dict["convertedWithLoss"] = converted_with_loss
        if is_archive_backup_configured is not UNSET:
            field_dict["isArchiveBackupConfigured"] = is_archive_backup_configured
        if is_schedule_configured is not UNSET:
            field_dict["isScheduleConfigured"] = is_schedule_configured
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
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
        if snapshot_settings is not UNSET:
            field_dict["snapshotSettings"] = snapshot_settings
        if daily_schedule is not UNSET:
            field_dict["dailySchedule"] = daily_schedule
        if weekly_schedule is not UNSET:
            field_dict["weeklySchedule"] = weekly_schedule
        if monthly_schedule is not UNSET:
            field_dict["monthlySchedule"] = monthly_schedule
        if yearly_schedule is not UNSET:
            field_dict["yearlySchedule"] = yearly_schedule
        if health_check_schedule is not UNSET:
            field_dict["healthCheckSchedule"] = health_check_schedule
        if cbt_reset_time_utc is not UNSET:
            field_dict["cbtResetTimeUtc"] = cbt_reset_time_utc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_schedule import DailySchedule
        from ..models.health_check_schedule import HealthCheckSchedule
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.monthly_schedule import MonthlySchedule
        from ..models.policy_notification_settings import PolicyNotificationSettings
        from ..models.retry_settings import RetrySettings
        from ..models.snapshot_settings import SnapshotSettings
        from ..models.weekly_schedule import WeeklySchedule
        from ..models.yearly_schedule import YearlySchedule

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        is_backup_configured = d.pop("isBackupConfigured")

        service_account_id = UUID(d.pop("serviceAccountId"))

        priority = d.pop("priority", UNSET)

        excluded_items_count = d.pop("excludedItemsCount", UNSET)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

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

        _archive_status = d.pop("archiveStatus", UNSET)
        archive_status: JobStatus | Unset
        if isinstance(_archive_status, Unset):
            archive_status = UNSET
        else:
            archive_status = JobStatus(_archive_status)

        _health_check_status = d.pop("healthCheckStatus", UNSET)
        health_check_status: JobStatus | Unset
        if isinstance(_health_check_status, Unset):
            health_check_status = UNSET
        else:
            health_check_status = JobStatus(_health_check_status)

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

        def _parse_converted_with_loss(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        converted_with_loss = _parse_converted_with_loss(d.pop("convertedWithLoss", UNSET))

        is_archive_backup_configured = d.pop("isArchiveBackupConfigured", UNSET)

        is_schedule_configured = d.pop("isScheduleConfigured", UNSET)

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

        _daily_schedule = d.pop("dailySchedule", UNSET)
        daily_schedule: DailySchedule | Unset
        if isinstance(_daily_schedule, Unset):
            daily_schedule = UNSET
        else:
            daily_schedule = DailySchedule.from_dict(_daily_schedule)

        _weekly_schedule = d.pop("weeklySchedule", UNSET)
        weekly_schedule: WeeklySchedule | Unset
        if isinstance(_weekly_schedule, Unset):
            weekly_schedule = UNSET
        else:
            weekly_schedule = WeeklySchedule.from_dict(_weekly_schedule)

        _monthly_schedule = d.pop("monthlySchedule", UNSET)
        monthly_schedule: MonthlySchedule | Unset
        if isinstance(_monthly_schedule, Unset):
            monthly_schedule = UNSET
        else:
            monthly_schedule = MonthlySchedule.from_dict(_monthly_schedule)

        _yearly_schedule = d.pop("yearlySchedule", UNSET)
        yearly_schedule: YearlySchedule | Unset
        if isinstance(_yearly_schedule, Unset):
            yearly_schedule = UNSET
        else:
            yearly_schedule = YearlySchedule.from_dict(_yearly_schedule)

        _health_check_schedule = d.pop("healthCheckSchedule", UNSET)
        health_check_schedule: HealthCheckSchedule | Unset
        if isinstance(_health_check_schedule, Unset):
            health_check_schedule = UNSET
        else:
            health_check_schedule = HealthCheckSchedule.from_dict(_health_check_schedule)

        def _parse_cbt_reset_time_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cbt_reset_time_utc_type_0 = isoparse(data)

                return cbt_reset_time_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cbt_reset_time_utc = _parse_cbt_reset_time_utc(d.pop("cbtResetTimeUtc", UNSET))

        policy = cls(
            id=id,
            is_backup_configured=is_backup_configured,
            service_account_id=service_account_id,
            priority=priority,
            excluded_items_count=excluded_items_count,
            tenant_id=tenant_id,
            snapshot_status=snapshot_status,
            backup_status=backup_status,
            archive_status=archive_status,
            health_check_status=health_check_status,
            next_execution_time=next_execution_time,
            converted_with_loss=converted_with_loss,
            is_archive_backup_configured=is_archive_backup_configured,
            is_schedule_configured=is_schedule_configured,
            field_links=field_links,
            name=name,
            description=description,
            retry_settings=retry_settings,
            policy_notification_settings=policy_notification_settings,
            is_enabled=is_enabled,
            backup_type=backup_type,
            snapshot_settings=snapshot_settings,
            daily_schedule=daily_schedule,
            weekly_schedule=weekly_schedule,
            monthly_schedule=monthly_schedule,
            yearly_schedule=yearly_schedule,
            health_check_schedule=health_check_schedule,
            cbt_reset_time_utc=cbt_reset_time_utc,
        )

        return policy
