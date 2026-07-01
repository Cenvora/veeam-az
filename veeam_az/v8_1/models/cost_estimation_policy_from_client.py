from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_type_nullable import BackupTypeNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimation_assumption_from_client import CostEstimationAssumptionFromClient
    from ..models.daily_schedule import DailySchedule
    from ..models.health_check_schedule import HealthCheckSchedule
    from ..models.monthly_schedule import MonthlySchedule
    from ..models.policy_backup_items_from_client import PolicyBackupItemsFromClient
    from ..models.policy_excluded_items_from_client import PolicyExcludedItemsFromClient
    from ..models.policy_notification_settings import PolicyNotificationSettings
    from ..models.policy_region_from_client import PolicyRegionFromClient
    from ..models.retry_settings import RetrySettings
    from ..models.snapshot_settings import SnapshotSettings
    from ..models.weekly_schedule import WeeklySchedule
    from ..models.yearly_schedule import YearlySchedule


T = TypeVar("T", bound="CostEstimationPolicyFromClient")


@_attrs_define
class CostEstimationPolicyFromClient:
    r"""
    Attributes:
        priority (int | Unset): Specifies the priority ordinal number of the backup policy.
        tenant_id (None | str | Unset): Specifies the tenant ID for which the policy is created.
        service_account_id (UUID | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST
            API to a service account whose permissions will be used to access Microsoft Azure resources.
        regions (list[PolicyRegionFromClient] | None | Unset): Specifies Azure regions where the protected resources
            reside.
        selected_items (PolicyBackupItemsFromClient | Unset): \[Applies if the *SelectedItems* value is specified for
            the `backupType` parameter] Specifies Azure resources to protect by the backup policy.
        excluded_items (PolicyExcludedItemsFromClient | Unset): Specifies Azure tags to identify the resources that
            should be excluded from the backup scope.
        name (None | str | Unset): Specifies a name of the backup policy.
        description (None | str | Unset): Specifies a description of the backup policy.
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
        cost_estimation_assumption (CostEstimationAssumptionFromClient | Unset): \[Optional assumptions about protected
            items] Specifies average daily churn and expected disk occupy ratio.
    """

    priority: int | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    service_account_id: UUID | Unset = UNSET
    regions: list[PolicyRegionFromClient] | None | Unset = UNSET
    selected_items: PolicyBackupItemsFromClient | Unset = UNSET
    excluded_items: PolicyExcludedItemsFromClient | Unset = UNSET
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
    cost_estimation_assumption: CostEstimationAssumptionFromClient | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        priority = self.priority

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        service_account_id: str | Unset = UNSET
        if not isinstance(self.service_account_id, Unset):
            service_account_id = str(self.service_account_id)

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

        cost_estimation_assumption: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cost_estimation_assumption, Unset):
            cost_estimation_assumption = self.cost_estimation_assumption.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if priority is not UNSET:
            field_dict["priority"] = priority
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if regions is not UNSET:
            field_dict["regions"] = regions
        if selected_items is not UNSET:
            field_dict["selectedItems"] = selected_items
        if excluded_items is not UNSET:
            field_dict["excludedItems"] = excluded_items
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
        if cost_estimation_assumption is not UNSET:
            field_dict["costEstimationAssumption"] = cost_estimation_assumption

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_estimation_assumption_from_client import CostEstimationAssumptionFromClient
        from ..models.daily_schedule import DailySchedule
        from ..models.health_check_schedule import HealthCheckSchedule
        from ..models.monthly_schedule import MonthlySchedule
        from ..models.policy_backup_items_from_client import PolicyBackupItemsFromClient
        from ..models.policy_excluded_items_from_client import PolicyExcludedItemsFromClient
        from ..models.policy_notification_settings import PolicyNotificationSettings
        from ..models.policy_region_from_client import PolicyRegionFromClient
        from ..models.retry_settings import RetrySettings
        from ..models.snapshot_settings import SnapshotSettings
        from ..models.weekly_schedule import WeeklySchedule
        from ..models.yearly_schedule import YearlySchedule

        d = dict(src_dict)
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

        _cost_estimation_assumption = d.pop("costEstimationAssumption", UNSET)
        cost_estimation_assumption: CostEstimationAssumptionFromClient | Unset
        if isinstance(_cost_estimation_assumption, Unset):
            cost_estimation_assumption = UNSET
        else:
            cost_estimation_assumption = CostEstimationAssumptionFromClient.from_dict(_cost_estimation_assumption)

        cost_estimation_policy_from_client = cls(
            priority=priority,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            regions=regions,
            selected_items=selected_items,
            excluded_items=excluded_items,
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
            cost_estimation_assumption=cost_estimation_assumption,
        )

        return cost_estimation_policy_from_client
