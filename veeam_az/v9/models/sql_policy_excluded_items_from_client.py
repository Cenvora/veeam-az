from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sql_policy_database_from_client import SqlPolicyDatabaseFromClient


T = TypeVar("T", bound="SqlPolicyExcludedItemsFromClient")


@_attrs_define
class SqlPolicyExcludedItemsFromClient:
    """Specifies Azure resources to exclude from the backup scope.

    Attributes:
        databases (list[SqlPolicyDatabaseFromClient] | None | Unset): Specifies a list of Azure SQL databases.
    """

    databases: list[SqlPolicyDatabaseFromClient] | None | Unset = UNSET

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if databases is not UNSET:
            field_dict["databases"] = databases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        sql_policy_excluded_items_from_client = cls(
            databases=databases,
        )

        return sql_policy_excluded_items_from_client
