from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_resource import AzureResource
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="JobDeletedRestorePoint")


@_attrs_define
class JobDeletedRestorePoint:
    """
    Attributes:
        backup_size_bytes (int | None | Unset): Size of the restore point file (in bytes).
        snapshot_time (datetime.datetime | None | Unset): Date and time when the restore point was created.
        repository_id (None | str | Unset): System ID assigned in the Veeam backup for Microsoft Azure REST API to a
            backup repository where backup files are stored.
        repository_name (None | str | Unset): Name of the repository.
        resource (AzureResource | Unset): Information on an Azure resource.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    backup_size_bytes: int | None | Unset = UNSET
    snapshot_time: datetime.datetime | None | Unset = UNSET
    repository_id: None | str | Unset = UNSET
    repository_name: None | str | Unset = UNSET
    resource: AzureResource | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        backup_size_bytes: int | None | Unset
        if isinstance(self.backup_size_bytes, Unset):
            backup_size_bytes = UNSET
        else:
            backup_size_bytes = self.backup_size_bytes

        snapshot_time: None | str | Unset
        if isinstance(self.snapshot_time, Unset):
            snapshot_time = UNSET
        elif isinstance(self.snapshot_time, datetime.datetime):
            snapshot_time = self.snapshot_time.isoformat()
        else:
            snapshot_time = self.snapshot_time

        repository_id: None | str | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        else:
            repository_id = self.repository_id

        repository_name: None | str | Unset
        if isinstance(self.repository_name, Unset):
            repository_name = UNSET
        else:
            repository_name = self.repository_name

        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_size_bytes is not UNSET:
            field_dict["backupSizeBytes"] = backup_size_bytes
        if snapshot_time is not UNSET:
            field_dict["snapshotTime"] = snapshot_time
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if resource is not UNSET:
            field_dict["resource"] = resource
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_resource import AzureResource
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)

        def _parse_backup_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_size_bytes = _parse_backup_size_bytes(d.pop("backupSizeBytes", UNSET))

        def _parse_snapshot_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                snapshot_time_type_0 = isoparse(data)

                return snapshot_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        snapshot_time = _parse_snapshot_time(d.pop("snapshotTime", UNSET))

        def _parse_repository_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_id = _parse_repository_id(d.pop("repositoryId", UNSET))

        def _parse_repository_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_name = _parse_repository_name(d.pop("repositoryName", UNSET))

        _resource = d.pop("resource", UNSET)
        resource: AzureResource | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = AzureResource.from_dict(_resource)

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

        job_deleted_restore_point = cls(
            backup_size_bytes=backup_size_bytes,
            snapshot_time=snapshot_time,
            repository_id=repository_id,
            repository_name=repository_name,
            resource=resource,
            field_links=field_links,
        )

        return job_deleted_restore_point
