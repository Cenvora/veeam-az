from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestoredDatabase")


@_attrs_define
class RestoredDatabase:
    """Information on each restored SQL database.

    Attributes:
        name (None | str | Unset): Name of the database.
        sql_server_name (None | str | Unset): Name of a SQL Server where the database belongs.
        elastic_pool_name (None | str | Unset): Name of an elastic pool where the database belongs.
    """

    name: None | str | Unset = UNSET
    sql_server_name: None | str | Unset = UNSET
    elastic_pool_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        sql_server_name: None | str | Unset
        if isinstance(self.sql_server_name, Unset):
            sql_server_name = UNSET
        else:
            sql_server_name = self.sql_server_name

        elastic_pool_name: None | str | Unset
        if isinstance(self.elastic_pool_name, Unset):
            elastic_pool_name = UNSET
        else:
            elastic_pool_name = self.elastic_pool_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if sql_server_name is not UNSET:
            field_dict["sqlServerName"] = sql_server_name
        if elastic_pool_name is not UNSET:
            field_dict["elasticPoolName"] = elastic_pool_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_sql_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sql_server_name = _parse_sql_server_name(d.pop("sqlServerName", UNSET))

        def _parse_elastic_pool_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        elastic_pool_name = _parse_elastic_pool_name(d.pop("elasticPoolName", UNSET))

        restored_database = cls(
            name=name,
            sql_server_name=sql_server_name,
            elastic_pool_name=elastic_pool_name,
        )

        return restored_database
