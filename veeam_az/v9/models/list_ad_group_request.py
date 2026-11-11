from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ad_group_query_options import AdGroupQueryOptions
    from ..models.azure_authentication_result import AzureAuthenticationResult


T = TypeVar("T", bound="ListAdGroupRequest")


@_attrs_define
class ListAdGroupRequest:
    """
    Attributes:
        tenant_id (None | str): Specifies the Microsoft Azure ID assigned to a tenant with which the service account is
            associated.
        azure_authentication (AzureAuthenticationResult | Unset): Specifies information on authentication in Microsoft
            Azure environment.
        query_options (AdGroupQueryOptions | Unset): Specifies the order to sort the returned items by value of the
            `displayName` property. Use `DisplayNameDesc` or `DisplayNameAsc` values. </br> Example&#58;
            `"queryOptions":{"sort":"DisplayNameDesc"}`
        edit_account_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure
            REST API to the service account that will be edited.
    """

    tenant_id: None | str
    azure_authentication: AzureAuthenticationResult | Unset = UNSET
    query_options: AdGroupQueryOptions | Unset = UNSET
    edit_account_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tenant_id: None | str
        tenant_id = self.tenant_id

        azure_authentication: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_authentication, Unset):
            azure_authentication = self.azure_authentication.to_dict()

        query_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_options, Unset):
            query_options = self.query_options.to_dict()

        edit_account_id: None | str | Unset
        if isinstance(self.edit_account_id, Unset):
            edit_account_id = UNSET
        else:
            edit_account_id = self.edit_account_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tenantId": tenant_id,
            }
        )
        if azure_authentication is not UNSET:
            field_dict["azureAuthentication"] = azure_authentication
        if query_options is not UNSET:
            field_dict["queryOptions"] = query_options
        if edit_account_id is not UNSET:
            field_dict["editAccountId"] = edit_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_group_query_options import AdGroupQueryOptions
        from ..models.azure_authentication_result import AzureAuthenticationResult

        d = dict(src_dict)

        def _parse_tenant_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId"))

        _azure_authentication = d.pop("azureAuthentication", UNSET)
        azure_authentication: AzureAuthenticationResult | Unset
        if isinstance(_azure_authentication, Unset):
            azure_authentication = UNSET
        else:
            azure_authentication = AzureAuthenticationResult.from_dict(_azure_authentication)

        _query_options = d.pop("queryOptions", UNSET)
        query_options: AdGroupQueryOptions | Unset
        if isinstance(_query_options, Unset):
            query_options = UNSET
        else:
            query_options = AdGroupQueryOptions.from_dict(_query_options)

        def _parse_edit_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edit_account_id = _parse_edit_account_id(d.pop("editAccountId", UNSET))

        list_ad_group_request = cls(
            tenant_id=tenant_id,
            azure_authentication=azure_authentication,
            query_options=query_options,
            edit_account_id=edit_account_id,
        )

        return list_ad_group_request
