from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.virtual_machine_validation_steps import VirtualMachineValidationSteps
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_machine_restore_options_with_restore_point import VirtualMachineRestoreOptionsWithRestorePoint


T = TypeVar("T", bound="BulkVmRestoreOptionsValidationConfig")


@_attrs_define
class BulkVmRestoreOptionsValidationConfig:
    """
    Attributes:
        validation_steps (list[VirtualMachineValidationSteps] | None | Unset): Specifies the steps of the Azure VM
            validation.
        restore_options (list[VirtualMachineRestoreOptionsWithRestorePoint] | None | Unset): Specifies Azure VM restore
            options.
    """

    validation_steps: list[VirtualMachineValidationSteps] | None | Unset = UNSET
    restore_options: list[VirtualMachineRestoreOptionsWithRestorePoint] | None | Unset = UNSET

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

        restore_options: list[dict[str, Any]] | None | Unset
        if isinstance(self.restore_options, Unset):
            restore_options = UNSET
        elif isinstance(self.restore_options, list):
            restore_options = []
            for restore_options_type_0_item_data in self.restore_options:
                restore_options_type_0_item = restore_options_type_0_item_data.to_dict()
                restore_options.append(restore_options_type_0_item)

        else:
            restore_options = self.restore_options

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if validation_steps is not UNSET:
            field_dict["validationSteps"] = validation_steps
        if restore_options is not UNSET:
            field_dict["restoreOptions"] = restore_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.virtual_machine_restore_options_with_restore_point import (
            VirtualMachineRestoreOptionsWithRestorePoint,
        )

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

        def _parse_restore_options(data: object) -> list[VirtualMachineRestoreOptionsWithRestorePoint] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                restore_options_type_0 = []
                _restore_options_type_0 = data
                for restore_options_type_0_item_data in _restore_options_type_0:
                    restore_options_type_0_item = VirtualMachineRestoreOptionsWithRestorePoint.from_dict(
                        restore_options_type_0_item_data
                    )

                    restore_options_type_0.append(restore_options_type_0_item)

                return restore_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VirtualMachineRestoreOptionsWithRestorePoint] | None | Unset, data)

        restore_options = _parse_restore_options(d.pop("restoreOptions", UNSET))

        bulk_vm_restore_options_validation_config = cls(
            validation_steps=validation_steps,
            restore_options=restore_options,
        )

        return bulk_vm_restore_options_validation_config
