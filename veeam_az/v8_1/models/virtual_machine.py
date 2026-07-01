from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.azure_environment import AzureEnvironment
from ..models.os_type import OSType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="VirtualMachine")


@_attrs_define
class VirtualMachine:
    """Information on an Azure VM.

    Attributes:
        id (None | str | Unset): System ID assigned to the Azure VM in the Veeam Backup for Microsoft Azure REST API.
        azure_id (None | str | Unset): Resource ID of the Azure VM.
        name (None | str | Unset): Name of the Azure VM.
        azure_environment (AzureEnvironment | Unset): Specifies the type of the Microsoft Azure cloud environment.
        os_type (OSType | Unset): Type of the operating system installed on the Azure VM.
        region_display_name (None | str | Unset): Name of the Azure region where the Azure VM resides as displayed in
            the Veeam Backup for Microsoft Azure UI.
        region_name (None | str | Unset): Name of the Azure region where the Azure VM resides.
        total_size_in_gb (int | Unset): Total size of all virtual disks attached to the Azure VM.
        vm_size (None | str | Unset): Size of the Azure VM.
        dns_name (None | str | Unset): DNS hostname of the Azure VM.
        virtual_network (None | str | Unset): Microsoft Azure ID assigned to a virtual network to which the backup
            appliance is connected.
        subnet (None | str | Unset): Name of a subnet connected to the backup appliance.
        public_ip (None | str | Unset): Public IP address associated with the backup appliance.
        private_ip (None | str | Unset): Private IP address associated with the backup appliance.
        has_ephemeral_os_disk (bool | Unset): Defines whether the Azure VM has an ephemeral OS disk attached.
        availability_zone (None | str | Unset): Specifies the Availability Zone where the Azure VM resides.
        is_controller (bool | Unset): Defines whether Veeam Backup for Microsoft Azure is installed on an Azure VM.
        is_deleted (bool | Unset): Defines whether the Azure VM is no longer present in the Azure infrastructure.
        subscription_id (UUID | Unset): Microsoft Azure ID assigned to a subscription to which the Azure VM belongs.
        subscription_name (None | str | Unset): Name of the subscription to which the Azure VM belongs.
        tenant_id (None | str | Unset): Microsoft Azure ID assigned to a Microsoft Entra tenant to which the Azure VM
            belongs.
        resource_group_name (None | str | Unset): Name of a resource group to which the Azure VM belongs.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    azure_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    azure_environment: AzureEnvironment | Unset = UNSET
    os_type: OSType | Unset = UNSET
    region_display_name: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    total_size_in_gb: int | Unset = UNSET
    vm_size: None | str | Unset = UNSET
    dns_name: None | str | Unset = UNSET
    virtual_network: None | str | Unset = UNSET
    subnet: None | str | Unset = UNSET
    public_ip: None | str | Unset = UNSET
    private_ip: None | str | Unset = UNSET
    has_ephemeral_os_disk: bool | Unset = UNSET
    availability_zone: None | str | Unset = UNSET
    is_controller: bool | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    subscription_name: None | str | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        azure_id: None | str | Unset
        if isinstance(self.azure_id, Unset):
            azure_id = UNSET
        else:
            azure_id = self.azure_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        azure_environment: str | Unset = UNSET
        if not isinstance(self.azure_environment, Unset):
            azure_environment = self.azure_environment.value

        os_type: str | Unset = UNSET
        if not isinstance(self.os_type, Unset):
            os_type = self.os_type.value

        region_display_name: None | str | Unset
        if isinstance(self.region_display_name, Unset):
            region_display_name = UNSET
        else:
            region_display_name = self.region_display_name

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        total_size_in_gb = self.total_size_in_gb

        vm_size: None | str | Unset
        if isinstance(self.vm_size, Unset):
            vm_size = UNSET
        else:
            vm_size = self.vm_size

        dns_name: None | str | Unset
        if isinstance(self.dns_name, Unset):
            dns_name = UNSET
        else:
            dns_name = self.dns_name

        virtual_network: None | str | Unset
        if isinstance(self.virtual_network, Unset):
            virtual_network = UNSET
        else:
            virtual_network = self.virtual_network

        subnet: None | str | Unset
        if isinstance(self.subnet, Unset):
            subnet = UNSET
        else:
            subnet = self.subnet

        public_ip: None | str | Unset
        if isinstance(self.public_ip, Unset):
            public_ip = UNSET
        else:
            public_ip = self.public_ip

        private_ip: None | str | Unset
        if isinstance(self.private_ip, Unset):
            private_ip = UNSET
        else:
            private_ip = self.private_ip

        has_ephemeral_os_disk = self.has_ephemeral_os_disk

        availability_zone: None | str | Unset
        if isinstance(self.availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = self.availability_zone

        is_controller = self.is_controller

        is_deleted = self.is_deleted

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        subscription_name: None | str | Unset
        if isinstance(self.subscription_name, Unset):
            subscription_name = UNSET
        else:
            subscription_name = self.subscription_name

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        resource_group_name: None | str | Unset
        if isinstance(self.resource_group_name, Unset):
            resource_group_name = UNSET
        else:
            resource_group_name = self.resource_group_name

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
        if azure_id is not UNSET:
            field_dict["azureId"] = azure_id
        if name is not UNSET:
            field_dict["name"] = name
        if azure_environment is not UNSET:
            field_dict["azureEnvironment"] = azure_environment
        if os_type is not UNSET:
            field_dict["osType"] = os_type
        if region_display_name is not UNSET:
            field_dict["regionDisplayName"] = region_display_name
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if total_size_in_gb is not UNSET:
            field_dict["totalSizeInGB"] = total_size_in_gb
        if vm_size is not UNSET:
            field_dict["vmSize"] = vm_size
        if dns_name is not UNSET:
            field_dict["dnsName"] = dns_name
        if virtual_network is not UNSET:
            field_dict["virtualNetwork"] = virtual_network
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if public_ip is not UNSET:
            field_dict["publicIP"] = public_ip
        if private_ip is not UNSET:
            field_dict["privateIP"] = private_ip
        if has_ephemeral_os_disk is not UNSET:
            field_dict["hasEphemeralOsDisk"] = has_ephemeral_os_disk
        if availability_zone is not UNSET:
            field_dict["availabilityZone"] = availability_zone
        if is_controller is not UNSET:
            field_dict["isController"] = is_controller
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_azure_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_id = _parse_azure_id(d.pop("azureId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _azure_environment = d.pop("azureEnvironment", UNSET)
        azure_environment: AzureEnvironment | Unset
        if isinstance(_azure_environment, Unset):
            azure_environment = UNSET
        else:
            azure_environment = AzureEnvironment(_azure_environment)

        _os_type = d.pop("osType", UNSET)
        os_type: OSType | Unset
        if isinstance(_os_type, Unset):
            os_type = UNSET
        else:
            os_type = OSType(_os_type)

        def _parse_region_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_display_name = _parse_region_display_name(d.pop("regionDisplayName", UNSET))

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        total_size_in_gb = d.pop("totalSizeInGB", UNSET)

        def _parse_vm_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vm_size = _parse_vm_size(d.pop("vmSize", UNSET))

        def _parse_dns_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dns_name = _parse_dns_name(d.pop("dnsName", UNSET))

        def _parse_virtual_network(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_network = _parse_virtual_network(d.pop("virtualNetwork", UNSET))

        def _parse_subnet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subnet = _parse_subnet(d.pop("subnet", UNSET))

        def _parse_public_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_ip = _parse_public_ip(d.pop("publicIP", UNSET))

        def _parse_private_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        private_ip = _parse_private_ip(d.pop("privateIP", UNSET))

        has_ephemeral_os_disk = d.pop("hasEphemeralOsDisk", UNSET)

        def _parse_availability_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        availability_zone = _parse_availability_zone(d.pop("availabilityZone", UNSET))

        is_controller = d.pop("isController", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        def _parse_subscription_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_name = _parse_subscription_name(d.pop("subscriptionName", UNSET))

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_name = _parse_resource_group_name(d.pop("resourceGroupName", UNSET))

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

        virtual_machine = cls(
            id=id,
            azure_id=azure_id,
            name=name,
            azure_environment=azure_environment,
            os_type=os_type,
            region_display_name=region_display_name,
            region_name=region_name,
            total_size_in_gb=total_size_in_gb,
            vm_size=vm_size,
            dns_name=dns_name,
            virtual_network=virtual_network,
            subnet=subnet,
            public_ip=public_ip,
            private_ip=private_ip,
            has_ephemeral_os_disk=has_ephemeral_os_disk,
            availability_zone=availability_zone,
            is_controller=is_controller,
            is_deleted=is_deleted,
            subscription_id=subscription_id,
            subscription_name=subscription_name,
            tenant_id=tenant_id,
            resource_group_name=resource_group_name,
            field_links=field_links,
        )

        return virtual_machine
