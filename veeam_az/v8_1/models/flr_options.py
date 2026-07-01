from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrOptions")


@_attrs_define
class FlrOptions:
    """
    Attributes:
        reason (None | str | Unset): Specifies a reason for performing the restore operation.
        service_account_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft
            Azure to a service account whose permissions will be used to restore data to the original location. If not
            provided, only download option will be available for the user.
        flr_rto (bool | Unset): Defines whether to restore data to the original location.
    """

    reason: None | str | Unset = UNSET
    service_account_id: None | str | Unset = UNSET
    flr_rto: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        service_account_id: None | str | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        else:
            service_account_id = self.service_account_id

        flr_rto = self.flr_rto

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if flr_rto is not UNSET:
            field_dict["flrRto"] = flr_rto

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_service_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_account_id = _parse_service_account_id(d.pop("serviceAccountId", UNSET))

        flr_rto = d.pop("flrRto", UNSET)

        flr_options = cls(
            reason=reason,
            service_account_id=service_account_id,
            flr_rto=flr_rto,
        )

        return flr_options
