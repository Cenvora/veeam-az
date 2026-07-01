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
    from ..models.daily_file_share_schedule import DailyFileShareSchedule
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.monthly_file_share_schedule import MonthlyFileShareSchedule
    from ..models.policy_notification_settings import PolicyNotificationSettings
    from ..models.retry_settings import RetrySettings
    from ..models.weekly_file_share_schedule import WeeklyFileShareSchedule


T = TypeVar("T", bound="FileSharePolicy")


@_attrs_define
class FileSharePolicy:
    """Information on each backup policy.

    Attributes:
        id (UUID | Unset): System ID assigned to a backup policy in the Veeam Backup for Microsoft Azure REST API.
        priority (int | Unset): Priority number of the backup policy.
        tenant_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a tenant for which the backup
            policy is created.
        service_account_id (UUID | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to a
            service account whose permissions are used to perform backups of Azure file shares.
        snapshot_status (JobStatus | Unset): Specifies the status of the performed session.
        indexing_status (JobStatus | Unset): Specifies the status of the performed session.
        next_execution_time (datetime.datetime | None | Unset): Date and time of the next backup session.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
        name (None | str | Unset): Name of the backup policy.
        description (None | str | Unset): Description of the backup policy.
        is_schedule_configured (bool | Unset): Defines whether the schedule is enabled for the backup policy.
        retry_settings (RetrySettings | Unset): Specifies the retry settings for the backup policy.
        policy_notification_settings (PolicyNotificationSettings | Unset): Specifies the notification settings for the
            backup policy.
        is_enabled (bool | None | Unset): Defines whether to enable the policy.
        enable_indexing (bool | None | Unset): Defines whether the indexing of the processed Azure file shares is
            enabled.
        backup_type (BackupTypeNullable | Unset): Defines whether you want to include to the backup scope all resources
            residing in the specified Azure regions and to which the specified service account has access.
        daily_schedule (DailyFileShareSchedule | Unset): Specifies daily schedule settings for the backup policy.
        weekly_schedule (WeeklyFileShareSchedule | Unset): Specifies weekly schedule settings for the backup policy.
        monthly_schedule (MonthlyFileShareSchedule | Unset): Specifies monthly schedule settings for the backup policy.
    """

    id: UUID | Unset = UNSET
    priority: int | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    service_account_id: UUID | Unset = UNSET
    snapshot_status: JobStatus | Unset = UNSET
    indexing_status: JobStatus | Unset = UNSET
    next_execution_time: datetime.datetime | None | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_schedule_configured: bool | Unset = UNSET
    retry_settings: RetrySettings | Unset = UNSET
    policy_notification_settings: PolicyNotificationSettings | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET
    enable_indexing: bool | None | Unset = UNSET
    backup_type: BackupTypeNullable | Unset = UNSET
    daily_schedule: DailyFileShareSchedule | Unset = UNSET
    weekly_schedule: WeeklyFileShareSchedule | Unset = UNSET
    monthly_schedule: MonthlyFileShareSchedule | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        priority = self.priority

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        service_account_id: str | Unset = UNSET
        if not isinstance(self.service_account_id, Unset):
            service_account_id = str(self.service_account_id)

        snapshot_status: str | Unset = UNSET
        if not isinstance(self.snapshot_status, Unset):
            snapshot_status = self.snapshot_status.value

        indexing_status: str | Unset = UNSET
        if not isinstance(self.indexing_status, Unset):
            indexing_status = self.indexing_status.value

        next_execution_time: None | str | Unset
        if isinstance(self.next_execution_time, Unset):
            next_execution_time = UNSET
        elif isinstance(self.next_execution_time, datetime.datetime):
            next_execution_time = self.next_execution_time.isoformat()
        else:
            next_execution_time = self.next_execution_time

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

        is_schedule_configured = self.is_schedule_configured

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

        enable_indexing: bool | None | Unset
        if isinstance(self.enable_indexing, Unset):
            enable_indexing = UNSET
        else:
            enable_indexing = self.enable_indexing

        backup_type: str | Unset = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value

        daily_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily_schedule, Unset):
            daily_schedule = self.daily_schedule.to_dict()

        weekly_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weekly_schedule, Unset):
            weekly_schedule = self.weekly_schedule.to_dict()

        monthly_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly_schedule, Unset):
            monthly_schedule = self.monthly_schedule.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if snapshot_status is not UNSET:
            field_dict["snapshotStatus"] = snapshot_status
        if indexing_status is not UNSET:
            field_dict["indexingStatus"] = indexing_status
        if next_execution_time is not UNSET:
            field_dict["nextExecutionTime"] = next_execution_time
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_schedule_configured is not UNSET:
            field_dict["isScheduleConfigured"] = is_schedule_configured
        if retry_settings is not UNSET:
            field_dict["retrySettings"] = retry_settings
        if policy_notification_settings is not UNSET:
            field_dict["policyNotificationSettings"] = policy_notification_settings
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if enable_indexing is not UNSET:
            field_dict["enableIndexing"] = enable_indexing
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
        if daily_schedule is not UNSET:
            field_dict["dailySchedule"] = daily_schedule
        if weekly_schedule is not UNSET:
            field_dict["weeklySchedule"] = weekly_schedule
        if monthly_schedule is not UNSET:
            field_dict["monthlySchedule"] = monthly_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_file_share_schedule import DailyFileShareSchedule
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.monthly_file_share_schedule import MonthlyFileShareSchedule
        from ..models.policy_notification_settings import PolicyNotificationSettings
        from ..models.retry_settings import RetrySettings
        from ..models.weekly_file_share_schedule import WeeklyFileShareSchedule

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        priority = d.pop("priority", UNSET)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        _service_account_id = d.pop("serviceAccountId", UNSET)
        service_account_id: UUID | Unset
        if isinstance(_service_account_id, Unset):
            service_account_id = UNSET
        else:
            service_account_id = UUID(_service_account_id)

        _snapshot_status = d.pop("snapshotStatus", UNSET)
        snapshot_status: JobStatus | Unset
        if isinstance(_snapshot_status, Unset):
            snapshot_status = UNSET
        else:
            snapshot_status = JobStatus(_snapshot_status)

        _indexing_status = d.pop("indexingStatus", UNSET)
        indexing_status: JobStatus | Unset
        if isinstance(_indexing_status, Unset):
            indexing_status = UNSET
        else:
            indexing_status = JobStatus(_indexing_status)

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

        is_schedule_configured = d.pop("isScheduleConfigured", UNSET)

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

        def _parse_enable_indexing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_indexing = _parse_enable_indexing(d.pop("enableIndexing", UNSET))

        _backup_type = d.pop("backupType", UNSET)
        backup_type: BackupTypeNullable | Unset
        if isinstance(_backup_type, Unset):
            backup_type = UNSET
        else:
            backup_type = BackupTypeNullable(_backup_type)

        _daily_schedule = d.pop("dailySchedule", UNSET)
        daily_schedule: DailyFileShareSchedule | Unset
        if isinstance(_daily_schedule, Unset):
            daily_schedule = UNSET
        else:
            daily_schedule = DailyFileShareSchedule.from_dict(_daily_schedule)

        _weekly_schedule = d.pop("weeklySchedule", UNSET)
        weekly_schedule: WeeklyFileShareSchedule | Unset
        if isinstance(_weekly_schedule, Unset):
            weekly_schedule = UNSET
        else:
            weekly_schedule = WeeklyFileShareSchedule.from_dict(_weekly_schedule)

        _monthly_schedule = d.pop("monthlySchedule", UNSET)
        monthly_schedule: MonthlyFileShareSchedule | Unset
        if isinstance(_monthly_schedule, Unset):
            monthly_schedule = UNSET
        else:
            monthly_schedule = MonthlyFileShareSchedule.from_dict(_monthly_schedule)

        file_share_policy = cls(
            id=id,
            priority=priority,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            snapshot_status=snapshot_status,
            indexing_status=indexing_status,
            next_execution_time=next_execution_time,
            field_links=field_links,
            name=name,
            description=description,
            is_schedule_configured=is_schedule_configured,
            retry_settings=retry_settings,
            policy_notification_settings=policy_notification_settings,
            is_enabled=is_enabled,
            enable_indexing=enable_indexing,
            backup_type=backup_type,
            daily_schedule=daily_schedule,
            weekly_schedule=weekly_schedule,
            monthly_schedule=monthly_schedule,
        )

        return file_share_policy
