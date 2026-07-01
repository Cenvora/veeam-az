from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.restore_config_parameters import RestoreConfigParameters


T = TypeVar("T", bound="RestoreSessionParameters")


@_attrs_define
class RestoreSessionParameters:
    """
    Attributes:
        initiator (None | str | Unset):
        reason (None | str | Unset):
        source_vm_name (None | str | Unset):
        backup_policy_display_name (None | str | Unset):
        restore_point_created_date_utc (datetime.datetime | None | Unset):
        config_parameters (RestoreConfigParameters | Unset):
    """

    initiator: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    source_vm_name: None | str | Unset = UNSET
    backup_policy_display_name: None | str | Unset = UNSET
    restore_point_created_date_utc: datetime.datetime | None | Unset = UNSET
    config_parameters: RestoreConfigParameters | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        initiator: None | str | Unset
        if isinstance(self.initiator, Unset):
            initiator = UNSET
        else:
            initiator = self.initiator

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        source_vm_name: None | str | Unset
        if isinstance(self.source_vm_name, Unset):
            source_vm_name = UNSET
        else:
            source_vm_name = self.source_vm_name

        backup_policy_display_name: None | str | Unset
        if isinstance(self.backup_policy_display_name, Unset):
            backup_policy_display_name = UNSET
        else:
            backup_policy_display_name = self.backup_policy_display_name

        restore_point_created_date_utc: None | str | Unset
        if isinstance(self.restore_point_created_date_utc, Unset):
            restore_point_created_date_utc = UNSET
        elif isinstance(self.restore_point_created_date_utc, datetime.datetime):
            restore_point_created_date_utc = self.restore_point_created_date_utc.isoformat()
        else:
            restore_point_created_date_utc = self.restore_point_created_date_utc

        config_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config_parameters, Unset):
            config_parameters = self.config_parameters.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if reason is not UNSET:
            field_dict["reason"] = reason
        if source_vm_name is not UNSET:
            field_dict["sourceVmName"] = source_vm_name
        if backup_policy_display_name is not UNSET:
            field_dict["backupPolicyDisplayName"] = backup_policy_display_name
        if restore_point_created_date_utc is not UNSET:
            field_dict["restorePointCreatedDateUtc"] = restore_point_created_date_utc
        if config_parameters is not UNSET:
            field_dict["configParameters"] = config_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.restore_config_parameters import RestoreConfigParameters

        d = dict(src_dict)

        def _parse_initiator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initiator = _parse_initiator(d.pop("initiator", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_source_vm_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_vm_name = _parse_source_vm_name(d.pop("sourceVmName", UNSET))

        def _parse_backup_policy_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_policy_display_name = _parse_backup_policy_display_name(d.pop("backupPolicyDisplayName", UNSET))

        def _parse_restore_point_created_date_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restore_point_created_date_utc_type_0 = isoparse(data)

                return restore_point_created_date_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        restore_point_created_date_utc = _parse_restore_point_created_date_utc(
            d.pop("restorePointCreatedDateUtc", UNSET)
        )

        _config_parameters = d.pop("configParameters", UNSET)
        config_parameters: RestoreConfigParameters | Unset
        if isinstance(_config_parameters, Unset):
            config_parameters = UNSET
        else:
            config_parameters = RestoreConfigParameters.from_dict(_config_parameters)

        restore_session_parameters = cls(
            initiator=initiator,
            reason=reason,
            source_vm_name=source_vm_name,
            backup_policy_display_name=backup_policy_display_name,
            restore_point_created_date_utc=restore_point_created_date_utc,
            config_parameters=config_parameters,
        )

        return restore_session_parameters
