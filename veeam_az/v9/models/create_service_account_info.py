from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ad_group_settings import AdGroupSettings
    from ..models.azure_account_info import AzureAccountInfo
    from ..models.azure_authentication_result import AzureAuthenticationResult
    from ..models.management_group_settings import ManagementGroupSettings


T = TypeVar("T", bound="CreateServiceAccountInfo")


@_attrs_define
class CreateServiceAccountInfo:
    """
    Attributes:
        service_account (AzureAccountInfo): Specifies information on a service account.
        azure_authentication_result (AzureAuthenticationResult): Specifies information on authentication in Microsoft
            Azure environment.
        ad_group_settings (AdGroupSettings | Unset): Specifies the settings of a Microsoft Entra group.
        subscriptions (list[UUID] | None | Unset):
        tenant_id (None | str | Unset):
        management_group_settings (ManagementGroupSettings | Unset):
    """

    service_account: AzureAccountInfo
    azure_authentication_result: AzureAuthenticationResult
    ad_group_settings: AdGroupSettings | Unset = UNSET
    subscriptions: list[UUID] | None | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    management_group_settings: ManagementGroupSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        service_account = self.service_account.to_dict()

        azure_authentication_result = self.azure_authentication_result.to_dict()

        ad_group_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ad_group_settings, Unset):
            ad_group_settings = self.ad_group_settings.to_dict()

        subscriptions: list[str] | None | Unset
        if isinstance(self.subscriptions, Unset):
            subscriptions = UNSET
        elif isinstance(self.subscriptions, list):
            subscriptions = []
            for subscriptions_type_0_item_data in self.subscriptions:
                subscriptions_type_0_item = str(subscriptions_type_0_item_data)
                subscriptions.append(subscriptions_type_0_item)

        else:
            subscriptions = self.subscriptions

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        management_group_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.management_group_settings, Unset):
            management_group_settings = self.management_group_settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serviceAccount": service_account,
                "azureAuthenticationResult": azure_authentication_result,
            }
        )
        if ad_group_settings is not UNSET:
            field_dict["adGroupSettings"] = ad_group_settings
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if management_group_settings is not UNSET:
            field_dict["managementGroupSettings"] = management_group_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_group_settings import AdGroupSettings
        from ..models.azure_account_info import AzureAccountInfo
        from ..models.azure_authentication_result import AzureAuthenticationResult
        from ..models.management_group_settings import ManagementGroupSettings

        d = dict(src_dict)
        service_account = AzureAccountInfo.from_dict(d.pop("serviceAccount"))

        azure_authentication_result = AzureAuthenticationResult.from_dict(d.pop("azureAuthenticationResult"))

        _ad_group_settings = d.pop("adGroupSettings", UNSET)
        ad_group_settings: AdGroupSettings | Unset
        if isinstance(_ad_group_settings, Unset):
            ad_group_settings = UNSET
        else:
            ad_group_settings = AdGroupSettings.from_dict(_ad_group_settings)

        def _parse_subscriptions(data: object) -> list[UUID] | None | Unset:
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
                    subscriptions_type_0_item = UUID(subscriptions_type_0_item_data)

                    subscriptions_type_0.append(subscriptions_type_0_item)

                return subscriptions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        subscriptions = _parse_subscriptions(d.pop("subscriptions", UNSET))

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        _management_group_settings = d.pop("managementGroupSettings", UNSET)
        management_group_settings: ManagementGroupSettings | Unset
        if isinstance(_management_group_settings, Unset):
            management_group_settings = UNSET
        else:
            management_group_settings = ManagementGroupSettings.from_dict(_management_group_settings)

        create_service_account_info = cls(
            service_account=service_account,
            azure_authentication_result=azure_authentication_result,
            ad_group_settings=ad_group_settings,
            subscriptions=subscriptions,
            tenant_id=tenant_id,
            management_group_settings=management_group_settings,
        )

        return create_service_account_info
