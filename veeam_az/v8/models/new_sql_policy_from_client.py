from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_type_nullable import BackupTypeNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_sql_schedule import DailySqlSchedule
    from ..models.health_check_schedule import HealthCheckSchedule
    from ..models.monthly_sql_schedule import MonthlySqlSchedule
    from ..models.policy_notification_settings import PolicyNotificationSettings
    from ..models.policy_region_from_client import PolicyRegionFromClient
    from ..models.retry_settings import RetrySettings
    from ..models.sql_policy_backup_items_from_client import SqlPolicyBackupItemsFromClient
    from ..models.sql_policy_excluded_items_from_client import SqlPolicyExcludedItemsFromClient
    from ..models.weekly_sql_schedule import WeeklySqlSchedule
    from ..models.yearly_schedule import YearlySchedule


T = TypeVar("T", bound="NewSqlPolicyFromClient")


@_attrs_define
class NewSqlPolicyFromClient:
    r"""
    Attributes:
        tenant_id (str): Specifies a Microsoft Azure ID assigned to a tenant with which the service account used to
            protect Azure resources is associated.
        service_account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to
            the service account whose permissions will be used to perform backups of Azure SQL databases.
        regions (list[PolicyRegionFromClient]): Azure regions where the resources that will be backed up reside.
        name (str): Specifies a name for the backup policy.
        is_enabled (bool | None): Defines whether to enable the policy.
        backup_type (BackupTypeNullable): Defines whether you want to include to the backup scope all resources residing
            in the specified Azure regions and to which the specified service account has access.
        selected_items (SqlPolicyBackupItemsFromClient | Unset): \[Applies if the *SelectedItems* value is specified for
            the `backupType` parameter] Specifies information on Azure resources to protect by the backup policy.
        excluded_items (SqlPolicyExcludedItemsFromClient | Unset): Specifies Azure resources to exclude from the backup
            scope.
        staging_server_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a staging server configured
            for the unmanaged instances.
        managed_staging_server_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a staging server
            configured for the managed instances.
        description (None | str | Unset): Specifies a description for the backup policy.
        retry_settings (RetrySettings | Unset): Specifies the retry settings for the backup policy.
        policy_notification_settings (PolicyNotificationSettings | Unset): Specifies the notification settings for the
            backup policy.
        create_private_endpoint_to_workload_automatically (bool | None | Unset): Defines whether the backup policy
            should create private endpoint to workload automatically.
        daily_schedule (DailySqlSchedule | Unset): Specifies daily schedule settings for the backup policy.
        weekly_schedule (WeeklySqlSchedule | Unset): Specifies weekly schedule settings for the backup policy.
        monthly_schedule (MonthlySqlSchedule | Unset): Specifies monthly schedule settings for the backup policy.
        yearly_schedule (YearlySchedule | Unset): Specifies the yearly schedule settings for the backup policy.
        health_check_schedule (HealthCheckSchedule | Unset): \[Applies if backup creation is enabled for the backup
            policy] Specifies the health check schedule settings.
    """

    tenant_id: str
    service_account_id: UUID
    regions: list[PolicyRegionFromClient]
    name: str
    is_enabled: bool | None
    backup_type: BackupTypeNullable
    selected_items: SqlPolicyBackupItemsFromClient | Unset = UNSET
    excluded_items: SqlPolicyExcludedItemsFromClient | Unset = UNSET
    staging_server_id: None | str | Unset = UNSET
    managed_staging_server_id: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    retry_settings: RetrySettings | Unset = UNSET
    policy_notification_settings: PolicyNotificationSettings | Unset = UNSET
    create_private_endpoint_to_workload_automatically: bool | None | Unset = UNSET
    daily_schedule: DailySqlSchedule | Unset = UNSET
    weekly_schedule: WeeklySqlSchedule | Unset = UNSET
    monthly_schedule: MonthlySqlSchedule | Unset = UNSET
    yearly_schedule: YearlySchedule | Unset = UNSET
    health_check_schedule: HealthCheckSchedule | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        service_account_id = str(self.service_account_id)

        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()
            regions.append(regions_item)

        name = self.name

        is_enabled: bool | None
        is_enabled = self.is_enabled

        backup_type = self.backup_type.value

        selected_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selected_items, Unset):
            selected_items = self.selected_items.to_dict()

        excluded_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.excluded_items, Unset):
            excluded_items = self.excluded_items.to_dict()

        staging_server_id: None | str | Unset
        if isinstance(self.staging_server_id, Unset):
            staging_server_id = UNSET
        else:
            staging_server_id = self.staging_server_id

        managed_staging_server_id: None | str | Unset
        if isinstance(self.managed_staging_server_id, Unset):
            managed_staging_server_id = UNSET
        else:
            managed_staging_server_id = self.managed_staging_server_id

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

        create_private_endpoint_to_workload_automatically: bool | None | Unset
        if isinstance(self.create_private_endpoint_to_workload_automatically, Unset):
            create_private_endpoint_to_workload_automatically = UNSET
        else:
            create_private_endpoint_to_workload_automatically = self.create_private_endpoint_to_workload_automatically

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tenantId": tenant_id,
                "serviceAccountId": service_account_id,
                "regions": regions,
                "name": name,
                "isEnabled": is_enabled,
                "backupType": backup_type,
            }
        )
        if selected_items is not UNSET:
            field_dict["selectedItems"] = selected_items
        if excluded_items is not UNSET:
            field_dict["excludedItems"] = excluded_items
        if staging_server_id is not UNSET:
            field_dict["stagingServerId"] = staging_server_id
        if managed_staging_server_id is not UNSET:
            field_dict["managedStagingServerId"] = managed_staging_server_id
        if description is not UNSET:
            field_dict["description"] = description
        if retry_settings is not UNSET:
            field_dict["retrySettings"] = retry_settings
        if policy_notification_settings is not UNSET:
            field_dict["policyNotificationSettings"] = policy_notification_settings
        if create_private_endpoint_to_workload_automatically is not UNSET:
            field_dict["createPrivateEndpointToWorkloadAutomatically"] = (
                create_private_endpoint_to_workload_automatically
            )
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_sql_schedule import DailySqlSchedule
        from ..models.health_check_schedule import HealthCheckSchedule
        from ..models.monthly_sql_schedule import MonthlySqlSchedule
        from ..models.policy_notification_settings import PolicyNotificationSettings
        from ..models.policy_region_from_client import PolicyRegionFromClient
        from ..models.retry_settings import RetrySettings
        from ..models.sql_policy_backup_items_from_client import SqlPolicyBackupItemsFromClient
        from ..models.sql_policy_excluded_items_from_client import SqlPolicyExcludedItemsFromClient
        from ..models.weekly_sql_schedule import WeeklySqlSchedule
        from ..models.yearly_schedule import YearlySchedule

        d = dict(src_dict)
        tenant_id = d.pop("tenantId")

        service_account_id = UUID(d.pop("serviceAccountId"))

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

        backup_type = BackupTypeNullable(d.pop("backupType"))

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

        def _parse_staging_server_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        staging_server_id = _parse_staging_server_id(d.pop("stagingServerId", UNSET))

        def _parse_managed_staging_server_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_staging_server_id = _parse_managed_staging_server_id(d.pop("managedStagingServerId", UNSET))

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

        def _parse_create_private_endpoint_to_workload_automatically(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        create_private_endpoint_to_workload_automatically = _parse_create_private_endpoint_to_workload_automatically(
            d.pop("createPrivateEndpointToWorkloadAutomatically", UNSET)
        )

        _daily_schedule = d.pop("dailySchedule", UNSET)
        daily_schedule: DailySqlSchedule | Unset
        if isinstance(_daily_schedule, Unset):
            daily_schedule = UNSET
        else:
            daily_schedule = DailySqlSchedule.from_dict(_daily_schedule)

        _weekly_schedule = d.pop("weeklySchedule", UNSET)
        weekly_schedule: WeeklySqlSchedule | Unset
        if isinstance(_weekly_schedule, Unset):
            weekly_schedule = UNSET
        else:
            weekly_schedule = WeeklySqlSchedule.from_dict(_weekly_schedule)

        _monthly_schedule = d.pop("monthlySchedule", UNSET)
        monthly_schedule: MonthlySqlSchedule | Unset
        if isinstance(_monthly_schedule, Unset):
            monthly_schedule = UNSET
        else:
            monthly_schedule = MonthlySqlSchedule.from_dict(_monthly_schedule)

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

        new_sql_policy_from_client = cls(
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            regions=regions,
            name=name,
            is_enabled=is_enabled,
            backup_type=backup_type,
            selected_items=selected_items,
            excluded_items=excluded_items,
            staging_server_id=staging_server_id,
            managed_staging_server_id=managed_staging_server_id,
            description=description,
            retry_settings=retry_settings,
            policy_notification_settings=policy_notification_settings,
            create_private_endpoint_to_workload_automatically=create_private_endpoint_to_workload_automatically,
            daily_schedule=daily_schedule,
            weekly_schedule=weekly_schedule,
            monthly_schedule=monthly_schedule,
            yearly_schedule=yearly_schedule,
            health_check_schedule=health_check_schedule,
        )

        return new_sql_policy_from_client
