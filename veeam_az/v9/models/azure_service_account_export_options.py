from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureServiceAccountExportOptions")


@_attrs_define
class AzureServiceAccountExportOptions:
    """
    Attributes:
        account_ids (list[UUID] | None | Unset): Specifies a list of system IDs assigned in the Veeam Backup for
            Microsoft Azure REST API to the service accounts whose data will be exported.
    """

    account_ids: list[UUID] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account_ids: list[str] | None | Unset
        if isinstance(self.account_ids, Unset):
            account_ids = UNSET
        elif isinstance(self.account_ids, list):
            account_ids = []
            for account_ids_type_0_item_data in self.account_ids:
                account_ids_type_0_item = str(account_ids_type_0_item_data)
                account_ids.append(account_ids_type_0_item)

        else:
            account_ids = self.account_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_account_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                account_ids_type_0 = []
                _account_ids_type_0 = data
                for account_ids_type_0_item_data in _account_ids_type_0:
                    account_ids_type_0_item = UUID(account_ids_type_0_item_data)

                    account_ids_type_0.append(account_ids_type_0_item)

                return account_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        account_ids = _parse_account_ids(d.pop("accountIds", UNSET))

        azure_service_account_export_options = cls(
            account_ids=account_ids,
        )

        return azure_service_account_export_options
