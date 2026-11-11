from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flr_session_pagination import FlrSessionPagination
    from ..models.flr_session_restore_task_log_item import FlrSessionRestoreTaskLogItem


T = TypeVar("T", bound="FlrSessionRestoreTaskLogsResponse")


@_attrs_define
class FlrSessionRestoreTaskLogsResponse:
    """
    Attributes:
        path (str | Unset):
        pagination (FlrSessionPagination | Unset):
        results (list[FlrSessionRestoreTaskLogItem] | Unset): List of log records.
    """

    path: str | Unset = UNSET
    pagination: FlrSessionPagination | Unset = UNSET
    results: list[FlrSessionRestoreTaskLogItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flr_session_pagination import FlrSessionPagination
        from ..models.flr_session_restore_task_log_item import FlrSessionRestoreTaskLogItem

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _pagination = d.pop("pagination", UNSET)
        pagination: FlrSessionPagination | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = FlrSessionPagination.from_dict(_pagination)

        _results = d.pop("results", UNSET)
        results: list[FlrSessionRestoreTaskLogItem] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = FlrSessionRestoreTaskLogItem.from_dict(results_item_data)

                results.append(results_item)

        flr_session_restore_task_logs_response = cls(
            path=path,
            pagination=pagination,
            results=results,
        )

        return flr_session_restore_task_logs_response
