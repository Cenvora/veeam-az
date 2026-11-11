from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_share import FileShare
    from ..models.file_share_policy_item_deleted_from_azure import FileSharePolicyItemDeletedFromAzure


T = TypeVar("T", bound="FileSharePolicyExcludedItem")


@_attrs_define
class FileSharePolicyExcludedItem:
    """Information on each excluded file share.

    Attributes:
        file_share (FileShare | Unset): Specifies information on a file share.
        deleted_item (FileSharePolicyItemDeletedFromAzure | Unset): Specifies information on a resource deleted from the
            Microsoft Azure infrastructure.
    """

    file_share: FileShare | Unset = UNSET
    deleted_item: FileSharePolicyItemDeletedFromAzure | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_share: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_share, Unset):
            file_share = self.file_share.to_dict()

        deleted_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deleted_item, Unset):
            deleted_item = self.deleted_item.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_share is not UNSET:
            field_dict["fileShare"] = file_share
        if deleted_item is not UNSET:
            field_dict["deletedItem"] = deleted_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_share import FileShare
        from ..models.file_share_policy_item_deleted_from_azure import FileSharePolicyItemDeletedFromAzure

        d = dict(src_dict)
        _file_share = d.pop("fileShare", UNSET)
        file_share: FileShare | Unset
        if isinstance(_file_share, Unset):
            file_share = UNSET
        else:
            file_share = FileShare.from_dict(_file_share)

        _deleted_item = d.pop("deletedItem", UNSET)
        deleted_item: FileSharePolicyItemDeletedFromAzure | Unset
        if isinstance(_deleted_item, Unset):
            deleted_item = UNSET
        else:
            deleted_item = FileSharePolicyItemDeletedFromAzure.from_dict(_deleted_item)

        file_share_policy_excluded_item = cls(
            file_share=file_share,
            deleted_item=deleted_item,
        )

        return file_share_policy_excluded_item
