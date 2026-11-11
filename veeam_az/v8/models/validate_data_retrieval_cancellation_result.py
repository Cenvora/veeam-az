from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_message import ValidationMessage


T = TypeVar("T", bound="ValidateDataRetrievalCancellationResult")


@_attrs_define
class ValidateDataRetrievalCancellationResult:
    """
    Attributes:
        validation_message (ValidationMessage | Unset): Information on each message on the validation.
        success (bool | Unset):
    """

    validation_message: ValidationMessage | Unset = UNSET
    success: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        validation_message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.validation_message, Unset):
            validation_message = self.validation_message.to_dict()

        success = self.success

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if validation_message is not UNSET:
            field_dict["validationMessage"] = validation_message
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validation_message import ValidationMessage

        d = dict(src_dict)
        _validation_message = d.pop("validationMessage", UNSET)
        validation_message: ValidationMessage | Unset
        if isinstance(_validation_message, Unset):
            validation_message = UNSET
        else:
            validation_message = ValidationMessage.from_dict(_validation_message)

        success = d.pop("success", UNSET)

        validate_data_retrieval_cancellation_result = cls(
            validation_message=validation_message,
            success=success,
        )

        return validate_data_retrieval_cancellation_result
