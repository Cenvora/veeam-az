from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.configuration_restore_point_type import ConfigurationRestorePointType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configuration_restore_point_metadata import ConfigurationRestorePointMetadata


T = TypeVar("T", bound="ConfigurationRestorePoint")


@_attrs_define
class ConfigurationRestorePoint:
    """
    Attributes:
        id (UUID): System ID assigned to the restore point in the Veeam Backup for Microsoft Azure REST API.
        type_ (ConfigurationRestorePointType): Type of the configuration restore point.
        creation_time_utc (datetime.datetime): Date and time when the restore point was created.
        metadata (ConfigurationRestorePointMetadata): Information on the configuration restore point.
        file_name (None | str | Unset): Name of the file that will be restored.
        repository_name (None | str | Unset): Name of the repository where the restore point is stored.
        repository_id (None | Unset | UUID): System ID assigned to the repository in the Veeam Backup for Microsoft
            Azure REST API.
        immutable_till (datetime.datetime | None | Unset): Date and time when immutability will be automatically
            disabled for the restore point.
    """

    id: UUID
    type_: ConfigurationRestorePointType
    creation_time_utc: datetime.datetime
    metadata: ConfigurationRestorePointMetadata
    file_name: None | str | Unset = UNSET
    repository_name: None | str | Unset = UNSET
    repository_id: None | Unset | UUID = UNSET
    immutable_till: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_.value

        creation_time_utc = self.creation_time_utc.isoformat()

        metadata = self.metadata.to_dict()

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        repository_name: None | str | Unset
        if isinstance(self.repository_name, Unset):
            repository_name = UNSET
        else:
            repository_name = self.repository_name

        repository_id: None | str | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        elif isinstance(self.repository_id, UUID):
            repository_id = str(self.repository_id)
        else:
            repository_id = self.repository_id

        immutable_till: None | str | Unset
        if isinstance(self.immutable_till, Unset):
            immutable_till = UNSET
        elif isinstance(self.immutable_till, datetime.datetime):
            immutable_till = self.immutable_till.isoformat()
        else:
            immutable_till = self.immutable_till

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "creationTimeUtc": creation_time_utc,
                "metadata": metadata,
            }
        )
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if immutable_till is not UNSET:
            field_dict["ImmutableTill"] = immutable_till

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration_restore_point_metadata import ConfigurationRestorePointMetadata

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = ConfigurationRestorePointType(d.pop("type"))

        creation_time_utc = isoparse(d.pop("creationTimeUtc"))

        metadata = ConfigurationRestorePointMetadata.from_dict(d.pop("metadata"))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))

        def _parse_repository_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_name = _parse_repository_name(d.pop("repositoryName", UNSET))

        def _parse_repository_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_id_type_0 = UUID(data)

                return repository_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        repository_id = _parse_repository_id(d.pop("repositoryId", UNSET))

        def _parse_immutable_till(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                immutable_till_type_0 = isoparse(data)

                return immutable_till_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        immutable_till = _parse_immutable_till(d.pop("ImmutableTill", UNSET))

        configuration_restore_point = cls(
            id=id,
            type_=type_,
            creation_time_utc=creation_time_utc,
            metadata=metadata,
            file_name=file_name,
            repository_name=repository_name,
            repository_id=repository_id,
            immutable_till=immutable_till,
        )

        return configuration_restore_point
