from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceProviderCertificate")


@_attrs_define
class ServiceProviderCertificate:
    """
    Attributes:
        certificate_pfx_base_64 (None | str | Unset): Specifies the new certificate.
        password (None | str | Unset): Specifies the password used to protect the certificate.
    """

    certificate_pfx_base_64: None | str | Unset = UNSET
    password: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        certificate_pfx_base_64: None | str | Unset
        if isinstance(self.certificate_pfx_base_64, Unset):
            certificate_pfx_base_64 = UNSET
        else:
            certificate_pfx_base_64 = self.certificate_pfx_base_64

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if certificate_pfx_base_64 is not UNSET:
            field_dict["certificatePfxBase64"] = certificate_pfx_base_64
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_certificate_pfx_base_64(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        certificate_pfx_base_64 = _parse_certificate_pfx_base_64(d.pop("certificatePfxBase64", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        service_provider_certificate = cls(
            certificate_pfx_base_64=certificate_pfx_base_64,
            password=password,
        )

        return service_provider_certificate
