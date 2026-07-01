from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyRegionFromClient")


@_attrs_define
class PolicyRegionFromClient:
    """Specifies Azure regions where the protected resources reside.

    Attributes:
        region_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a region.
    """

    region_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if region_id is not UNSET:
            field_dict["regionId"] = region_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

        policy_region_from_client = cls(
            region_id=region_id,
        )

        return policy_region_from_client
