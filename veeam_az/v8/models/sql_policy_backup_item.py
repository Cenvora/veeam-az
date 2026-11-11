from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database import Database
    from ..models.sql_policy_item_deleted_from_azure import SqlPolicyItemDeletedFromAzure
    from ..models.sql_server import SqlServer


T = TypeVar("T", bound="SqlPolicyBackupItem")


@_attrs_define
class SqlPolicyBackupItem:
    """
    Attributes:
        database (Database | Unset): Information on an Azure SQL database.
        sql_server (SqlServer | Unset): Information on an Azure SQL Server.
        deleted_item (SqlPolicyItemDeletedFromAzure | Unset): Specifies information on a resource deleted from the
            Microsoft Azure infrastructure.
    """

    database: Database | Unset = UNSET
    sql_server: SqlServer | Unset = UNSET
    deleted_item: SqlPolicyItemDeletedFromAzure | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        database: dict[str, Any] | Unset = UNSET
        if not isinstance(self.database, Unset):
            database = self.database.to_dict()

        sql_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sql_server, Unset):
            sql_server = self.sql_server.to_dict()

        deleted_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deleted_item, Unset):
            deleted_item = self.deleted_item.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if database is not UNSET:
            field_dict["database"] = database
        if sql_server is not UNSET:
            field_dict["sqlServer"] = sql_server
        if deleted_item is not UNSET:
            field_dict["deletedItem"] = deleted_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database import Database
        from ..models.sql_policy_item_deleted_from_azure import SqlPolicyItemDeletedFromAzure
        from ..models.sql_server import SqlServer

        d = dict(src_dict)
        _database = d.pop("database", UNSET)
        database: Database | Unset
        if isinstance(_database, Unset):
            database = UNSET
        else:
            database = Database.from_dict(_database)

        _sql_server = d.pop("sqlServer", UNSET)
        sql_server: SqlServer | Unset
        if isinstance(_sql_server, Unset):
            sql_server = UNSET
        else:
            sql_server = SqlServer.from_dict(_sql_server)

        _deleted_item = d.pop("deletedItem", UNSET)
        deleted_item: SqlPolicyItemDeletedFromAzure | Unset
        if isinstance(_deleted_item, Unset):
            deleted_item = UNSET
        else:
            deleted_item = SqlPolicyItemDeletedFromAzure.from_dict(_deleted_item)

        sql_policy_backup_item = cls(
            database=database,
            sql_server=sql_server,
            deleted_item=deleted_item,
        )

        return sql_policy_backup_item
