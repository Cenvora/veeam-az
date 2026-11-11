from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SupportInfo")


@_attrs_define
class SupportInfo:
    """
    Attributes:
        azure_tenant_id (None | str | Unset): Microsoft Azure ID assigned to a tenant where the backup appliance is
            deployed.
        support_code (None | str | Unset): Unique identification number of the Veeam support contract.
    """

    azure_tenant_id: None | str | Unset = UNSET
    support_code: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        azure_tenant_id: None | str | Unset
        if isinstance(self.azure_tenant_id, Unset):
            azure_tenant_id = UNSET
        else:
            azure_tenant_id = self.azure_tenant_id

        support_code: None | str | Unset
        if isinstance(self.support_code, Unset):
            support_code = UNSET
        else:
            support_code = self.support_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if azure_tenant_id is not UNSET:
            field_dict["azureTenantId"] = azure_tenant_id
        if support_code is not UNSET:
            field_dict["supportCode"] = support_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_azure_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_tenant_id = _parse_azure_tenant_id(d.pop("azureTenantId", UNSET))

        def _parse_support_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_code = _parse_support_code(d.pop("supportCode", UNSET))

        support_info = cls(
            azure_tenant_id=azure_tenant_id,
            support_code=support_code,
        )

        return support_info
