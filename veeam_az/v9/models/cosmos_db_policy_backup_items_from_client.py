from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cosmos_db_account_from_client import CosmosDbAccountFromClient
    from ..models.policy_resource_group_from_client import PolicyResourceGroupFromClient
    from ..models.policy_subscription_from_client import PolicySubscriptionFromClient
    from ..models.policy_tag_group_from_client import PolicyTagGroupFromClient
    from ..models.tag_from_client import TagFromClient


T = TypeVar("T", bound="CosmosDbPolicyBackupItemsFromClient")


@_attrs_define
class CosmosDbPolicyBackupItemsFromClient:
    """Specifies information on Azure resources to protect by the backup policy.

    Attributes:
        subscriptions (list[PolicySubscriptionFromClient] | None | Unset): Specifies a list of subscriptions where the
            protected resources belong.
        tags (list[TagFromClient] | None | Unset): Specifies a list of tags assigned to the protected resources.
        resource_groups (list[PolicyResourceGroupFromClient] | None | Unset): Specifies a list of resource groups that
            contain protected resources.
        cosmos_db_accounts (list[CosmosDbAccountFromClient] | None | Unset): Specifies a list of protected Cosmos DB
            accounts.
        tag_groups (list[PolicyTagGroupFromClient] | None | Unset): Specifies a list of conditions.
    """

    subscriptions: list[PolicySubscriptionFromClient] | None | Unset = UNSET
    tags: list[TagFromClient] | None | Unset = UNSET
    resource_groups: list[PolicyResourceGroupFromClient] | None | Unset = UNSET
    cosmos_db_accounts: list[CosmosDbAccountFromClient] | None | Unset = UNSET
    tag_groups: list[PolicyTagGroupFromClient] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subscriptions: list[dict[str, Any]] | None | Unset
        if isinstance(self.subscriptions, Unset):
            subscriptions = UNSET
        elif isinstance(self.subscriptions, list):
            subscriptions = []
            for subscriptions_type_0_item_data in self.subscriptions:
                subscriptions_type_0_item = subscriptions_type_0_item_data.to_dict()
                subscriptions.append(subscriptions_type_0_item)

        else:
            subscriptions = self.subscriptions

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

        resource_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.resource_groups, Unset):
            resource_groups = UNSET
        elif isinstance(self.resource_groups, list):
            resource_groups = []
            for resource_groups_type_0_item_data in self.resource_groups:
                resource_groups_type_0_item = resource_groups_type_0_item_data.to_dict()
                resource_groups.append(resource_groups_type_0_item)

        else:
            resource_groups = self.resource_groups

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

        tag_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.tag_groups, Unset):
            tag_groups = UNSET
        elif isinstance(self.tag_groups, list):
            tag_groups = []
            for tag_groups_type_0_item_data in self.tag_groups:
                tag_groups_type_0_item = tag_groups_type_0_item_data.to_dict()
                tag_groups.append(tag_groups_type_0_item)

        else:
            tag_groups = self.tag_groups

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if tags is not UNSET:
            field_dict["tags"] = tags
        if resource_groups is not UNSET:
            field_dict["resourceGroups"] = resource_groups
        if cosmos_db_accounts is not UNSET:
            field_dict["cosmosDbAccounts"] = cosmos_db_accounts
        if tag_groups is not UNSET:
            field_dict["tagGroups"] = tag_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cosmos_db_account_from_client import CosmosDbAccountFromClient
        from ..models.policy_resource_group_from_client import PolicyResourceGroupFromClient
        from ..models.policy_subscription_from_client import PolicySubscriptionFromClient
        from ..models.policy_tag_group_from_client import PolicyTagGroupFromClient
        from ..models.tag_from_client import TagFromClient

        d = dict(src_dict)

        def _parse_subscriptions(data: object) -> list[PolicySubscriptionFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subscriptions_type_0 = []
                _subscriptions_type_0 = data
                for subscriptions_type_0_item_data in _subscriptions_type_0:
                    subscriptions_type_0_item = PolicySubscriptionFromClient.from_dict(subscriptions_type_0_item_data)

                    subscriptions_type_0.append(subscriptions_type_0_item)

                return subscriptions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PolicySubscriptionFromClient] | None | Unset, data)

        subscriptions = _parse_subscriptions(d.pop("subscriptions", UNSET))

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

        def _parse_resource_groups(data: object) -> list[PolicyResourceGroupFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resource_groups_type_0 = []
                _resource_groups_type_0 = data
                for resource_groups_type_0_item_data in _resource_groups_type_0:
                    resource_groups_type_0_item = PolicyResourceGroupFromClient.from_dict(
                        resource_groups_type_0_item_data
                    )

                    resource_groups_type_0.append(resource_groups_type_0_item)

                return resource_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PolicyResourceGroupFromClient] | None | Unset, data)

        resource_groups = _parse_resource_groups(d.pop("resourceGroups", UNSET))

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

        def _parse_tag_groups(data: object) -> list[PolicyTagGroupFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tag_groups_type_0 = []
                _tag_groups_type_0 = data
                for tag_groups_type_0_item_data in _tag_groups_type_0:
                    tag_groups_type_0_item = PolicyTagGroupFromClient.from_dict(tag_groups_type_0_item_data)

                    tag_groups_type_0.append(tag_groups_type_0_item)

                return tag_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PolicyTagGroupFromClient] | None | Unset, data)

        tag_groups = _parse_tag_groups(d.pop("tagGroups", UNSET))

        cosmos_db_policy_backup_items_from_client = cls(
            subscriptions=subscriptions,
            tags=tags,
            resource_groups=resource_groups,
            cosmos_db_accounts=cosmos_db_accounts,
            tag_groups=tag_groups,
        )

        return cosmos_db_policy_backup_items_from_client
