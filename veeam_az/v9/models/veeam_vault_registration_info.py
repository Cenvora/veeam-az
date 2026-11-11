from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamVaultRegistrationInfo")


@_attrs_define
class VeeamVaultRegistrationInfo:
    """
    Attributes:
        instance_registered (bool | Unset): Defines whether your backup appliance is registered in Veeam Data Cloud
            Vault.
        vdc_manage_link (str | Unset): Link to the Veeam Data Cloud Vault management page.
    """

    instance_registered: bool | Unset = UNSET
    vdc_manage_link: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        instance_registered = self.instance_registered

        vdc_manage_link = self.vdc_manage_link

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if instance_registered is not UNSET:
            field_dict["instanceRegistered"] = instance_registered
        if vdc_manage_link is not UNSET:
            field_dict["vdcManageLink"] = vdc_manage_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance_registered = d.pop("instanceRegistered", UNSET)

        vdc_manage_link = d.pop("vdcManageLink", UNSET)

        veeam_vault_registration_info = cls(
            instance_registered=instance_registered,
            vdc_manage_link=vdc_manage_link,
        )

        return veeam_vault_registration_info
