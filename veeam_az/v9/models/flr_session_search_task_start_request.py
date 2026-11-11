from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrSessionSearchTaskStartRequest")


@_attrs_define
class FlrSessionSearchTaskStartRequest:
    """
    Attributes:
        path (str | Unset): Specifies the absolute path to the directory on the Azure VM whose items will be returned in
            the response. **Note**&#58; Relative paths are not allowed.
        limit (int | None | Unset): Specifies the maximum number of items of a resource collection to return in a
            response.
        traverse (bool | Unset): Defines whether the search must be performed through all subdirectories and nested
            elements.
        search_pattern (str | Unset): Returns only those items of a resource collection whose names match the specified
            search pattern in the parameter value.
    """

    path: str | Unset = UNSET
    limit: int | None | Unset = UNSET
    traverse: bool | Unset = UNSET
    search_pattern: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        traverse = self.traverse

        search_pattern = self.search_pattern

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if limit is not UNSET:
            field_dict["limit"] = limit
        if traverse is not UNSET:
            field_dict["traverse"] = traverse
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        traverse = d.pop("traverse", UNSET)

        search_pattern = d.pop("searchPattern", UNSET)

        flr_session_search_task_start_request = cls(
            path=path,
            limit=limit,
            traverse=traverse,
            search_pattern=search_pattern,
        )

        return flr_session_search_task_start_request
