from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerProfileDeletionResult")


@_attrs_define
class WorkerProfileDeletionResult:
    """Result of the performed operation.

    Attributes:
        busy_workers_exists (bool | Unset): Defines whether any workers with the removing worker profile are currently
            running.
        deletion_successfull (bool | Unset): Defines whether the worker profile was removed successfully.
    """

    busy_workers_exists: bool | Unset = UNSET
    deletion_successfull: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        busy_workers_exists = self.busy_workers_exists

        deletion_successfull = self.deletion_successfull

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if busy_workers_exists is not UNSET:
            field_dict["busyWorkersExists"] = busy_workers_exists
        if deletion_successfull is not UNSET:
            field_dict["deletionSuccessfull"] = deletion_successfull

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        busy_workers_exists = d.pop("busyWorkersExists", UNSET)

        deletion_successfull = d.pop("deletionSuccessfull", UNSET)

        worker_profile_deletion_result = cls(
            busy_workers_exists=busy_workers_exists,
            deletion_successfull=deletion_successfull,
        )

        return worker_profile_deletion_result
