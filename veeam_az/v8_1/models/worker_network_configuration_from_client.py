from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerNetworkConfigurationFromClient")


@_attrs_define
class WorkerNetworkConfigurationFromClient:
    """
    Attributes:
        subnet (str): Specifies the name of the subnet to which worker instances will be connected.
        virtual_network_resource_id (str): Specifies the complete resource ID containing all information on the virtual
            network where the worker resides.
        region_id (str): Specifies a Microsoft Azure ID assigned to a region where the worker configuration will reside.
        network_security_group_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a network security
            group.
        forbid_public_ip (bool | None | Unset): Defines whether to assign only private IP addresses to worker instances
            used for file-level recovery operations.
        tenant_id (None | Unset | UUID): Specifies the Microsoft Azure ID assigned to a tenant in which worker instances
            will be launched. If no value is specified for the property, Veeam Backup for Microsoft Azure will use the
            tenant where the backup appliance is deployed. Consider that if private network deployment is enabled on the
            backup appliance, you can only specify a tenant where the backup appliance is deployed.
        subscription_id (None | Unset | UUID): Specifies the Microsoft Azure ID assigned to a subscription in which
            worker instances will be launched. Note that the subscription must belong to the tenant specified in the value
            of the `tenantId` property. If no value is specified for the `subscriptionId` property, Veeam Backup for
            Microsoft Azure will use the subscription where the backup appliance is deployed. Consider that if private
            network deployment is enabled on the backup appliance, you can only specify a subscription belonging to the
            tenant where the backup appliance is deployed.
        resource_group (None | str | Unset): Specifies the name of the resource group in which the worker instances will
            be launched. Note that the resource group must belong to the subscription specified in the `subscriptionId`
            property. If no value is specified for the `resourceGroup` property, Veeam Backup for Microsoft Azure will
            automatically generate the value and create a resource group in the subscription specified in the
            `subscriptionId` property, or in the subscription where the backup appliance is deployed.
    """

    subnet: str
    virtual_network_resource_id: str
    region_id: str
    network_security_group_id: None | str | Unset = UNSET
    forbid_public_ip: bool | None | Unset = UNSET
    tenant_id: None | Unset | UUID = UNSET
    subscription_id: None | Unset | UUID = UNSET
    resource_group: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subnet = self.subnet

        virtual_network_resource_id = self.virtual_network_resource_id

        region_id = self.region_id

        network_security_group_id: None | str | Unset
        if isinstance(self.network_security_group_id, Unset):
            network_security_group_id = UNSET
        else:
            network_security_group_id = self.network_security_group_id

        forbid_public_ip: bool | None | Unset
        if isinstance(self.forbid_public_ip, Unset):
            forbid_public_ip = UNSET
        else:
            forbid_public_ip = self.forbid_public_ip

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        elif isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        elif isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

        resource_group: None | str | Unset
        if isinstance(self.resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = self.resource_group

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "subnet": subnet,
                "virtualNetworkResourceId": virtual_network_resource_id,
                "regionId": region_id,
            }
        )
        if network_security_group_id is not UNSET:
            field_dict["networkSecurityGroupId"] = network_security_group_id
        if forbid_public_ip is not UNSET:
            field_dict["forbidPublicIp"] = forbid_public_ip
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subnet = d.pop("subnet")

        virtual_network_resource_id = d.pop("virtualNetworkResourceId")

        region_id = d.pop("regionId")

        def _parse_network_security_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_security_group_id = _parse_network_security_group_id(d.pop("networkSecurityGroupId", UNSET))

        def _parse_forbid_public_ip(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        forbid_public_ip = _parse_forbid_public_ip(d.pop("forbidPublicIp", UNSET))

        def _parse_tenant_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_id_type_0 = UUID(data)

                return tenant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_subscription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_type_0 = UUID(data)

                return subscription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        def _parse_resource_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group = _parse_resource_group(d.pop("resourceGroup", UNSET))

        worker_network_configuration_from_client = cls(
            subnet=subnet,
            virtual_network_resource_id=virtual_network_resource_id,
            region_id=region_id,
            network_security_group_id=network_security_group_id,
            forbid_public_ip=forbid_public_ip,
            tenant_id=tenant_id,
            subscription_id=subscription_id,
            resource_group=resource_group,
        )

        return worker_network_configuration_from_client
