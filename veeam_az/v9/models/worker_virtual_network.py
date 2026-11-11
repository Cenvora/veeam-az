from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerVirtualNetwork")


@_attrs_define
class WorkerVirtualNetwork:
    """Information on a virtual network in which worker instances are launched.

    Attributes:
        name (None | str | Unset): Name of the virtual network.
        resource_id (None | str | Unset): Resource ID of the virtual network.
        subnet (None | str | Unset): Name of a subnet to which worker instances are connected.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region where the virtual network resides.
        resource_group_id (None | str | Unset): Resource ID assigned to a resource group that hosts the virtual network.
        subscription_id (UUID | Unset): Microsoft Azure ID assigned to a subscription where the virtual network belongs.
        resource_group_name (None | str | Unset): Name of the resource group.
    """

    name: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    subnet: None | str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    resource_group_id: None | str | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        subnet: None | str | Unset
        if isinstance(self.subnet, Unset):
            subnet = UNSET
        else:
            subnet = self.subnet

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        resource_group_id: None | str | Unset
        if isinstance(self.resource_group_id, Unset):
            resource_group_id = UNSET
        else:
            resource_group_id = self.resource_group_id

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        resource_group_name: None | str | Unset
        if isinstance(self.resource_group_name, Unset):
            resource_group_name = UNSET
        else:
            resource_group_name = self.resource_group_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if resource_group_id is not UNSET:
            field_dict["resourceGroupId"] = resource_group_id
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name

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

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        def _parse_subnet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subnet = _parse_subnet(d.pop("subnet", UNSET))

        def _parse_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

        def _parse_resource_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_id = _parse_resource_group_id(d.pop("resourceGroupId", UNSET))

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        def _parse_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_name = _parse_resource_group_name(d.pop("resourceGroupName", UNSET))

        worker_virtual_network = cls(
            name=name,
            resource_id=resource_id,
            subnet=subnet,
            region_id=region_id,
            resource_group_id=resource_group_id,
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
        )

        return worker_virtual_network
