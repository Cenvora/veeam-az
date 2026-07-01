from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrSessionBrowseRequest")


@_attrs_define
class FlrSessionBrowseRequest:
    """
    Attributes:
        path (str | Unset): Specifies the absolute path to the Azure VM whose files and folders are restored by the FLR
            session. **Note**&#58; Relative paths are not allowed.
    """

    path: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        flr_session_browse_request = cls(
            path=path,
        )

        return flr_session_browse_request
