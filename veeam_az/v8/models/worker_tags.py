from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.worker_tag import WorkerTag


T = TypeVar("T", bound="WorkerTags")


@_attrs_define
class WorkerTags:
    """
    Attributes:
        tags (list[WorkerTag] | None | Unset): Information on each Azure tag assigned to worker instances.
    """

    tags: list[WorkerTag] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worker_tag import WorkerTag

        d = dict(src_dict)

        def _parse_tags(data: object) -> list[WorkerTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = WorkerTag.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WorkerTag] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        worker_tags = cls(
            tags=tags,
        )

        return worker_tags
