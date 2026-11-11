from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CosmosDbAccountDatabase")


@_attrs_define
class CosmosDbAccountDatabase:
    """Information on a database of a Cosmos DB account.

    Attributes:
        database_rid (str | Unset): Resource ID assigned to the database in Microsoft Azure.
        name (None | str | Unset): Name of the database.
        deletion_time (datetime.datetime | None | Unset): /[Applies only to databases deleted from the Cosmos DB account
            in Microsoft Azure] Date and time when the database was deleted.
    """

    database_rid: str | Unset = UNSET
    name: None | str | Unset = UNSET
    deletion_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        database_rid = self.database_rid

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        deletion_time: None | str | Unset
        if isinstance(self.deletion_time, Unset):
            deletion_time = UNSET
        elif isinstance(self.deletion_time, datetime.datetime):
            deletion_time = self.deletion_time.isoformat()
        else:
            deletion_time = self.deletion_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if database_rid is not UNSET:
            field_dict["databaseRid"] = database_rid
        if name is not UNSET:
            field_dict["name"] = name
        if deletion_time is not UNSET:
            field_dict["deletionTime"] = deletion_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database_rid = d.pop("databaseRid", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_deletion_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deletion_time_type_0 = isoparse(data)

                return deletion_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deletion_time = _parse_deletion_time(d.pop("deletionTime", UNSET))

        cosmos_db_account_database = cls(
            database_rid=database_rid,
            name=name,
            deletion_time=deletion_time,
        )

        return cosmos_db_account_database
