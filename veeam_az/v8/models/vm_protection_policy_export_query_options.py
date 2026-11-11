from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VmProtectionPolicyExportQueryOptions")


@_attrs_define
class VmProtectionPolicyExportQueryOptions:
    """
    Attributes:
        policy_name (None | str | Unset): Exports only data on an SLA-based backup policy with the specified name.
        protection_policy_ids (list[str] | None | Unset): Specifies a list of system IDs assigned in the Veeam Backup
            for Microsoft Azure REST API to SLA-based backup policies whose data will be exported.
    """

    policy_name: None | str | Unset = UNSET
    protection_policy_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        policy_name: None | str | Unset
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        protection_policy_ids: list[str] | None | Unset
        if isinstance(self.protection_policy_ids, Unset):
            protection_policy_ids = UNSET
        elif isinstance(self.protection_policy_ids, list):
            protection_policy_ids = self.protection_policy_ids

        else:
            protection_policy_ids = self.protection_policy_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if protection_policy_ids is not UNSET:
            field_dict["protectionPolicyIds"] = protection_policy_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        def _parse_protection_policy_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protection_policy_ids_type_0 = cast(list[str], data)

                return protection_policy_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        protection_policy_ids = _parse_protection_policy_ids(d.pop("protectionPolicyIds", UNSET))

        vm_protection_policy_export_query_options = cls(
            policy_name=policy_name,
            protection_policy_ids=protection_policy_ids,
        )

        return vm_protection_policy_export_query_options
