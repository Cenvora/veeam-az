from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.validation_message_severity import ValidationMessageSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationMessage")


@_attrs_define
class ValidationMessage:
    """Information on each message on the validation.

    Attributes:
        severity (ValidationMessageSeverity | Unset): Severity level.
        message_id (None | str | Unset): System ID assigned to the validation message in the Veeam Backup for Microsoft
            Azure REST API.
        message (None | str | Unset): Text of the message.
        context_id (None | str | Unset): System ID assigned to the error in the Veeam Backup for Microsoft Azure REST
            API.
        target_name (None | str | Unset): Name of the instance where the error has occurred.
    """

    severity: ValidationMessageSeverity | Unset = UNSET
    message_id: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    context_id: None | str | Unset = UNSET
    target_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        message_id: None | str | Unset
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        else:
            message_id = self.message_id

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        context_id: None | str | Unset
        if isinstance(self.context_id, Unset):
            context_id = UNSET
        else:
            context_id = self.context_id

        target_name: None | str | Unset
        if isinstance(self.target_name, Unset):
            target_name = UNSET
        else:
            target_name = self.target_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if severity is not UNSET:
            field_dict["severity"] = severity
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if message is not UNSET:
            field_dict["message"] = message
        if context_id is not UNSET:
            field_dict["contextId"] = context_id
        if target_name is not UNSET:
            field_dict["targetName"] = target_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _severity = d.pop("severity", UNSET)
        severity: ValidationMessageSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = ValidationMessageSeverity(_severity)

        def _parse_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_id = _parse_message_id(d.pop("messageId", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_context_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_id = _parse_context_id(d.pop("contextId", UNSET))

        def _parse_target_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_name = _parse_target_name(d.pop("targetName", UNSET))

        validation_message = cls(
            severity=severity,
            message_id=message_id,
            message=message,
            context_id=context_id,
            target_name=target_name,
        )

        return validation_message
