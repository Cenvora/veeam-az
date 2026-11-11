from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="VirtualNetworkFromClient")


@_attrs_define
class VirtualNetworkFromClient:
    """
    Attributes:
        network_name (str): Specifies a name for the new virtual network.
        region (str): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to an Azure
            region in which the virtual network will be created.
        network_address_space (str): Specifies an IP address range for the virtual network.
        subnet_name (str): Specifies a name for a subnet that will be created in the virtual network.
        subnet_address_space (str): Specifies an IP address range for the subnet.
    """

    network_name: str
    region: str
    network_address_space: str
    subnet_name: str
    subnet_address_space: str

    def to_dict(self) -> dict[str, Any]:
        network_name = self.network_name

        region = self.region

        network_address_space = self.network_address_space

        subnet_name = self.subnet_name

        subnet_address_space = self.subnet_address_space

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "networkName": network_name,
                "region": region,
                "networkAddressSpace": network_address_space,
                "subnetName": subnet_name,
                "subnetAddressSpace": subnet_address_space,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network_name = d.pop("networkName")

        region = d.pop("region")

        network_address_space = d.pop("networkAddressSpace")

        subnet_name = d.pop("subnetName")

        subnet_address_space = d.pop("subnetAddressSpace")

        virtual_network_from_client = cls(
            network_name=network_name,
            region=region,
            network_address_space=network_address_space,
            subnet_name=subnet_name,
            subnet_address_space=subnet_address_space,
        )

        return virtual_network_from_client
