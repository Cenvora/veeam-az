from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_agreement import LicenseAgreement


T = TypeVar("T", bound="LicenseAgreementResult")


@_attrs_define
class LicenseAgreementResult:
    """Information on license agreements.

    Attributes:
        license_agreements (list[LicenseAgreement] | None | Unset): Information on each license agreement.
    """

    license_agreements: list[LicenseAgreement] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        license_agreements: list[dict[str, Any]] | None | Unset
        if isinstance(self.license_agreements, Unset):
            license_agreements = UNSET
        elif isinstance(self.license_agreements, list):
            license_agreements = []
            for license_agreements_type_0_item_data in self.license_agreements:
                license_agreements_type_0_item = license_agreements_type_0_item_data.to_dict()
                license_agreements.append(license_agreements_type_0_item)

        else:
            license_agreements = self.license_agreements

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if license_agreements is not UNSET:
            field_dict["licenseAgreements"] = license_agreements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_agreement import LicenseAgreement

        d = dict(src_dict)

        def _parse_license_agreements(data: object) -> list[LicenseAgreement] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                license_agreements_type_0 = []
                _license_agreements_type_0 = data
                for license_agreements_type_0_item_data in _license_agreements_type_0:
                    license_agreements_type_0_item = LicenseAgreement.from_dict(license_agreements_type_0_item_data)

                    license_agreements_type_0.append(license_agreements_type_0_item)

                return license_agreements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LicenseAgreement] | None | Unset, data)

        license_agreements = _parse_license_agreements(d.pop("licenseAgreements", UNSET))

        license_agreement_result = cls(
            license_agreements=license_agreements,
        )

        return license_agreement_result
