from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageFolderV2")


@_attrs_define
class StorageFolderV2:
    """
    Attributes:
        folder_name (str):
        account_id (None | str | Unset):
    """

    folder_name: str
    account_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        folder_name = self.folder_name

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "folderName": folder_name,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folder_name = d.pop("folderName")

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))

        storage_folder_v2 = cls(
            folder_name=folder_name,
            account_id=account_id,
        )

        return storage_folder_v2
