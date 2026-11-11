from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_virtual_machine_from_client import PolicyVirtualMachineFromClient
    from ..models.tag_from_client import TagFromClient


T = TypeVar("T", bound="PolicyExcludedItemsFromClient")


@_attrs_define
class PolicyExcludedItemsFromClient:
    """Specifies Azure tags to identify the resources that should be excluded from the backup scope.

    Attributes:
        virtual_machines (list[PolicyVirtualMachineFromClient] | None | Unset): Specifies the Azure VMs that will be
            excluded from the backup policy.
        tags (list[TagFromClient] | None | Unset): Specifies Azure tags to exclude from the backup policy Azure VMs that
            have this tag assigned.
    """

    virtual_machines: list[PolicyVirtualMachineFromClient] | None | Unset = UNSET
    tags: list[TagFromClient] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        virtual_machines: list[dict[str, Any]] | None | Unset
        if isinstance(self.virtual_machines, Unset):
            virtual_machines = UNSET
        elif isinstance(self.virtual_machines, list):
            virtual_machines = []
            for virtual_machines_type_0_item_data in self.virtual_machines:
                virtual_machines_type_0_item = virtual_machines_type_0_item_data.to_dict()
                virtual_machines.append(virtual_machines_type_0_item)

        else:
            virtual_machines = self.virtual_machines

        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if virtual_machines is not UNSET:
            field_dict["virtualMachines"] = virtual_machines
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_virtual_machine_from_client import PolicyVirtualMachineFromClient
        from ..models.tag_from_client import TagFromClient

        d = dict(src_dict)

        def _parse_virtual_machines(data: object) -> list[PolicyVirtualMachineFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                virtual_machines_type_0 = []
                _virtual_machines_type_0 = data
                for virtual_machines_type_0_item_data in _virtual_machines_type_0:
                    virtual_machines_type_0_item = PolicyVirtualMachineFromClient.from_dict(
                        virtual_machines_type_0_item_data
                    )

                    virtual_machines_type_0.append(virtual_machines_type_0_item)

                return virtual_machines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PolicyVirtualMachineFromClient] | None | Unset, data)

        virtual_machines = _parse_virtual_machines(d.pop("virtualMachines", UNSET))

        def _parse_tags(data: object) -> list[TagFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = TagFromClient.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TagFromClient] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        policy_excluded_items_from_client = cls(
            virtual_machines=virtual_machines,
            tags=tags,
        )

        return policy_excluded_items_from_client
