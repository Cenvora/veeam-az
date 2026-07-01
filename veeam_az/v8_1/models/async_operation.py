from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.job_status import JobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.problem_details import ProblemDetails


T = TypeVar("T", bound="AsyncOperation")


@_attrs_define
class AsyncOperation:
    r"""
    Attributes:
        id (UUID): System ID assigned to the session in the Veeam Backup for Microsoft Azure REST API.
        start_time (datetime.datetime): Date and time when the session started.
        status (JobStatus): Specifies the status of the performed session.
        error (ProblemDetails | Unset): \[Applies only if the session completes with an error] Information on the error.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: UUID
    start_time: datetime.datetime
    status: JobStatus
    error: ProblemDetails | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id = str(self.id)

        start_time = self.start_time.isoformat()

        status = self.status.value

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "startTime": start_time,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.problem_details import ProblemDetails

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        start_time = isoparse(d.pop("startTime"))

        status = JobStatus(d.pop("status"))

        _error = d.pop("error", UNSET)
        error: ProblemDetails | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ProblemDetails.from_dict(_error)

        def _parse_field_links(data: object) -> LinksDictionaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_links_dictionary_type_0 = LinksDictionaryType0.from_dict(data)

                return componentsschemas_links_dictionary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinksDictionaryType0 | None | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        async_operation = cls(
            id=id,
            start_time=start_time,
            status=status,
            error=error,
            field_links=field_links,
        )

        return async_operation
