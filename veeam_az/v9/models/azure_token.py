from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.azure_account_purpose import AzureAccountPurpose
from ..models.azure_environment import AzureEnvironment
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="AzureToken")


@_attrs_define
class AzureToken:
    """Specifies information on authentication in Microsoft Azure environment.

    Attributes:
        access_token_cache (File): Specifies a string value representing authorization token to the Microsoft Azure
            Cross-platform Command Line Interface (Azure CLI).
        azure_environment (AzureEnvironment | Unset): Specifies the type of the Microsoft Azure cloud environment.
        azure_account_purposes (list[AzureAccountPurpose] | None | Unset): List of operations that can be performed
            using the service account.
        tenant_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a tenant with which the service
            account is associated.
    """

    access_token_cache: File
    azure_environment: AzureEnvironment | Unset = UNSET
    azure_account_purposes: list[AzureAccountPurpose] | None | Unset = UNSET
    tenant_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        access_token_cache = self.access_token_cache.to_tuple()

        azure_environment: str | Unset = UNSET
        if not isinstance(self.azure_environment, Unset):
            azure_environment = self.azure_environment.value

        azure_account_purposes: list[str] | None | Unset
        if isinstance(self.azure_account_purposes, Unset):
            azure_account_purposes = UNSET
        elif isinstance(self.azure_account_purposes, list):
            azure_account_purposes = []
            for azure_account_purposes_type_0_item_data in self.azure_account_purposes:
                azure_account_purposes_type_0_item = azure_account_purposes_type_0_item_data.value
                azure_account_purposes.append(azure_account_purposes_type_0_item)

        else:
            azure_account_purposes = self.azure_account_purposes

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accessTokenCache": access_token_cache,
            }
        )
        if azure_environment is not UNSET:
            field_dict["azureEnvironment"] = azure_environment
        if azure_account_purposes is not UNSET:
            field_dict["azureAccountPurposes"] = azure_account_purposes
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token_cache = File(payload=BytesIO(d.pop("accessTokenCache")))

        _azure_environment = d.pop("azureEnvironment", UNSET)
        azure_environment: AzureEnvironment | Unset
        if isinstance(_azure_environment, Unset):
            azure_environment = UNSET
        else:
            azure_environment = AzureEnvironment(_azure_environment)

        def _parse_azure_account_purposes(data: object) -> list[AzureAccountPurpose] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                azure_account_purposes_type_0 = []
                _azure_account_purposes_type_0 = data
                for azure_account_purposes_type_0_item_data in _azure_account_purposes_type_0:
                    azure_account_purposes_type_0_item = AzureAccountPurpose(azure_account_purposes_type_0_item_data)

                    azure_account_purposes_type_0.append(azure_account_purposes_type_0_item)

                return azure_account_purposes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AzureAccountPurpose] | None | Unset, data)

        azure_account_purposes = _parse_azure_account_purposes(d.pop("azureAccountPurposes", UNSET))

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        azure_token = cls(
            access_token_cache=access_token_cache,
            azure_environment=azure_environment,
            azure_account_purposes=azure_account_purposes,
            tenant_id=tenant_id,
        )

        return azure_token
