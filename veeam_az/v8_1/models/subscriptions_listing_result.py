from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.azure_environment import AzureEnvironment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_for_service_account import SubscriptionForServiceAccount


T = TypeVar("T", bound="SubscriptionsListingResult")


@_attrs_define
class SubscriptionsListingResult:
    """Result of the performed operation.

    Attributes:
        environment (AzureEnvironment | Unset): Specifies the type of the Microsoft Azure cloud environment.
        appliance_tenant_id (None | str | Unset): Microsoft Azure ID assigned to a tenant to which the backup appliance
            belongs.
        default_tenant_id (None | str | Unset): Microsoft Azure ID assigned to a tenant with which the service account
            is associated.
        default_tenant_name (None | str | Unset): Name of the tenant.
        subscriptions (list[SubscriptionForServiceAccount] | None | Unset): Information on each subscription available
            for the tenant.
        required_roles_hint (list[str] | None | Unset): List of user role hints.
    """

    environment: AzureEnvironment | Unset = UNSET
    appliance_tenant_id: None | str | Unset = UNSET
    default_tenant_id: None | str | Unset = UNSET
    default_tenant_name: None | str | Unset = UNSET
    subscriptions: list[SubscriptionForServiceAccount] | None | Unset = UNSET
    required_roles_hint: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        environment: str | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value

        appliance_tenant_id: None | str | Unset
        if isinstance(self.appliance_tenant_id, Unset):
            appliance_tenant_id = UNSET
        else:
            appliance_tenant_id = self.appliance_tenant_id

        default_tenant_id: None | str | Unset
        if isinstance(self.default_tenant_id, Unset):
            default_tenant_id = UNSET
        else:
            default_tenant_id = self.default_tenant_id

        default_tenant_name: None | str | Unset
        if isinstance(self.default_tenant_name, Unset):
            default_tenant_name = UNSET
        else:
            default_tenant_name = self.default_tenant_name

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

        required_roles_hint: list[str] | None | Unset
        if isinstance(self.required_roles_hint, Unset):
            required_roles_hint = UNSET
        elif isinstance(self.required_roles_hint, list):
            required_roles_hint = self.required_roles_hint

        else:
            required_roles_hint = self.required_roles_hint

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if environment is not UNSET:
            field_dict["environment"] = environment
        if appliance_tenant_id is not UNSET:
            field_dict["applianceTenantId"] = appliance_tenant_id
        if default_tenant_id is not UNSET:
            field_dict["defaultTenantId"] = default_tenant_id
        if default_tenant_name is not UNSET:
            field_dict["defaultTenantName"] = default_tenant_name
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if required_roles_hint is not UNSET:
            field_dict["requiredRolesHint"] = required_roles_hint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_for_service_account import SubscriptionForServiceAccount

        d = dict(src_dict)
        _environment = d.pop("environment", UNSET)
        environment: AzureEnvironment | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = AzureEnvironment(_environment)

        def _parse_appliance_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        appliance_tenant_id = _parse_appliance_tenant_id(d.pop("applianceTenantId", UNSET))

        def _parse_default_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_tenant_id = _parse_default_tenant_id(d.pop("defaultTenantId", UNSET))

        def _parse_default_tenant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_tenant_name = _parse_default_tenant_name(d.pop("defaultTenantName", UNSET))

        def _parse_subscriptions(data: object) -> list[SubscriptionForServiceAccount] | None | Unset:
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
                    subscriptions_type_0_item = SubscriptionForServiceAccount.from_dict(subscriptions_type_0_item_data)

                    subscriptions_type_0.append(subscriptions_type_0_item)

                return subscriptions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SubscriptionForServiceAccount] | None | Unset, data)

        subscriptions = _parse_subscriptions(d.pop("subscriptions", UNSET))

        def _parse_required_roles_hint(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_roles_hint_type_0 = cast(list[str], data)

                return required_roles_hint_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        required_roles_hint = _parse_required_roles_hint(d.pop("requiredRolesHint", UNSET))

        subscriptions_listing_result = cls(
            environment=environment,
            appliance_tenant_id=appliance_tenant_id,
            default_tenant_id=default_tenant_id,
            default_tenant_name=default_tenant_name,
            subscriptions=subscriptions,
            required_roles_hint=required_roles_hint,
        )

        return subscriptions_listing_result
