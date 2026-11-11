from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_share_policy_file_share_from_client import FileSharePolicyFileShareFromClient


T = TypeVar("T", bound="FileSharePolicyExcludedItemsFromClient")


@_attrs_define
class FileSharePolicyExcludedItemsFromClient:
    """Specifies Azure file shares to exclude from the backup scope.

    Attributes:
        file_shares (list[FileSharePolicyFileShareFromClient] | None | Unset): List of file shares.
    """

    file_shares: list[FileSharePolicyFileShareFromClient] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_shares: list[dict[str, Any]] | None | Unset
        if isinstance(self.file_shares, Unset):
            file_shares = UNSET
        elif isinstance(self.file_shares, list):
            file_shares = []
            for file_shares_type_0_item_data in self.file_shares:
                file_shares_type_0_item = file_shares_type_0_item_data.to_dict()
                file_shares.append(file_shares_type_0_item)

        else:
            file_shares = self.file_shares

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_shares is not UNSET:
            field_dict["fileShares"] = file_shares

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_share_policy_file_share_from_client import FileSharePolicyFileShareFromClient

        d = dict(src_dict)

        def _parse_file_shares(data: object) -> list[FileSharePolicyFileShareFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_shares_type_0 = []
                _file_shares_type_0 = data
                for file_shares_type_0_item_data in _file_shares_type_0:
                    file_shares_type_0_item = FileSharePolicyFileShareFromClient.from_dict(file_shares_type_0_item_data)

                    file_shares_type_0.append(file_shares_type_0_item)

                return file_shares_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileSharePolicyFileShareFromClient] | None | Unset, data)

        file_shares = _parse_file_shares(d.pop("fileShares", UNSET))

        file_share_policy_excluded_items_from_client = cls(
            file_shares=file_shares,
        )

        return file_share_policy_excluded_items_from_client
