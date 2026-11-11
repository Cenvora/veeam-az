from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_type_nullable import BackupTypeNullable
from ..models.policy_cosmos_db_backup_tier import PolicyCosmosDbBackupTier
from ..models.policy_cosmos_db_backup_workload import PolicyCosmosDbBackupWorkload
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cosmos_db_policy_backup_items_from_client import CosmosDbPolicyBackupItemsFromClient
    from ..models.cosmos_db_policy_excluded_items_from_client import CosmosDbPolicyExcludedItemsFromClient
    from ..models.cosmos_db_processing_credentials_type_0 import CosmosDbProcessingCredentialsType0
    from ..models.daily_cosmos_db_schedule import DailyCosmosDbSchedule
    from ..models.health_check_schedule import HealthCheckSchedule
    from ..models.monthly_cosmos_db_schedule import MonthlyCosmosDbSchedule
    from ..models.policy_notification_settings import PolicyNotificationSettings
    from ..models.policy_region_from_client import PolicyRegionFromClient
    from ..models.retry_settings import RetrySettings
    from ..models.weekly_cosmos_db_schedule import WeeklyCosmosDbSchedule
    from ..models.yearly_schedule import YearlySchedule


T = TypeVar("T", bound="UpdatedCosmosDbPolicyFromClient")


@_attrs_define
class UpdatedCosmosDbPolicyFromClient:
    r"""
    Attributes:
        regions (list[PolicyRegionFromClient]): Specifies Azure regions where the backed up resources will reside.
        name (str): Specifies a name for the backup policy.
        is_enabled (bool | None): Defines whether to enable the policy.
        backup_type (BackupTypeNullable): Defines whether you want to include to the backup scope all resources residing
            in the specified Azure regions and to which the specified service account has access.
        tenant_id (None | str | Unset): Specifies a Microsoft Azure ID assigned to a tenant to which the protected Azure
            resources belong.
        service_account_id (None | Unset | UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft
            Azure REST API to the service account whose permissions will be used to create backups of Cosmos DB accounts.
        selected_items (CosmosDbPolicyBackupItemsFromClient | Unset): Specifies information on Azure resources to
            protect by the backup policy.
        excluded_items (CosmosDbPolicyExcludedItemsFromClient | Unset): Specifies Azure resources to exclude from the
            backup scope.
        continuous_backup_type (PolicyCosmosDbBackupTier | Unset): Specifies the retention period for Cosmos DB
            continuous backup.
        description (None | str | Unset): Specifies a description for the backup policy.
        retry_settings (RetrySettings | Unset): Specifies the retry settings for the backup policy.
        policy_notification_settings (PolicyNotificationSettings | Unset): Specifies the notification settings for the
            backup policy.
        create_private_endpoint_to_workload_automatically (bool | None | Unset): Defines whether the backup policy
            should create private endpoint to workload automatically.
        backup_workloads (list[PolicyCosmosDbBackupWorkload] | None | Unset): Specifies kinds of the Cosmos DB accounts
            protected using the *Backup to repository* option.
        daily_schedule (DailyCosmosDbSchedule | Unset): /[Applies only to backup policies that have the *Backup to
            repository* option enabled] Specifies daily schedule settings for the backup policy.
        weekly_schedule (WeeklyCosmosDbSchedule | Unset): /[Applies only to backup policies that have the *Backup to
            repository* option enabled] Specifies weekly schedule settings for the backup policy.
        monthly_schedule (MonthlyCosmosDbSchedule | Unset): /[Applies only to backup policies that have the *Backup to
            repository* option enabled] Specifies monthly schedule settings for the backup policy.
        yearly_schedule (YearlySchedule | Unset): Specifies the yearly schedule settings for the backup policy.
        health_check_schedule (HealthCheckSchedule | Unset): \[Applies if backup creation is enabled for the backup
            policy] Specifies the health check schedule settings.
        default_backup_account_id (None | str | Unset): /[Applies only to backup policies that have the *Backup to
            repository* option enabled] Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to
            a default database account that will be used to access all protected databases.
        credentials_list (CosmosDbProcessingCredentialsType0 | None | Unset): Specifies a list of credentials that will
            be used to connect to the databases of the specified Cosmos DB accounts.
    """

    regions: list[PolicyRegionFromClient]
    name: str
    is_enabled: bool | None
    backup_type: BackupTypeNullable
    tenant_id: None | str | Unset = UNSET
    service_account_id: None | Unset | UUID = UNSET
    selected_items: CosmosDbPolicyBackupItemsFromClient | Unset = UNSET
    excluded_items: CosmosDbPolicyExcludedItemsFromClient | Unset = UNSET
    continuous_backup_type: PolicyCosmosDbBackupTier | Unset = UNSET
    description: None | str | Unset = UNSET
    retry_settings: RetrySettings | Unset = UNSET
    policy_notification_settings: PolicyNotificationSettings | Unset = UNSET
    create_private_endpoint_to_workload_automatically: bool | None | Unset = UNSET
    backup_workloads: list[PolicyCosmosDbBackupWorkload] | None | Unset = UNSET
    daily_schedule: DailyCosmosDbSchedule | Unset = UNSET
    weekly_schedule: WeeklyCosmosDbSchedule | Unset = UNSET
    monthly_schedule: MonthlyCosmosDbSchedule | Unset = UNSET
    yearly_schedule: YearlySchedule | Unset = UNSET
    health_check_schedule: HealthCheckSchedule | Unset = UNSET
    default_backup_account_id: None | str | Unset = UNSET
    credentials_list: CosmosDbProcessingCredentialsType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cosmos_db_processing_credentials_type_0 import CosmosDbProcessingCredentialsType0

        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()
            regions.append(regions_item)

        name = self.name

        is_enabled: bool | None
        is_enabled = self.is_enabled

        backup_type = self.backup_type.value

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

        continuous_backup_type: str | Unset = UNSET
        if not isinstance(self.continuous_backup_type, Unset):
            continuous_backup_type = self.continuous_backup_type.value

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

        backup_workloads: list[str] | None | Unset
        if isinstance(self.backup_workloads, Unset):
            backup_workloads = UNSET
        elif isinstance(self.backup_workloads, list):
            backup_workloads = []
            for backup_workloads_type_0_item_data in self.backup_workloads:
                backup_workloads_type_0_item = backup_workloads_type_0_item_data.value
                backup_workloads.append(backup_workloads_type_0_item)

        else:
            backup_workloads = self.backup_workloads

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

        default_backup_account_id: None | str | Unset
        if isinstance(self.default_backup_account_id, Unset):
            default_backup_account_id = UNSET
        else:
            default_backup_account_id = self.default_backup_account_id

        credentials_list: dict[str, Any] | None | Unset
        if isinstance(self.credentials_list, Unset):
            credentials_list = UNSET
        elif isinstance(self.credentials_list, CosmosDbProcessingCredentialsType0):
            credentials_list = self.credentials_list.to_dict()
        else:
            credentials_list = self.credentials_list

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "regions": regions,
                "name": name,
                "isEnabled": is_enabled,
                "backupType": backup_type,
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
        if continuous_backup_type is not UNSET:
            field_dict["continuousBackupType"] = continuous_backup_type
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
        if backup_workloads is not UNSET:
            field_dict["backupWorkloads"] = backup_workloads
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
        if default_backup_account_id is not UNSET:
            field_dict["defaultBackupAccountId"] = default_backup_account_id
        if credentials_list is not UNSET:
            field_dict["credentialsList"] = credentials_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cosmos_db_policy_backup_items_from_client import CosmosDbPolicyBackupItemsFromClient
        from ..models.cosmos_db_policy_excluded_items_from_client import CosmosDbPolicyExcludedItemsFromClient
        from ..models.cosmos_db_processing_credentials_type_0 import CosmosDbProcessingCredentialsType0
        from ..models.daily_cosmos_db_schedule import DailyCosmosDbSchedule
        from ..models.health_check_schedule import HealthCheckSchedule
        from ..models.monthly_cosmos_db_schedule import MonthlyCosmosDbSchedule
        from ..models.policy_notification_settings import PolicyNotificationSettings
        from ..models.policy_region_from_client import PolicyRegionFromClient
        from ..models.retry_settings import RetrySettings
        from ..models.weekly_cosmos_db_schedule import WeeklyCosmosDbSchedule
        from ..models.yearly_schedule import YearlySchedule

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

        backup_type = BackupTypeNullable(d.pop("backupType"))

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

        _continuous_backup_type = d.pop("continuousBackupType", UNSET)
        continuous_backup_type: PolicyCosmosDbBackupTier | Unset
        if isinstance(_continuous_backup_type, Unset):
            continuous_backup_type = UNSET
        else:
            continuous_backup_type = PolicyCosmosDbBackupTier(_continuous_backup_type)

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

        def _parse_backup_workloads(data: object) -> list[PolicyCosmosDbBackupWorkload] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                backup_workloads_type_0 = []
                _backup_workloads_type_0 = data
                for backup_workloads_type_0_item_data in _backup_workloads_type_0:
                    backup_workloads_type_0_item = PolicyCosmosDbBackupWorkload(backup_workloads_type_0_item_data)

                    backup_workloads_type_0.append(backup_workloads_type_0_item)

                return backup_workloads_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PolicyCosmosDbBackupWorkload] | None | Unset, data)

        backup_workloads = _parse_backup_workloads(d.pop("backupWorkloads", UNSET))

        _daily_schedule = d.pop("dailySchedule", UNSET)
        daily_schedule: DailyCosmosDbSchedule | Unset
        if isinstance(_daily_schedule, Unset):
            daily_schedule = UNSET
        else:
            daily_schedule = DailyCosmosDbSchedule.from_dict(_daily_schedule)

        _weekly_schedule = d.pop("weeklySchedule", UNSET)
        weekly_schedule: WeeklyCosmosDbSchedule | Unset
        if isinstance(_weekly_schedule, Unset):
            weekly_schedule = UNSET
        else:
            weekly_schedule = WeeklyCosmosDbSchedule.from_dict(_weekly_schedule)

        _monthly_schedule = d.pop("monthlySchedule", UNSET)
        monthly_schedule: MonthlyCosmosDbSchedule | Unset
        if isinstance(_monthly_schedule, Unset):
            monthly_schedule = UNSET
        else:
            monthly_schedule = MonthlyCosmosDbSchedule.from_dict(_monthly_schedule)

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

        def _parse_default_backup_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_backup_account_id = _parse_default_backup_account_id(d.pop("defaultBackupAccountId", UNSET))

        def _parse_credentials_list(data: object) -> CosmosDbProcessingCredentialsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_cosmos_db_processing_credentials_type_0 = (
                    CosmosDbProcessingCredentialsType0.from_dict(data)
                )

                return componentsschemas_cosmos_db_processing_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CosmosDbProcessingCredentialsType0 | None | Unset, data)

        credentials_list = _parse_credentials_list(d.pop("credentialsList", UNSET))

        updated_cosmos_db_policy_from_client = cls(
            regions=regions,
            name=name,
            is_enabled=is_enabled,
            backup_type=backup_type,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            selected_items=selected_items,
            excluded_items=excluded_items,
            continuous_backup_type=continuous_backup_type,
            description=description,
            retry_settings=retry_settings,
            policy_notification_settings=policy_notification_settings,
            create_private_endpoint_to_workload_automatically=create_private_endpoint_to_workload_automatically,
            backup_workloads=backup_workloads,
            daily_schedule=daily_schedule,
            weekly_schedule=weekly_schedule,
            monthly_schedule=monthly_schedule,
            yearly_schedule=yearly_schedule,
            health_check_schedule=health_check_schedule,
            default_backup_account_id=default_backup_account_id,
            credentials_list=credentials_list,
        )

        return updated_cosmos_db_policy_from_client
