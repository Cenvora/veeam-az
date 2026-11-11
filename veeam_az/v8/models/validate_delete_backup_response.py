from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.validate_backup_removal_result import ValidateBackupRemovalResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validate_delete_backup_response_resource import ValidateDeleteBackupResponseResource


T = TypeVar("T", bound="ValidateDeleteBackupResponse")


@_attrs_define
class ValidateDeleteBackupResponse:
    """
    Attributes:
        id (str):
        isvalid (ValidateBackupRemovalResult): Specifies the result value for resource backup delete validation.
        errors (list[str] | None | Unset):
        details (ValidateDeleteBackupResponseResource | Unset):
    """

    id: str
    isvalid: ValidateBackupRemovalResult
    errors: list[str] | None | Unset = UNSET
    details: ValidateDeleteBackupResponseResource | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        isvalid = self.isvalid.value

        errors: list[str] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = self.errors

        else:
            errors = self.errors

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "isvalid": isvalid,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validate_delete_backup_response_resource import ValidateDeleteBackupResponseResource

        d = dict(src_dict)
        id = d.pop("id")

        isvalid = ValidateBackupRemovalResult(d.pop("isvalid"))

        def _parse_errors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = cast(list[str], data)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        _details = d.pop("details", UNSET)
        details: ValidateDeleteBackupResponseResource | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ValidateDeleteBackupResponseResource.from_dict(_details)

        validate_delete_backup_response = cls(
            id=id,
            isvalid=isvalid,
            errors=errors,
            details=details,
        )

        return validate_delete_backup_response
