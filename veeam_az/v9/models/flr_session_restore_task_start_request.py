from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.flr_session_restore_type import FlrSessionRestoreType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrSessionRestoreTaskStartRequest")


@_attrs_define
class FlrSessionRestoreTaskStartRequest:
    """
    Attributes:
        item_paths (list[str] | Unset): Specifies a list of absolute paths to the items you want to restore.
            **Note**&#58; Relative paths are not allowed.
        restore_type (FlrSessionRestoreType | Unset): Defines whether you want to download a copy of the items or to
            restore the original items.
        alternative_path (None | str | Unset): Specifies an alternative path to the directory to which the items will be
            restored if the original directory no longer exists. **Note**&#58; Relative paths are not allowed.
    """

    item_paths: list[str] | Unset = UNSET
    restore_type: FlrSessionRestoreType | Unset = UNSET
    alternative_path: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_paths: list[str] | Unset = UNSET
        if not isinstance(self.item_paths, Unset):
            item_paths = self.item_paths

        restore_type: str | Unset = UNSET
        if not isinstance(self.restore_type, Unset):
            restore_type = self.restore_type.value

        alternative_path: None | str | Unset
        if isinstance(self.alternative_path, Unset):
            alternative_path = UNSET
        else:
            alternative_path = self.alternative_path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if item_paths is not UNSET:
            field_dict["itemPaths"] = item_paths
        if restore_type is not UNSET:
            field_dict["restoreType"] = restore_type
        if alternative_path is not UNSET:
            field_dict["alternativePath"] = alternative_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_paths = cast(list[str], d.pop("itemPaths", UNSET))

        _restore_type = d.pop("restoreType", UNSET)
        restore_type: FlrSessionRestoreType | Unset
        if isinstance(_restore_type, Unset):
            restore_type = UNSET
        else:
            restore_type = FlrSessionRestoreType(_restore_type)

        def _parse_alternative_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alternative_path = _parse_alternative_path(d.pop("alternativePath", UNSET))

        flr_session_restore_task_start_request = cls(
            item_paths=item_paths,
            restore_type=restore_type,
            alternative_path=alternative_path,
        )

        return flr_session_restore_task_start_request
