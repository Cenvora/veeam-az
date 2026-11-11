from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualMachineRestoreConfigParameters")


@_attrs_define
class VirtualMachineRestoreConfigParameters:
    """
    Attributes:
        name (None | str | Unset):
        subscription (None | str | Unset):
        region (None | str | Unset):
        resource_group (None | str | Unset):
        vm_size_name (None | str | Unset):
        virtual_network_name (None | str | Unset):
        virtual_network_subnet_name (None | str | Unset):
        network_security_group_name (None | str | Unset):
        is_accelerated_networking_enabled (bool | Unset):
        availability_zone (None | str | Unset):
        availability_set_name (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    subscription: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    resource_group: None | str | Unset = UNSET
    vm_size_name: None | str | Unset = UNSET
    virtual_network_name: None | str | Unset = UNSET
    virtual_network_subnet_name: None | str | Unset = UNSET
    network_security_group_name: None | str | Unset = UNSET
    is_accelerated_networking_enabled: bool | Unset = UNSET
    availability_zone: None | str | Unset = UNSET
    availability_set_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        subscription: None | str | Unset
        if isinstance(self.subscription, Unset):
            subscription = UNSET
        else:
            subscription = self.subscription

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        resource_group: None | str | Unset
        if isinstance(self.resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = self.resource_group

        vm_size_name: None | str | Unset
        if isinstance(self.vm_size_name, Unset):
            vm_size_name = UNSET
        else:
            vm_size_name = self.vm_size_name

        virtual_network_name: None | str | Unset
        if isinstance(self.virtual_network_name, Unset):
            virtual_network_name = UNSET
        else:
            virtual_network_name = self.virtual_network_name

        virtual_network_subnet_name: None | str | Unset
        if isinstance(self.virtual_network_subnet_name, Unset):
            virtual_network_subnet_name = UNSET
        else:
            virtual_network_subnet_name = self.virtual_network_subnet_name

        network_security_group_name: None | str | Unset
        if isinstance(self.network_security_group_name, Unset):
            network_security_group_name = UNSET
        else:
            network_security_group_name = self.network_security_group_name

        is_accelerated_networking_enabled = self.is_accelerated_networking_enabled

        availability_zone: None | str | Unset
        if isinstance(self.availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = self.availability_zone

        availability_set_name: None | str | Unset
        if isinstance(self.availability_set_name, Unset):
            availability_set_name = UNSET
        else:
            availability_set_name = self.availability_set_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if region is not UNSET:
            field_dict["region"] = region
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if vm_size_name is not UNSET:
            field_dict["vmSizeName"] = vm_size_name
        if virtual_network_name is not UNSET:
            field_dict["virtualNetworkName"] = virtual_network_name
        if virtual_network_subnet_name is not UNSET:
            field_dict["virtualNetworkSubnetName"] = virtual_network_subnet_name
        if network_security_group_name is not UNSET:
            field_dict["networkSecurityGroupName"] = network_security_group_name
        if is_accelerated_networking_enabled is not UNSET:
            field_dict["isAcceleratedNetworkingEnabled"] = is_accelerated_networking_enabled
        if availability_zone is not UNSET:
            field_dict["availabilityZone"] = availability_zone
        if availability_set_name is not UNSET:
            field_dict["availabilitySetName"] = availability_set_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_subscription(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription = _parse_subscription(d.pop("subscription", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_resource_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group = _parse_resource_group(d.pop("resourceGroup", UNSET))

        def _parse_vm_size_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vm_size_name = _parse_vm_size_name(d.pop("vmSizeName", UNSET))

        def _parse_virtual_network_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_network_name = _parse_virtual_network_name(d.pop("virtualNetworkName", UNSET))

        def _parse_virtual_network_subnet_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_network_subnet_name = _parse_virtual_network_subnet_name(d.pop("virtualNetworkSubnetName", UNSET))

        def _parse_network_security_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_security_group_name = _parse_network_security_group_name(d.pop("networkSecurityGroupName", UNSET))

        is_accelerated_networking_enabled = d.pop("isAcceleratedNetworkingEnabled", UNSET)

        def _parse_availability_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        availability_zone = _parse_availability_zone(d.pop("availabilityZone", UNSET))

        def _parse_availability_set_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        availability_set_name = _parse_availability_set_name(d.pop("availabilitySetName", UNSET))

        virtual_machine_restore_config_parameters = cls(
            name=name,
            subscription=subscription,
            region=region,
            resource_group=resource_group,
            vm_size_name=vm_size_name,
            virtual_network_name=virtual_network_name,
            virtual_network_subnet_name=virtual_network_subnet_name,
            network_security_group_name=network_security_group_name,
            is_accelerated_networking_enabled=is_accelerated_networking_enabled,
            availability_zone=availability_zone,
            availability_set_name=availability_set_name,
        )

        return virtual_machine_restore_config_parameters
