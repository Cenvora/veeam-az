from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mongo_db_restore_options import MongoDbRestoreOptions


T = TypeVar("T", bound="CosmosDbRepositoryRestoreOptions")


@_attrs_define
class CosmosDbRepositoryRestoreOptions:
    r"""
    Attributes:
        service_account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to
            a service account whose permissions will be used to perform the restore operation.
        target_cosmos_db_account_id (str): Specifies the Microsoft Azure ID assigned to a Cosmos DB for PostgreSQL
            cluster or a Cosmos DB for MongoDB account to which the database will be restored.
        database_account_id (None | str | Unset): \[Applies to Cosmos DB for PostgreSQL accounts only] Specifies the
            system ID assigned in the Veeam Backup for Microsoft Azure REST API to a database account that will be used to
            access the restored database.
        reason (str | Unset): Specifies a reason for restoring the database.
        mongo_db_restore_options (MongoDbRestoreOptions | Unset):
    """

    service_account_id: UUID
    target_cosmos_db_account_id: str
    database_account_id: None | str | Unset = UNSET
    reason: str | Unset = UNSET
    mongo_db_restore_options: MongoDbRestoreOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_account_id = str(self.service_account_id)

        target_cosmos_db_account_id = self.target_cosmos_db_account_id

        database_account_id: None | str | Unset
        if isinstance(self.database_account_id, Unset):
            database_account_id = UNSET
        else:
            database_account_id = self.database_account_id

        reason = self.reason

        mongo_db_restore_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mongo_db_restore_options, Unset):
            mongo_db_restore_options = self.mongo_db_restore_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ServiceAccountId": service_account_id,
                "TargetCosmosDbAccountId": target_cosmos_db_account_id,
            }
        )
        if database_account_id is not UNSET:
            field_dict["DatabaseAccountId"] = database_account_id
        if reason is not UNSET:
            field_dict["Reason"] = reason
        if mongo_db_restore_options is not UNSET:
            field_dict["MongoDbRestoreOptions"] = mongo_db_restore_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mongo_db_restore_options import MongoDbRestoreOptions

        d = dict(src_dict)
        service_account_id = UUID(d.pop("ServiceAccountId"))

        target_cosmos_db_account_id = d.pop("TargetCosmosDbAccountId")

        def _parse_database_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        database_account_id = _parse_database_account_id(d.pop("DatabaseAccountId", UNSET))

        reason = d.pop("Reason", UNSET)

        _mongo_db_restore_options = d.pop("MongoDbRestoreOptions", UNSET)
        mongo_db_restore_options: MongoDbRestoreOptions | Unset
        if isinstance(_mongo_db_restore_options, Unset):
            mongo_db_restore_options = UNSET
        else:
            mongo_db_restore_options = MongoDbRestoreOptions.from_dict(_mongo_db_restore_options)

        cosmos_db_repository_restore_options = cls(
            service_account_id=service_account_id,
            target_cosmos_db_account_id=target_cosmos_db_account_id,
            database_account_id=database_account_id,
            reason=reason,
            mongo_db_restore_options=mongo_db_restore_options,
        )

        cosmos_db_repository_restore_options.additional_properties = d
        return cosmos_db_repository_restore_options

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
