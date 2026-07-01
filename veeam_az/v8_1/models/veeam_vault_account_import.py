from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="VeeamVaultAccountImport")


@_attrs_define
class VeeamVaultAccountImport:
    """
    Attributes:
        veeam_vault_id (int): System ID assigned in the Veeam infrastructure to the storage vault whose data will be
            imported.
    """

    veeam_vault_id: int

    def to_dict(self) -> dict[str, Any]:
        veeam_vault_id = self.veeam_vault_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "veeamVaultId": veeam_vault_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        veeam_vault_id = d.pop("veeamVaultId")

        veeam_vault_account_import = cls(
            veeam_vault_id=veeam_vault_id,
        )

        return veeam_vault_account_import
