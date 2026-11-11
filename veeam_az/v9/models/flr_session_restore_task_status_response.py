from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flr_session_restore_item import FlrSessionRestoreItem


T = TypeVar("T", bound="FlrSessionRestoreTaskStatusResponse")


@_attrs_define
class FlrSessionRestoreTaskStatusResponse:
    """
    Attributes:
        restore_task_id (UUID | Unset): System ID assigned to the restore task in the Veeam Backup for Microsoft Azure
            REST API.
        results (list[FlrSessionRestoreItem] | Unset): Information on the restore task.
    """

    restore_task_id: UUID | Unset = UNSET
    results: list[FlrSessionRestoreItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_task_id: str | Unset = UNSET
        if not isinstance(self.restore_task_id, Unset):
            restore_task_id = str(self.restore_task_id)

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if restore_task_id is not UNSET:
            field_dict["restoreTaskId"] = restore_task_id
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flr_session_restore_item import FlrSessionRestoreItem

        d = dict(src_dict)
        _restore_task_id = d.pop("restoreTaskId", UNSET)
        restore_task_id: UUID | Unset
        if isinstance(_restore_task_id, Unset):
            restore_task_id = UNSET
        else:
            restore_task_id = UUID(_restore_task_id)

        _results = d.pop("results", UNSET)
        results: list[FlrSessionRestoreItem] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = FlrSessionRestoreItem.from_dict(results_item_data)

                results.append(results_item)

        flr_session_restore_task_status_response = cls(
            restore_task_id=restore_task_id,
            results=results,
        )

        return flr_session_restore_task_status_response
