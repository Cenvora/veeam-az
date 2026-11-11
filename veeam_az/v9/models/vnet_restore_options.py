from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vnet_restore_point_restore_type import VnetRestorePointRestoreType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vnet_to_alternative_restore_options import VnetToAlternativeRestoreOptions


T = TypeVar("T", bound="VnetRestoreOptions")


@_attrs_define
class VnetRestoreOptions:
    r"""Specifies Azure network restore options.

    Attributes:
        service_account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to
            a service account whose permissions will be used to perform the operation. </br> **Note**&#58; This parameter is
            required.
        restore_type (VnetRestorePointRestoreType): Defines whether to restore the entire virtual network configuration
            to the original location, to restore the entire virtual network configuration to a custom location, or to
            restore specific virtual network configuration items to the original location. </br> **Note**&#58; This
            parameter is required.
        source_region (str): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to an
            Azure region whose network configuration items you want to restore. </br> **Note**&#58; This parameter is
            required.
        reason (str | Unset): Specifies a reason for performing the restore operation.
        resource_ids_to_restore (list[str] | None | Unset): \[Applies only if the *SelectedItems* value has been
            specified for the `VnetRestorePointRestoreType` parameter] Specifies the Azure IDs assigned to virtual network
            configuration items that will be restored.
        to_alternative (VnetToAlternativeRestoreOptions | Unset): \[Applies only if the *ToDifferent* value has been
            specified for the `VnetRestorePointRestoreType` parameter] Specifies the settings configured when restoring to a
            new location or with different settings.
    """

    service_account_id: UUID
    restore_type: VnetRestorePointRestoreType
    source_region: str
    reason: str | Unset = UNSET
    resource_ids_to_restore: list[str] | None | Unset = UNSET
    to_alternative: VnetToAlternativeRestoreOptions | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        service_account_id = str(self.service_account_id)

        restore_type = self.restore_type.value

        source_region = self.source_region

        reason = self.reason

        resource_ids_to_restore: list[str] | None | Unset
        if isinstance(self.resource_ids_to_restore, Unset):
            resource_ids_to_restore = UNSET
        elif isinstance(self.resource_ids_to_restore, list):
            resource_ids_to_restore = self.resource_ids_to_restore

        else:
            resource_ids_to_restore = self.resource_ids_to_restore

        to_alternative: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_alternative, Unset):
            to_alternative = self.to_alternative.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serviceAccountId": service_account_id,
                "restoreType": restore_type,
                "sourceRegion": source_region,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if resource_ids_to_restore is not UNSET:
            field_dict["resourceIdsToRestore"] = resource_ids_to_restore
        if to_alternative is not UNSET:
            field_dict["toAlternative"] = to_alternative

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vnet_to_alternative_restore_options import VnetToAlternativeRestoreOptions

        d = dict(src_dict)
        service_account_id = UUID(d.pop("serviceAccountId"))

        restore_type = VnetRestorePointRestoreType(d.pop("restoreType"))

        source_region = d.pop("sourceRegion")

        reason = d.pop("reason", UNSET)

        def _parse_resource_ids_to_restore(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resource_ids_to_restore_type_0 = cast(list[str], data)

                return resource_ids_to_restore_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        resource_ids_to_restore = _parse_resource_ids_to_restore(d.pop("resourceIdsToRestore", UNSET))

        _to_alternative = d.pop("toAlternative", UNSET)
        to_alternative: VnetToAlternativeRestoreOptions | Unset
        if isinstance(_to_alternative, Unset):
            to_alternative = UNSET
        else:
            to_alternative = VnetToAlternativeRestoreOptions.from_dict(_to_alternative)

        vnet_restore_options = cls(
            service_account_id=service_account_id,
            restore_type=restore_type,
            source_region=source_region,
            reason=reason,
            resource_ids_to_restore=resource_ids_to_restore,
            to_alternative=to_alternative,
        )

        return vnet_restore_options
