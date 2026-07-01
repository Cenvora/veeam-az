from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.storage_account_performance import StorageAccountPerformance
from ..models.storage_account_redundancy import StorageAccountRedundancy
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryStorageAccount")


@_attrs_define
class RepositoryStorageAccount:
    """
    Attributes:
        performance (StorageAccountPerformance | Unset): Specifies the type of a performance tier specified for the
            storage account.
        redundancy (StorageAccountRedundancy | Unset): Specifies the type of Azure storage data redundancy.
        access_tier (None | str | Unset):
        subscription (None | str | Unset):
        resource_group (None | str | Unset):
    """

    performance: StorageAccountPerformance | Unset = UNSET
    redundancy: StorageAccountRedundancy | Unset = UNSET
    access_tier: None | str | Unset = UNSET
    subscription: None | str | Unset = UNSET
    resource_group: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        performance: str | Unset = UNSET
        if not isinstance(self.performance, Unset):
            performance = self.performance.value

        redundancy: str | Unset = UNSET
        if not isinstance(self.redundancy, Unset):
            redundancy = self.redundancy.value

        access_tier: None | str | Unset
        if isinstance(self.access_tier, Unset):
            access_tier = UNSET
        else:
            access_tier = self.access_tier

        subscription: None | str | Unset
        if isinstance(self.subscription, Unset):
            subscription = UNSET
        else:
            subscription = self.subscription

        resource_group: None | str | Unset
        if isinstance(self.resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = self.resource_group

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if performance is not UNSET:
            field_dict["performance"] = performance
        if redundancy is not UNSET:
            field_dict["redundancy"] = redundancy
        if access_tier is not UNSET:
            field_dict["accessTier"] = access_tier
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _performance = d.pop("performance", UNSET)
        performance: StorageAccountPerformance | Unset
        if isinstance(_performance, Unset):
            performance = UNSET
        else:
            performance = StorageAccountPerformance(_performance)

        _redundancy = d.pop("redundancy", UNSET)
        redundancy: StorageAccountRedundancy | Unset
        if isinstance(_redundancy, Unset):
            redundancy = UNSET
        else:
            redundancy = StorageAccountRedundancy(_redundancy)

        def _parse_access_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_tier = _parse_access_tier(d.pop("accessTier", UNSET))

        def _parse_subscription(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription = _parse_subscription(d.pop("subscription", UNSET))

        def _parse_resource_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group = _parse_resource_group(d.pop("resourceGroup", UNSET))

        repository_storage_account = cls(
            performance=performance,
            redundancy=redundancy,
            access_tier=access_tier,
            subscription=subscription,
            resource_group=resource_group,
        )

        return repository_storage_account
