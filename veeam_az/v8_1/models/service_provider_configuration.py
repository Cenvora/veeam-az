from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceProviderConfiguration")


@_attrs_define
class ServiceProviderConfiguration:
    """
    Attributes:
        entity_id (None | str | Unset): System ID assigned to the service provider in the Veeam Backup for Microsoft
            Azure REST API.
        assertion_consumer_url (None | str | Unset): Assertion consumer URL obtained from the service provider.
        has_certificate (bool | Unset): Defines whether the authentication is encrypted.
        certificate_thumbprint (None | str | Unset): Thumbprint uniquely identifying a certificate.
    """

    entity_id: None | str | Unset = UNSET
    assertion_consumer_url: None | str | Unset = UNSET
    has_certificate: bool | Unset = UNSET
    certificate_thumbprint: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        entity_id: None | str | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = self.entity_id

        assertion_consumer_url: None | str | Unset
        if isinstance(self.assertion_consumer_url, Unset):
            assertion_consumer_url = UNSET
        else:
            assertion_consumer_url = self.assertion_consumer_url

        has_certificate = self.has_certificate

        certificate_thumbprint: None | str | Unset
        if isinstance(self.certificate_thumbprint, Unset):
            certificate_thumbprint = UNSET
        else:
            certificate_thumbprint = self.certificate_thumbprint

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if assertion_consumer_url is not UNSET:
            field_dict["assertionConsumerUrl"] = assertion_consumer_url
        if has_certificate is not UNSET:
            field_dict["hasCertificate"] = has_certificate
        if certificate_thumbprint is not UNSET:
            field_dict["certificateThumbprint"] = certificate_thumbprint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_entity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_id = _parse_entity_id(d.pop("entityId", UNSET))

        def _parse_assertion_consumer_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assertion_consumer_url = _parse_assertion_consumer_url(d.pop("assertionConsumerUrl", UNSET))

        has_certificate = d.pop("hasCertificate", UNSET)

        def _parse_certificate_thumbprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        certificate_thumbprint = _parse_certificate_thumbprint(d.pop("certificateThumbprint", UNSET))

        service_provider_configuration = cls(
            entity_id=entity_id,
            assertion_consumer_url=assertion_consumer_url,
            has_certificate=has_certificate,
            certificate_thumbprint=certificate_thumbprint,
        )

        return service_provider_configuration
