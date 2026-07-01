from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualNetworkFromClientForToAlternative")


@_attrs_define
class VirtualNetworkFromClientForToAlternative:
    """Specifies a virtual network to which Azure VM will be restored.

    Attributes:
        id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to a
            virtual network.
        name (None | str | Unset): Specifies the name of the virtual network.
        region_name (None | str | Unset): Specifies the name of an Azure region where the virtual network resides.
        address_spaces (list[str] | None | Unset): Specifies IP address spaces that can be used for the restored Azure
            VM.
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    address_spaces: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        address_spaces: list[str] | None | Unset
        if isinstance(self.address_spaces, Unset):
            address_spaces = UNSET
        elif isinstance(self.address_spaces, list):
            address_spaces = self.address_spaces

        else:
            address_spaces = self.address_spaces

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if address_spaces is not UNSET:
            field_dict["addressSpaces"] = address_spaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        def _parse_address_spaces(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                address_spaces_type_0 = cast(list[str], data)

                return address_spaces_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        address_spaces = _parse_address_spaces(d.pop("addressSpaces", UNSET))

        virtual_network_from_client_for_to_alternative = cls(
            id=id,
            name=name,
            region_name=region_name,
            address_spaces=address_spaces,
        )

        return virtual_network_from_client_for_to_alternative
