from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ad_group import AdGroup
    from ..models.user_ad_permissions import UserAdPermissions


T = TypeVar("T", bound="AdGroupListingResult")


@_attrs_define
class AdGroupListingResult:
    """Result of the performed operation.

    Attributes:
        ad_groups (list[AdGroup] | None | Unset): Information on a Microsoft Entra group.
        user_ad_permissions (UserAdPermissions | Unset): Define whether the user has permissions required for operations
            with Microsoft Entra groups and applications.
    """

    ad_groups: list[AdGroup] | None | Unset = UNSET
    user_ad_permissions: UserAdPermissions | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ad_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.ad_groups, Unset):
            ad_groups = UNSET
        elif isinstance(self.ad_groups, list):
            ad_groups = []
            for ad_groups_type_0_item_data in self.ad_groups:
                ad_groups_type_0_item = ad_groups_type_0_item_data.to_dict()
                ad_groups.append(ad_groups_type_0_item)

        else:
            ad_groups = self.ad_groups

        user_ad_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_ad_permissions, Unset):
            user_ad_permissions = self.user_ad_permissions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ad_groups is not UNSET:
            field_dict["adGroups"] = ad_groups
        if user_ad_permissions is not UNSET:
            field_dict["userAdPermissions"] = user_ad_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_group import AdGroup
        from ..models.user_ad_permissions import UserAdPermissions

        d = dict(src_dict)

        def _parse_ad_groups(data: object) -> list[AdGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ad_groups_type_0 = []
                _ad_groups_type_0 = data
                for ad_groups_type_0_item_data in _ad_groups_type_0:
                    ad_groups_type_0_item = AdGroup.from_dict(ad_groups_type_0_item_data)

                    ad_groups_type_0.append(ad_groups_type_0_item)

                return ad_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AdGroup] | None | Unset, data)

        ad_groups = _parse_ad_groups(d.pop("adGroups", UNSET))

        _user_ad_permissions = d.pop("userAdPermissions", UNSET)
        user_ad_permissions: UserAdPermissions | Unset
        if isinstance(_user_ad_permissions, Unset):
            user_ad_permissions = UNSET
        else:
            user_ad_permissions = UserAdPermissions.from_dict(_user_ad_permissions)

        ad_group_listing_result = cls(
            ad_groups=ad_groups,
            user_ad_permissions=user_ad_permissions,
        )

        return ad_group_listing_result
