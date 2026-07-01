from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrLink")


@_attrs_define
class FlrLink:
    """Information on a File-level recovery link.

    Attributes:
        url (None | str | Unset): URL used to open the File Level Recovery Veeam Backup browser.
        thumbprint (None | str | Unset): Thumbprint uniquely identifying a TLS certificate installed on the worker
            instance hosting the File-level recovery browser.
    """

    url: None | str | Unset = UNSET
    thumbprint: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        thumbprint: None | str | Unset
        if isinstance(self.thumbprint, Unset):
            thumbprint = UNSET
        else:
            thumbprint = self.thumbprint

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_thumbprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbprint = _parse_thumbprint(d.pop("thumbprint", UNSET))

        flr_link = cls(
            url=url,
            thumbprint=thumbprint,
        )

        return flr_link
