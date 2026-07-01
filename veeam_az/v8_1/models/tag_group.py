from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_subscription import AzureSubscription
    from ..models.resource_group import ResourceGroup
    from ..models.tag import Tag


T = TypeVar("T", bound="TagGroup")


@_attrs_define
class TagGroup:
    """Information on a condition.

    Attributes:
        name (str | Unset): Name of the condition.
        subscription (AzureSubscription | Unset): Specifies information on an Azure subscription.
        resource_group (ResourceGroup | Unset): Specifies information on a resource group.
        tags (list[Tag] | Unset): Azure tags included in the condition.
    """

    name: str | Unset = UNSET
    subscription: AzureSubscription | Unset = UNSET
    resource_group: ResourceGroup | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        resource_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_group, Unset):
            resource_group = self.resource_group.to_dict()

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_subscription import AzureSubscription
        from ..models.resource_group import ResourceGroup
        from ..models.tag import Tag

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _subscription = d.pop("subscription", UNSET)
        subscription: AzureSubscription | Unset
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = AzureSubscription.from_dict(_subscription)

        _resource_group = d.pop("resourceGroup", UNSET)
        resource_group: ResourceGroup | Unset
        if isinstance(_resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = ResourceGroup.from_dict(_resource_group)

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        tag_group = cls(
            name=name,
            subscription=subscription,
            resource_group=resource_group,
            tags=tags,
        )

        tag_group.additional_properties = d
        return tag_group

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
