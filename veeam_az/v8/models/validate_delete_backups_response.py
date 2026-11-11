from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.validate_delete_backup_response import ValidateDeleteBackupResponse


T = TypeVar("T", bound="ValidateDeleteBackupsResponse")


@_attrs_define
class ValidateDeleteBackupsResponse:
    """
    Attributes:
        validations (list[ValidateDeleteBackupResponse]):
    """

    validations: list[ValidateDeleteBackupResponse]

    def to_dict(self) -> dict[str, Any]:
        validations = []
        for validations_item_data in self.validations:
            validations_item = validations_item_data.to_dict()
            validations.append(validations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "validations": validations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validate_delete_backup_response import ValidateDeleteBackupResponse

        d = dict(src_dict)
        validations = []
        _validations = d.pop("validations")
        for validations_item_data in _validations:
            validations_item = ValidateDeleteBackupResponse.from_dict(validations_item_data)

            validations.append(validations_item)

        validate_delete_backups_response = cls(
            validations=validations,
        )

        return validate_delete_backups_response
