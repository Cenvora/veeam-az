from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationOverrideOwnershipResponse")


@_attrs_define
class ConfigurationOverrideOwnershipResponse:
    """
    Attributes:
        job_session_ids (list[UUID] | Unset):
    """

    job_session_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_session_ids: list[str] | Unset = UNSET
        if not isinstance(self.job_session_ids, Unset):
            job_session_ids = []
            for job_session_ids_item_data in self.job_session_ids:
                job_session_ids_item = str(job_session_ids_item_data)
                job_session_ids.append(job_session_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_session_ids is not UNSET:
            field_dict["jobSessionIds"] = job_session_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _job_session_ids = d.pop("jobSessionIds", UNSET)
        job_session_ids: list[UUID] | Unset = UNSET
        if _job_session_ids is not UNSET:
            job_session_ids = []
            for job_session_ids_item_data in _job_session_ids:
                job_session_ids_item = UUID(job_session_ids_item_data)

                job_session_ids.append(job_session_ids_item)

        configuration_override_ownership_response = cls(
            job_session_ids=job_session_ids,
        )

        configuration_override_ownership_response.additional_properties = d
        return configuration_override_ownership_response

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
