from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_account_info import AzureAccountInfo
    from ..models.azure_authentication_result import AzureAuthenticationResult


T = TypeVar("T", bound="CreateRepositoryAccountInfo")


@_attrs_define
class CreateRepositoryAccountInfo:
    """
    Attributes:
        repository_account (AzureAccountInfo | Unset): Specifies information on a service account.
        azure_authentication_result (AzureAuthenticationResult | Unset): Specifies information on authentication in
            Microsoft Azure environment.
    """

    repository_account: AzureAccountInfo | Unset = UNSET
    azure_authentication_result: AzureAuthenticationResult | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        repository_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository_account, Unset):
            repository_account = self.repository_account.to_dict()

        azure_authentication_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_authentication_result, Unset):
            azure_authentication_result = self.azure_authentication_result.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository_account is not UNSET:
            field_dict["repositoryAccount"] = repository_account
        if azure_authentication_result is not UNSET:
            field_dict["azureAuthenticationResult"] = azure_authentication_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_account_info import AzureAccountInfo
        from ..models.azure_authentication_result import AzureAuthenticationResult

        d = dict(src_dict)
        _repository_account = d.pop("repositoryAccount", UNSET)
        repository_account: AzureAccountInfo | Unset
        if isinstance(_repository_account, Unset):
            repository_account = UNSET
        else:
            repository_account = AzureAccountInfo.from_dict(_repository_account)

        _azure_authentication_result = d.pop("azureAuthenticationResult", UNSET)
        azure_authentication_result: AzureAuthenticationResult | Unset
        if isinstance(_azure_authentication_result, Unset):
            azure_authentication_result = UNSET
        else:
            azure_authentication_result = AzureAuthenticationResult.from_dict(_azure_authentication_result)

        create_repository_account_info = cls(
            repository_account=repository_account,
            azure_authentication_result=azure_authentication_result,
        )

        return create_repository_account_info
