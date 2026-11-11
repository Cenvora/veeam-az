from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlaTemplateAssignment")


@_attrs_define
class SlaTemplateAssignment:
    """
    Attributes:
        protection_policy_id (UUID | Unset): System ID assigned to an SLA-based backup policy in the Veeam Backup for
            Microsoft Azure REST API.
        protection_policy_name (str | Unset): Name of the SLA-based backup policy.
    """

    protection_policy_id: UUID | Unset = UNSET
    protection_policy_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        protection_policy_id: str | Unset = UNSET
        if not isinstance(self.protection_policy_id, Unset):
            protection_policy_id = str(self.protection_policy_id)

        protection_policy_name = self.protection_policy_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if protection_policy_id is not UNSET:
            field_dict["protectionPolicyId"] = protection_policy_id
        if protection_policy_name is not UNSET:
            field_dict["protectionPolicyName"] = protection_policy_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _protection_policy_id = d.pop("protectionPolicyId", UNSET)
        protection_policy_id: UUID | Unset
        if isinstance(_protection_policy_id, Unset):
            protection_policy_id = UNSET
        else:
            protection_policy_id = UUID(_protection_policy_id)

        protection_policy_name = d.pop("protectionPolicyName", UNSET)

        sla_template_assignment = cls(
            protection_policy_id=protection_policy_id,
            protection_policy_name=protection_policy_name,
        )

        sla_template_assignment.additional_properties = d
        return sla_template_assignment

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
