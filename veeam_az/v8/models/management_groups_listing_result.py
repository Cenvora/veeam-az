from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.management_group import ManagementGroup


T = TypeVar("T", bound="ManagementGroupsListingResult")


@_attrs_define
class ManagementGroupsListingResult:
    """
    Attributes:
        management_groups (list[ManagementGroup] | None | Unset): Information on an Azure management groups.
    """

    management_groups: list[ManagementGroup] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        management_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.management_groups, Unset):
            management_groups = UNSET
        elif isinstance(self.management_groups, list):
            management_groups = []
            for management_groups_type_0_item_data in self.management_groups:
                management_groups_type_0_item = management_groups_type_0_item_data.to_dict()
                management_groups.append(management_groups_type_0_item)

        else:
            management_groups = self.management_groups

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if management_groups is not UNSET:
            field_dict["managementGroups"] = management_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.management_group import ManagementGroup

        d = dict(src_dict)

        def _parse_management_groups(data: object) -> list[ManagementGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                management_groups_type_0 = []
                _management_groups_type_0 = data
                for management_groups_type_0_item_data in _management_groups_type_0:
                    management_groups_type_0_item = ManagementGroup.from_dict(management_groups_type_0_item_data)

                    management_groups_type_0.append(management_groups_type_0_item)

                return management_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ManagementGroup] | None | Unset, data)

        management_groups = _parse_management_groups(d.pop("managementGroups", UNSET))

        management_groups_listing_result = cls(
            management_groups=management_groups,
        )

        return management_groups_listing_result
