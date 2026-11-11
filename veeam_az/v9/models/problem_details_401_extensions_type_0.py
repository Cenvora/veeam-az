from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProblemDetails401ExtensionsType0")


@_attrs_define
class ProblemDetails401ExtensionsType0:
    """Additional information on the error."""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        problem_details_401_extensions_type_0 = cls()

        return problem_details_401_extensions_type_0
