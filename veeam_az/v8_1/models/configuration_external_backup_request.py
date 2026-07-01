from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="ConfigurationExternalBackupRequest")


@_attrs_define
class ConfigurationExternalBackupRequest:
    """
    Attributes:
        password_hint (str | Unset):
        recovery_rec (File | Unset):
        session_key (File | Unset):
        recovery_rec_password_loss_protection (str | Unset):
    """

    password_hint: str | Unset = UNSET
    recovery_rec: File | Unset = UNSET
    session_key: File | Unset = UNSET
    recovery_rec_password_loss_protection: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password_hint = self.password_hint

        recovery_rec: FileTypes | Unset = UNSET
        if not isinstance(self.recovery_rec, Unset):
            recovery_rec = self.recovery_rec.to_tuple()

        session_key: FileTypes | Unset = UNSET
        if not isinstance(self.session_key, Unset):
            session_key = self.session_key.to_tuple()

        recovery_rec_password_loss_protection = self.recovery_rec_password_loss_protection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password_hint is not UNSET:
            field_dict["passwordHint"] = password_hint
        if recovery_rec is not UNSET:
            field_dict["recoveryRec"] = recovery_rec
        if session_key is not UNSET:
            field_dict["sessionKey"] = session_key
        if recovery_rec_password_loss_protection is not UNSET:
            field_dict["recoveryRecPasswordLossProtection"] = recovery_rec_password_loss_protection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password_hint = d.pop("passwordHint", UNSET)

        _recovery_rec = d.pop("recoveryRec", UNSET)
        recovery_rec: File | Unset
        if isinstance(_recovery_rec, Unset):
            recovery_rec = UNSET
        else:
            recovery_rec = File(payload=BytesIO(_recovery_rec))

        _session_key = d.pop("sessionKey", UNSET)
        session_key: File | Unset
        if isinstance(_session_key, Unset):
            session_key = UNSET
        else:
            session_key = File(payload=BytesIO(_session_key))

        recovery_rec_password_loss_protection = d.pop("recoveryRecPasswordLossProtection", UNSET)

        configuration_external_backup_request = cls(
            password_hint=password_hint,
            recovery_rec=recovery_rec,
            session_key=session_key,
            recovery_rec_password_loss_protection=recovery_rec_password_loss_protection,
        )

        configuration_external_backup_request.additional_properties = d
        return configuration_external_backup_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
