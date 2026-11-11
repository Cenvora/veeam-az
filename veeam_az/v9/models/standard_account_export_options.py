from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.standard_account_kind import StandardAccountKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="StandardAccountExportOptions")


@_attrs_define
class StandardAccountExportOptions:
    """
    Attributes:
        type_ (list[StandardAccountKind] | None | Unset): Returns only accounts of the specified type.
        search_pattern (None | str | Unset): Returns only those items of a resource collection whose names match the
            specified search pattern in the parameter value.
        account_ids (list[str] | None | Unset): Specifies the system IDs assigned in the Veeam Backup for Microsoft
            Azure REST API to SMTP and database accounts whose data will be exported.
    """

    type_: list[StandardAccountKind] | None | Unset = UNSET
    search_pattern: None | str | Unset = UNSET
    account_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: list[str] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, list):
            type_ = []
            for type_type_0_item_data in self.type_:
                type_type_0_item = type_type_0_item_data.value
                type_.append(type_type_0_item)

        else:
            type_ = self.type_

        search_pattern: None | str | Unset
        if isinstance(self.search_pattern, Unset):
            search_pattern = UNSET
        else:
            search_pattern = self.search_pattern

        account_ids: list[str] | None | Unset
        if isinstance(self.account_ids, Unset):
            account_ids = UNSET
        elif isinstance(self.account_ids, list):
            account_ids = self.account_ids

        else:
            account_ids = self.account_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_type_(data: object) -> list[StandardAccountKind] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                type_type_0 = []
                _type_type_0 = data
                for type_type_0_item_data in _type_type_0:
                    type_type_0_item = StandardAccountKind(type_type_0_item_data)

                    type_type_0.append(type_type_0_item)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StandardAccountKind] | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_search_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_pattern = _parse_search_pattern(d.pop("searchPattern", UNSET))

        def _parse_account_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                account_ids_type_0 = cast(list[str], data)

                return account_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        account_ids = _parse_account_ids(d.pop("accountIds", UNSET))

        standard_account_export_options = cls(
            type_=type_,
            search_pattern=search_pattern,
            account_ids=account_ids,
        )

        return standard_account_export_options
