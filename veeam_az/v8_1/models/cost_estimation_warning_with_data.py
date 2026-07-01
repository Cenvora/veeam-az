from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.cost_estimation_schedule_period import CostEstimationSchedulePeriod
from ..types import UNSET, Unset

T = TypeVar("T", bound="CostEstimationWarningWithData")


@_attrs_define
class CostEstimationWarningWithData:
    """Information on each warning in the warning group.

    Attributes:
        id (None | str | Unset): System ID assigned to a warning in the Veeam Backup for Microsoft Azure REST API.
        protected_item_hash_ids (list[str] | None | Unset): Internal IDs assigned to the protected resources in the
            Veeam Backup for Microsoft Azure REST API.
        schedules (list[CostEstimationSchedulePeriod] | None | Unset): Time interval for cost estimation scheduling.
        text (None | str | Unset): Text of the warning message.
    """

    id: None | str | Unset = UNSET
    protected_item_hash_ids: list[str] | None | Unset = UNSET
    schedules: list[CostEstimationSchedulePeriod] | None | Unset = UNSET
    text: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        protected_item_hash_ids: list[str] | None | Unset
        if isinstance(self.protected_item_hash_ids, Unset):
            protected_item_hash_ids = UNSET
        elif isinstance(self.protected_item_hash_ids, list):
            protected_item_hash_ids = self.protected_item_hash_ids

        else:
            protected_item_hash_ids = self.protected_item_hash_ids

        schedules: list[str] | None | Unset
        if isinstance(self.schedules, Unset):
            schedules = UNSET
        elif isinstance(self.schedules, list):
            schedules = []
            for schedules_type_0_item_data in self.schedules:
                schedules_type_0_item = schedules_type_0_item_data.value
                schedules.append(schedules_type_0_item)

        else:
            schedules = self.schedules

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if protected_item_hash_ids is not UNSET:
            field_dict["protectedItemHashIds"] = protected_item_hash_ids
        if schedules is not UNSET:
            field_dict["schedules"] = schedules
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_protected_item_hash_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protected_item_hash_ids_type_0 = cast(list[str], data)

                return protected_item_hash_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        protected_item_hash_ids = _parse_protected_item_hash_ids(d.pop("protectedItemHashIds", UNSET))

        def _parse_schedules(data: object) -> list[CostEstimationSchedulePeriod] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                schedules_type_0 = []
                _schedules_type_0 = data
                for schedules_type_0_item_data in _schedules_type_0:
                    schedules_type_0_item = CostEstimationSchedulePeriod(schedules_type_0_item_data)

                    schedules_type_0.append(schedules_type_0_item)

                return schedules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CostEstimationSchedulePeriod] | None | Unset, data)

        schedules = _parse_schedules(d.pop("schedules", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        cost_estimation_warning_with_data = cls(
            id=id,
            protected_item_hash_ids=protected_item_hash_ids,
            schedules=schedules,
            text=text,
        )

        return cost_estimation_warning_with_data
