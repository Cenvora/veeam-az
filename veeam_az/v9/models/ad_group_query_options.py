from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AdGroupQueryOptions")


@_attrs_define
class AdGroupQueryOptions:
    """Specifies the order to sort the returned items by value of the `displayName` property. Use `DisplayNameDesc` or
    `DisplayNameAsc` values. </br> Example&#58; `"queryOptions":{"sort":"DisplayNameDesc"}`

    """

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        ad_group_query_options = cls()

        return ad_group_query_options
