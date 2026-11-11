from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sql_server import SqlServer


T = TypeVar("T", bound="SqlStagingServers")


@_attrs_define
class SqlStagingServers:
    """
    Attributes:
        managed (SqlServer | Unset): Information on an Azure SQL Server.
        unmanaged (SqlServer | Unset): Information on an Azure SQL Server.
    """

    managed: SqlServer | Unset = UNSET
    unmanaged: SqlServer | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        managed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.managed, Unset):
            managed = self.managed.to_dict()

        unmanaged: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unmanaged, Unset):
            unmanaged = self.unmanaged.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if managed is not UNSET:
            field_dict["managed"] = managed
        if unmanaged is not UNSET:
            field_dict["unmanaged"] = unmanaged

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sql_server import SqlServer

        d = dict(src_dict)
        _managed = d.pop("managed", UNSET)
        managed: SqlServer | Unset
        if isinstance(_managed, Unset):
            managed = UNSET
        else:
            managed = SqlServer.from_dict(_managed)

        _unmanaged = d.pop("unmanaged", UNSET)
        unmanaged: SqlServer | Unset
        if isinstance(_unmanaged, Unset):
            unmanaged = UNSET
        else:
            unmanaged = SqlServer.from_dict(_unmanaged)

        sql_staging_servers = cls(
            managed=managed,
            unmanaged=unmanaged,
        )

        return sql_staging_servers
