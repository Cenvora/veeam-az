from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenewClientSecretResult")


@_attrs_define
class RenewClientSecretResult:
    """
    Attributes:
        client_secret_expiration (datetime.datetime | Unset):
    """

    client_secret_expiration: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_secret_expiration: str | Unset = UNSET
        if not isinstance(self.client_secret_expiration, Unset):
            client_secret_expiration = self.client_secret_expiration.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if client_secret_expiration is not UNSET:
            field_dict["clientSecretExpiration"] = client_secret_expiration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _client_secret_expiration = d.pop("clientSecretExpiration", UNSET)
        client_secret_expiration: datetime.datetime | Unset
        if isinstance(_client_secret_expiration, Unset):
            client_secret_expiration = UNSET
        else:
            client_secret_expiration = isoparse(_client_secret_expiration)

        renew_client_secret_result = cls(
            client_secret_expiration=client_secret_expiration,
        )

        return renew_client_secret_result
