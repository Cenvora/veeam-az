from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.availability_set import AvailabilitySet
    from ..models.availability_zone_info import AvailabilityZoneInfo
    from ..models.azure_subscription import AzureSubscription
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.network_security_group import NetworkSecurityGroup
    from ..models.region import Region
    from ..models.resource_group import ResourceGroup
    from ..models.virtual_network import VirtualNetwork
    from ..models.virtual_network_subnet_base import VirtualNetworkSubnetBase
    from ..models.vm_disk_snapshot import VmDiskSnapshot


T = TypeVar("T", bound="VmSnapshot")


@_attrs_define
class VmSnapshot:
    """
    Attributes:
        size (str): Size of the protected Azure VM.
        vm_id (None | str | Unset): System ID assigned to the protected Azure VM in the Veeam Backup for Microsoft Azure
            REST API.
        vm_azure_resource_id (None | str | Unset): Resource ID of the Azure VM.
        service_account_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to
            the service account to which the protected Azure VM is linked.
        name (None | str | Unset): Name of the protected Azure VM.
        subscription (AzureSubscription | Unset): Specifies information on an Azure subscription.
        resource_group (ResourceGroup | Unset): Specifies information on a resource group.
        region (Region | Unset): Specifies Azure regions for which the operation is performed.
        has_ephemeral_os_disk (bool | Unset): Defines whether the Azure VM has an ephemeral OS disk attached.
        os_disk (VmDiskSnapshot | Unset): Specifies virtual disks that must be excluded from restore.
        data_disks (list[VmDiskSnapshot] | None | Unset): Information on the data disks of the protected Azure VM.
        disk_size_in_gb (int | Unset): Specifies the size of the disk where the Azure VM snapshot is stored.
        virtual_network (VirtualNetwork | Unset): Specifies information on a virtual network.
        subnet (VirtualNetworkSubnetBase | Unset): Information on the subnet.
        network_security_group (NetworkSecurityGroup | Unset): Information on a network security group.
        availability_set (AvailabilitySet | Unset): Specifies information on an availability set.
        availability_zone (AvailabilityZoneInfo | Unset): Specifies information on an availability zone.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    size: str
    vm_id: None | str | Unset = UNSET
    vm_azure_resource_id: None | str | Unset = UNSET
    service_account_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    subscription: AzureSubscription | Unset = UNSET
    resource_group: ResourceGroup | Unset = UNSET
    region: Region | Unset = UNSET
    has_ephemeral_os_disk: bool | Unset = UNSET
    os_disk: VmDiskSnapshot | Unset = UNSET
    data_disks: list[VmDiskSnapshot] | None | Unset = UNSET
    disk_size_in_gb: int | Unset = UNSET
    virtual_network: VirtualNetwork | Unset = UNSET
    subnet: VirtualNetworkSubnetBase | Unset = UNSET
    network_security_group: NetworkSecurityGroup | Unset = UNSET
    availability_set: AvailabilitySet | Unset = UNSET
    availability_zone: AvailabilityZoneInfo | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        size = self.size

        vm_id: None | str | Unset
        if isinstance(self.vm_id, Unset):
            vm_id = UNSET
        else:
            vm_id = self.vm_id

        vm_azure_resource_id: None | str | Unset
        if isinstance(self.vm_azure_resource_id, Unset):
            vm_azure_resource_id = UNSET
        else:
            vm_azure_resource_id = self.vm_azure_resource_id

        service_account_id: None | str | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        else:
            service_account_id = self.service_account_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        resource_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_group, Unset):
            resource_group = self.resource_group.to_dict()

        region: dict[str, Any] | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        has_ephemeral_os_disk = self.has_ephemeral_os_disk

        os_disk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.os_disk, Unset):
            os_disk = self.os_disk.to_dict()

        data_disks: list[dict[str, Any]] | None | Unset
        if isinstance(self.data_disks, Unset):
            data_disks = UNSET
        elif isinstance(self.data_disks, list):
            data_disks = []
            for data_disks_type_0_item_data in self.data_disks:
                data_disks_type_0_item = data_disks_type_0_item_data.to_dict()
                data_disks.append(data_disks_type_0_item)

        else:
            data_disks = self.data_disks

        disk_size_in_gb = self.disk_size_in_gb

        virtual_network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.virtual_network, Unset):
            virtual_network = self.virtual_network.to_dict()

        subnet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subnet, Unset):
            subnet = self.subnet.to_dict()

        network_security_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network_security_group, Unset):
            network_security_group = self.network_security_group.to_dict()

        availability_set: dict[str, Any] | Unset = UNSET
        if not isinstance(self.availability_set, Unset):
            availability_set = self.availability_set.to_dict()

        availability_zone: dict[str, Any] | Unset = UNSET
        if not isinstance(self.availability_zone, Unset):
            availability_zone = self.availability_zone.to_dict()

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "size": size,
            }
        )
        if vm_id is not UNSET:
            field_dict["vmId"] = vm_id
        if vm_azure_resource_id is not UNSET:
            field_dict["vmAzureResourceId"] = vm_azure_resource_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if name is not UNSET:
            field_dict["name"] = name
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if region is not UNSET:
            field_dict["region"] = region
        if has_ephemeral_os_disk is not UNSET:
            field_dict["hasEphemeralOsDisk"] = has_ephemeral_os_disk
        if os_disk is not UNSET:
            field_dict["osDisk"] = os_disk
        if data_disks is not UNSET:
            field_dict["dataDisks"] = data_disks
        if disk_size_in_gb is not UNSET:
            field_dict["diskSizeInGb"] = disk_size_in_gb
        if virtual_network is not UNSET:
            field_dict["virtualNetwork"] = virtual_network
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if network_security_group is not UNSET:
            field_dict["networkSecurityGroup"] = network_security_group
        if availability_set is not UNSET:
            field_dict["availabilitySet"] = availability_set
        if availability_zone is not UNSET:
            field_dict["availabilityZone"] = availability_zone
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.availability_set import AvailabilitySet
        from ..models.availability_zone_info import AvailabilityZoneInfo
        from ..models.azure_subscription import AzureSubscription
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.network_security_group import NetworkSecurityGroup
        from ..models.region import Region
        from ..models.resource_group import ResourceGroup
        from ..models.virtual_network import VirtualNetwork
        from ..models.virtual_network_subnet_base import VirtualNetworkSubnetBase
        from ..models.vm_disk_snapshot import VmDiskSnapshot

        d = dict(src_dict)
        size = d.pop("size")

        def _parse_vm_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vm_id = _parse_vm_id(d.pop("vmId", UNSET))

        def _parse_vm_azure_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vm_azure_resource_id = _parse_vm_azure_resource_id(d.pop("vmAzureResourceId", UNSET))

        def _parse_service_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_account_id = _parse_service_account_id(d.pop("serviceAccountId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _subscription = d.pop("subscription", UNSET)
        subscription: AzureSubscription | Unset
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = AzureSubscription.from_dict(_subscription)

        _resource_group = d.pop("resourceGroup", UNSET)
        resource_group: ResourceGroup | Unset
        if isinstance(_resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = ResourceGroup.from_dict(_resource_group)

        _region = d.pop("region", UNSET)
        region: Region | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Region.from_dict(_region)

        has_ephemeral_os_disk = d.pop("hasEphemeralOsDisk", UNSET)

        _os_disk = d.pop("osDisk", UNSET)
        os_disk: VmDiskSnapshot | Unset
        if isinstance(_os_disk, Unset):
            os_disk = UNSET
        else:
            os_disk = VmDiskSnapshot.from_dict(_os_disk)

        def _parse_data_disks(data: object) -> list[VmDiskSnapshot] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_disks_type_0 = []
                _data_disks_type_0 = data
                for data_disks_type_0_item_data in _data_disks_type_0:
                    data_disks_type_0_item = VmDiskSnapshot.from_dict(data_disks_type_0_item_data)

                    data_disks_type_0.append(data_disks_type_0_item)

                return data_disks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VmDiskSnapshot] | None | Unset, data)

        data_disks = _parse_data_disks(d.pop("dataDisks", UNSET))

        disk_size_in_gb = d.pop("diskSizeInGb", UNSET)

        _virtual_network = d.pop("virtualNetwork", UNSET)
        virtual_network: VirtualNetwork | Unset
        if isinstance(_virtual_network, Unset):
            virtual_network = UNSET
        else:
            virtual_network = VirtualNetwork.from_dict(_virtual_network)

        _subnet = d.pop("subnet", UNSET)
        subnet: VirtualNetworkSubnetBase | Unset
        if isinstance(_subnet, Unset):
            subnet = UNSET
        else:
            subnet = VirtualNetworkSubnetBase.from_dict(_subnet)

        _network_security_group = d.pop("networkSecurityGroup", UNSET)
        network_security_group: NetworkSecurityGroup | Unset
        if isinstance(_network_security_group, Unset):
            network_security_group = UNSET
        else:
            network_security_group = NetworkSecurityGroup.from_dict(_network_security_group)

        _availability_set = d.pop("availabilitySet", UNSET)
        availability_set: AvailabilitySet | Unset
        if isinstance(_availability_set, Unset):
            availability_set = UNSET
        else:
            availability_set = AvailabilitySet.from_dict(_availability_set)

        _availability_zone = d.pop("availabilityZone", UNSET)
        availability_zone: AvailabilityZoneInfo | Unset
        if isinstance(_availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = AvailabilityZoneInfo.from_dict(_availability_zone)

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

        vm_snapshot = cls(
            size=size,
            vm_id=vm_id,
            vm_azure_resource_id=vm_azure_resource_id,
            service_account_id=service_account_id,
            name=name,
            subscription=subscription,
            resource_group=resource_group,
            region=region,
            has_ephemeral_os_disk=has_ephemeral_os_disk,
            os_disk=os_disk,
            data_disks=data_disks,
            disk_size_in_gb=disk_size_in_gb,
            virtual_network=virtual_network,
            subnet=subnet,
            network_security_group=network_security_group,
            availability_set=availability_set,
            availability_zone=availability_zone,
            field_links=field_links,
        )

        return vm_snapshot
