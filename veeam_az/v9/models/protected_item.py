from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_resource import AzureResource
    from ..models.protected_item_resource_parent import ProtectedItemResourceParent
    from ..models.protected_progress import ProtectedProgress


T = TypeVar("T", bound="ProtectedItem")


@_attrs_define
class ProtectedItem:
    """
    Attributes:
        resource (AzureResource | Unset): Information on an Azure resource.
        resource_parent (ProtectedItemResourceParent | Unset): Information on an Azure resource that contains the
            protected resource (parent resource).
        runs (list[ProtectedProgress] | None | Unset): Information on the backup policy.
        success_count (int | Unset): Number of successfully completed backups.
        failure_count (int | Unset): Number of failed backup attempts.
        protected_regions_count (int | Unset): Number of protected regions.
    """

    resource: AzureResource | Unset = UNSET
    resource_parent: ProtectedItemResourceParent | Unset = UNSET
    runs: list[ProtectedProgress] | None | Unset = UNSET
    success_count: int | Unset = UNSET
    failure_count: int | Unset = UNSET
    protected_regions_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        resource_parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_parent, Unset):
            resource_parent = self.resource_parent.to_dict()

        runs: list[dict[str, Any]] | None | Unset
        if isinstance(self.runs, Unset):
            runs = UNSET
        elif isinstance(self.runs, list):
            runs = []
            for runs_type_0_item_data in self.runs:
                runs_type_0_item = runs_type_0_item_data.to_dict()
                runs.append(runs_type_0_item)

        else:
            runs = self.runs

        success_count = self.success_count

        failure_count = self.failure_count

        protected_regions_count = self.protected_regions_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resource is not UNSET:
            field_dict["resource"] = resource
        if resource_parent is not UNSET:
            field_dict["resourceParent"] = resource_parent
        if runs is not UNSET:
            field_dict["runs"] = runs
        if success_count is not UNSET:
            field_dict["successCount"] = success_count
        if failure_count is not UNSET:
            field_dict["failureCount"] = failure_count
        if protected_regions_count is not UNSET:
            field_dict["protectedRegionsCount"] = protected_regions_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_resource import AzureResource
        from ..models.protected_item_resource_parent import ProtectedItemResourceParent
        from ..models.protected_progress import ProtectedProgress

        d = dict(src_dict)
        _resource = d.pop("resource", UNSET)
        resource: AzureResource | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = AzureResource.from_dict(_resource)

        _resource_parent = d.pop("resourceParent", UNSET)
        resource_parent: ProtectedItemResourceParent | Unset
        if isinstance(_resource_parent, Unset):
            resource_parent = UNSET
        else:
            resource_parent = ProtectedItemResourceParent.from_dict(_resource_parent)

        def _parse_runs(data: object) -> list[ProtectedProgress] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                runs_type_0 = []
                _runs_type_0 = data
                for runs_type_0_item_data in _runs_type_0:
                    runs_type_0_item = ProtectedProgress.from_dict(runs_type_0_item_data)

                    runs_type_0.append(runs_type_0_item)

                return runs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProtectedProgress] | None | Unset, data)

        runs = _parse_runs(d.pop("runs", UNSET))

        success_count = d.pop("successCount", UNSET)

        failure_count = d.pop("failureCount", UNSET)

        protected_regions_count = d.pop("protectedRegionsCount", UNSET)

        protected_item = cls(
            resource=resource,
            resource_parent=resource_parent,
            runs=runs,
            success_count=success_count,
            failure_count=failure_count,
            protected_regions_count=protected_regions_count,
        )

        return protected_item
