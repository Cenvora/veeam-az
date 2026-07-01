from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.policy_notification_settings import PolicyNotificationSettings
    from ..models.vnet_policy_additional_protected_resources import VnetPolicyAdditionalProtectedResources
    from ..models.vnet_policy_auto_discovered_protected_resources import VnetPolicyAutoDiscoveredProtectedResources


T = TypeVar("T", bound="VnetPolicy")


@_attrs_define
class VnetPolicy:
    r"""Information on the virtual network configuration backup policy.

    Attributes:
        id (UUID | Unset): System ID assigned to the backup policy in the Veeam Backup for Microsoft Azure REST API.
        name (None | str | Unset): Name of the backup policy.
        is_enabled (bool | Unset): Defines whether the policy is enabled.
        auto_discover_subscriptions (bool | Unset): Defines whether automatic protection of Azure subscriptions is
            enabled for the policy.
        auto_discovered_protected_resources (list[VnetPolicyAutoDiscoveredProtectedResources] | None | Unset):
            Information on a service account whose permissions are used to perform virtual network configuration backup, and
            on the automatically protected subscriptions.
        additional_protected_resources (list[VnetPolicyAdditionalProtectedResources] | None | Unset): Information on a
            service account whose permissions are used to perform virtual network configuration backup, and on the
            subscriptions manually added to the virtual network configuration backup policy.
        next_execution_time (datetime.datetime | None | Unset): Date and time of the next backup session.
        is_schedule_configured (bool | Unset): Defines whether the schedule is enabled for the backup policy.
        backup_interval_minutes (int | None | Unset): \[Applies only if no value has been specified for the
            `backupIntervalHours` parameter] Time interval (in minutes) at which the backup policy will be collecting data.
        backup_interval_hours (int | None | Unset): \[Applies only if no value has been specified for the
            `backupIntervalMinutes` parameter] Time interval (in hours) at which the backup policy will be collecting data.
        retention_period_days (int | None | Unset): \[Applies only if no values have been specified for parameters
            `retentionPeriodWeeks` and `retentionPeriodMonths`] Time period (in days) for which the backups will be kept in
            the Veeam Backup for Microsoft Azure configuration database.
        retention_period_weeks (int | None | Unset): \[Applies only if no values have been specified for parameters
            `retentionPeriodDays` and `retentionPeriodMonths`] Time period (in weeks) for which the backups will be kept in
            the Veeam Backup for Microsoft Azure configuration database.
        retention_period_months (int | None | Unset): \[Applies only if no values have been specified for parameters
            `retentionPeriodDays` and `retentionPeriodWeeks`] Time period (in months) for which the backups will be kept in
            the Veeam Backup for Microsoft Azure configuration database.
        target_repository_id (None | str | Unset): System ID assigned to the repository in the Veeam Backup for
            Microsoft Azure REST API.
        policy_notification_settings (PolicyNotificationSettings | Unset): Specifies the notification settings for the
            backup policy.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    auto_discover_subscriptions: bool | Unset = UNSET
    auto_discovered_protected_resources: list[VnetPolicyAutoDiscoveredProtectedResources] | None | Unset = UNSET
    additional_protected_resources: list[VnetPolicyAdditionalProtectedResources] | None | Unset = UNSET
    next_execution_time: datetime.datetime | None | Unset = UNSET
    is_schedule_configured: bool | Unset = UNSET
    backup_interval_minutes: int | None | Unset = UNSET
    backup_interval_hours: int | None | Unset = UNSET
    retention_period_days: int | None | Unset = UNSET
    retention_period_weeks: int | None | Unset = UNSET
    retention_period_months: int | None | Unset = UNSET
    target_repository_id: None | str | Unset = UNSET
    policy_notification_settings: PolicyNotificationSettings | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_enabled = self.is_enabled

        auto_discover_subscriptions = self.auto_discover_subscriptions

        auto_discovered_protected_resources: list[dict[str, Any]] | None | Unset
        if isinstance(self.auto_discovered_protected_resources, Unset):
            auto_discovered_protected_resources = UNSET
        elif isinstance(self.auto_discovered_protected_resources, list):
            auto_discovered_protected_resources = []
            for auto_discovered_protected_resources_type_0_item_data in self.auto_discovered_protected_resources:
                auto_discovered_protected_resources_type_0_item = (
                    auto_discovered_protected_resources_type_0_item_data.to_dict()
                )
                auto_discovered_protected_resources.append(auto_discovered_protected_resources_type_0_item)

        else:
            auto_discovered_protected_resources = self.auto_discovered_protected_resources

        additional_protected_resources: list[dict[str, Any]] | None | Unset
        if isinstance(self.additional_protected_resources, Unset):
            additional_protected_resources = UNSET
        elif isinstance(self.additional_protected_resources, list):
            additional_protected_resources = []
            for additional_protected_resources_type_0_item_data in self.additional_protected_resources:
                additional_protected_resources_type_0_item = additional_protected_resources_type_0_item_data.to_dict()
                additional_protected_resources.append(additional_protected_resources_type_0_item)

        else:
            additional_protected_resources = self.additional_protected_resources

        next_execution_time: None | str | Unset
        if isinstance(self.next_execution_time, Unset):
            next_execution_time = UNSET
        elif isinstance(self.next_execution_time, datetime.datetime):
            next_execution_time = self.next_execution_time.isoformat()
        else:
            next_execution_time = self.next_execution_time

        is_schedule_configured = self.is_schedule_configured

        backup_interval_minutes: int | None | Unset
        if isinstance(self.backup_interval_minutes, Unset):
            backup_interval_minutes = UNSET
        else:
            backup_interval_minutes = self.backup_interval_minutes

        backup_interval_hours: int | None | Unset
        if isinstance(self.backup_interval_hours, Unset):
            backup_interval_hours = UNSET
        else:
            backup_interval_hours = self.backup_interval_hours

        retention_period_days: int | None | Unset
        if isinstance(self.retention_period_days, Unset):
            retention_period_days = UNSET
        else:
            retention_period_days = self.retention_period_days

        retention_period_weeks: int | None | Unset
        if isinstance(self.retention_period_weeks, Unset):
            retention_period_weeks = UNSET
        else:
            retention_period_weeks = self.retention_period_weeks

        retention_period_months: int | None | Unset
        if isinstance(self.retention_period_months, Unset):
            retention_period_months = UNSET
        else:
            retention_period_months = self.retention_period_months

        target_repository_id: None | str | Unset
        if isinstance(self.target_repository_id, Unset):
            target_repository_id = UNSET
        else:
            target_repository_id = self.target_repository_id

        policy_notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy_notification_settings, Unset):
            policy_notification_settings = self.policy_notification_settings.to_dict()

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
        if name is not UNSET:
            field_dict["name"] = name
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if auto_discover_subscriptions is not UNSET:
            field_dict["autoDiscoverSubscriptions"] = auto_discover_subscriptions
        if auto_discovered_protected_resources is not UNSET:
            field_dict["autoDiscoveredProtectedResources"] = auto_discovered_protected_resources
        if additional_protected_resources is not UNSET:
            field_dict["additionalProtectedResources"] = additional_protected_resources
        if next_execution_time is not UNSET:
            field_dict["nextExecutionTime"] = next_execution_time
        if is_schedule_configured is not UNSET:
            field_dict["isScheduleConfigured"] = is_schedule_configured
        if backup_interval_minutes is not UNSET:
            field_dict["backupIntervalMinutes"] = backup_interval_minutes
        if backup_interval_hours is not UNSET:
            field_dict["backupIntervalHours"] = backup_interval_hours
        if retention_period_days is not UNSET:
            field_dict["retentionPeriodDays"] = retention_period_days
        if retention_period_weeks is not UNSET:
            field_dict["retentionPeriodWeeks"] = retention_period_weeks
        if retention_period_months is not UNSET:
            field_dict["retentionPeriodMonths"] = retention_period_months
        if target_repository_id is not UNSET:
            field_dict["targetRepositoryId"] = target_repository_id
        if policy_notification_settings is not UNSET:
            field_dict["policyNotificationSettings"] = policy_notification_settings
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.policy_notification_settings import PolicyNotificationSettings
        from ..models.vnet_policy_additional_protected_resources import VnetPolicyAdditionalProtectedResources
        from ..models.vnet_policy_auto_discovered_protected_resources import VnetPolicyAutoDiscoveredProtectedResources

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        is_enabled = d.pop("isEnabled", UNSET)

        auto_discover_subscriptions = d.pop("autoDiscoverSubscriptions", UNSET)

        def _parse_auto_discovered_protected_resources(
            data: object,
        ) -> list[VnetPolicyAutoDiscoveredProtectedResources] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                auto_discovered_protected_resources_type_0 = []
                _auto_discovered_protected_resources_type_0 = data
                for auto_discovered_protected_resources_type_0_item_data in _auto_discovered_protected_resources_type_0:
                    auto_discovered_protected_resources_type_0_item = (
                        VnetPolicyAutoDiscoveredProtectedResources.from_dict(
                            auto_discovered_protected_resources_type_0_item_data
                        )
                    )

                    auto_discovered_protected_resources_type_0.append(auto_discovered_protected_resources_type_0_item)

                return auto_discovered_protected_resources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VnetPolicyAutoDiscoveredProtectedResources] | None | Unset, data)

        auto_discovered_protected_resources = _parse_auto_discovered_protected_resources(
            d.pop("autoDiscoveredProtectedResources", UNSET)
        )

        def _parse_additional_protected_resources(
            data: object,
        ) -> list[VnetPolicyAdditionalProtectedResources] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_protected_resources_type_0 = []
                _additional_protected_resources_type_0 = data
                for additional_protected_resources_type_0_item_data in _additional_protected_resources_type_0:
                    additional_protected_resources_type_0_item = VnetPolicyAdditionalProtectedResources.from_dict(
                        additional_protected_resources_type_0_item_data
                    )

                    additional_protected_resources_type_0.append(additional_protected_resources_type_0_item)

                return additional_protected_resources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VnetPolicyAdditionalProtectedResources] | None | Unset, data)

        additional_protected_resources = _parse_additional_protected_resources(
            d.pop("additionalProtectedResources", UNSET)
        )

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

        is_schedule_configured = d.pop("isScheduleConfigured", UNSET)

        def _parse_backup_interval_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_interval_minutes = _parse_backup_interval_minutes(d.pop("backupIntervalMinutes", UNSET))

        def _parse_backup_interval_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_interval_hours = _parse_backup_interval_hours(d.pop("backupIntervalHours", UNSET))

        def _parse_retention_period_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_period_days = _parse_retention_period_days(d.pop("retentionPeriodDays", UNSET))

        def _parse_retention_period_weeks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_period_weeks = _parse_retention_period_weeks(d.pop("retentionPeriodWeeks", UNSET))

        def _parse_retention_period_months(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_period_months = _parse_retention_period_months(d.pop("retentionPeriodMonths", UNSET))

        def _parse_target_repository_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_repository_id = _parse_target_repository_id(d.pop("targetRepositoryId", UNSET))

        _policy_notification_settings = d.pop("policyNotificationSettings", UNSET)
        policy_notification_settings: PolicyNotificationSettings | Unset
        if isinstance(_policy_notification_settings, Unset):
            policy_notification_settings = UNSET
        else:
            policy_notification_settings = PolicyNotificationSettings.from_dict(_policy_notification_settings)

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

        vnet_policy = cls(
            id=id,
            name=name,
            is_enabled=is_enabled,
            auto_discover_subscriptions=auto_discover_subscriptions,
            auto_discovered_protected_resources=auto_discovered_protected_resources,
            additional_protected_resources=additional_protected_resources,
            next_execution_time=next_execution_time,
            is_schedule_configured=is_schedule_configured,
            backup_interval_minutes=backup_interval_minutes,
            backup_interval_hours=backup_interval_hours,
            retention_period_days=retention_period_days,
            retention_period_weeks=retention_period_weeks,
            retention_period_months=retention_period_months,
            target_repository_id=target_repository_id,
            policy_notification_settings=policy_notification_settings,
            field_links=field_links,
        )

        return vnet_policy
