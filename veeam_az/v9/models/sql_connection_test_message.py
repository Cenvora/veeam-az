from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.connection_test_message_severity import ConnectionTestMessageSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlConnectionTestMessage")


@_attrs_define
class SqlConnectionTestMessage:
    """
    Attributes:
        severity (ConnectionTestMessageSeverity | Unset): Severity level.
        type_ (None | str | Unset): Type of the message.
        message (None | str | Unset): Text of the message.
    """

    severity: ConnectionTestMessageSeverity | Unset = UNSET
    type_: None | str | Unset = UNSET
    message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if severity is not UNSET:
            field_dict["severity"] = severity
        if type_ is not UNSET:
            field_dict["type"] = type_
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _severity = d.pop("severity", UNSET)
        severity: ConnectionTestMessageSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = ConnectionTestMessageSeverity(_severity)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        sql_connection_test_message = cls(
            severity=severity,
            type_=type_,
            message=message,
        )

        return sql_connection_test_message
