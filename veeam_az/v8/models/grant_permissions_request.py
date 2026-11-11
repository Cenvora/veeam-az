from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_authentication_result import AzureAuthenticationResult
    from ..models.management_group_settings import ManagementGroupSettings


T = TypeVar("T", bound="GrantPermissionsRequest")


@_attrs_define
class GrantPermissionsRequest:
    """
    Attributes:
        azure_authentication_result (AzureAuthenticationResult): Specifies information on authentication in Microsoft
            Azure environment.
        subscriptions (list[UUID] | None | Unset):
        management_group_settings (ManagementGroupSettings | Unset):
    """

    azure_authentication_result: AzureAuthenticationResult
    subscriptions: list[UUID] | None | Unset = UNSET
    management_group_settings: ManagementGroupSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        azure_authentication_result = self.azure_authentication_result.to_dict()

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

        management_group_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.management_group_settings, Unset):
            management_group_settings = self.management_group_settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "azureAuthenticationResult": azure_authentication_result,
            }
        )
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if management_group_settings is not UNSET:
            field_dict["managementGroupSettings"] = management_group_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_authentication_result import AzureAuthenticationResult
        from ..models.management_group_settings import ManagementGroupSettings

        d = dict(src_dict)
        azure_authentication_result = AzureAuthenticationResult.from_dict(d.pop("azureAuthenticationResult"))

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

        _management_group_settings = d.pop("managementGroupSettings", UNSET)
        management_group_settings: ManagementGroupSettings | Unset
        if isinstance(_management_group_settings, Unset):
            management_group_settings = UNSET
        else:
            management_group_settings = ManagementGroupSettings.from_dict(_management_group_settings)

        grant_permissions_request = cls(
            azure_authentication_result=azure_authentication_result,
            subscriptions=subscriptions,
            management_group_settings=management_group_settings,
        )

        return grant_permissions_request
