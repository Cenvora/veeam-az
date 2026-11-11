from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.configuration_restore_status import ConfigurationRestoreStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationRestoreStatusResponse")


@_attrs_define
class ConfigurationRestoreStatusResponse:
    """
    Attributes:
        restore_status (ConfigurationRestoreStatus | Unset):
    """

    restore_status: ConfigurationRestoreStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_status: str | Unset = UNSET
        if not isinstance(self.restore_status, Unset):
            restore_status = self.restore_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if restore_status is not UNSET:
            field_dict["restoreStatus"] = restore_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _restore_status = d.pop("restoreStatus", UNSET)
        restore_status: ConfigurationRestoreStatus | Unset
        if isinstance(_restore_status, Unset):
            restore_status = UNSET
        else:
            restore_status = ConfigurationRestoreStatus(_restore_status)

        configuration_restore_status_response = cls(
            restore_status=restore_status,
        )

        configuration_restore_status_response.additional_properties = d
        return configuration_restore_status_response

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
