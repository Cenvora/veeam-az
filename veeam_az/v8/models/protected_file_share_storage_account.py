from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedFileShareStorageAccount")


@_attrs_define
class ProtectedFileShareStorageAccount:
    """Information on the storage account where the file share resides.

    Attributes:
        id (str | Unset): System ID assigned to the storage account in the Veeam Backup for Microsoft Azure REST API.
        resource_id (str | Unset): Resource ID of the storage account.
        name (str | Unset): Name of the storage account.
    """

    id: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource_id = self.resource_id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        resource_id = d.pop("resourceId", UNSET)

        name = d.pop("name", UNSET)

        protected_file_share_storage_account = cls(
            id=id,
            resource_id=resource_id,
            name=name,
        )

        return protected_file_share_storage_account
