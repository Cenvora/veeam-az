from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.job_status import JobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="VnetRestoredItem")


@_attrs_define
class VnetRestoredItem:
    """Information on each restored resource.

    Attributes:
        name (None | str | Unset): Name of the resource.
        resource_group_name (None | str | Unset): Name of a resource group to which the restored resource belongs.
        region_name (None | str | Unset): Name of the Azure region where the restored resource resides.
        subscription_name (None | str | Unset): Name of the Azure subscription where the restored resource resides.
        status (JobStatus | Unset): Specifies the status of the performed session.
    """

    name: None | str | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    subscription_name: None | str | Unset = UNSET
    status: JobStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        resource_group_name: None | str | Unset
        if isinstance(self.resource_group_name, Unset):
            resource_group_name = UNSET
        else:
            resource_group_name = self.resource_group_name

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        subscription_name: None | str | Unset
        if isinstance(self.subscription_name, Unset):
            subscription_name = UNSET
        else:
            subscription_name = self.subscription_name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
        if status is not UNSET:
            field_dict["status"] = status

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

        def _parse_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_name = _parse_resource_group_name(d.pop("resourceGroupName", UNSET))

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        def _parse_subscription_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_name = _parse_subscription_name(d.pop("subscriptionName", UNSET))

        _status = d.pop("status", UNSET)
        status: JobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobStatus(_status)

        vnet_restored_item = cls(
            name=name,
            resource_group_name=resource_group_name,
            region_name=region_name,
            subscription_name=subscription_name,
            status=status,
        )

        return vnet_restored_item
