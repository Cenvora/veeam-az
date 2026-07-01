from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.o_auth_2_status import OAuth2Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamVaultSignInState")


@_attrs_define
class VeeamVaultSignInState:
    """
    Attributes:
        status (OAuth2Status): Authorization status.
        message (None | str | Unset): Authorization details.
    """

    status: OAuth2Status
    message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = OAuth2Status(d.pop("status"))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        veeam_vault_sign_in_state = cls(
            status=status,
            message=message,
        )

        return veeam_vault_sign_in_state
