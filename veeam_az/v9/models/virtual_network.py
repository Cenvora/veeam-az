from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="VirtualNetwork")


@_attrs_define
class VirtualNetwork:
    """Specifies information on a virtual network.

    Attributes:
        id (None | str | Unset): Resource ID of the virtual network.
        name (None | str | Unset): Name of the virtual network.
        region_name (None | str | Unset): Azure region where the virtual network resides.
        address_spaces (list[str] | None | Unset): IP address ranges for the virtual network.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    address_spaces: list[str] | None | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

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
        if name is not UNSET:
            field_dict["name"] = name
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if address_spaces is not UNSET:
            field_dict["addressSpaces"] = address_spaces
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

        virtual_network = cls(
            id=id,
            name=name,
            region_name=region_name,
            address_spaces=address_spaces,
            field_links=field_links,
        )

        return virtual_network
