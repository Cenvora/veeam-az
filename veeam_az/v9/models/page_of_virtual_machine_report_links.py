from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.link_hal import LinkHAL


T = TypeVar("T", bound="PageOfVirtualMachineReportLinks")


@_attrs_define
class PageOfVirtualMachineReportLinks:
    """URLs of operations where the properties obtained in the response can be used as an input."""

    additional_properties: dict[str, LinkHAL] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link_hal import LinkHAL

        d = dict(src_dict)
        page_of_virtual_machine_report_links = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = LinkHAL.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        page_of_virtual_machine_report_links.additional_properties = additional_properties
        return page_of_virtual_machine_report_links

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> LinkHAL:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: LinkHAL) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
