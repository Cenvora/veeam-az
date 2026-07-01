from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.smtp_server_certificate_status import SmtpServerCertificateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_model import CertificateModel


T = TypeVar("T", bound="SmtpServerStateModel")


@_attrs_define
class SmtpServerStateModel:
    """
    Attributes:
        certificate (CertificateModel | Unset):
        is_certificate_valid (bool | None | Unset):
        is_certificate_accepted (bool | None | Unset):
        certificate_status (SmtpServerCertificateStatus | Unset):
    """

    certificate: CertificateModel | Unset = UNSET
    is_certificate_valid: bool | None | Unset = UNSET
    is_certificate_accepted: bool | None | Unset = UNSET
    certificate_status: SmtpServerCertificateStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        certificate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.certificate, Unset):
            certificate = self.certificate.to_dict()

        is_certificate_valid: bool | None | Unset
        if isinstance(self.is_certificate_valid, Unset):
            is_certificate_valid = UNSET
        else:
            is_certificate_valid = self.is_certificate_valid

        is_certificate_accepted: bool | None | Unset
        if isinstance(self.is_certificate_accepted, Unset):
            is_certificate_accepted = UNSET
        else:
            is_certificate_accepted = self.is_certificate_accepted

        certificate_status: str | Unset = UNSET
        if not isinstance(self.certificate_status, Unset):
            certificate_status = self.certificate_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if is_certificate_valid is not UNSET:
            field_dict["isCertificateValid"] = is_certificate_valid
        if is_certificate_accepted is not UNSET:
            field_dict["isCertificateAccepted"] = is_certificate_accepted
        if certificate_status is not UNSET:
            field_dict["certificateStatus"] = certificate_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_model import CertificateModel

        d = dict(src_dict)
        _certificate = d.pop("certificate", UNSET)
        certificate: CertificateModel | Unset
        if isinstance(_certificate, Unset):
            certificate = UNSET
        else:
            certificate = CertificateModel.from_dict(_certificate)

        def _parse_is_certificate_valid(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_certificate_valid = _parse_is_certificate_valid(d.pop("isCertificateValid", UNSET))

        def _parse_is_certificate_accepted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_certificate_accepted = _parse_is_certificate_accepted(d.pop("isCertificateAccepted", UNSET))

        _certificate_status = d.pop("certificateStatus", UNSET)
        certificate_status: SmtpServerCertificateStatus | Unset
        if isinstance(_certificate_status, Unset):
            certificate_status = UNSET
        else:
            certificate_status = SmtpServerCertificateStatus(_certificate_status)

        smtp_server_state_model = cls(
            certificate=certificate,
            is_certificate_valid=is_certificate_valid,
            is_certificate_accepted=is_certificate_accepted,
            certificate_status=certificate_status,
        )

        return smtp_server_state_model
