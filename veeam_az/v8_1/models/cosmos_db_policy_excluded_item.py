from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cosmos_db_account import CosmosDbAccount
    from ..models.cosmos_db_policy_item_deleted_from_azure import CosmosDbPolicyItemDeletedFromAzure
    from ..models.tag import Tag


T = TypeVar("T", bound="CosmosDbPolicyExcludedItem")


@_attrs_define
class CosmosDbPolicyExcludedItem:
    """
    Attributes:
        account (CosmosDbAccount | Unset): Information on a Cosmos DB account.
        deleted_item (CosmosDbPolicyItemDeletedFromAzure | Unset): Specifies information on a resource deleted from the
            Microsoft Azure infrastructure.
        tag (Tag | Unset): Information on an Azure tag.
    """

    account: CosmosDbAccount | Unset = UNSET
    deleted_item: CosmosDbPolicyItemDeletedFromAzure | Unset = UNSET
    tag: Tag | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        deleted_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deleted_item, Unset):
            deleted_item = self.deleted_item.to_dict()

        tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if deleted_item is not UNSET:
            field_dict["deletedItem"] = deleted_item
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cosmos_db_account import CosmosDbAccount
        from ..models.cosmos_db_policy_item_deleted_from_azure import CosmosDbPolicyItemDeletedFromAzure
        from ..models.tag import Tag

        d = dict(src_dict)
        _account = d.pop("account", UNSET)
        account: CosmosDbAccount | Unset
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = CosmosDbAccount.from_dict(_account)

        _deleted_item = d.pop("deletedItem", UNSET)
        deleted_item: CosmosDbPolicyItemDeletedFromAzure | Unset
        if isinstance(_deleted_item, Unset):
            deleted_item = UNSET
        else:
            deleted_item = CosmosDbPolicyItemDeletedFromAzure.from_dict(_deleted_item)

        _tag = d.pop("tag", UNSET)
        tag: Tag | Unset
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = Tag.from_dict(_tag)

        cosmos_db_policy_excluded_item = cls(
            account=account,
            deleted_item=deleted_item,
            tag=tag,
        )

        return cosmos_db_policy_excluded_item
