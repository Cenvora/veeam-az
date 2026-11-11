from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.worker_network_configuration_type import WorkerNetworkConfigurationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_security_group import NetworkSecurityGroup
    from ..models.region import Region
    from ..models.worker_network_configuration_links_type_0 import WorkerNetworkConfigurationLinksType0
    from ..models.worker_virtual_network import WorkerVirtualNetwork


T = TypeVar("T", bound="WorkerNetworkConfiguration")


@_attrs_define
class WorkerNetworkConfiguration:
    """Information on a worker network configuration.

    Attributes:
        virtual_network (WorkerVirtualNetwork | Unset): Information on a virtual network in which worker instances are
            launched.
        region (Region | Unset): Specifies Azure regions for which the operation is performed.
        network_security_group (NetworkSecurityGroup | Unset): Information on a network security group.
        forbid_public_ip (bool | Unset): Defines whether to assign only private IP addresses to worker instances used
            for file-level recovery operations.
        tenant_id (None | Unset | UUID): Microsoft Azure ID assigned to a tenant in which worker instances are launched.
            If no value is returned, Veeam Backup for Microsoft Azure uses the tenant where the backup appliance is
            deployed.
        tenant_name (None | str | Unset): Name of the tenant in which worker instances are launched.
        subscription_id (None | Unset | UUID): Microsoft Azure ID assigned to a subscription in which worker instances
            are launched.
        subscription_name (None | str | Unset): Name of the subscription in which worker instances are launched.
        resource_group (None | str | Unset): Name of the resource group in which the worker instances are launched.
        configuration_type (WorkerNetworkConfigurationType | Unset): Worker network configuration are automatically
            created during policy run or other worker job if no manual worker configuration is created. Worker Network
            configurations created by older release might contain Unknown value.
        field_links (None | Unset | WorkerNetworkConfigurationLinksType0): URLs of operations where the properties
            obtained in the response can be used as an input.
    """

    virtual_network: WorkerVirtualNetwork | Unset = UNSET
    region: Region | Unset = UNSET
    network_security_group: NetworkSecurityGroup | Unset = UNSET
    forbid_public_ip: bool | Unset = UNSET
    tenant_id: None | Unset | UUID = UNSET
    tenant_name: None | str | Unset = UNSET
    subscription_id: None | Unset | UUID = UNSET
    subscription_name: None | str | Unset = UNSET
    resource_group: None | str | Unset = UNSET
    configuration_type: WorkerNetworkConfigurationType | Unset = UNSET
    field_links: None | Unset | WorkerNetworkConfigurationLinksType0 = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.worker_network_configuration_links_type_0 import WorkerNetworkConfigurationLinksType0

        virtual_network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.virtual_network, Unset):
            virtual_network = self.virtual_network.to_dict()

        region: dict[str, Any] | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        network_security_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network_security_group, Unset):
            network_security_group = self.network_security_group.to_dict()

        forbid_public_ip = self.forbid_public_ip

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        elif isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        tenant_name: None | str | Unset
        if isinstance(self.tenant_name, Unset):
            tenant_name = UNSET
        else:
            tenant_name = self.tenant_name

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        elif isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

        subscription_name: None | str | Unset
        if isinstance(self.subscription_name, Unset):
            subscription_name = UNSET
        else:
            subscription_name = self.subscription_name

        resource_group: None | str | Unset
        if isinstance(self.resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = self.resource_group

        configuration_type: str | Unset = UNSET
        if not isinstance(self.configuration_type, Unset):
            configuration_type = self.configuration_type.value

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, WorkerNetworkConfigurationLinksType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if virtual_network is not UNSET:
            field_dict["virtualNetwork"] = virtual_network
        if region is not UNSET:
            field_dict["region"] = region
        if network_security_group is not UNSET:
            field_dict["networkSecurityGroup"] = network_security_group
        if forbid_public_ip is not UNSET:
            field_dict["forbidPublicIp"] = forbid_public_ip
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if tenant_name is not UNSET:
            field_dict["tenantName"] = tenant_name
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if configuration_type is not UNSET:
            field_dict["configurationType"] = configuration_type
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_security_group import NetworkSecurityGroup
        from ..models.region import Region
        from ..models.worker_network_configuration_links_type_0 import WorkerNetworkConfigurationLinksType0
        from ..models.worker_virtual_network import WorkerVirtualNetwork

        d = dict(src_dict)
        _virtual_network = d.pop("virtualNetwork", UNSET)
        virtual_network: WorkerVirtualNetwork | Unset
        if isinstance(_virtual_network, Unset):
            virtual_network = UNSET
        else:
            virtual_network = WorkerVirtualNetwork.from_dict(_virtual_network)

        _region = d.pop("region", UNSET)
        region: Region | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Region.from_dict(_region)

        _network_security_group = d.pop("networkSecurityGroup", UNSET)
        network_security_group: NetworkSecurityGroup | Unset
        if isinstance(_network_security_group, Unset):
            network_security_group = UNSET
        else:
            network_security_group = NetworkSecurityGroup.from_dict(_network_security_group)

        forbid_public_ip = d.pop("forbidPublicIp", UNSET)

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

        def _parse_tenant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_name = _parse_tenant_name(d.pop("tenantName", UNSET))

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

        def _parse_subscription_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_name = _parse_subscription_name(d.pop("subscriptionName", UNSET))

        def _parse_resource_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group = _parse_resource_group(d.pop("resourceGroup", UNSET))

        _configuration_type = d.pop("configurationType", UNSET)
        configuration_type: WorkerNetworkConfigurationType | Unset
        if isinstance(_configuration_type, Unset):
            configuration_type = UNSET
        else:
            configuration_type = WorkerNetworkConfigurationType(_configuration_type)

        def _parse_field_links(data: object) -> None | Unset | WorkerNetworkConfigurationLinksType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_links_type_0 = WorkerNetworkConfigurationLinksType0.from_dict(data)

                return field_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkerNetworkConfigurationLinksType0, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        worker_network_configuration = cls(
            virtual_network=virtual_network,
            region=region,
            network_security_group=network_security_group,
            forbid_public_ip=forbid_public_ip,
            tenant_id=tenant_id,
            tenant_name=tenant_name,
            subscription_id=subscription_id,
            subscription_name=subscription_name,
            resource_group=resource_group,
            configuration_type=configuration_type,
            field_links=field_links,
        )

        return worker_network_configuration
