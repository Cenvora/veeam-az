from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="VnetPolicyAdditionalProtectedResourcesFromClient")


@_attrs_define
class VnetPolicyAdditionalProtectedResourcesFromClient:
    """
    Attributes:
        account_id (None | UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to a
            service account whose permissions will be used to perform virtual network configuration backup.
        subscriptions_ids (list[UUID]): Specifies the Azure IDs assigned to subscriptions that will be protected by the
            virtual network configuration backup policy.
    """

    account_id: None | UUID
    subscriptions_ids: list[UUID]

    def to_dict(self) -> dict[str, Any]:
        account_id: None | str
        if isinstance(self.account_id, UUID):
            account_id = str(self.account_id)
        else:
            account_id = self.account_id

        subscriptions_ids = []
        for subscriptions_ids_item_data in self.subscriptions_ids:
            subscriptions_ids_item = str(subscriptions_ids_item_data)
            subscriptions_ids.append(subscriptions_ids_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accountId": account_id,
                "subscriptionsIds": subscriptions_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_account_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                account_id_type_0 = UUID(data)

                return account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        account_id = _parse_account_id(d.pop("accountId"))

        subscriptions_ids = []
        _subscriptions_ids = d.pop("subscriptionsIds")
        for subscriptions_ids_item_data in _subscriptions_ids:
            subscriptions_ids_item = UUID(subscriptions_ids_item_data)

            subscriptions_ids.append(subscriptions_ids_item)

        vnet_policy_additional_protected_resources_from_client = cls(
            account_id=account_id,
            subscriptions_ids=subscriptions_ids,
        )

        return vnet_policy_additional_protected_resources_from_client
