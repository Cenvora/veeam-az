from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlAccountsInfo")


@_attrs_define
class SqlAccountsInfo:
    """
    Attributes:
        sql_account_id (int | None | Unset):
        service_account_id (None | Unset | UUID):
    """

    sql_account_id: int | None | Unset = UNSET
    service_account_id: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        sql_account_id: int | None | Unset
        if isinstance(self.sql_account_id, Unset):
            sql_account_id = UNSET
        else:
            sql_account_id = self.sql_account_id

        service_account_id: None | str | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        elif isinstance(self.service_account_id, UUID):
            service_account_id = str(self.service_account_id)
        else:
            service_account_id = self.service_account_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sql_account_id is not UNSET:
            field_dict["sqlAccountId"] = sql_account_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_sql_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sql_account_id = _parse_sql_account_id(d.pop("sqlAccountId", UNSET))

        def _parse_service_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_account_id_type_0 = UUID(data)

                return service_account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        service_account_id = _parse_service_account_id(d.pop("serviceAccountId", UNSET))

        sql_accounts_info = cls(
            sql_account_id=sql_account_id,
            service_account_id=service_account_id,
        )

        return sql_accounts_info
