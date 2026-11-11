from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.storage_template_configuration import StorageTemplateConfiguration


T = TypeVar("T", bound="StorageTemplate")


@_attrs_define
class StorageTemplate:
    """
    Attributes:
        id (UUID | Unset): System ID assigned to a storage template in the Veeam Backup for Microsoft Azure REST API.
        name (str | Unset): Name of the storage template.
        description (None | str | Unset): Description of the storage template.
        is_assigned (bool | Unset): Defines whether the storage template is assigned to any SLA-based backup policies.
        storage_configuration (StorageTemplateConfiguration | Unset): Storage template configuration.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_assigned: bool | Unset = UNSET
    storage_configuration: StorageTemplateConfiguration | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_assigned = self.is_assigned

        storage_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_configuration, Unset):
            storage_configuration = self.storage_configuration.to_dict()

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
        if is_assigned is not UNSET:
            field_dict["isAssigned"] = is_assigned
        if storage_configuration is not UNSET:
            field_dict["storageConfiguration"] = storage_configuration
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.storage_template_configuration import StorageTemplateConfiguration

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        is_assigned = d.pop("isAssigned", UNSET)

        _storage_configuration = d.pop("storageConfiguration", UNSET)
        storage_configuration: StorageTemplateConfiguration | Unset
        if isinstance(_storage_configuration, Unset):
            storage_configuration = UNSET
        else:
            storage_configuration = StorageTemplateConfiguration.from_dict(_storage_configuration)

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

        storage_template = cls(
            id=id,
            name=name,
            description=description,
            is_assigned=is_assigned,
            storage_configuration=storage_configuration,
            field_links=field_links,
        )

        storage_template.additional_properties = d
        return storage_template

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
