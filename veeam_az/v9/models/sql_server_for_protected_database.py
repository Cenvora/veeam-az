from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sql_server_type import SqlServerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlServerForProtectedDatabase")


@_attrs_define
class SqlServerForProtectedDatabase:
    """Information on a SQL Server where the database belongs.

    Attributes:
        id (None | str | Unset): System ID assigned to the SQL Server in the Veeam Backup for Microsoft Azure REST API.
        name (None | str | Unset): Name of the SQL Server.
        server_type (SqlServerType | Unset): Type of the SQL Server.
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    server_type: SqlServerType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        server_type: str | Unset = UNSET
        if not isinstance(self.server_type, Unset):
            server_type = self.server_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if server_type is not UNSET:
            field_dict["serverType"] = server_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _server_type = d.pop("serverType", UNSET)
        server_type: SqlServerType | Unset
        if isinstance(_server_type, Unset):
            server_type = UNSET
        else:
            server_type = SqlServerType(_server_type)

        sql_server_for_protected_database = cls(
            id=id,
            name=name,
            server_type=server_type,
        )

        return sql_server_for_protected_database
