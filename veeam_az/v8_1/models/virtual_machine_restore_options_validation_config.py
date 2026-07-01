from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.virtual_machine_validation_steps import VirtualMachineValidationSteps
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_machine_restore_options import VirtualMachineRestoreOptions


T = TypeVar("T", bound="VirtualMachineRestoreOptionsValidationConfig")


@_attrs_define
class VirtualMachineRestoreOptionsValidationConfig:
    """
    Attributes:
        validation_steps (list[VirtualMachineValidationSteps] | None | Unset): Specifies the steps of the Azure VM
            validation.
        restore_options (VirtualMachineRestoreOptions | Unset): Specifies Azure VM restore options.
    """

    validation_steps: list[VirtualMachineValidationSteps] | None | Unset = UNSET
    restore_options: VirtualMachineRestoreOptions | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        validation_steps: list[str] | None | Unset
        if isinstance(self.validation_steps, Unset):
            validation_steps = UNSET
        elif isinstance(self.validation_steps, list):
            validation_steps = []
            for validation_steps_type_0_item_data in self.validation_steps:
                validation_steps_type_0_item = validation_steps_type_0_item_data.value
                validation_steps.append(validation_steps_type_0_item)

        else:
            validation_steps = self.validation_steps

        restore_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restore_options, Unset):
            restore_options = self.restore_options.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if validation_steps is not UNSET:
            field_dict["validationSteps"] = validation_steps
        if restore_options is not UNSET:
            field_dict["restoreOptions"] = restore_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.virtual_machine_restore_options import VirtualMachineRestoreOptions

        d = dict(src_dict)

        def _parse_validation_steps(data: object) -> list[VirtualMachineValidationSteps] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                validation_steps_type_0 = []
                _validation_steps_type_0 = data
                for validation_steps_type_0_item_data in _validation_steps_type_0:
                    validation_steps_type_0_item = VirtualMachineValidationSteps(validation_steps_type_0_item_data)

                    validation_steps_type_0.append(validation_steps_type_0_item)

                return validation_steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VirtualMachineValidationSteps] | None | Unset, data)

        validation_steps = _parse_validation_steps(d.pop("validationSteps", UNSET))

        _restore_options = d.pop("restoreOptions", UNSET)
        restore_options: VirtualMachineRestoreOptions | Unset
        if isinstance(_restore_options, Unset):
            restore_options = UNSET
        else:
            restore_options = VirtualMachineRestoreOptions.from_dict(_restore_options)

        virtual_machine_restore_options_validation_config = cls(
            validation_steps=validation_steps,
            restore_options=restore_options,
        )

        return virtual_machine_restore_options_validation_config
