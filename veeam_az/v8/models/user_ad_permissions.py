from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAdPermissions")


@_attrs_define
class UserAdPermissions:
    """Define whether the user has permissions required for operations with Microsoft Entra groups and applications.

    Attributes:
        user_can_set_ad_group (bool | Unset): Defines whether the user has permissions to add Microsoft Entra
            applications to Microsoft Entra groups.
        user_can_renew_ad_app (bool | Unset): Defines whether the user has permissions to create client secrets for
            existing Microsoft Entra applications.
    """

    user_can_set_ad_group: bool | Unset = UNSET
    user_can_renew_ad_app: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_can_set_ad_group = self.user_can_set_ad_group

        user_can_renew_ad_app = self.user_can_renew_ad_app

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_can_set_ad_group is not UNSET:
            field_dict["userCanSetAdGroup"] = user_can_set_ad_group
        if user_can_renew_ad_app is not UNSET:
            field_dict["userCanRenewAdApp"] = user_can_renew_ad_app

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_can_set_ad_group = d.pop("userCanSetAdGroup", UNSET)

        user_can_renew_ad_app = d.pop("userCanRenewAdApp", UNSET)

        user_ad_permissions = cls(
            user_can_set_ad_group=user_can_set_ad_group,
            user_can_renew_ad_app=user_can_renew_ad_app,
        )

        return user_ad_permissions
