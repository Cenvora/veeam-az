from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_resource_group_from_client import PolicyResourceGroupFromClient
    from ..models.policy_subscription_from_client import PolicySubscriptionFromClient
    from ..models.tag_from_client import TagFromClient


T = TypeVar("T", bound="PolicyTagGroupFromClient")


@_attrs_define
class PolicyTagGroupFromClient:
    """Specifies information on each condition.

    Attributes:
        name (str | Unset): Specifies the name for the condition.
        subscription (PolicySubscriptionFromClient | Unset):
        resource_group (PolicyResourceGroupFromClient | Unset):
        tags (list[TagFromClient] | Unset): Specifies one or more Azure tags that will be included in the condition.
    """

    name: str | Unset = UNSET
    subscription: PolicySubscriptionFromClient | Unset = UNSET
    resource_group: PolicyResourceGroupFromClient | Unset = UNSET
    tags: list[TagFromClient] | Unset = UNSET
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
        from ..models.policy_resource_group_from_client import PolicyResourceGroupFromClient
        from ..models.policy_subscription_from_client import PolicySubscriptionFromClient
        from ..models.tag_from_client import TagFromClient

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _subscription = d.pop("subscription", UNSET)
        subscription: PolicySubscriptionFromClient | Unset
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = PolicySubscriptionFromClient.from_dict(_subscription)

        _resource_group = d.pop("resourceGroup", UNSET)
        resource_group: PolicyResourceGroupFromClient | Unset
        if isinstance(_resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = PolicyResourceGroupFromClient.from_dict(_resource_group)

        _tags = d.pop("tags", UNSET)
        tags: list[TagFromClient] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = TagFromClient.from_dict(tags_item_data)

                tags.append(tags_item)

        policy_tag_group_from_client = cls(
            name=name,
            subscription=subscription,
            resource_group=resource_group,
            tags=tags,
        )

        policy_tag_group_from_client.additional_properties = d
        return policy_tag_group_from_client

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
