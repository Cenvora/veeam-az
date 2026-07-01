from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.tenant_access_status import TenantAccessStatus
from ..models.user_app_registration_status import UserAppRegistrationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_subscription import AzureSubscription
    from ..models.tenant import Tenant


T = TypeVar("T", bound="TenantForServiceAccount")


@_attrs_define
class TenantForServiceAccount:
    """Information on each tenant.

    Attributes:
        tenant (Tenant | Unset): Information on a Microsoft Entra tenant.
        subscriptions (list[AzureSubscription] | Unset): Information on Azure subscriptions associated with the tenant.
        user_app_registration_status (UserAppRegistrationStatus | Unset): Defines whether the Microsoft Azure account
            used to access the Azure CLI has permissions to create Entra ID applications in the tenant.
        access_status (TenantAccessStatus | Unset):
    """

    tenant: Tenant | Unset = UNSET
    subscriptions: list[AzureSubscription] | Unset = UNSET
    user_app_registration_status: UserAppRegistrationStatus | Unset = UNSET
    access_status: TenantAccessStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tenant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tenant, Unset):
            tenant = self.tenant.to_dict()

        subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item = subscriptions_item_data.to_dict()
                subscriptions.append(subscriptions_item)

        user_app_registration_status: str | Unset = UNSET
        if not isinstance(self.user_app_registration_status, Unset):
            user_app_registration_status = self.user_app_registration_status.value

        access_status: str | Unset = UNSET
        if not isinstance(self.access_status, Unset):
            access_status = self.access_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if user_app_registration_status is not UNSET:
            field_dict["userAppRegistrationStatus"] = user_app_registration_status
        if access_status is not UNSET:
            field_dict["accessStatus"] = access_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_subscription import AzureSubscription
        from ..models.tenant import Tenant

        d = dict(src_dict)
        _tenant = d.pop("tenant", UNSET)
        tenant: Tenant | Unset
        if isinstance(_tenant, Unset):
            tenant = UNSET
        else:
            tenant = Tenant.from_dict(_tenant)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[AzureSubscription] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:
                subscriptions_item = AzureSubscription.from_dict(subscriptions_item_data)

                subscriptions.append(subscriptions_item)

        _user_app_registration_status = d.pop("userAppRegistrationStatus", UNSET)
        user_app_registration_status: UserAppRegistrationStatus | Unset
        if isinstance(_user_app_registration_status, Unset):
            user_app_registration_status = UNSET
        else:
            user_app_registration_status = UserAppRegistrationStatus(_user_app_registration_status)

        _access_status = d.pop("accessStatus", UNSET)
        access_status: TenantAccessStatus | Unset
        if isinstance(_access_status, Unset):
            access_status = UNSET
        else:
            access_status = TenantAccessStatus(_access_status)

        tenant_for_service_account = cls(
            tenant=tenant,
            subscriptions=subscriptions,
            user_app_registration_status=user_app_registration_status,
            access_status=access_status,
        )

        return tenant_for_service_account
