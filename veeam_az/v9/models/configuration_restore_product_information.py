from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationRestoreProductInformation")


@_attrs_define
class ConfigurationRestoreProductInformation:
    """
    Attributes:
        product_name (str | Unset):
        product_version (str | Unset):
        flr_version (str | Unset):
    """

    product_name: str | Unset = UNSET
    product_version: str | Unset = UNSET
    flr_version: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        product_name = self.product_name

        product_version = self.product_version

        flr_version = self.flr_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if product_version is not UNSET:
            field_dict["productVersion"] = product_version
        if flr_version is not UNSET:
            field_dict["flrVersion"] = flr_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_name = d.pop("productName", UNSET)

        product_version = d.pop("productVersion", UNSET)

        flr_version = d.pop("flrVersion", UNSET)

        configuration_restore_product_information = cls(
            product_name=product_name,
            product_version=product_version,
            flr_version=flr_version,
        )

        return configuration_restore_product_information
