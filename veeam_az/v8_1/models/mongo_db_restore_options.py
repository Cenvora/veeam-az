from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mongo_db_database_restore_options import MongoDbDatabaseRestoreOptions


T = TypeVar("T", bound="MongoDbRestoreOptions")


@_attrs_define
class MongoDbRestoreOptions:
    """
    Attributes:
        databases (list[MongoDbDatabaseRestoreOptions] | Unset):
    """

    databases: list[MongoDbDatabaseRestoreOptions] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        databases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.databases, Unset):
            databases = []
            for databases_item_data in self.databases:
                databases_item = databases_item_data.to_dict()
                databases.append(databases_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if databases is not UNSET:
            field_dict["Databases"] = databases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mongo_db_database_restore_options import MongoDbDatabaseRestoreOptions

        d = dict(src_dict)
        _databases = d.pop("Databases", UNSET)
        databases: list[MongoDbDatabaseRestoreOptions] | Unset = UNSET
        if _databases is not UNSET:
            databases = []
            for databases_item_data in _databases:
                databases_item = MongoDbDatabaseRestoreOptions.from_dict(databases_item_data)

                databases.append(databases_item)

        mongo_db_restore_options = cls(
            databases=databases,
        )

        mongo_db_restore_options.additional_properties = d
        return mongo_db_restore_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
