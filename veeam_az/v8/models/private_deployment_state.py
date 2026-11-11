from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.message_service import MessageService
from ..models.private_dns_setting import PrivateDnsSetting
from ..models.storage_account_public_access import StorageAccountPublicAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateDeploymentState")


@_attrs_define
class PrivateDeploymentState:
    r"""Specifies the backup appliance deployment settings.

    Attributes:
        message_service (MessageService | Unset): Specifies the messaging service that will be used to transfer data.
        private_deployment_enabled (bool | Unset): Defines whether to enable the private network deployment
            functionality.
        private_dns_zone_setting (PrivateDnsSetting | Unset): Specifies the private DNS zone settings&#58; <ul><li>If
            you select the *Disabled* value, you must do the following&#58; create the DNS zones, add to the DNS zones A
            records for the private endpoints of disk access resources and Veeam storage accounts, and add to the DNS zones
            the VNet to which the backup appliance is connected and the VNet to which worker instances are
            connected.</li><li>If you select the *ManageARecords* value, you must create the DNS zones and add to these DNS
            zones the VNet to which the backup appliance is connected and the VNet to which worker instances are connected,
            while Veeam Backup for Microsoft Azure will automatically add to the DNS zones A records for the private
            endpoint of disk access resources and Veeam storage accounts.</li><li>If you select the *ManageAutomatically*
            value, Veeam Backup for Microsoft Azure will automatically create the DNS zones in the resource group to which
            worker instances belong, add to these DNS zones A records for the private endpoint of disk access resources and
            Veeam storage accounts, and add to the DNS zones the VNet to which the backup appliance is connected and the
            VNet to which worker instances are connected.</li></ul> <div class="note"><strong>NOTE</strong></br>Regardless
            of the value you selected for the `PrivateDnsSetting` parameter, you must configure peering connections between
            the VNet to which the backup appliance is connected and the VNet to which worker instances are connected. For
            more information, see the <a
            href="https://helpcenter.veeam.com/docs/vbazure/guide/app_private_network.html?ver=81">Veeam Backup for
            Microsoft Azure User Guide.</a>
        private_dns_zone_resource_group_id (None | str | Unset): \[Applies only if you have selected the
            *ManageARecords* value for the `privateDnsZoneSetting` parameter] Specifies the Microsoft Azure ID assigned to
            the resource group to which the private DNS zones that will be used for private network deployment belong or in
            which these DNS zones will be created.
        auto_create_service_endpoints (bool | Unset): Defines whether to enable automatic creation of service endpoints.
        storage_account_public_access (StorageAccountPublicAccess | Unset): Specifies the Veeam storage account
            settings&#58; <ul><li>If you select the *Enabled* value, the Veeam storage accounts will have public network
            access enabled.</li><li>If you select the *Disabled* value, the Veeam storage accounts will have public network
            access disabled.</li><li>If you select the *DoNotModify* value, Veeam Backup for Microsoft Azure will keep the
            existing network configuration of the Veeam storage accounts. </li></ul>
        is_updating (bool | Unset): Defines whether any of the backup appliance deployment settings is currently being
            updated.
        error (None | str | Unset): \[Applies only if the private network deployment functionality configuration
            completes with an error] Information on the error.
    """

    message_service: MessageService | Unset = UNSET
    private_deployment_enabled: bool | Unset = UNSET
    private_dns_zone_setting: PrivateDnsSetting | Unset = UNSET
    private_dns_zone_resource_group_id: None | str | Unset = UNSET
    auto_create_service_endpoints: bool | Unset = UNSET
    storage_account_public_access: StorageAccountPublicAccess | Unset = UNSET
    is_updating: bool | Unset = UNSET
    error: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message_service: str | Unset = UNSET
        if not isinstance(self.message_service, Unset):
            message_service = self.message_service.value

        private_deployment_enabled = self.private_deployment_enabled

        private_dns_zone_setting: str | Unset = UNSET
        if not isinstance(self.private_dns_zone_setting, Unset):
            private_dns_zone_setting = self.private_dns_zone_setting.value

        private_dns_zone_resource_group_id: None | str | Unset
        if isinstance(self.private_dns_zone_resource_group_id, Unset):
            private_dns_zone_resource_group_id = UNSET
        else:
            private_dns_zone_resource_group_id = self.private_dns_zone_resource_group_id

        auto_create_service_endpoints = self.auto_create_service_endpoints

        storage_account_public_access: str | Unset = UNSET
        if not isinstance(self.storage_account_public_access, Unset):
            storage_account_public_access = self.storage_account_public_access.value

        is_updating = self.is_updating

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if message_service is not UNSET:
            field_dict["messageService"] = message_service
        if private_deployment_enabled is not UNSET:
            field_dict["privateDeploymentEnabled"] = private_deployment_enabled
        if private_dns_zone_setting is not UNSET:
            field_dict["privateDnsZoneSetting"] = private_dns_zone_setting
        if private_dns_zone_resource_group_id is not UNSET:
            field_dict["privateDnsZoneResourceGroupId"] = private_dns_zone_resource_group_id
        if auto_create_service_endpoints is not UNSET:
            field_dict["autoCreateServiceEndpoints"] = auto_create_service_endpoints
        if storage_account_public_access is not UNSET:
            field_dict["storageAccountPublicAccess"] = storage_account_public_access
        if is_updating is not UNSET:
            field_dict["isUpdating"] = is_updating
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _message_service = d.pop("messageService", UNSET)
        message_service: MessageService | Unset
        if isinstance(_message_service, Unset):
            message_service = UNSET
        else:
            message_service = MessageService(_message_service)

        private_deployment_enabled = d.pop("privateDeploymentEnabled", UNSET)

        _private_dns_zone_setting = d.pop("privateDnsZoneSetting", UNSET)
        private_dns_zone_setting: PrivateDnsSetting | Unset
        if isinstance(_private_dns_zone_setting, Unset):
            private_dns_zone_setting = UNSET
        else:
            private_dns_zone_setting = PrivateDnsSetting(_private_dns_zone_setting)

        def _parse_private_dns_zone_resource_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        private_dns_zone_resource_group_id = _parse_private_dns_zone_resource_group_id(
            d.pop("privateDnsZoneResourceGroupId", UNSET)
        )

        auto_create_service_endpoints = d.pop("autoCreateServiceEndpoints", UNSET)

        _storage_account_public_access = d.pop("storageAccountPublicAccess", UNSET)
        storage_account_public_access: StorageAccountPublicAccess | Unset
        if isinstance(_storage_account_public_access, Unset):
            storage_account_public_access = UNSET
        else:
            storage_account_public_access = StorageAccountPublicAccess(_storage_account_public_access)

        is_updating = d.pop("isUpdating", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        private_deployment_state = cls(
            message_service=message_service,
            private_deployment_enabled=private_deployment_enabled,
            private_dns_zone_setting=private_dns_zone_setting,
            private_dns_zone_resource_group_id=private_dns_zone_resource_group_id,
            auto_create_service_endpoints=auto_create_service_endpoints,
            storage_account_public_access=storage_account_public_access,
            is_updating=is_updating,
            error=error,
        )

        return private_deployment_state
