from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sla_configuration import SlaConfiguration


T = TypeVar("T", bound="NewSlaTemplateFromClient")


@_attrs_define
class NewSlaTemplateFromClient:
    """
    Attributes:
        name (str | Unset): Specifies the name for the SLA template.
        description (str | Unset): Specifies the description of the SLA template.
        sla_configuration (SlaConfiguration | Unset): Specifies the SLA template configuration.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    sla_configuration: SlaConfiguration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        sla_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sla_configuration, Unset):
            sla_configuration = self.sla_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if sla_configuration is not UNSET:
            field_dict["slaConfiguration"] = sla_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sla_configuration import SlaConfiguration

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _sla_configuration = d.pop("slaConfiguration", UNSET)
        sla_configuration: SlaConfiguration | Unset
        if isinstance(_sla_configuration, Unset):
            sla_configuration = UNSET
        else:
            sla_configuration = SlaConfiguration.from_dict(_sla_configuration)

        new_sla_template_from_client = cls(
            name=name,
            description=description,
            sla_configuration=sla_configuration,
        )

        new_sla_template_from_client.additional_properties = d
        return new_sla_template_from_client

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
