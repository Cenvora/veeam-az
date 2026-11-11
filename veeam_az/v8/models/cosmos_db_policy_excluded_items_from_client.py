from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cosmos_db_account_from_client import CosmosDbAccountFromClient
    from ..models.tag_from_client import TagFromClient


T = TypeVar("T", bound="CosmosDbPolicyExcludedItemsFromClient")


@_attrs_define
class CosmosDbPolicyExcludedItemsFromClient:
    """Specifies Azure resources to exclude from the backup scope.

    Attributes:
        cosmos_db_accounts (list[CosmosDbAccountFromClient] | None | Unset): Specifies a list of Cosmos DB accounts that
            are excluded from the backup policy.
        tags (list[TagFromClient] | None | Unset): Specifies Azure tags to identify the resources that should be
            excluded from the backup scope.
    """

    cosmos_db_accounts: list[CosmosDbAccountFromClient] | None | Unset = UNSET
    tags: list[TagFromClient] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cosmos_db_accounts: list[dict[str, Any]] | None | Unset
        if isinstance(self.cosmos_db_accounts, Unset):
            cosmos_db_accounts = UNSET
        elif isinstance(self.cosmos_db_accounts, list):
            cosmos_db_accounts = []
            for cosmos_db_accounts_type_0_item_data in self.cosmos_db_accounts:
                cosmos_db_accounts_type_0_item = cosmos_db_accounts_type_0_item_data.to_dict()
                cosmos_db_accounts.append(cosmos_db_accounts_type_0_item)

        else:
            cosmos_db_accounts = self.cosmos_db_accounts

        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cosmos_db_accounts is not UNSET:
            field_dict["cosmosDbAccounts"] = cosmos_db_accounts
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cosmos_db_account_from_client import CosmosDbAccountFromClient
        from ..models.tag_from_client import TagFromClient

        d = dict(src_dict)

        def _parse_cosmos_db_accounts(data: object) -> list[CosmosDbAccountFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cosmos_db_accounts_type_0 = []
                _cosmos_db_accounts_type_0 = data
                for cosmos_db_accounts_type_0_item_data in _cosmos_db_accounts_type_0:
                    cosmos_db_accounts_type_0_item = CosmosDbAccountFromClient.from_dict(
                        cosmos_db_accounts_type_0_item_data
                    )

                    cosmos_db_accounts_type_0.append(cosmos_db_accounts_type_0_item)

                return cosmos_db_accounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CosmosDbAccountFromClient] | None | Unset, data)

        cosmos_db_accounts = _parse_cosmos_db_accounts(d.pop("cosmosDbAccounts", UNSET))

        def _parse_tags(data: object) -> list[TagFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = TagFromClient.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TagFromClient] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        cosmos_db_policy_excluded_items_from_client = cls(
            cosmos_db_accounts=cosmos_db_accounts,
            tags=tags,
        )

        return cosmos_db_policy_excluded_items_from_client
