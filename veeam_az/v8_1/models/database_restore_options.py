from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_new_location_options import DatabaseNewLocationOptions


T = TypeVar("T", bound="DatabaseRestoreOptions")


@_attrs_define
class DatabaseRestoreOptions:
    """
    Attributes:
        service_account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to
            a service account whose permissions will be used to perform the restore operation.
        sql_account_id (str): Specifies a system ID assigned in the Veeam Backup for Microsoft Azure REST API to the
            Azure SQL account in the Veeam Backup for Microsoft Azure REST API.
        new_location (DatabaseNewLocationOptions | Unset): Specifies information on a new restore target location.
        reason (None | str | Unset): Specifies a reason for the restore operation.
    """

    service_account_id: UUID
    sql_account_id: str
    new_location: DatabaseNewLocationOptions | Unset = UNSET
    reason: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        service_account_id = str(self.service_account_id)

        sql_account_id = self.sql_account_id

        new_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_location, Unset):
            new_location = self.new_location.to_dict()

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serviceAccountId": service_account_id,
                "sqlAccountId": sql_account_id,
            }
        )
        if new_location is not UNSET:
            field_dict["newLocation"] = new_location
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_new_location_options import DatabaseNewLocationOptions

        d = dict(src_dict)
        service_account_id = UUID(d.pop("serviceAccountId"))

        sql_account_id = d.pop("sqlAccountId")

        _new_location = d.pop("newLocation", UNSET)
        new_location: DatabaseNewLocationOptions | Unset
        if isinstance(_new_location, Unset):
            new_location = UNSET
        else:
            new_location = DatabaseNewLocationOptions.from_dict(_new_location)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        database_restore_options = cls(
            service_account_id=service_account_id,
            sql_account_id=sql_account_id,
            new_location=new_location,
            reason=reason,
        )

        return database_restore_options
