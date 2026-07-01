from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_item_deleted_from_azure import PolicyItemDeletedFromAzure
    from ..models.tag import Tag
    from ..models.virtual_machine import VirtualMachine


T = TypeVar("T", bound="PolicyExcludedItem")


@_attrs_define
class PolicyExcludedItem:
    """Information on each excluded resource.

    Attributes:
        virtual_machine (VirtualMachine | Unset): Information on an Azure VM.
        deleted_item (PolicyItemDeletedFromAzure | Unset): Specifies information on a resource deleted from the
            Microsoft Azure infrastructure.
        tag (Tag | Unset): Information on an Azure tag.
    """

    virtual_machine: VirtualMachine | Unset = UNSET
    deleted_item: PolicyItemDeletedFromAzure | Unset = UNSET
    tag: Tag | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        virtual_machine: dict[str, Any] | Unset = UNSET
        if not isinstance(self.virtual_machine, Unset):
            virtual_machine = self.virtual_machine.to_dict()

        deleted_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deleted_item, Unset):
            deleted_item = self.deleted_item.to_dict()

        tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if virtual_machine is not UNSET:
            field_dict["virtualMachine"] = virtual_machine
        if deleted_item is not UNSET:
            field_dict["deletedItem"] = deleted_item
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_item_deleted_from_azure import PolicyItemDeletedFromAzure
        from ..models.tag import Tag
        from ..models.virtual_machine import VirtualMachine

        d = dict(src_dict)
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

        _tag = d.pop("tag", UNSET)
        tag: Tag | Unset
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = Tag.from_dict(_tag)

        policy_excluded_item = cls(
            virtual_machine=virtual_machine,
            deleted_item=deleted_item,
            tag=tag,
        )

        return policy_excluded_item
