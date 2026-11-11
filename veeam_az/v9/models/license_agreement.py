from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseAgreement")


@_attrs_define
class LicenseAgreement:
    """
    Attributes:
        checksum (None | str | Unset): Specifies the checksum for accepting terms of the license agreement.
        content (None | str | Unset): Terms of the license agreement.
        type_ (None | str | Unset): Type of the agreement.
    """

    checksum: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        checksum: None | str | Unset
        if isinstance(self.checksum, Unset):
            checksum = UNSET
        else:
            checksum = self.checksum

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if content is not UNSET:
            field_dict["content"] = content
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_checksum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checksum = _parse_checksum(d.pop("checksum", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        license_agreement = cls(
            checksum=checksum,
            content=content,
            type_=type_,
        )

        return license_agreement
