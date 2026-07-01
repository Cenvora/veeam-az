from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.o_auth_2_status import OAuth2Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2SignInState")


@_attrs_define
class OAuth2SignInState:
    """
    Attributes:
        status (OAuth2Status): Authorization status.
        credentials_id (None | Unset | UUID): Specifies credentials of OAuth2 account.
        message (None | str | Unset): Specifies credentials of OAuth2 account status message.
    """

    status: OAuth2Status
    credentials_id: None | Unset | UUID = UNSET
    message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        credentials_id: None | str | Unset
        if isinstance(self.credentials_id, Unset):
            credentials_id = UNSET
        elif isinstance(self.credentials_id, UUID):
            credentials_id = str(self.credentials_id)
        else:
            credentials_id = self.credentials_id

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
        if credentials_id is not UNSET:
            field_dict["credentialsId"] = credentials_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = OAuth2Status(d.pop("status"))

        def _parse_credentials_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credentials_id_type_0 = UUID(data)

                return credentials_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        credentials_id = _parse_credentials_id(d.pop("credentialsId", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        o_auth_2_sign_in_state = cls(
            status=status,
            credentials_id=credentials_id,
            message=message,
        )

        return o_auth_2_sign_in_state
