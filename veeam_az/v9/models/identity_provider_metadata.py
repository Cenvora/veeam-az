from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityProviderMetadata")


@_attrs_define
class IdentityProviderMetadata:
    """
    Attributes:
        xml_base_64 (None | str | Unset): Specifies the contents of Identity Provider metadata file in the *base64*
            format after the *data:application/octet-stream;base64,* content header at the beginning.
    """

    xml_base_64: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        xml_base_64: None | str | Unset
        if isinstance(self.xml_base_64, Unset):
            xml_base_64 = UNSET
        else:
            xml_base_64 = self.xml_base_64

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if xml_base_64 is not UNSET:
            field_dict["xmlBase64"] = xml_base_64

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_xml_base_64(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xml_base_64 = _parse_xml_base_64(d.pop("xmlBase64", UNSET))

        identity_provider_metadata = cls(
            xml_base_64=xml_base_64,
        )

        return identity_provider_metadata
