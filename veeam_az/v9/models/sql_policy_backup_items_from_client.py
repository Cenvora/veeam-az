from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_sql_policy_server_from_client import RESTSqlPolicyServerFromClient
    from ..models.sql_policy_database_from_client import SqlPolicyDatabaseFromClient


T = TypeVar("T", bound="SqlPolicyBackupItemsFromClient")


@_attrs_define
class SqlPolicyBackupItemsFromClient:
    r"""\[Applies if the *SelectedItems* value is specified for the `backupType` parameter] Specifies information on Azure
    resources to protect by the backup policy.

        Attributes:
            databases (list[SqlPolicyDatabaseFromClient] | None | Unset): Specifies a list of Azure SQL databases.
            sql_servers (list[RESTSqlPolicyServerFromClient] | None | Unset): Specifies a list of Azure SQL Servers.
    """

    databases: list[SqlPolicyDatabaseFromClient] | None | Unset = UNSET
    sql_servers: list[RESTSqlPolicyServerFromClient] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        databases: list[dict[str, Any]] | None | Unset
        if isinstance(self.databases, Unset):
            databases = UNSET
        elif isinstance(self.databases, list):
            databases = []
            for databases_type_0_item_data in self.databases:
                databases_type_0_item = databases_type_0_item_data.to_dict()
                databases.append(databases_type_0_item)

        else:
            databases = self.databases

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
        if databases is not UNSET:
            field_dict["databases"] = databases
        if sql_servers is not UNSET:
            field_dict["sqlServers"] = sql_servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_sql_policy_server_from_client import RESTSqlPolicyServerFromClient
        from ..models.sql_policy_database_from_client import SqlPolicyDatabaseFromClient

        d = dict(src_dict)

        def _parse_databases(data: object) -> list[SqlPolicyDatabaseFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                databases_type_0 = []
                _databases_type_0 = data
                for databases_type_0_item_data in _databases_type_0:
                    databases_type_0_item = SqlPolicyDatabaseFromClient.from_dict(databases_type_0_item_data)

                    databases_type_0.append(databases_type_0_item)

                return databases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SqlPolicyDatabaseFromClient] | None | Unset, data)

        databases = _parse_databases(d.pop("databases", UNSET))

        def _parse_sql_servers(data: object) -> list[RESTSqlPolicyServerFromClient] | None | Unset:
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
                    sql_servers_type_0_item = RESTSqlPolicyServerFromClient.from_dict(sql_servers_type_0_item_data)

                    sql_servers_type_0.append(sql_servers_type_0_item)

                return sql_servers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RESTSqlPolicyServerFromClient] | None | Unset, data)

        sql_servers = _parse_sql_servers(d.pop("sqlServers", UNSET))

        sql_policy_backup_items_from_client = cls(
            databases=databases,
            sql_servers=sql_servers,
        )

        return sql_policy_backup_items_from_client
