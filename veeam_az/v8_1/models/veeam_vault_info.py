from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamVaultInfo")


@_attrs_define
class VeeamVaultInfo:
    """
    Attributes:
        id (int | Unset): System ID assigned in the Veeam infrastructure to a storage vault.
        name (str | Unset): Name of the storage vault.
        storage_account_name (str | Unset): Name of the Azure storage account in which the storage vault resides.
        storage_container_name (str | Unset): Name of the blob container in which the storage vault resides.
        is_read_only (bool | Unset): Defines whether the storage vault has a *Read-only* status.
        read_only_reason (None | str | Unset): Message that contains information on the reason the storage vault has a
            *Read-only* status.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    storage_account_name: str | Unset = UNSET
    storage_container_name: str | Unset = UNSET
    is_read_only: bool | Unset = UNSET
    read_only_reason: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        storage_account_name = self.storage_account_name

        storage_container_name = self.storage_container_name

        is_read_only = self.is_read_only

        read_only_reason: None | str | Unset
        if isinstance(self.read_only_reason, Unset):
            read_only_reason = UNSET
        else:
            read_only_reason = self.read_only_reason

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if storage_account_name is not UNSET:
            field_dict["storageAccountName"] = storage_account_name
        if storage_container_name is not UNSET:
            field_dict["storageContainerName"] = storage_container_name
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if read_only_reason is not UNSET:
            field_dict["readOnlyReason"] = read_only_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        storage_account_name = d.pop("storageAccountName", UNSET)

        storage_container_name = d.pop("storageContainerName", UNSET)

        is_read_only = d.pop("isReadOnly", UNSET)

        def _parse_read_only_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        read_only_reason = _parse_read_only_reason(d.pop("readOnlyReason", UNSET))

        veeam_vault_info = cls(
            id=id,
            name=name,
            storage_account_name=storage_account_name,
            storage_container_name=storage_container_name,
            is_read_only=is_read_only,
            read_only_reason=read_only_reason,
        )

        return veeam_vault_info
