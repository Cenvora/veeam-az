from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tenant_for_service_account import TenantForServiceAccount


T = TypeVar("T", bound="TenantsListingResult")


@_attrs_define
class TenantsListingResult:
    """List of tenants to which the Microsoft Azure account used to authenticate to the Azure CLI has access.

    Attributes:
        tenants (list[TenantForServiceAccount] | Unset): Information on each tenant.
    """

    tenants: list[TenantForServiceAccount] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tenants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tenants, Unset):
            tenants = []
            for tenants_item_data in self.tenants:
                tenants_item = tenants_item_data.to_dict()
                tenants.append(tenants_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tenants is not UNSET:
            field_dict["tenants"] = tenants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_for_service_account import TenantForServiceAccount

        d = dict(src_dict)
        _tenants = d.pop("tenants", UNSET)
        tenants: list[TenantForServiceAccount] | Unset = UNSET
        if _tenants is not UNSET:
            tenants = []
            for tenants_item_data in _tenants:
                tenants_item = TenantForServiceAccount.from_dict(tenants_item_data)

                tenants.append(tenants_item)

        tenants_listing_result = cls(
            tenants=tenants,
        )

        return tenants_listing_result
