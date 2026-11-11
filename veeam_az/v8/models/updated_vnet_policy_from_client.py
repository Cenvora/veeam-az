from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_notification_settings import PolicyNotificationSettings
    from ..models.vnet_policy_additional_protected_resources_from_client import (
        VnetPolicyAdditionalProtectedResourcesFromClient,
    )


T = TypeVar("T", bound="UpdatedVnetPolicyFromClient")


@_attrs_define
class UpdatedVnetPolicyFromClient:
    """
    Attributes:
        is_enabled (bool | None): Defines whether to enable the policy.
        auto_discover_subscriptions (bool | None): Defines whether to protect virtual network configuration of all Azure
            subscriptions specified in Azure VM, Azure SQL and Azure file share backup policy settings.
        backup_interval_minutes (int | None | Unset): Time interval (in minutes) at which the backup policy will run.
        backup_interval_hours (int | None | Unset): Time interval (in hours) at which the backup policy will run.
        retention_period_days (int | None | Unset): Time period (in days) for which the backups will be stored in the
            Veeam Backup for Microsoft Azure configuration database.
        retention_period_weeks (int | None | Unset): Time period (in weeks) for which the backups will be stored in the
            Veeam Backup for Microsoft Azure configuration database.
        retention_period_months (int | None | Unset): Time period (in months) for which the backups will be stored in
            the Veeam Backup for Microsoft Azure configuration database.
        target_repository_id (None | str | Unset): System ID assigned to the repository in the Veeam Backup for
            Microsoft Azure REST API.
        additional_protected_resources (list[VnetPolicyAdditionalProtectedResourcesFromClient] | None | Unset):
            Information on a service account whose permissions will be used to perform virtual network configuration backup,
            and on the subscriptions that will be protected by the virtual network configuration backup policy.
        policy_notification_settings (PolicyNotificationSettings | Unset): Specifies the notification settings for the
            backup policy.
    """

    is_enabled: bool | None
    auto_discover_subscriptions: bool | None
    backup_interval_minutes: int | None | Unset = UNSET
    backup_interval_hours: int | None | Unset = UNSET
    retention_period_days: int | None | Unset = UNSET
    retention_period_weeks: int | None | Unset = UNSET
    retention_period_months: int | None | Unset = UNSET
    target_repository_id: None | str | Unset = UNSET
    additional_protected_resources: list[VnetPolicyAdditionalProtectedResourcesFromClient] | None | Unset = UNSET
    policy_notification_settings: PolicyNotificationSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_enabled: bool | None
        is_enabled = self.is_enabled

        auto_discover_subscriptions: bool | None
        auto_discover_subscriptions = self.auto_discover_subscriptions

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

        policy_notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy_notification_settings, Unset):
            policy_notification_settings = self.policy_notification_settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isEnabled": is_enabled,
                "autoDiscoverSubscriptions": auto_discover_subscriptions,
            }
        )
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
        if additional_protected_resources is not UNSET:
            field_dict["additionalProtectedResources"] = additional_protected_resources
        if policy_notification_settings is not UNSET:
            field_dict["policyNotificationSettings"] = policy_notification_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_notification_settings import PolicyNotificationSettings
        from ..models.vnet_policy_additional_protected_resources_from_client import (
            VnetPolicyAdditionalProtectedResourcesFromClient,
        )

        d = dict(src_dict)

        def _parse_is_enabled(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled"))

        def _parse_auto_discover_subscriptions(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        auto_discover_subscriptions = _parse_auto_discover_subscriptions(d.pop("autoDiscoverSubscriptions"))

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

        def _parse_additional_protected_resources(
            data: object,
        ) -> list[VnetPolicyAdditionalProtectedResourcesFromClient] | None | Unset:
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
                    additional_protected_resources_type_0_item = (
                        VnetPolicyAdditionalProtectedResourcesFromClient.from_dict(
                            additional_protected_resources_type_0_item_data
                        )
                    )

                    additional_protected_resources_type_0.append(additional_protected_resources_type_0_item)

                return additional_protected_resources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VnetPolicyAdditionalProtectedResourcesFromClient] | None | Unset, data)

        additional_protected_resources = _parse_additional_protected_resources(
            d.pop("additionalProtectedResources", UNSET)
        )

        _policy_notification_settings = d.pop("policyNotificationSettings", UNSET)
        policy_notification_settings: PolicyNotificationSettings | Unset
        if isinstance(_policy_notification_settings, Unset):
            policy_notification_settings = UNSET
        else:
            policy_notification_settings = PolicyNotificationSettings.from_dict(_policy_notification_settings)

        updated_vnet_policy_from_client = cls(
            is_enabled=is_enabled,
            auto_discover_subscriptions=auto_discover_subscriptions,
            backup_interval_minutes=backup_interval_minutes,
            backup_interval_hours=backup_interval_hours,
            retention_period_days=retention_period_days,
            retention_period_weeks=retention_period_weeks,
            retention_period_months=retention_period_months,
            target_repository_id=target_repository_id,
            additional_protected_resources=additional_protected_resources,
            policy_notification_settings=policy_notification_settings,
        )

        return updated_vnet_policy_from_client
