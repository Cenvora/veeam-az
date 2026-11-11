from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_subscription import AzureSubscription
    from ..models.policy_item_deleted_from_azure import PolicyItemDeletedFromAzure
    from ..models.resource_group import ResourceGroup
    from ..models.tag import Tag
    from ..models.tag_group import TagGroup
    from ..models.virtual_machine import VirtualMachine


T = TypeVar("T", bound="PolicyBackupItem")


@_attrs_define
class PolicyBackupItem:
    """
    Attributes:
        subscription (AzureSubscription | Unset): Specifies information on an Azure subscription.
        tag (Tag | Unset): Information on an Azure tag.
        resource_group (ResourceGroup | Unset): Specifies information on a resource group.
        virtual_machine (VirtualMachine | Unset): Information on an Azure VM.
        deleted_item (PolicyItemDeletedFromAzure | Unset): Specifies information on a resource deleted from the
            Microsoft Azure infrastructure.
        tag_group (TagGroup | Unset): Information on a condition.
    """

    subscription: AzureSubscription | Unset = UNSET
    tag: Tag | Unset = UNSET
    resource_group: ResourceGroup | Unset = UNSET
    virtual_machine: VirtualMachine | Unset = UNSET
    deleted_item: PolicyItemDeletedFromAzure | Unset = UNSET
    tag_group: TagGroup | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.to_dict()

        resource_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_group, Unset):
            resource_group = self.resource_group.to_dict()

        virtual_machine: dict[str, Any] | Unset = UNSET
        if not isinstance(self.virtual_machine, Unset):
            virtual_machine = self.virtual_machine.to_dict()

        deleted_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deleted_item, Unset):
            deleted_item = self.deleted_item.to_dict()

        tag_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag_group, Unset):
            tag_group = self.tag_group.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if tag is not UNSET:
            field_dict["tag"] = tag
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if virtual_machine is not UNSET:
            field_dict["virtualMachine"] = virtual_machine
        if deleted_item is not UNSET:
            field_dict["deletedItem"] = deleted_item
        if tag_group is not UNSET:
            field_dict["tagGroup"] = tag_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_subscription import AzureSubscription
        from ..models.policy_item_deleted_from_azure import PolicyItemDeletedFromAzure
        from ..models.resource_group import ResourceGroup
        from ..models.tag import Tag
        from ..models.tag_group import TagGroup
        from ..models.virtual_machine import VirtualMachine

        d = dict(src_dict)
        _subscription = d.pop("subscription", UNSET)
        subscription: AzureSubscription | Unset
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = AzureSubscription.from_dict(_subscription)

        _tag = d.pop("tag", UNSET)
        tag: Tag | Unset
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = Tag.from_dict(_tag)

        _resource_group = d.pop("resourceGroup", UNSET)
        resource_group: ResourceGroup | Unset
        if isinstance(_resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = ResourceGroup.from_dict(_resource_group)

        _virtual_machine = d.pop("virtualMachine", UNSET)
        virtual_machine: VirtualMachine | Unset
        if isinstance(_virtual_machine, Unset):
            virtual_machine = UNSET
        else:
            virtual_machine = VirtualMachine.from_dict(_virtual_machine)

        _deleted_item = d.pop("deletedItem", UNSET)
        deleted_item: PolicyItemDeletedFromAzure | Unset
        if isinstance(_deleted_item, Unset):
            deleted_item = UNSET
        else:
            deleted_item = PolicyItemDeletedFromAzure.from_dict(_deleted_item)

        _tag_group = d.pop("tagGroup", UNSET)
        tag_group: TagGroup | Unset
        if isinstance(_tag_group, Unset):
            tag_group = UNSET
        else:
            tag_group = TagGroup.from_dict(_tag_group)

        policy_backup_item = cls(
            subscription=subscription,
            tag=tag,
            resource_group=resource_group,
            virtual_machine=virtual_machine,
            deleted_item=deleted_item,
            tag_group=tag_group,
        )

        return policy_backup_item
