from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.private_dns_setting import PrivateDnsSetting
from ..models.storage_account_public_access import StorageAccountPublicAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetDeploymentModeRequest")


@_attrs_define
class SetDeploymentModeRequest:
    r"""Specifies the deployment mode settings.

    Attributes:
        private_deployment_enabled (bool): Defines whether to enable or disable the private network deployment
            functionality.
        auto_create_service_endpoints (bool): Defines whether to enable or disable automatic creation of service
            endpoints for the `Microsoft.Storage.Global` service to communicate with worker instances in public virtual
            networks.
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
        storage_account_public_access (StorageAccountPublicAccess | Unset): Specifies the Veeam storage account
            settings&#58; <ul><li>If you select the *Enabled* value, the Veeam storage accounts will have public network
            access enabled.</li><li>If you select the *Disabled* value, the Veeam storage accounts will have public network
            access disabled.</li><li>If you select the *DoNotModify* value, Veeam Backup for Microsoft Azure will keep the
            existing network configuration of the Veeam storage accounts. </li></ul>
    """

    private_deployment_enabled: bool
    auto_create_service_endpoints: bool
    private_dns_zone_setting: PrivateDnsSetting | Unset = UNSET
    private_dns_zone_resource_group_id: None | str | Unset = UNSET
    storage_account_public_access: StorageAccountPublicAccess | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        private_deployment_enabled = self.private_deployment_enabled

        auto_create_service_endpoints = self.auto_create_service_endpoints

        private_dns_zone_setting: str | Unset = UNSET
        if not isinstance(self.private_dns_zone_setting, Unset):
            private_dns_zone_setting = self.private_dns_zone_setting.value

        private_dns_zone_resource_group_id: None | str | Unset
        if isinstance(self.private_dns_zone_resource_group_id, Unset):
            private_dns_zone_resource_group_id = UNSET
        else:
            private_dns_zone_resource_group_id = self.private_dns_zone_resource_group_id

        storage_account_public_access: str | Unset = UNSET
        if not isinstance(self.storage_account_public_access, Unset):
            storage_account_public_access = self.storage_account_public_access.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "privateDeploymentEnabled": private_deployment_enabled,
                "autoCreateServiceEndpoints": auto_create_service_endpoints,
            }
        )
        if private_dns_zone_setting is not UNSET:
            field_dict["privateDnsZoneSetting"] = private_dns_zone_setting
        if private_dns_zone_resource_group_id is not UNSET:
            field_dict["privateDnsZoneResourceGroupId"] = private_dns_zone_resource_group_id
        if storage_account_public_access is not UNSET:
            field_dict["storageAccountPublicAccess"] = storage_account_public_access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        private_deployment_enabled = d.pop("privateDeploymentEnabled")

        auto_create_service_endpoints = d.pop("autoCreateServiceEndpoints")

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

        _storage_account_public_access = d.pop("storageAccountPublicAccess", UNSET)
        storage_account_public_access: StorageAccountPublicAccess | Unset
        if isinstance(_storage_account_public_access, Unset):
            storage_account_public_access = UNSET
        else:
            storage_account_public_access = StorageAccountPublicAccess(_storage_account_public_access)

        set_deployment_mode_request = cls(
            private_deployment_enabled=private_deployment_enabled,
            auto_create_service_endpoints=auto_create_service_endpoints,
            private_dns_zone_setting=private_dns_zone_setting,
            private_dns_zone_resource_group_id=private_dns_zone_resource_group_id,
            storage_account_public_access=storage_account_public_access,
        )

        set_deployment_mode_request.additional_properties = d
        return set_deployment_mode_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
