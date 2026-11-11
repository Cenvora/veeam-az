from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.azure_account_purpose import AzureAccountPurpose
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_account_info import AzureAccountInfo


T = TypeVar("T", bound="UpdateServiceAccountInfo")


@_attrs_define
class UpdateServiceAccountInfo:
    """
    Attributes:
        service_account (AzureAccountInfo): Specifies information on a service account.
        azure_account_purposes (list[AzureAccountPurpose] | None | Unset): List of operations that can be performed
            using the service account.
    """

    service_account: AzureAccountInfo
    azure_account_purposes: list[AzureAccountPurpose] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        service_account = self.service_account.to_dict()

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serviceAccount": service_account,
            }
        )
        if azure_account_purposes is not UNSET:
            field_dict["azureAccountPurposes"] = azure_account_purposes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_account_info import AzureAccountInfo

        d = dict(src_dict)
        service_account = AzureAccountInfo.from_dict(d.pop("serviceAccount"))

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

        update_service_account_info = cls(
            service_account=service_account,
            azure_account_purposes=azure_account_purposes,
        )

        return update_service_account_info
