from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.azure_authentication_result import AzureAuthenticationResult


T = TypeVar("T", bound="RecreateServiceAccountRequest")


@_attrs_define
class RecreateServiceAccountRequest:
    """
    Attributes:
        azure_authentication_result (AzureAuthenticationResult): Specifies information on authentication in Microsoft
            Azure environment.
    """

    azure_authentication_result: AzureAuthenticationResult

    def to_dict(self) -> dict[str, Any]:
        azure_authentication_result = self.azure_authentication_result.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "azureAuthenticationResult": azure_authentication_result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_authentication_result import AzureAuthenticationResult

        d = dict(src_dict)
        azure_authentication_result = AzureAuthenticationResult.from_dict(d.pop("azureAuthenticationResult"))

        recreate_service_account_request = cls(
            azure_authentication_result=azure_authentication_result,
        )

        return recreate_service_account_request
