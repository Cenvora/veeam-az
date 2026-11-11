from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.repository_validation_step import RepositoryValidationStep
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_create_from_client import RepositoryCreateFromClient


T = TypeVar("T", bound="RepositoryValidationConfig")


@_attrs_define
class RepositoryValidationConfig:
    """
    Attributes:
        steps (list[RepositoryValidationStep] | None | Unset): Specifies the steps of the backup repository settings
            validation.
        repository (RepositoryCreateFromClient | Unset): Specifies information on a backup repository.
    """

    steps: list[RepositoryValidationStep] | None | Unset = UNSET
    repository: RepositoryCreateFromClient | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        steps: list[str] | None | Unset
        if isinstance(self.steps, Unset):
            steps = UNSET
        elif isinstance(self.steps, list):
            steps = []
            for steps_type_0_item_data in self.steps:
                steps_type_0_item = steps_type_0_item_data.value
                steps.append(steps_type_0_item)

        else:
            steps = self.steps

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if steps is not UNSET:
            field_dict["steps"] = steps
        if repository is not UNSET:
            field_dict["repository"] = repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_create_from_client import RepositoryCreateFromClient

        d = dict(src_dict)

        def _parse_steps(data: object) -> list[RepositoryValidationStep] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                steps_type_0 = []
                _steps_type_0 = data
                for steps_type_0_item_data in _steps_type_0:
                    steps_type_0_item = RepositoryValidationStep(steps_type_0_item_data)

                    steps_type_0.append(steps_type_0_item)

                return steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RepositoryValidationStep] | None | Unset, data)

        steps = _parse_steps(d.pop("steps", UNSET))

        _repository = d.pop("repository", UNSET)
        repository: RepositoryCreateFromClient | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = RepositoryCreateFromClient.from_dict(_repository)

        repository_validation_config = cls(
            steps=steps,
            repository=repository,
        )

        return repository_validation_config
