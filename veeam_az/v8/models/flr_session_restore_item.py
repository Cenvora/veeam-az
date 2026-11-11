from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.flr_session_restore_task_status import FlrSessionRestoreTaskStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrSessionRestoreItem")


@_attrs_define
class FlrSessionRestoreItem:
    """
    Attributes:
        path (str | Unset): Path to the directory on the Azure VM where the restore task was initiated.
        status (FlrSessionRestoreTaskStatus | Unset): Status of the restore task.
    """

    path: str | Unset = UNSET
    status: FlrSessionRestoreTaskStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _status = d.pop("status", UNSET)
        status: FlrSessionRestoreTaskStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FlrSessionRestoreTaskStatus(_status)

        flr_session_restore_item = cls(
            path=path,
            status=status,
        )

        return flr_session_restore_item
