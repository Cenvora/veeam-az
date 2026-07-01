from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.disk_type import DiskType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.availability_set_from_client import AvailabilitySetFromClient
    from ..models.availability_zone_info import AvailabilityZoneInfo
    from ..models.azure_subscription import AzureSubscription
    from ..models.disk_restore_options_base import DiskRestoreOptionsBase
    from ..models.network_security_group import NetworkSecurityGroup
    from ..models.region import Region
    from ..models.resource_group import ResourceGroup
    from ..models.virtual_network_from_client_for_to_alternative import VirtualNetworkFromClientForToAlternative
    from ..models.virtual_network_subnet import VirtualNetworkSubnet


T = TypeVar("T", bound="VirtualMachineToAlternativeRestoreOptions")


@_attrs_define
class VirtualMachineToAlternativeRestoreOptions:
    """/[Applies if restore is performed to a new location or with different settings/] Specifies Azure VM restore
    settings.

        Attributes:
            name (None | str | Unset): Specifies a name for the restored Azure VM.
            subscription (AzureSubscription | Unset): Specifies information on an Azure subscription.
            resource_group (ResourceGroup | Unset): Specifies information on a resource group.
            region (Region | Unset): Specifies Azure regions for which the operation is performed.
            vm_size_name (None | str | Unset): Specifies the Azure VM size for the restored Azure VM.
            virtual_network (VirtualNetworkFromClientForToAlternative | Unset): Specifies a virtual network to which Azure
                VM will be restored.
            subnet (VirtualNetworkSubnet | Unset): Specifies a subnet of the virtual network.
            network_security_group (NetworkSecurityGroup | Unset): Information on a network security group.
            availability_set (AvailabilitySetFromClient | Unset):
            availability_zone (AvailabilityZoneInfo | Unset): Specifies information on an availability zone.
            disk_type (DiskType | Unset): Specifies the type of the virtual disk.
            os_disk (DiskRestoreOptionsBase | Unset): Specifies information on OS and data disks attached to the restored
                Azure VM.
            data_disks (list[DiskRestoreOptionsBase] | None | Unset): Specifies information on OS and data disks attached to
                the restored Azure VM.
    """

    name: None | str | Unset = UNSET
    subscription: AzureSubscription | Unset = UNSET
    resource_group: ResourceGroup | Unset = UNSET
    region: Region | Unset = UNSET
    vm_size_name: None | str | Unset = UNSET
    virtual_network: VirtualNetworkFromClientForToAlternative | Unset = UNSET
    subnet: VirtualNetworkSubnet | Unset = UNSET
    network_security_group: NetworkSecurityGroup | Unset = UNSET
    availability_set: AvailabilitySetFromClient | Unset = UNSET
    availability_zone: AvailabilityZoneInfo | Unset = UNSET
    disk_type: DiskType | Unset = UNSET
    os_disk: DiskRestoreOptionsBase | Unset = UNSET
    data_disks: list[DiskRestoreOptionsBase] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        vm_size_name: None | str | Unset
        if isinstance(self.vm_size_name, Unset):
            vm_size_name = UNSET
        else:
            vm_size_name = self.vm_size_name

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

        disk_type: str | Unset = UNSET
        if not isinstance(self.disk_type, Unset):
            disk_type = self.disk_type.value

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if region is not UNSET:
            field_dict["region"] = region
        if vm_size_name is not UNSET:
            field_dict["vmSizeName"] = vm_size_name
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
        if disk_type is not UNSET:
            field_dict["diskType"] = disk_type
        if os_disk is not UNSET:
            field_dict["osDisk"] = os_disk
        if data_disks is not UNSET:
            field_dict["dataDisks"] = data_disks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.availability_set_from_client import AvailabilitySetFromClient
        from ..models.availability_zone_info import AvailabilityZoneInfo
        from ..models.azure_subscription import AzureSubscription
        from ..models.disk_restore_options_base import DiskRestoreOptionsBase
        from ..models.network_security_group import NetworkSecurityGroup
        from ..models.region import Region
        from ..models.resource_group import ResourceGroup
        from ..models.virtual_network_from_client_for_to_alternative import VirtualNetworkFromClientForToAlternative
        from ..models.virtual_network_subnet import VirtualNetworkSubnet

        d = dict(src_dict)

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

        def _parse_vm_size_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vm_size_name = _parse_vm_size_name(d.pop("vmSizeName", UNSET))

        _virtual_network = d.pop("virtualNetwork", UNSET)
        virtual_network: VirtualNetworkFromClientForToAlternative | Unset
        if isinstance(_virtual_network, Unset):
            virtual_network = UNSET
        else:
            virtual_network = VirtualNetworkFromClientForToAlternative.from_dict(_virtual_network)

        _subnet = d.pop("subnet", UNSET)
        subnet: VirtualNetworkSubnet | Unset
        if isinstance(_subnet, Unset):
            subnet = UNSET
        else:
            subnet = VirtualNetworkSubnet.from_dict(_subnet)

        _network_security_group = d.pop("networkSecurityGroup", UNSET)
        network_security_group: NetworkSecurityGroup | Unset
        if isinstance(_network_security_group, Unset):
            network_security_group = UNSET
        else:
            network_security_group = NetworkSecurityGroup.from_dict(_network_security_group)

        _availability_set = d.pop("availabilitySet", UNSET)
        availability_set: AvailabilitySetFromClient | Unset
        if isinstance(_availability_set, Unset):
            availability_set = UNSET
        else:
            availability_set = AvailabilitySetFromClient.from_dict(_availability_set)

        _availability_zone = d.pop("availabilityZone", UNSET)
        availability_zone: AvailabilityZoneInfo | Unset
        if isinstance(_availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = AvailabilityZoneInfo.from_dict(_availability_zone)

        _disk_type = d.pop("diskType", UNSET)
        disk_type: DiskType | Unset
        if isinstance(_disk_type, Unset):
            disk_type = UNSET
        else:
            disk_type = DiskType(_disk_type)

        _os_disk = d.pop("osDisk", UNSET)
        os_disk: DiskRestoreOptionsBase | Unset
        if isinstance(_os_disk, Unset):
            os_disk = UNSET
        else:
            os_disk = DiskRestoreOptionsBase.from_dict(_os_disk)

        def _parse_data_disks(data: object) -> list[DiskRestoreOptionsBase] | None | Unset:
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
                    data_disks_type_0_item = DiskRestoreOptionsBase.from_dict(data_disks_type_0_item_data)

                    data_disks_type_0.append(data_disks_type_0_item)

                return data_disks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DiskRestoreOptionsBase] | None | Unset, data)

        data_disks = _parse_data_disks(d.pop("dataDisks", UNSET))

        virtual_machine_to_alternative_restore_options = cls(
            name=name,
            subscription=subscription,
            resource_group=resource_group,
            region=region,
            vm_size_name=vm_size_name,
            virtual_network=virtual_network,
            subnet=subnet,
            network_security_group=network_security_group,
            availability_set=availability_set,
            availability_zone=availability_zone,
            disk_type=disk_type,
            os_disk=os_disk,
            data_disks=data_disks,
        )

        return virtual_machine_to_alternative_restore_options
