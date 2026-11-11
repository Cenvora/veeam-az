from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_authentication_result import AzureAuthenticationResult


T = TypeVar("T", bound="RenewClientSecretRequest")


@_attrs_define
class RenewClientSecretRequest:
    """
    Attributes:
        azure_authentication_result (AzureAuthenticationResult): Specifies information on authentication in Microsoft
            Azure environment.
        require_valid_login_count (int | None | Unset):
    """

    azure_authentication_result: AzureAuthenticationResult
    require_valid_login_count: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        azure_authentication_result = self.azure_authentication_result.to_dict()

        require_valid_login_count: int | None | Unset
        if isinstance(self.require_valid_login_count, Unset):
            require_valid_login_count = UNSET
        else:
            require_valid_login_count = self.require_valid_login_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "azureAuthenticationResult": azure_authentication_result,
            }
        )
        if require_valid_login_count is not UNSET:
            field_dict["requireValidLoginCount"] = require_valid_login_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_authentication_result import AzureAuthenticationResult

        d = dict(src_dict)
        azure_authentication_result = AzureAuthenticationResult.from_dict(d.pop("azureAuthenticationResult"))

        def _parse_require_valid_login_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        require_valid_login_count = _parse_require_valid_login_count(d.pop("requireValidLoginCount", UNSET))

        renew_client_secret_request = cls(
            azure_authentication_result=azure_authentication_result,
            require_valid_login_count=require_valid_login_count,
        )

        return renew_client_secret_request
