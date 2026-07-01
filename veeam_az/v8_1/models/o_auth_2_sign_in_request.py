from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2SignInRequest")


@_attrs_define
class OAuth2SignInRequest:
    """
    Attributes:
        error (None | str | Unset): Specifies an error returned to the authentication request.
        error_description (None | str | Unset): Specifies the error description.
        code (None | str | Unset): Specifies the code returned to the authentication request.
        state (None | str | Unset): Specifies the state returned to the authentication request.
    """

    error: None | str | Unset = UNSET
    error_description: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    state: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        error_description: None | str | Unset
        if isinstance(self.error_description, Unset):
            error_description = UNSET
        else:
            error_description = self.error_description

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if code is not UNSET:
            field_dict["code"] = code
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_error_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_description = _parse_error_description(d.pop("errorDescription", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        o_auth_2_sign_in_request = cls(
            error=error,
            error_description=error_description,
            code=code,
            state=state,
        )

        return o_auth_2_sign_in_request
