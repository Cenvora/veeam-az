from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.licensing_server_status import LicensingServerStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LicensingServerInfo")


@_attrs_define
class LicensingServerInfo:
    r"""\[Applies if the backup appliance is managed by a Veeam Backup & Replication server] Information on the Veeam Backup
    & Replication server managing the backup appliance.

        Attributes:
            id (UUID | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the managing Veeam
                Backup & Replication server.
            hostname (None | str | Unset): DNS name or IP address of the managing Veeam Backup & Replication server.
            status (LicensingServerStatus | Unset): Specifies the status of the managing Veeam Backup & Replication server.
            last_connection_time (datetime.datetime | None | Unset): Date and time of the most recent connection to the
                Veeam Backup & Replication server.
            is_expired (bool | Unset): Defines whether the managing Veeam Backup & Replication server is expired.
    """

    id: UUID | Unset = UNSET
    hostname: None | str | Unset = UNSET
    status: LicensingServerStatus | Unset = UNSET
    last_connection_time: datetime.datetime | None | Unset = UNSET
    is_expired: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        hostname: None | str | Unset
        if isinstance(self.hostname, Unset):
            hostname = UNSET
        else:
            hostname = self.hostname

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        last_connection_time: None | str | Unset
        if isinstance(self.last_connection_time, Unset):
            last_connection_time = UNSET
        elif isinstance(self.last_connection_time, datetime.datetime):
            last_connection_time = self.last_connection_time.isoformat()
        else:
            last_connection_time = self.last_connection_time

        is_expired = self.is_expired

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if status is not UNSET:
            field_dict["status"] = status
        if last_connection_time is not UNSET:
            field_dict["lastConnectionTime"] = last_connection_time
        if is_expired is not UNSET:
            field_dict["isExpired"] = is_expired

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

        def _parse_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostname = _parse_hostname(d.pop("hostname", UNSET))

        _status = d.pop("status", UNSET)
        status: LicensingServerStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LicensingServerStatus(_status)

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

        is_expired = d.pop("isExpired", UNSET)

        licensing_server_info = cls(
            id=id,
            hostname=hostname,
            status=status,
            last_connection_time=last_connection_time,
            is_expired=is_expired,
        )

        return licensing_server_info
