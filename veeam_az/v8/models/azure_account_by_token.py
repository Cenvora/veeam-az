from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_permissions_update import AzurePermissionsUpdate


T = TypeVar("T", bound="AzureAccountByToken")


@_attrs_define
class AzureAccountByToken:
    r"""Result of the performed operation.

    Attributes:
        account_id (str): System ID assigned to a service account in the Veeam Backup for Microsoft Azure REST API.
        application_id (str | Unset): Microsoft Azure ID assigned to the Entra ID application with which the service
            account is associated.
        azure_permissions_update (AzurePermissionsUpdate | Unset): \[Applies if any permissions of the account must be
            updated] Information on the update of the account permissions.
    """

    account_id: str
    application_id: str | Unset = UNSET
    azure_permissions_update: AzurePermissionsUpdate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        application_id = self.application_id

        azure_permissions_update: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_permissions_update, Unset):
            azure_permissions_update = self.azure_permissions_update.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
            }
        )
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if azure_permissions_update is not UNSET:
            field_dict["azurePermissionsUpdate"] = azure_permissions_update

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_permissions_update import AzurePermissionsUpdate

        d = dict(src_dict)
        account_id = d.pop("accountId")

        application_id = d.pop("applicationId", UNSET)

        _azure_permissions_update = d.pop("azurePermissionsUpdate", UNSET)
        azure_permissions_update: AzurePermissionsUpdate | Unset
        if isinstance(_azure_permissions_update, Unset):
            azure_permissions_update = UNSET
        else:
            azure_permissions_update = AzurePermissionsUpdate.from_dict(_azure_permissions_update)

        azure_account_by_token = cls(
            account_id=account_id,
            application_id=application_id,
            azure_permissions_update=azure_permissions_update,
        )

        azure_account_by_token.additional_properties = d
        return azure_account_by_token

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
