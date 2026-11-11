from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.azure_permissions_update import AzurePermissionsUpdate


T = TypeVar("T", bound="GrantPermissionsResult")


@_attrs_define
class GrantPermissionsResult:
    r"""Result of the performed operation.

    Attributes:
        azure_permissions_update (AzurePermissionsUpdate): \[Applies if any permissions of the account must be updated]
            Information on the update of the account permissions.
    """

    azure_permissions_update: AzurePermissionsUpdate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        azure_permissions_update = self.azure_permissions_update.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "azurePermissionsUpdate": azure_permissions_update,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_permissions_update import AzurePermissionsUpdate

        d = dict(src_dict)
        azure_permissions_update = AzurePermissionsUpdate.from_dict(d.pop("azurePermissionsUpdate"))

        grant_permissions_result = cls(
            azure_permissions_update=azure_permissions_update,
        )

        grant_permissions_result.additional_properties = d
        return grant_permissions_result

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
