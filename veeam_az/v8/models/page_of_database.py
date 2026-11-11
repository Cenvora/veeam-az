from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database import Database
    from ..models.page_of_database_links import PageOfDatabaseLinks


T = TypeVar("T", bound="PageOfDatabase")


@_attrs_define
class PageOfDatabase:
    """Information on the response.

    Attributes:
        offset (int): Number of items excluded from the response.
        limit (int): Maximum number of items to return in the response.
        total_count (int | None | Unset): Total number of items.
        field_links (PageOfDatabaseLinks | Unset): URLs of operations where the properties obtained in the response can
            be used as an input.
        results (list[Database] | Unset): Results of the performed operation.
    """

    offset: int
    limit: int
    total_count: int | None | Unset = UNSET
    field_links: PageOfDatabaseLinks | Unset = UNSET
    results: list[Database] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        total_count: int | None | Unset
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        else:
            total_count = self.total_count

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database import Database
        from ..models.page_of_database_links import PageOfDatabaseLinks

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_total_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_count = _parse_total_count(d.pop("totalCount", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: PageOfDatabaseLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = PageOfDatabaseLinks.from_dict(_field_links)

        _results = d.pop("results", UNSET)
        results: list[Database] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = Database.from_dict(results_item_data)

                results.append(results_item)

        page_of_database = cls(
            offset=offset,
            limit=limit,
            total_count=total_count,
            field_links=field_links,
            results=results,
        )

        page_of_database.additional_properties = d
        return page_of_database

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
