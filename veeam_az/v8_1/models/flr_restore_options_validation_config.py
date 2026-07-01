from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="FlrRestoreOptionsValidationConfig")


@_attrs_define
class FlrRestoreOptionsValidationConfig:
    """
    Attributes:
        service_account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to
            a service account whose permissions will be used to restore files.
    """

    service_account_id: UUID

    def to_dict(self) -> dict[str, Any]:
        service_account_id = str(self.service_account_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serviceAccountId": service_account_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_account_id = UUID(d.pop("serviceAccountId"))

        flr_restore_options_validation_config = cls(
            service_account_id=service_account_id,
        )

        return flr_restore_options_validation_config
