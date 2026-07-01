from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_account_info import AzureAccountInfo
    from ..models.client_login_parameters import ClientLoginParameters


T = TypeVar("T", bound="SaveAzureAccountInfo")


@_attrs_define
class SaveAzureAccountInfo:
    """
    Attributes:
        account_info (AzureAccountInfo): Specifies information on a service account.
        client_login_parameters (ClientLoginParameters | Unset): Specifies the login data of the Entra ID application.
    """

    account_info: AzureAccountInfo
    client_login_parameters: ClientLoginParameters | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account_info = self.account_info.to_dict()

        client_login_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_login_parameters, Unset):
            client_login_parameters = self.client_login_parameters.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accountInfo": account_info,
            }
        )
        if client_login_parameters is not UNSET:
            field_dict["clientLoginParameters"] = client_login_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_account_info import AzureAccountInfo
        from ..models.client_login_parameters import ClientLoginParameters

        d = dict(src_dict)
        account_info = AzureAccountInfo.from_dict(d.pop("accountInfo"))

        _client_login_parameters = d.pop("clientLoginParameters", UNSET)
        client_login_parameters: ClientLoginParameters | Unset
        if isinstance(_client_login_parameters, Unset):
            client_login_parameters = UNSET
        else:
            client_login_parameters = ClientLoginParameters.from_dict(_client_login_parameters)

        save_azure_account_info = cls(
            account_info=account_info,
            client_login_parameters=client_login_parameters,
        )

        return save_azure_account_info
