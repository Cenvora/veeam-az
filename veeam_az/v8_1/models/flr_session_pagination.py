from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrSessionPagination")


@_attrs_define
class FlrSessionPagination:
    """
    Attributes:
        total_count (int | None | Unset):
        count (int | Unset):
        offset (int | Unset):
        limit (int | Unset):
    """

    total_count: int | None | Unset = UNSET
    count: int | Unset = UNSET
    offset: int | Unset = UNSET
    limit: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_count: int | None | Unset
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        else:
            total_count = self.total_count

        count = self.count

        offset = self.offset

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if count is not UNSET:
            field_dict["count"] = count
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_total_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_count = _parse_total_count(d.pop("totalCount", UNSET))

        count = d.pop("count", UNSET)

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        flr_session_pagination = cls(
            total_count=total_count,
            count=count,
            offset=offset,
            limit=limit,
        )

        return flr_session_pagination
