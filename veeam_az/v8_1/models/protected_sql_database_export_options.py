from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedSqlDatabaseExportOptions")


@_attrs_define
class ProtectedSqlDatabaseExportOptions:
    """
    Attributes:
        database_ids (list[str] | None | Unset): Specifies system IDs assigned in the Veeam Backup for Microsoft Azure
            REST API to the Azure SQL databases whose data will be exported.
        search_pattern (None | str | Unset): Exports only data on those items of a resource collection that match the
            specified search pattern in the parameter value.
    """

    database_ids: list[str] | None | Unset = UNSET
    search_pattern: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        database_ids: list[str] | None | Unset
        if isinstance(self.database_ids, Unset):
            database_ids = UNSET
        elif isinstance(self.database_ids, list):
            database_ids = self.database_ids

        else:
            database_ids = self.database_ids

        search_pattern: None | str | Unset
        if isinstance(self.search_pattern, Unset):
            search_pattern = UNSET
        else:
            search_pattern = self.search_pattern

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if database_ids is not UNSET:
            field_dict["databaseIds"] = database_ids
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_database_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                database_ids_type_0 = cast(list[str], data)

                return database_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        database_ids = _parse_database_ids(d.pop("databaseIds", UNSET))

        def _parse_search_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_pattern = _parse_search_pattern(d.pop("searchPattern", UNSET))

        protected_sql_database_export_options = cls(
            database_ids=database_ids,
            search_pattern=search_pattern,
        )

        return protected_sql_database_export_options
