from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database import Database
    from ..models.sql_policy_item_deleted_from_azure import SqlPolicyItemDeletedFromAzure


T = TypeVar("T", bound="SqlPolicyExcludedItem")


@_attrs_define
class SqlPolicyExcludedItem:
    """
    Attributes:
        database (Database | Unset): Information on an Azure SQL database.
        deleted_item (SqlPolicyItemDeletedFromAzure | Unset): Specifies information on a resource deleted from the
            Microsoft Azure infrastructure.
    """

    database: Database | Unset = UNSET
    deleted_item: SqlPolicyItemDeletedFromAzure | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        database: dict[str, Any] | Unset = UNSET
        if not isinstance(self.database, Unset):
            database = self.database.to_dict()

        deleted_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deleted_item, Unset):
            deleted_item = self.deleted_item.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if database is not UNSET:
            field_dict["database"] = database
        if deleted_item is not UNSET:
            field_dict["deletedItem"] = deleted_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database import Database
        from ..models.sql_policy_item_deleted_from_azure import SqlPolicyItemDeletedFromAzure

        d = dict(src_dict)
        _database = d.pop("database", UNSET)
        database: Database | Unset
        if isinstance(_database, Unset):
            database = UNSET
        else:
            database = Database.from_dict(_database)

        _deleted_item = d.pop("deletedItem", UNSET)
        deleted_item: SqlPolicyItemDeletedFromAzure | Unset
        if isinstance(_deleted_item, Unset):
            deleted_item = UNSET
        else:
            deleted_item = SqlPolicyItemDeletedFromAzure.from_dict(_deleted_item)

        sql_policy_excluded_item = cls(
            database=database,
            deleted_item=deleted_item,
        )

        return sql_policy_excluded_item
