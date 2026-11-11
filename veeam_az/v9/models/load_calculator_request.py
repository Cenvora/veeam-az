from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadCalculatorRequest")


@_attrs_define
class LoadCalculatorRequest:
    """
    Attributes:
        tenant_id (None | UUID):
        subscription_ids (list[UUID] | None | Unset):
        management_group_ids (list[str] | None | Unset):
    """

    tenant_id: None | UUID
    subscription_ids: list[UUID] | None | Unset = UNSET
    management_group_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_id: None | str
        if isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        subscription_ids: list[str] | None | Unset
        if isinstance(self.subscription_ids, Unset):
            subscription_ids = UNSET
        elif isinstance(self.subscription_ids, list):
            subscription_ids = []
            for subscription_ids_type_0_item_data in self.subscription_ids:
                subscription_ids_type_0_item = str(subscription_ids_type_0_item_data)
                subscription_ids.append(subscription_ids_type_0_item)

        else:
            subscription_ids = self.subscription_ids

        management_group_ids: list[str] | None | Unset
        if isinstance(self.management_group_ids, Unset):
            management_group_ids = UNSET
        elif isinstance(self.management_group_ids, list):
            management_group_ids = self.management_group_ids

        else:
            management_group_ids = self.management_group_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenantId": tenant_id,
            }
        )
        if subscription_ids is not UNSET:
            field_dict["subscriptionIds"] = subscription_ids
        if management_group_ids is not UNSET:
            field_dict["managementGroupIds"] = management_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_tenant_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_id_type_0 = UUID(data)

                return tenant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId"))

        def _parse_subscription_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subscription_ids_type_0 = []
                _subscription_ids_type_0 = data
                for subscription_ids_type_0_item_data in _subscription_ids_type_0:
                    subscription_ids_type_0_item = UUID(subscription_ids_type_0_item_data)

                    subscription_ids_type_0.append(subscription_ids_type_0_item)

                return subscription_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        subscription_ids = _parse_subscription_ids(d.pop("subscriptionIds", UNSET))

        def _parse_management_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                management_group_ids_type_0 = cast(list[str], data)

                return management_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        management_group_ids = _parse_management_group_ids(d.pop("managementGroupIds", UNSET))

        load_calculator_request = cls(
            tenant_id=tenant_id,
            subscription_ids=subscription_ids,
            management_group_ids=management_group_ids,
        )

        load_calculator_request.additional_properties = d
        return load_calculator_request

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
