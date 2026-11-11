from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserMfaSetup")


@_attrs_define
class UserMfaSetup:
    """
    Attributes:
        recreate (bool | Unset): Defines whether you want to recreate the existing MFA secret key (*true*) or to enable
            MFA for the user (*false*).
    """

    recreate: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        recreate = self.recreate

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if recreate is not UNSET:
            field_dict["recreate"] = recreate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recreate = d.pop("recreate", UNSET)

        user_mfa_setup = cls(
            recreate=recreate,
        )

        return user_mfa_setup
