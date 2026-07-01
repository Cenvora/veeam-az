from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedFileShareExportOptions")


@_attrs_define
class ProtectedFileShareExportOptions:
    """
    Attributes:
        file_share_ids (list[str] | None | Unset): Specifies system IDs assigned in the Veeam Backup for Microsoft Azure
            REST API to the Azure file shares whose data will be exported.
        search_pattern (None | str | Unset): Exports only data on those items of a resource collection that match the
            specified search pattern in the parameter value.
    """

    file_share_ids: list[str] | None | Unset = UNSET
    search_pattern: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_share_ids: list[str] | None | Unset
        if isinstance(self.file_share_ids, Unset):
            file_share_ids = UNSET
        elif isinstance(self.file_share_ids, list):
            file_share_ids = self.file_share_ids

        else:
            file_share_ids = self.file_share_ids

        search_pattern: None | str | Unset
        if isinstance(self.search_pattern, Unset):
            search_pattern = UNSET
        else:
            search_pattern = self.search_pattern

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_share_ids is not UNSET:
            field_dict["fileShareIds"] = file_share_ids
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_file_share_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_share_ids_type_0 = cast(list[str], data)

                return file_share_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        file_share_ids = _parse_file_share_ids(d.pop("fileShareIds", UNSET))

        def _parse_search_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_pattern = _parse_search_pattern(d.pop("searchPattern", UNSET))

        protected_file_share_export_options = cls(
            file_share_ids=file_share_ids,
            search_pattern=search_pattern,
        )

        return protected_file_share_export_options
