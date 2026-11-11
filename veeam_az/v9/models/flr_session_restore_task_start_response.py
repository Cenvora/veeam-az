from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrSessionRestoreTaskStartResponse")


@_attrs_define
class FlrSessionRestoreTaskStartResponse:
    """
    Attributes:
        restore_task_id (UUID | Unset):
    """

    restore_task_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_task_id: str | Unset = UNSET
        if not isinstance(self.restore_task_id, Unset):
            restore_task_id = str(self.restore_task_id)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if restore_task_id is not UNSET:
            field_dict["restoreTaskId"] = restore_task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _restore_task_id = d.pop("restoreTaskId", UNSET)
        restore_task_id: UUID | Unset
        if isinstance(_restore_task_id, Unset):
            restore_task_id = UNSET
        else:
            restore_task_id = UUID(_restore_task_id)

        flr_session_restore_task_start_response = cls(
            restore_task_id=restore_task_id,
        )

        return flr_session_restore_task_start_response
