from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProblemDetailsExtensionsType0AdditionalProperty")


@_attrs_define
class ProblemDetailsExtensionsType0AdditionalProperty:
    """ """

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        problem_details_extensions_type_0_additional_property = cls()

        return problem_details_extensions_type_0_additional_property
