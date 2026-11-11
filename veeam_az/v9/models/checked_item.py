from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.job_status import JobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_resource import AzureResource
    from ..models.repository import Repository


T = TypeVar("T", bound="CheckedItem")


@_attrs_define
class CheckedItem:
    """Information on each checked resource.

    Attributes:
        id (str | Unset):
        resource (AzureResource | Unset): Information on an Azure resource.
        repository (Repository | Unset): Information on a backup repository.
        status (JobStatus | Unset): Specifies the status of the performed session.
        error (None | str | Unset): Information on an error occurred during the health check.
        total_restore_points (int | Unset): Total number of restore points used for the resource protection.
        corrupted_restore_points (int | Unset): Total number of corrupted restore points used for the resource
            protection.
    """

    id: str | Unset = UNSET
    resource: AzureResource | Unset = UNSET
    repository: Repository | Unset = UNSET
    status: JobStatus | Unset = UNSET
    error: None | str | Unset = UNSET
    total_restore_points: int | Unset = UNSET
    corrupted_restore_points: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        total_restore_points = self.total_restore_points

        corrupted_restore_points = self.corrupted_restore_points

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if resource is not UNSET:
            field_dict["resource"] = resource
        if repository is not UNSET:
            field_dict["repository"] = repository
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error
        if total_restore_points is not UNSET:
            field_dict["totalRestorePoints"] = total_restore_points
        if corrupted_restore_points is not UNSET:
            field_dict["corruptedRestorePoints"] = corrupted_restore_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_resource import AzureResource
        from ..models.repository import Repository

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _resource = d.pop("resource", UNSET)
        resource: AzureResource | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = AzureResource.from_dict(_resource)

        _repository = d.pop("repository", UNSET)
        repository: Repository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        _status = d.pop("status", UNSET)
        status: JobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobStatus(_status)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        total_restore_points = d.pop("totalRestorePoints", UNSET)

        corrupted_restore_points = d.pop("corruptedRestorePoints", UNSET)

        checked_item = cls(
            id=id,
            resource=resource,
            repository=repository,
            status=status,
            error=error,
            total_restore_points=total_restore_points,
            corrupted_restore_points=corrupted_restore_points,
        )

        return checked_item
