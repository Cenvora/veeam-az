from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CosmosDbAccountRestoreTimeRange")


@_attrs_define
class CosmosDbAccountRestoreTimeRange:
    """Information on a Cosmos DB account.

    Attributes:
        id (None | str | Unset): System ID assigned to a Cosmos DB account in the Veeam Backup for Microsoft Azure REST
            API.
        name (None | str | Unset): Name of the Cosmos DB account.
        latest_restorable_timestamp (datetime.datetime | None | Unset): Date and time when the point-in-time restore
            period ends.
        earliest_restorable_timestamp (datetime.datetime | None | Unset): Date and time when the point-in-time restore
            period starts.
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    latest_restorable_timestamp: datetime.datetime | None | Unset = UNSET
    earliest_restorable_timestamp: datetime.datetime | None | Unset = UNSET

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

        latest_restorable_timestamp: None | str | Unset
        if isinstance(self.latest_restorable_timestamp, Unset):
            latest_restorable_timestamp = UNSET
        elif isinstance(self.latest_restorable_timestamp, datetime.datetime):
            latest_restorable_timestamp = self.latest_restorable_timestamp.isoformat()
        else:
            latest_restorable_timestamp = self.latest_restorable_timestamp

        earliest_restorable_timestamp: None | str | Unset
        if isinstance(self.earliest_restorable_timestamp, Unset):
            earliest_restorable_timestamp = UNSET
        elif isinstance(self.earliest_restorable_timestamp, datetime.datetime):
            earliest_restorable_timestamp = self.earliest_restorable_timestamp.isoformat()
        else:
            earliest_restorable_timestamp = self.earliest_restorable_timestamp

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if latest_restorable_timestamp is not UNSET:
            field_dict["latestRestorableTimestamp"] = latest_restorable_timestamp
        if earliest_restorable_timestamp is not UNSET:
            field_dict["earliestRestorableTimestamp"] = earliest_restorable_timestamp

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

        def _parse_latest_restorable_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_restorable_timestamp_type_0 = isoparse(data)

                return latest_restorable_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        latest_restorable_timestamp = _parse_latest_restorable_timestamp(d.pop("latestRestorableTimestamp", UNSET))

        def _parse_earliest_restorable_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                earliest_restorable_timestamp_type_0 = isoparse(data)

                return earliest_restorable_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        earliest_restorable_timestamp = _parse_earliest_restorable_timestamp(
            d.pop("earliestRestorableTimestamp", UNSET)
        )

        cosmos_db_account_restore_time_range = cls(
            id=id,
            name=name,
            latest_restorable_timestamp=latest_restorable_timestamp,
            earliest_restorable_timestamp=earliest_restorable_timestamp,
        )

        return cosmos_db_account_restore_time_range
