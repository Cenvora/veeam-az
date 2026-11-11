from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.azure_account_purpose import AzureAccountPurpose
from ..models.subscription_availability import SubscriptionAvailability
from ..models.subscription_permissions_state import SubscriptionPermissionsState
from ..models.subscription_resource_providers_state import SubscriptionResourceProvidersState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.missing_subscription_purpose import MissingSubscriptionPurpose


T = TypeVar("T", bound="SubscriptionForServiceAccount")


@_attrs_define
class SubscriptionForServiceAccount:
    """Information on each subscription.

    Attributes:
        id (UUID | Unset): Microsoft Azure ID assigned to a subscription.
        name (None | str | Unset): Name of the subscription.
        tenant_id (None | str | Unset): Microsoft Azure ID assigned to the tenant to which the subscription belongs.
        permissions_state (SubscriptionPermissionsState | Unset): Status of the permission.
        missing_permissions (list[str] | None | Unset): Permissions that are missing in the current subscription.
        missing_data_actions (list[str] | None | Unset): Data actions that are missing in the current subscription.
        resource_providers_state (SubscriptionResourceProvidersState | Unset): Status of Azure resource providers
            registered in the subscription.
        missing_resource_providers (list[str] | None | Unset): Azure resource providers that are disabled in the current
            subscription.
        purposes (list[AzureAccountPurpose] | Unset): List of operations that can be performed using the service account
            to the Azure resources that belong to the subscription.
        missing_purposes (list[MissingSubscriptionPurpose] | None | Unset): List of operations that cannot be performed
            using the service account to the Azure resources that belong to the subscription, as the account permissions are
            insufficient.
        availability (SubscriptionAvailability | Unset): Specifies the subscription availability.
    """

    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    permissions_state: SubscriptionPermissionsState | Unset = UNSET
    missing_permissions: list[str] | None | Unset = UNSET
    missing_data_actions: list[str] | None | Unset = UNSET
    resource_providers_state: SubscriptionResourceProvidersState | Unset = UNSET
    missing_resource_providers: list[str] | None | Unset = UNSET
    purposes: list[AzureAccountPurpose] | Unset = UNSET
    missing_purposes: list[MissingSubscriptionPurpose] | None | Unset = UNSET
    availability: SubscriptionAvailability | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        permissions_state: str | Unset = UNSET
        if not isinstance(self.permissions_state, Unset):
            permissions_state = self.permissions_state.value

        missing_permissions: list[str] | None | Unset
        if isinstance(self.missing_permissions, Unset):
            missing_permissions = UNSET
        elif isinstance(self.missing_permissions, list):
            missing_permissions = self.missing_permissions

        else:
            missing_permissions = self.missing_permissions

        missing_data_actions: list[str] | None | Unset
        if isinstance(self.missing_data_actions, Unset):
            missing_data_actions = UNSET
        elif isinstance(self.missing_data_actions, list):
            missing_data_actions = self.missing_data_actions

        else:
            missing_data_actions = self.missing_data_actions

        resource_providers_state: str | Unset = UNSET
        if not isinstance(self.resource_providers_state, Unset):
            resource_providers_state = self.resource_providers_state.value

        missing_resource_providers: list[str] | None | Unset
        if isinstance(self.missing_resource_providers, Unset):
            missing_resource_providers = UNSET
        elif isinstance(self.missing_resource_providers, list):
            missing_resource_providers = self.missing_resource_providers

        else:
            missing_resource_providers = self.missing_resource_providers

        purposes: list[str] | Unset = UNSET
        if not isinstance(self.purposes, Unset):
            purposes = []
            for purposes_item_data in self.purposes:
                purposes_item = purposes_item_data.value
                purposes.append(purposes_item)

        missing_purposes: list[dict[str, Any]] | None | Unset
        if isinstance(self.missing_purposes, Unset):
            missing_purposes = UNSET
        elif isinstance(self.missing_purposes, list):
            missing_purposes = []
            for missing_purposes_type_0_item_data in self.missing_purposes:
                missing_purposes_type_0_item = missing_purposes_type_0_item_data.to_dict()
                missing_purposes.append(missing_purposes_type_0_item)

        else:
            missing_purposes = self.missing_purposes

        availability: str | Unset = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if permissions_state is not UNSET:
            field_dict["permissionsState"] = permissions_state
        if missing_permissions is not UNSET:
            field_dict["missingPermissions"] = missing_permissions
        if missing_data_actions is not UNSET:
            field_dict["missingDataActions"] = missing_data_actions
        if resource_providers_state is not UNSET:
            field_dict["resourceProvidersState"] = resource_providers_state
        if missing_resource_providers is not UNSET:
            field_dict["missingResourceProviders"] = missing_resource_providers
        if purposes is not UNSET:
            field_dict["purposes"] = purposes
        if missing_purposes is not UNSET:
            field_dict["missingPurposes"] = missing_purposes
        if availability is not UNSET:
            field_dict["availability"] = availability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.missing_subscription_purpose import MissingSubscriptionPurpose

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        _permissions_state = d.pop("permissionsState", UNSET)
        permissions_state: SubscriptionPermissionsState | Unset
        if isinstance(_permissions_state, Unset):
            permissions_state = UNSET
        else:
            permissions_state = SubscriptionPermissionsState(_permissions_state)

        def _parse_missing_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_permissions_type_0 = cast(list[str], data)

                return missing_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        missing_permissions = _parse_missing_permissions(d.pop("missingPermissions", UNSET))

        def _parse_missing_data_actions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_data_actions_type_0 = cast(list[str], data)

                return missing_data_actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        missing_data_actions = _parse_missing_data_actions(d.pop("missingDataActions", UNSET))

        _resource_providers_state = d.pop("resourceProvidersState", UNSET)
        resource_providers_state: SubscriptionResourceProvidersState | Unset
        if isinstance(_resource_providers_state, Unset):
            resource_providers_state = UNSET
        else:
            resource_providers_state = SubscriptionResourceProvidersState(_resource_providers_state)

        def _parse_missing_resource_providers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_resource_providers_type_0 = cast(list[str], data)

                return missing_resource_providers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        missing_resource_providers = _parse_missing_resource_providers(d.pop("missingResourceProviders", UNSET))

        _purposes = d.pop("purposes", UNSET)
        purposes: list[AzureAccountPurpose] | Unset = UNSET
        if _purposes is not UNSET:
            purposes = []
            for purposes_item_data in _purposes:
                purposes_item = AzureAccountPurpose(purposes_item_data)

                purposes.append(purposes_item)

        def _parse_missing_purposes(data: object) -> list[MissingSubscriptionPurpose] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_purposes_type_0 = []
                _missing_purposes_type_0 = data
                for missing_purposes_type_0_item_data in _missing_purposes_type_0:
                    missing_purposes_type_0_item = MissingSubscriptionPurpose.from_dict(
                        missing_purposes_type_0_item_data
                    )

                    missing_purposes_type_0.append(missing_purposes_type_0_item)

                return missing_purposes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MissingSubscriptionPurpose] | None | Unset, data)

        missing_purposes = _parse_missing_purposes(d.pop("missingPurposes", UNSET))

        _availability = d.pop("availability", UNSET)
        availability: SubscriptionAvailability | Unset
        if isinstance(_availability, Unset):
            availability = UNSET
        else:
            availability = SubscriptionAvailability(_availability)

        subscription_for_service_account = cls(
            id=id,
            name=name,
            tenant_id=tenant_id,
            permissions_state=permissions_state,
            missing_permissions=missing_permissions,
            missing_data_actions=missing_data_actions,
            resource_providers_state=resource_providers_state,
            missing_resource_providers=missing_resource_providers,
            purposes=purposes,
            missing_purposes=missing_purposes,
            availability=availability,
        )

        return subscription_for_service_account
