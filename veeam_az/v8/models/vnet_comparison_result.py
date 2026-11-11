from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.vnet_comparison_diff_type import VnetComparisonDiffType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VnetComparisonResult")


@_attrs_define
class VnetComparisonResult:
    """
    Attributes:
        name (None | str | Unset): Name of a virtual network configuration attribute.
        id (None | str | Unset):
        resource_type (None | str | Unset):
        type_ (VnetComparisonDiffType | Unset): Type of difference between the current Azure virtual network
            configuration and the backed-up virtual network configuration.
        old (None | str | Unset): Backed-up value of the virtual network configuration attribute.
        new (None | str | Unset): Current value of the virtual network configuration attribute.
        children (list[VnetComparisonResult] | None | Unset): Child attributes of the virtual network configuration
            attribute.
        can_expand (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    resource_type: None | str | Unset = UNSET
    type_: VnetComparisonDiffType | Unset = UNSET
    old: None | str | Unset = UNSET
    new: None | str | Unset = UNSET
    children: list[VnetComparisonResult] | None | Unset = UNSET
    can_expand: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        resource_type: None | str | Unset
        if isinstance(self.resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = self.resource_type

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        old: None | str | Unset
        if isinstance(self.old, Unset):
            old = UNSET
        else:
            old = self.old

        new: None | str | Unset
        if isinstance(self.new, Unset):
            new = UNSET
        else:
            new = self.new

        children: list[dict[str, Any]] | None | Unset
        if isinstance(self.children, Unset):
            children = UNSET
        elif isinstance(self.children, list):
            children = []
            for children_type_0_item_data in self.children:
                children_type_0_item = children_type_0_item_data.to_dict()
                children.append(children_type_0_item)

        else:
            children = self.children

        can_expand: bool | None | Unset
        if isinstance(self.can_expand, Unset):
            can_expand = UNSET
        else:
            can_expand = self.can_expand

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if old is not UNSET:
            field_dict["old"] = old
        if new is not UNSET:
            field_dict["new"] = new
        if children is not UNSET:
            field_dict["children"] = children
        if can_expand is not UNSET:
            field_dict["canExpand"] = can_expand

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_resource_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_type = _parse_resource_type(d.pop("resourceType", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: VnetComparisonDiffType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VnetComparisonDiffType(_type_)

        def _parse_old(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old = _parse_old(d.pop("old", UNSET))

        def _parse_new(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new = _parse_new(d.pop("new", UNSET))

        def _parse_children(data: object) -> list[VnetComparisonResult] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = []
                _children_type_0 = data
                for children_type_0_item_data in _children_type_0:
                    children_type_0_item = VnetComparisonResult.from_dict(children_type_0_item_data)

                    children_type_0.append(children_type_0_item)

                return children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VnetComparisonResult] | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))

        def _parse_can_expand(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_expand = _parse_can_expand(d.pop("canExpand", UNSET))

        vnet_comparison_result = cls(
            name=name,
            id=id,
            resource_type=resource_type,
            type_=type_,
            old=old,
            new=new,
            children=children,
            can_expand=can_expand,
        )

        return vnet_comparison_result
