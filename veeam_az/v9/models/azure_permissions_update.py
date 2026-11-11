from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_permissions_update_error import AzurePermissionsUpdateError


T = TypeVar("T", bound="AzurePermissionsUpdate")


@_attrs_define
class AzurePermissionsUpdate:
    r"""\[Applies if any permissions of the account must be updated] Information on the update of the account permissions.

    Attributes:
        is_success (bool | Unset): Defines whether the permissions were updated successfully.
        errors (list[AzurePermissionsUpdateError] | None | Unset):
        trace_id (None | str | Unset): Unique identifier that can be used to search logs for more details.
    """

    is_success: bool | Unset = UNSET
    errors: list[AzurePermissionsUpdateError] | None | Unset = UNSET
    trace_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_success = self.is_success

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        trace_id: None | str | Unset
        if isinstance(self.trace_id, Unset):
            trace_id = UNSET
        else:
            trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_success is not UNSET:
            field_dict["isSuccess"] = is_success
        if errors is not UNSET:
            field_dict["errors"] = errors
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_permissions_update_error import AzurePermissionsUpdateError

        d = dict(src_dict)
        is_success = d.pop("isSuccess", UNSET)

        def _parse_errors(data: object) -> list[AzurePermissionsUpdateError] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = AzurePermissionsUpdateError.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AzurePermissionsUpdateError] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        def _parse_trace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trace_id = _parse_trace_id(d.pop("traceId", UNSET))

        azure_permissions_update = cls(
            is_success=is_success,
            errors=errors,
            trace_id=trace_id,
        )

        azure_permissions_update.additional_properties = d
        return azure_permissions_update

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
