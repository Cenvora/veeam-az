from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCosmosDbAccountExportOptions")


@_attrs_define
class ProtectedCosmosDbAccountExportOptions:
    """
    Attributes:
        accounts (list[str] | None | Unset): Returns only information on the Cosmos DB accounts with the specified IDs.
        search_pattern (None | str | Unset): Returns only those items of a resource collection that match the specified
            search pattern in the parameter value.
    """

    accounts: list[str] | None | Unset = UNSET
    search_pattern: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        accounts: list[str] | None | Unset
        if isinstance(self.accounts, Unset):
            accounts = UNSET
        elif isinstance(self.accounts, list):
            accounts = self.accounts

        else:
            accounts = self.accounts

        search_pattern: None | str | Unset
        if isinstance(self.search_pattern, Unset):
            search_pattern = UNSET
        else:
            search_pattern = self.search_pattern

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_accounts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                accounts_type_0 = cast(list[str], data)

                return accounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        accounts = _parse_accounts(d.pop("accounts", UNSET))

        def _parse_search_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_pattern = _parse_search_pattern(d.pop("searchPattern", UNSET))

        protected_cosmos_db_account_export_options = cls(
            accounts=accounts,
            search_pattern=search_pattern,
        )

        return protected_cosmos_db_account_export_options
