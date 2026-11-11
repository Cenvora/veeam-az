from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.file_share_policy_backup_item_type import FileSharePolicyBackupItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSharePolicyItemDeletedFromAzure")


@_attrs_define
class FileSharePolicyItemDeletedFromAzure:
    """Specifies information on a resource deleted from the Microsoft Azure infrastructure.

    Attributes:
        type_ (FileSharePolicyBackupItemType | Unset): Type of the protected resource.
        name (None | str | Unset): Name of the deleted resource.
        id (None | str | Unset): System ID assigned to the deleted resource in the Veeam Backup for Microsoft Azure REST
            API.
    """

    type_: FileSharePolicyBackupItemType | Unset = UNSET
    name: None | str | Unset = UNSET
    id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: FileSharePolicyBackupItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FileSharePolicyBackupItemType(_type_)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        file_share_policy_item_deleted_from_azure = cls(
            type_=type_,
            name=name,
            id=id,
        )

        return file_share_policy_item_deleted_from_azure
