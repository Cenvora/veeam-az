from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostEstimationMeterResource")


@_attrs_define
class CostEstimationMeterResource:
    """Information on the disk used by the backup policy.

    Attributes:
        name (None | str | Unset): Name of the disk used by the backup policy.
        hash_id (None | str | Unset): Internal ID assigned to the disk in the Veeam Backup for Microsoft Azure REST API.
        resource_id (None | str | Unset): Resource ID of the disk.
        size_gb (float | Unset): Size of the disk (in GB).
    """

    name: None | str | Unset = UNSET
    hash_id: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    size_gb: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        hash_id: None | str | Unset
        if isinstance(self.hash_id, Unset):
            hash_id = UNSET
        else:
            hash_id = self.hash_id

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        size_gb = self.size_gb

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if hash_id is not UNSET:
            field_dict["hashId"] = hash_id
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if size_gb is not UNSET:
            field_dict["sizeGB"] = size_gb

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

        def _parse_hash_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hash_id = _parse_hash_id(d.pop("hashId", UNSET))

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        size_gb = d.pop("sizeGB", UNSET)

        cost_estimation_meter_resource = cls(
            name=name,
            hash_id=hash_id,
            resource_id=resource_id,
            size_gb=size_gb,
        )

        return cost_estimation_meter_resource
