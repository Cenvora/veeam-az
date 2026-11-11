from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deployment_consumption_tenant_response import DeploymentConsumptionTenantResponse
    from ..models.entra_id_resource import EntraIdResource
    from ..models.issue import Issue


T = TypeVar("T", bound="DeploymentConsumptionResponse")


@_attrs_define
class DeploymentConsumptionResponse:
    """
    Attributes:
        instance_id (str): TBD Specifies ID of an instance where VBAz is deployed
        tenants (list[DeploymentConsumptionTenantResponse]): TBD Array of tenants added to the VBAz server
        instance_capacity (EntraIdResource): TBD Resource consumption; The exact number value doesn't mean anything, we
            care about ratio, but we need to be consistent so e.g. two different VBAz instances don't return different
            numbers for the same tenant etc.
        issue (Issue): TBD Issue status
    """

    instance_id: str
    tenants: list[DeploymentConsumptionTenantResponse]
    instance_capacity: EntraIdResource
    issue: Issue
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_id = self.instance_id

        tenants = []
        for tenants_item_data in self.tenants:
            tenants_item = tenants_item_data.to_dict()
            tenants.append(tenants_item)

        instance_capacity = self.instance_capacity.to_dict()

        issue = self.issue.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instanceID": instance_id,
                "tenants": tenants,
                "instanceCapacity": instance_capacity,
                "issue": issue,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_consumption_tenant_response import DeploymentConsumptionTenantResponse
        from ..models.entra_id_resource import EntraIdResource
        from ..models.issue import Issue

        d = dict(src_dict)
        instance_id = d.pop("instanceID")

        tenants = []
        _tenants = d.pop("tenants")
        for tenants_item_data in _tenants:
            tenants_item = DeploymentConsumptionTenantResponse.from_dict(tenants_item_data)

            tenants.append(tenants_item)

        instance_capacity = EntraIdResource.from_dict(d.pop("instanceCapacity"))

        issue = Issue.from_dict(d.pop("issue"))

        deployment_consumption_response = cls(
            instance_id=instance_id,
            tenants=tenants,
            instance_capacity=instance_capacity,
            issue=issue,
        )

        deployment_consumption_response.additional_properties = d
        return deployment_consumption_response

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
