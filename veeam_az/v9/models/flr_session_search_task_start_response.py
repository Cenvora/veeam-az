from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrSessionSearchTaskStartResponse")


@_attrs_define
class FlrSessionSearchTaskStartResponse:
    """
    Attributes:
        search_id (UUID | Unset): Specifies the system ID assigned to the search task in the Veeam Backup for Microsoft
            Azure REST API.
    """

    search_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        search_id: str | Unset = UNSET
        if not isinstance(self.search_id, Unset):
            search_id = str(self.search_id)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if search_id is not UNSET:
            field_dict["searchId"] = search_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _search_id = d.pop("searchId", UNSET)
        search_id: UUID | Unset
        if isinstance(_search_id, Unset):
            search_id = UNSET
        else:
            search_id = UUID(_search_id)

        flr_session_search_task_start_response = cls(
            search_id=search_id,
        )

        return flr_session_search_task_start_response
