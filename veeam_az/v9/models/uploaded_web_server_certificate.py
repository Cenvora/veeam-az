from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadedWebServerCertificate")


@_attrs_define
class UploadedWebServerCertificate:
    """
    Attributes:
        web_server_certificate_pfx_base_64 (None | str | Unset): Specifies the new web server certificate. Example:
            data:application/octet-stream;base64,encoded certificate.
        web_server_certificate_pfx_password (None | str | Unset): Specifies the password used to protect the
            certificate. Example: certificate password.
    """

    web_server_certificate_pfx_base_64: None | str | Unset = UNSET
    web_server_certificate_pfx_password: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        web_server_certificate_pfx_base_64: None | str | Unset
        if isinstance(self.web_server_certificate_pfx_base_64, Unset):
            web_server_certificate_pfx_base_64 = UNSET
        else:
            web_server_certificate_pfx_base_64 = self.web_server_certificate_pfx_base_64

        web_server_certificate_pfx_password: None | str | Unset
        if isinstance(self.web_server_certificate_pfx_password, Unset):
            web_server_certificate_pfx_password = UNSET
        else:
            web_server_certificate_pfx_password = self.web_server_certificate_pfx_password

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if web_server_certificate_pfx_base_64 is not UNSET:
            field_dict["webServerCertificatePfxBase64"] = web_server_certificate_pfx_base_64
        if web_server_certificate_pfx_password is not UNSET:
            field_dict["webServerCertificatePfxPassword"] = web_server_certificate_pfx_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_web_server_certificate_pfx_base_64(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        web_server_certificate_pfx_base_64 = _parse_web_server_certificate_pfx_base_64(
            d.pop("webServerCertificatePfxBase64", UNSET)
        )

        def _parse_web_server_certificate_pfx_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        web_server_certificate_pfx_password = _parse_web_server_certificate_pfx_password(
            d.pop("webServerCertificatePfxPassword", UNSET)
        )

        uploaded_web_server_certificate = cls(
            web_server_certificate_pfx_base_64=web_server_certificate_pfx_base_64,
            web_server_certificate_pfx_password=web_server_certificate_pfx_password,
        )

        return uploaded_web_server_certificate
