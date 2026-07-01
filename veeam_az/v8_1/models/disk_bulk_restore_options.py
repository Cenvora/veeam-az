from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disk_bulk_restore_to_original_options import DiskBulkRestoreToOriginalOptions
    from ..models.disk_restore_options import DiskRestoreOptions


T = TypeVar("T", bound="DiskBulkRestoreOptions")


@_attrs_define
class DiskBulkRestoreOptions:
    r"""Specifies disk restore settings.

    Attributes:
        reason (str): Specifies a reason for performing the restore operation.
        service_account_id (str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST
            API to a service account whose permissions will be used to perform the restore operation. </br> **Note**&#58;
            This parameter is required.
        source_service_account_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for
            Microsoft Azure REST API to a service account whose permissions were used to perform the backup operation.
        to_original (DiskBulkRestoreToOriginalOptions | Unset): /[Applies only if restore to the original location is
            performed/] Specifies disk restore settings.
        to_alternative (list[DiskRestoreOptions] | None | Unset): \[Applies if restore is performed to a new location or
            with different settings] Specifies disk restore settings.
    """

    reason: str
    service_account_id: str | Unset = UNSET
    source_service_account_id: None | str | Unset = UNSET
    to_original: DiskBulkRestoreToOriginalOptions | Unset = UNSET
    to_alternative: list[DiskRestoreOptions] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        service_account_id = self.service_account_id

        source_service_account_id: None | str | Unset
        if isinstance(self.source_service_account_id, Unset):
            source_service_account_id = UNSET
        else:
            source_service_account_id = self.source_service_account_id

        to_original: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_original, Unset):
            to_original = self.to_original.to_dict()

        to_alternative: list[dict[str, Any]] | None | Unset
        if isinstance(self.to_alternative, Unset):
            to_alternative = UNSET
        elif isinstance(self.to_alternative, list):
            to_alternative = []
            for to_alternative_type_0_item_data in self.to_alternative:
                to_alternative_type_0_item = to_alternative_type_0_item_data.to_dict()
                to_alternative.append(to_alternative_type_0_item)

        else:
            to_alternative = self.to_alternative

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reason": reason,
            }
        )
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if source_service_account_id is not UNSET:
            field_dict["sourceServiceAccountId"] = source_service_account_id
        if to_original is not UNSET:
            field_dict["toOriginal"] = to_original
        if to_alternative is not UNSET:
            field_dict["toAlternative"] = to_alternative

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disk_bulk_restore_to_original_options import DiskBulkRestoreToOriginalOptions
        from ..models.disk_restore_options import DiskRestoreOptions

        d = dict(src_dict)
        reason = d.pop("reason")

        service_account_id = d.pop("serviceAccountId", UNSET)

        def _parse_source_service_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_service_account_id = _parse_source_service_account_id(d.pop("sourceServiceAccountId", UNSET))

        _to_original = d.pop("toOriginal", UNSET)
        to_original: DiskBulkRestoreToOriginalOptions | Unset
        if isinstance(_to_original, Unset):
            to_original = UNSET
        else:
            to_original = DiskBulkRestoreToOriginalOptions.from_dict(_to_original)

        def _parse_to_alternative(data: object) -> list[DiskRestoreOptions] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_alternative_type_0 = []
                _to_alternative_type_0 = data
                for to_alternative_type_0_item_data in _to_alternative_type_0:
                    to_alternative_type_0_item = DiskRestoreOptions.from_dict(to_alternative_type_0_item_data)

                    to_alternative_type_0.append(to_alternative_type_0_item)

                return to_alternative_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DiskRestoreOptions] | None | Unset, data)

        to_alternative = _parse_to_alternative(d.pop("toAlternative", UNSET))

        disk_bulk_restore_options = cls(
            reason=reason,
            service_account_id=service_account_id,
            source_service_account_id=source_service_account_id,
            to_original=to_original,
            to_alternative=to_alternative,
        )

        return disk_bulk_restore_options
