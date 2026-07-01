from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.resource_type import ResourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="AzureResource")


@_attrs_define
class AzureResource:
    """Information on an Azure resource.

    Attributes:
        id (None | str | Unset): System ID of the Azure resource.
        name (None | str | Unset): Name of the Azure resource.
        display_name (None | str | Unset): Azure name of the Azure resource.
        resource_group_name (None | str | Unset): Name of a resource group where the Azure resource belongs.
        resource_type (ResourceType | Unset): Type of the Azure resource.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region where the Azure resource resides.
        region_name (None | str | Unset): Name of the Azure region where the Azure resource resides.
        subscription_id (UUID | Unset): Microsoft Azure ID assigned to a subscription to which the Azure resource
            belongs.
        subscription_name (None | str | Unset):
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET
    resource_type: ResourceType | Unset = UNSET
    region_id: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    subscription_name: None | str | Unset = UNSET
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

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        resource_group_name: None | str | Unset
        if isinstance(self.resource_group_name, Unset):
            resource_group_name = UNSET
        else:
            resource_group_name = self.resource_group_name

        resource_type: str | Unset = UNSET
        if not isinstance(self.resource_type, Unset):
            resource_type = self.resource_type.value

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        subscription_name: None | str | Unset
        if isinstance(self.subscription_name, Unset):
            subscription_name = UNSET
        else:
            subscription_name = self.subscription_name

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
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
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

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_name = _parse_resource_group_name(d.pop("resourceGroupName", UNSET))

        _resource_type = d.pop("resourceType", UNSET)
        resource_type: ResourceType | Unset
        if isinstance(_resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = ResourceType(_resource_type)

        def _parse_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        def _parse_subscription_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_name = _parse_subscription_name(d.pop("subscriptionName", UNSET))

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

        azure_resource = cls(
            id=id,
            name=name,
            display_name=display_name,
            resource_group_name=resource_group_name,
            resource_type=resource_type,
            region_id=region_id,
            region_name=region_name,
            subscription_id=subscription_id,
            subscription_name=subscription_name,
            field_links=field_links,
        )

        return azure_resource
