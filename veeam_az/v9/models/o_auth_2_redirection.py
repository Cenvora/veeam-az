from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="OAuth2Redirection")


@_attrs_define
class OAuth2Redirection:
    """
    Attributes:
        location (str): Redirect URL that Veeam Backup for Microsoft Azure will use to authenticate against the
            necessary service.
        request_id (str): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the authentication
            request.
    """

    location: str
    request_id: str

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        request_id = self.request_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "location": location,
                "requestId": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location = d.pop("location")

        request_id = d.pop("requestId")

        o_auth_2_redirection = cls(
            location=location,
            request_id=request_id,
        )

        return o_auth_2_redirection
