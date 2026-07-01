from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_security_group import NetworkSecurityGroup


T = TypeVar("T", bound="VirtualNetworkSubnet")


@_attrs_define
class VirtualNetworkSubnet:
    """Specifies a subnet of the virtual network.

    Attributes:
        network_security_group (NetworkSecurityGroup | Unset): Information on a network security group.
        name (None | str | Unset): Specifies the name of the subnet.
        address_space (None | str | Unset): Specifies IP address spaces in the subnet for the restored Azure VM.
    """

    network_security_group: NetworkSecurityGroup | Unset = UNSET
    name: None | str | Unset = UNSET
    address_space: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        network_security_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network_security_group, Unset):
            network_security_group = self.network_security_group.to_dict()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        address_space: None | str | Unset
        if isinstance(self.address_space, Unset):
            address_space = UNSET
        else:
            address_space = self.address_space

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if network_security_group is not UNSET:
            field_dict["networkSecurityGroup"] = network_security_group
        if name is not UNSET:
            field_dict["name"] = name
        if address_space is not UNSET:
            field_dict["addressSpace"] = address_space

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_security_group import NetworkSecurityGroup

        d = dict(src_dict)
        _network_security_group = d.pop("networkSecurityGroup", UNSET)
        network_security_group: NetworkSecurityGroup | Unset
        if isinstance(_network_security_group, Unset):
            network_security_group = UNSET
        else:
            network_security_group = NetworkSecurityGroup.from_dict(_network_security_group)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_address_space(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_space = _parse_address_space(d.pop("addressSpace", UNSET))

        virtual_network_subnet = cls(
            network_security_group=network_security_group,
            name=name,
            address_space=address_space,
        )

        return virtual_network_subnet
