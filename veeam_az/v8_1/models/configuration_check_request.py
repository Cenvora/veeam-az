from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.configuration_check_type import ConfigurationCheckType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationCheckRequest")


@_attrs_define
class ConfigurationCheckRequest:
    """
    Attributes:
        check_type (list[ConfigurationCheckType] | Unset): Specifies types of configuration checks that must be run.
    """

    check_type: list[ConfigurationCheckType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_type: list[str] | Unset = UNSET
        if not isinstance(self.check_type, Unset):
            check_type = []
            for check_type_item_data in self.check_type:
                check_type_item = check_type_item_data.value
                check_type.append(check_type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_type is not UNSET:
            field_dict["checkType"] = check_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _check_type = d.pop("checkType", UNSET)
        check_type: list[ConfigurationCheckType] | Unset = UNSET
        if _check_type is not UNSET:
            check_type = []
            for check_type_item_data in _check_type:
                check_type_item = ConfigurationCheckType(check_type_item_data)

                check_type.append(check_type_item)

        configuration_check_request = cls(
            check_type=check_type,
        )

        configuration_check_request.additional_properties = d
        return configuration_check_request

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
