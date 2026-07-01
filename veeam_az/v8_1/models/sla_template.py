from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.sla_configuration import SlaConfiguration


T = TypeVar("T", bound="SlaTemplate")


@_attrs_define
class SlaTemplate:
    """Information on each SLA template.

    Attributes:
        id (UUID | Unset): System ID assigned to the SLA template in the Veeam Backup for Microsoft Azure REST API.
        name (str | Unset): Name of the SLA template.
        description (str | Unset): Description of the SLA template.
        last_modified_utc (datetime.datetime | None | Unset): Date and time when the SLA template was last modified.
        assigned_policies (int | Unset): Number of SLA-based backup policies using the SLA template.
        sla_configuration (SlaConfiguration | Unset): Specifies the SLA template configuration.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    last_modified_utc: datetime.datetime | None | Unset = UNSET
    assigned_policies: int | Unset = UNSET
    sla_configuration: SlaConfiguration | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        description = self.description

        last_modified_utc: None | str | Unset
        if isinstance(self.last_modified_utc, Unset):
            last_modified_utc = UNSET
        elif isinstance(self.last_modified_utc, datetime.datetime):
            last_modified_utc = self.last_modified_utc.isoformat()
        else:
            last_modified_utc = self.last_modified_utc

        assigned_policies = self.assigned_policies

        sla_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sla_configuration, Unset):
            sla_configuration = self.sla_configuration.to_dict()

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if last_modified_utc is not UNSET:
            field_dict["lastModifiedUtc"] = last_modified_utc
        if assigned_policies is not UNSET:
            field_dict["assignedPolicies"] = assigned_policies
        if sla_configuration is not UNSET:
            field_dict["slaConfiguration"] = sla_configuration
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.sla_configuration import SlaConfiguration

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_last_modified_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_utc_type_0 = isoparse(data)

                return last_modified_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_modified_utc = _parse_last_modified_utc(d.pop("lastModifiedUtc", UNSET))

        assigned_policies = d.pop("assignedPolicies", UNSET)

        _sla_configuration = d.pop("slaConfiguration", UNSET)
        sla_configuration: SlaConfiguration | Unset
        if isinstance(_sla_configuration, Unset):
            sla_configuration = UNSET
        else:
            sla_configuration = SlaConfiguration.from_dict(_sla_configuration)

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

        sla_template = cls(
            id=id,
            name=name,
            description=description,
            last_modified_utc=last_modified_utc,
            assigned_policies=assigned_policies,
            sla_configuration=sla_configuration,
            field_links=field_links,
        )

        sla_template.additional_properties = d
        return sla_template

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
