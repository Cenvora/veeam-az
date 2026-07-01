from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.flr_search_task_state import FlrSearchTaskState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flr_session_item import FlrSessionItem


T = TypeVar("T", bound="FlrSessionSearchTaskResult")


@_attrs_define
class FlrSessionSearchTaskResult:
    """
    Attributes:
        search_state (FlrSearchTaskState | Unset): State of the search task.
        count (int | Unset): Number of items in the response.
        results (list[FlrSessionItem] | Unset): Information on each item.
    """

    search_state: FlrSearchTaskState | Unset = UNSET
    count: int | Unset = UNSET
    results: list[FlrSessionItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        search_state: str | Unset = UNSET
        if not isinstance(self.search_state, Unset):
            search_state = self.search_state.value

        count = self.count

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if search_state is not UNSET:
            field_dict["searchState"] = search_state
        if count is not UNSET:
            field_dict["count"] = count
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flr_session_item import FlrSessionItem

        d = dict(src_dict)
        _search_state = d.pop("searchState", UNSET)
        search_state: FlrSearchTaskState | Unset
        if isinstance(_search_state, Unset):
            search_state = UNSET
        else:
            search_state = FlrSearchTaskState(_search_state)

        count = d.pop("count", UNSET)

        _results = d.pop("results", UNSET)
        results: list[FlrSessionItem] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = FlrSessionItem.from_dict(results_item_data)

                results.append(results_item)

        flr_session_search_task_result = cls(
            search_state=search_state,
            count=count,
            results=results,
        )

        return flr_session_search_task_result
