from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entra_id_resource import EntraIdResource
    from ..models.issue import Issue
    from ..models.tenant_response import TenantResponse


T = TypeVar("T", bound="TenantLoadCalculatorResponse")


@_attrs_define
class TenantLoadCalculatorResponse:
    """
    Attributes:
        instance_id (str): TBD Specifies ID of an instance where VBAz is deployed
        tenant_id (UUID):
        tenant_items (TenantResponse):
        tenant_consumption (EntraIdResource): TBD Resource consumption; The exact number value doesn't mean anything, we
            care about ratio, but we need to be consistent so e.g. two different VBAz instances don't return different
            numbers for the same tenant etc.
        issue (Issue): TBD Issue status
        instance_resource_left (EntraIdResource | Unset): TBD Resource consumption; The exact number value doesn't mean
            anything, we care about ratio, but we need to be consistent so e.g. two different VBAz instances don't return
            different numbers for the same tenant etc.
    """

    instance_id: str
    tenant_id: UUID
    tenant_items: TenantResponse
    tenant_consumption: EntraIdResource
    issue: Issue
    instance_resource_left: EntraIdResource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_id = self.instance_id

        tenant_id = str(self.tenant_id)

        tenant_items = self.tenant_items.to_dict()

        tenant_consumption = self.tenant_consumption.to_dict()

        issue = self.issue.to_dict()

        instance_resource_left: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instance_resource_left, Unset):
            instance_resource_left = self.instance_resource_left.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instanceID": instance_id,
                "tenantId": tenant_id,
                "tenantItems": tenant_items,
                "tenantConsumption": tenant_consumption,
                "issue": issue,
            }
        )
        if instance_resource_left is not UNSET:
            field_dict["instanceResourceLeft"] = instance_resource_left

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entra_id_resource import EntraIdResource
        from ..models.issue import Issue
        from ..models.tenant_response import TenantResponse

        d = dict(src_dict)
        instance_id = d.pop("instanceID")

        tenant_id = UUID(d.pop("tenantId"))

        tenant_items = TenantResponse.from_dict(d.pop("tenantItems"))

        tenant_consumption = EntraIdResource.from_dict(d.pop("tenantConsumption"))

        issue = Issue.from_dict(d.pop("issue"))

        _instance_resource_left = d.pop("instanceResourceLeft", UNSET)
        instance_resource_left: EntraIdResource | Unset
        if isinstance(_instance_resource_left, Unset):
            instance_resource_left = UNSET
        else:
            instance_resource_left = EntraIdResource.from_dict(_instance_resource_left)

        tenant_load_calculator_response = cls(
            instance_id=instance_id,
            tenant_id=tenant_id,
            tenant_items=tenant_items,
            tenant_consumption=tenant_consumption,
            issue=issue,
            instance_resource_left=instance_resource_left,
        )

        tenant_load_calculator_response.additional_properties = d
        return tenant_load_calculator_response

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
