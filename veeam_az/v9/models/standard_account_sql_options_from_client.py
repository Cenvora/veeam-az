from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standard_account_sql_server_from_client import StandardAccountSqlServerFromClient


T = TypeVar("T", bound="StandardAccountSqlOptionsFromClient")


@_attrs_define
class StandardAccountSqlOptionsFromClient:
    """Specifies SQL options for the account.

    Attributes:
        sql_servers (list[StandardAccountSqlServerFromClient] | None | Unset): List of the SQL Servers.
    """

    sql_servers: list[StandardAccountSqlServerFromClient] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sql_servers: list[dict[str, Any]] | None | Unset
        if isinstance(self.sql_servers, Unset):
            sql_servers = UNSET
        elif isinstance(self.sql_servers, list):
            sql_servers = []
            for sql_servers_type_0_item_data in self.sql_servers:
                sql_servers_type_0_item = sql_servers_type_0_item_data.to_dict()
                sql_servers.append(sql_servers_type_0_item)

        else:
            sql_servers = self.sql_servers

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sql_servers is not UNSET:
            field_dict["sqlServers"] = sql_servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.standard_account_sql_server_from_client import StandardAccountSqlServerFromClient

        d = dict(src_dict)

        def _parse_sql_servers(data: object) -> list[StandardAccountSqlServerFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sql_servers_type_0 = []
                _sql_servers_type_0 = data
                for sql_servers_type_0_item_data in _sql_servers_type_0:
                    sql_servers_type_0_item = StandardAccountSqlServerFromClient.from_dict(sql_servers_type_0_item_data)

                    sql_servers_type_0.append(sql_servers_type_0_item)

                return sql_servers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StandardAccountSqlServerFromClient] | None | Unset, data)

        sql_servers = _parse_sql_servers(d.pop("sqlServers", UNSET))

        standard_account_sql_options_from_client = cls(
            sql_servers=sql_servers,
        )

        return standard_account_sql_options_from_client
