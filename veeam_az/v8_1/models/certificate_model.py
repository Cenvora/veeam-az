from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateModel")


@_attrs_define
class CertificateModel:
    """
    Attributes:
        thumbprint (str):
        serial_number (str):
        key_algorithm (str):
        key_size (int | None):
        subject (str):
        issued_to (str):
        issued_by (str):
        valid_from (datetime.datetime | None | Unset):
        valid_by (datetime.datetime | None | Unset):
        automatically_generated (bool | None | Unset):
    """

    thumbprint: str
    serial_number: str
    key_algorithm: str
    key_size: int | None
    subject: str
    issued_to: str
    issued_by: str
    valid_from: datetime.datetime | None | Unset = UNSET
    valid_by: datetime.datetime | None | Unset = UNSET
    automatically_generated: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thumbprint = self.thumbprint

        serial_number = self.serial_number

        key_algorithm = self.key_algorithm

        key_size: int | None
        key_size = self.key_size

        subject = self.subject

        issued_to = self.issued_to

        issued_by = self.issued_by

        valid_from: None | str | Unset
        if isinstance(self.valid_from, Unset):
            valid_from = UNSET
        elif isinstance(self.valid_from, datetime.datetime):
            valid_from = self.valid_from.isoformat()
        else:
            valid_from = self.valid_from

        valid_by: None | str | Unset
        if isinstance(self.valid_by, Unset):
            valid_by = UNSET
        elif isinstance(self.valid_by, datetime.datetime):
            valid_by = self.valid_by.isoformat()
        else:
            valid_by = self.valid_by

        automatically_generated: bool | None | Unset
        if isinstance(self.automatically_generated, Unset):
            automatically_generated = UNSET
        else:
            automatically_generated = self.automatically_generated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thumbprint": thumbprint,
                "serialNumber": serial_number,
                "keyAlgorithm": key_algorithm,
                "keySize": key_size,
                "subject": subject,
                "issuedTo": issued_to,
                "issuedBy": issued_by,
            }
        )
        if valid_from is not UNSET:
            field_dict["ValidFrom"] = valid_from
        if valid_by is not UNSET:
            field_dict["ValidBy"] = valid_by
        if automatically_generated is not UNSET:
            field_dict["AutomaticallyGenerated"] = automatically_generated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thumbprint = d.pop("thumbprint")

        serial_number = d.pop("serialNumber")

        key_algorithm = d.pop("keyAlgorithm")

        def _parse_key_size(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        key_size = _parse_key_size(d.pop("keySize"))

        subject = d.pop("subject")

        issued_to = d.pop("issuedTo")

        issued_by = d.pop("issuedBy")

        def _parse_valid_from(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_from_type_0 = isoparse(data)

                return valid_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        valid_from = _parse_valid_from(d.pop("ValidFrom", UNSET))

        def _parse_valid_by(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_by_type_0 = isoparse(data)

                return valid_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        valid_by = _parse_valid_by(d.pop("ValidBy", UNSET))

        def _parse_automatically_generated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        automatically_generated = _parse_automatically_generated(d.pop("AutomaticallyGenerated", UNSET))

        certificate_model = cls(
            thumbprint=thumbprint,
            serial_number=serial_number,
            key_algorithm=key_algorithm,
            key_size=key_size,
            subject=subject,
            issued_to=issued_to,
            issued_by=issued_by,
            valid_from=valid_from,
            valid_by=valid_by,
            automatically_generated=automatically_generated,
        )

        certificate_model.additional_properties = d
        return certificate_model

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
