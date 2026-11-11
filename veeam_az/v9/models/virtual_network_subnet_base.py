from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualNetworkSubnetBase")


@_attrs_define
class VirtualNetworkSubnetBase:
    """Information on the subnet.

    Attributes:
        name (None | str | Unset): Subnet name.
        address_space (None | str | Unset): Specifies an IP address range for the subnet.
    """

    name: None | str | Unset = UNSET
    address_space: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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
        if name is not UNSET:
            field_dict["name"] = name
        if address_space is not UNSET:
            field_dict["addressSpace"] = address_space

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

        def _parse_address_space(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_space = _parse_address_space(d.pop("addressSpace", UNSET))

        virtual_network_subnet_base = cls(
            name=name,
            address_space=address_space,
        )

        return virtual_network_subnet_base
