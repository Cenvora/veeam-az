from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataRetrievalJobParameters")


@_attrs_define
class DataRetrievalJobParameters:
    """
    Attributes:
        is_restore_point_deleted (bool | Unset):
    """

    is_restore_point_deleted: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_restore_point_deleted = self.is_restore_point_deleted

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_restore_point_deleted is not UNSET:
            field_dict["isRestorePointDeleted"] = is_restore_point_deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_restore_point_deleted = d.pop("isRestorePointDeleted", UNSET)

        data_retrieval_job_parameters = cls(
            is_restore_point_deleted=is_restore_point_deleted,
        )

        return data_retrieval_job_parameters
