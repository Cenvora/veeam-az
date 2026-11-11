from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicensingServer")


@_attrs_define
class LicensingServer:
    """
    Attributes:
        id (UUID | Unset): Specifies the system ID assigned in Veeam Backup & Replication to the Veeam Backup &
            Replication server.
        host_name (None | str | Unset): Specifies the DNS name or IP address of the Veeam Backup & Replication server.
        last_connection_time (datetime.datetime | None | Unset): Date and time of the most recent connection to the
            Veeam Backup & Replication server.
    """

    id: UUID | Unset = UNSET
    host_name: None | str | Unset = UNSET
    last_connection_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        host_name: None | str | Unset
        if isinstance(self.host_name, Unset):
            host_name = UNSET
        else:
            host_name = self.host_name

        last_connection_time: None | str | Unset
        if isinstance(self.last_connection_time, Unset):
            last_connection_time = UNSET
        elif isinstance(self.last_connection_time, datetime.datetime):
            last_connection_time = self.last_connection_time.isoformat()
        else:
            last_connection_time = self.last_connection_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if last_connection_time is not UNSET:
            field_dict["lastConnectionTime"] = last_connection_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_host_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_name = _parse_host_name(d.pop("hostName", UNSET))

        def _parse_last_connection_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_connection_time_type_0 = isoparse(data)

                return last_connection_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_connection_time = _parse_last_connection_time(d.pop("lastConnectionTime", UNSET))

        licensing_server = cls(
            id=id,
            host_name=host_name,
            last_connection_time=last_connection_time,
        )

        return licensing_server
