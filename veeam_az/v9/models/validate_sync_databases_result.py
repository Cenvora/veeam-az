from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateSyncDatabasesResult")


@_attrs_define
class ValidateSyncDatabasesResult:
    """
    Attributes:
        error (bool | Unset):
        error_message (None | str | Unset):
        failed_database_ids (list[str] | None | Unset):
    """

    error: bool | Unset = UNSET
    error_message: None | str | Unset = UNSET
    failed_database_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        failed_database_ids: list[str] | None | Unset
        if isinstance(self.failed_database_ids, Unset):
            failed_database_ids = UNSET
        elif isinstance(self.failed_database_ids, list):
            failed_database_ids = self.failed_database_ids

        else:
            failed_database_ids = self.failed_database_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if failed_database_ids is not UNSET:
            field_dict["failedDatabaseIds"] = failed_database_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error", UNSET)

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        def _parse_failed_database_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                failed_database_ids_type_0 = cast(list[str], data)

                return failed_database_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        failed_database_ids = _parse_failed_database_ids(d.pop("failedDatabaseIds", UNSET))

        validate_sync_databases_result = cls(
            error=error,
            error_message=error_message,
            failed_database_ids=failed_database_ids,
        )

        return validate_sync_databases_result
