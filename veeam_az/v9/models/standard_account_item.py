from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sql_server_for_standard_account import SqlServerForStandardAccount


T = TypeVar("T", bound="StandardAccountItem")


@_attrs_define
class StandardAccountItem:
    """
    Attributes:
        sql_server (SqlServerForStandardAccount | Unset):
    """

    sql_server: SqlServerForStandardAccount | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sql_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sql_server, Unset):
            sql_server = self.sql_server.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sql_server is not UNSET:
            field_dict["sqlServer"] = sql_server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sql_server_for_standard_account import SqlServerForStandardAccount

        d = dict(src_dict)
        _sql_server = d.pop("sqlServer", UNSET)
        sql_server: SqlServerForStandardAccount | Unset
        if isinstance(_sql_server, Unset):
            sql_server = UNSET
        else:
            sql_server = SqlServerForStandardAccount.from_dict(_sql_server)

        standard_account_item = cls(
            sql_server=sql_server,
        )

        return standard_account_item
