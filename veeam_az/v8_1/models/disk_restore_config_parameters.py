from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.disk_type import DiskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiskRestoreConfigParameters")


@_attrs_define
class DiskRestoreConfigParameters:
    """
    Attributes:
        name (None | str | Unset):
        subscription (None | str | Unset):
        region (None | str | Unset):
        resource_group (None | str | Unset):
        type_ (DiskType | Unset): Specifies the type of the virtual disk.
        storage_account_name (None | str | Unset):
        availability_zone (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    subscription: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    resource_group: None | str | Unset = UNSET
    type_: DiskType | Unset = UNSET
    storage_account_name: None | str | Unset = UNSET
    availability_zone: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        subscription: None | str | Unset
        if isinstance(self.subscription, Unset):
            subscription = UNSET
        else:
            subscription = self.subscription

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        resource_group: None | str | Unset
        if isinstance(self.resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = self.resource_group

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        storage_account_name: None | str | Unset
        if isinstance(self.storage_account_name, Unset):
            storage_account_name = UNSET
        else:
            storage_account_name = self.storage_account_name

        availability_zone: None | str | Unset
        if isinstance(self.availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = self.availability_zone

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if region is not UNSET:
            field_dict["region"] = region
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if type_ is not UNSET:
            field_dict["type"] = type_
        if storage_account_name is not UNSET:
            field_dict["storageAccountName"] = storage_account_name
        if availability_zone is not UNSET:
            field_dict["availabilityZone"] = availability_zone

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

        def _parse_subscription(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription = _parse_subscription(d.pop("subscription", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_resource_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group = _parse_resource_group(d.pop("resourceGroup", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: DiskType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DiskType(_type_)

        def _parse_storage_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_account_name = _parse_storage_account_name(d.pop("storageAccountName", UNSET))

        def _parse_availability_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        availability_zone = _parse_availability_zone(d.pop("availabilityZone", UNSET))

        disk_restore_config_parameters = cls(
            name=name,
            subscription=subscription,
            region=region,
            resource_group=resource_group,
            type_=type_,
            storage_account_name=storage_account_name,
            availability_zone=availability_zone,
        )

        return disk_restore_config_parameters
