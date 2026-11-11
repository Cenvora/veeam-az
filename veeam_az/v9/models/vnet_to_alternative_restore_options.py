from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VnetToAlternativeRestoreOptions")


@_attrs_define
class VnetToAlternativeRestoreOptions:
    r"""\[Applies only if the *ToDifferent* value has been specified for the `VnetRestorePointRestoreType` parameter]
    Specifies the settings configured when restoring to a new location or with different settings.

        Attributes:
            subscription_id (None | Unset | UUID): Specifies the Microsoft Azure ID assigned to a subscription to which the
                virtual network configuration items will be restored.
            region_id (None | str | Unset): Specifies a Microsoft Azure ID assigned to a region to which the virtual network
                configuration items will be restored.
            suffix (None | str | Unset): Specifies the suffix that will be added to restored item names if items with the
                same names already exist.
    """

    subscription_id: None | Unset | UUID = UNSET
    region_id: None | str | Unset = UNSET
    suffix: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        elif isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        suffix: None | str | Unset
        if isinstance(self.suffix, Unset):
            suffix = UNSET
        else:
            suffix = self.suffix

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if suffix is not UNSET:
            field_dict["suffix"] = suffix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_subscription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_type_0 = UUID(data)

                return subscription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        def _parse_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

        def _parse_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suffix = _parse_suffix(d.pop("suffix", UNSET))

        vnet_to_alternative_restore_options = cls(
            subscription_id=subscription_id,
            region_id=region_id,
            suffix=suffix,
        )

        return vnet_to_alternative_restore_options
