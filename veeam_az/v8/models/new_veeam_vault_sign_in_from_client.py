from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewVeeamVaultSignInFromClient")


@_attrs_define
class NewVeeamVaultSignInFromClient:
    """
    Attributes:
        redirect_url (str): Specifies the backup appliance URL that will be used as a redirect URL in the Veeam Data
            Cloud Vault authorization.
    """

    redirect_url: str

    def to_dict(self) -> dict[str, Any]:
        redirect_url = self.redirect_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "redirectUrl": redirect_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        redirect_url = d.pop("redirectUrl")

        new_veeam_vault_sign_in_from_client = cls(
            redirect_url=redirect_url,
        )

        return new_veeam_vault_sign_in_from_client
