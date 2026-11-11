from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationRestorePointMetadata")


@_attrs_define
class ConfigurationRestorePointMetadata:
    """Information on the configuration restore point.

    Attributes:
        product_version (str): Version of the product that was installed on the backup appliance when the restore point
            was created.
        flr_version (str): Version of the File-Level Recovery Service that was running on the backup appliance.
        product_name (str): Name of the product installed on the backup appliance.
        standard_repository_count (int): Number of saved backup repositories.
        archive_repository_count (int): Number of saved archive repositories.
        vm_policy_count (int): Number of saved Azure VM schedule-based backup policies.
        sql_policy_count (int): Number of saved Azure SQL backup policies.
        file_share_policy_count (int): Number of saved Azure Files backup policies.
        cosmos_db_policy_count (int): Number of saved Cosmos DB backup policies.
        protection_policy_vm_count (int): Number of saved Azure VM SLA-based backup policies.
        service_account_count (int): Number of saved service accounts.
        repository_account_count (int): Number of saved repository accounts.
        session_count (int): Number of saved sessions.
        size (int): Size of the configuration backup file (in bytes).
        instance_id (str): Microsoft Azure ID assigned to an instance running the backup appliance for which the restore
            point was created.
        creation_time_utc (datetime.datetime | Unset): Date and time when the restore point was created.
        is_version_error (bool | Unset): Defines whether the configuration backup was completed with an error.
        version_error_message (None | str | Unset): Message of the configuration backup error.
    """

    product_version: str
    flr_version: str
    product_name: str
    standard_repository_count: int
    archive_repository_count: int
    vm_policy_count: int
    sql_policy_count: int
    file_share_policy_count: int
    cosmos_db_policy_count: int
    protection_policy_vm_count: int
    service_account_count: int
    repository_account_count: int
    session_count: int
    size: int
    instance_id: str
    creation_time_utc: datetime.datetime | Unset = UNSET
    is_version_error: bool | Unset = UNSET
    version_error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_version = self.product_version

        flr_version = self.flr_version

        product_name = self.product_name

        standard_repository_count = self.standard_repository_count

        archive_repository_count = self.archive_repository_count

        vm_policy_count = self.vm_policy_count

        sql_policy_count = self.sql_policy_count

        file_share_policy_count = self.file_share_policy_count

        cosmos_db_policy_count = self.cosmos_db_policy_count

        protection_policy_vm_count = self.protection_policy_vm_count

        service_account_count = self.service_account_count

        repository_account_count = self.repository_account_count

        session_count = self.session_count

        size = self.size

        instance_id = self.instance_id

        creation_time_utc: str | Unset = UNSET
        if not isinstance(self.creation_time_utc, Unset):
            creation_time_utc = self.creation_time_utc.isoformat()

        is_version_error = self.is_version_error

        version_error_message: None | str | Unset
        if isinstance(self.version_error_message, Unset):
            version_error_message = UNSET
        else:
            version_error_message = self.version_error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productVersion": product_version,
                "flrVersion": flr_version,
                "productName": product_name,
                "standardRepositoryCount": standard_repository_count,
                "archiveRepositoryCount": archive_repository_count,
                "vmPolicyCount": vm_policy_count,
                "sqlPolicyCount": sql_policy_count,
                "fileSharePolicyCount": file_share_policy_count,
                "cosmosDbPolicyCount": cosmos_db_policy_count,
                "protectionPolicyVmCount": protection_policy_vm_count,
                "serviceAccountCount": service_account_count,
                "repositoryAccountCount": repository_account_count,
                "sessionCount": session_count,
                "size": size,
                "instanceId": instance_id,
            }
        )
        if creation_time_utc is not UNSET:
            field_dict["creationTimeUtc"] = creation_time_utc
        if is_version_error is not UNSET:
            field_dict["isVersionError"] = is_version_error
        if version_error_message is not UNSET:
            field_dict["versionErrorMessage"] = version_error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_version = d.pop("productVersion")

        flr_version = d.pop("flrVersion")

        product_name = d.pop("productName")

        standard_repository_count = d.pop("standardRepositoryCount")

        archive_repository_count = d.pop("archiveRepositoryCount")

        vm_policy_count = d.pop("vmPolicyCount")

        sql_policy_count = d.pop("sqlPolicyCount")

        file_share_policy_count = d.pop("fileSharePolicyCount")

        cosmos_db_policy_count = d.pop("cosmosDbPolicyCount")

        protection_policy_vm_count = d.pop("protectionPolicyVmCount")

        service_account_count = d.pop("serviceAccountCount")

        repository_account_count = d.pop("repositoryAccountCount")

        session_count = d.pop("sessionCount")

        size = d.pop("size")

        instance_id = d.pop("instanceId")

        _creation_time_utc = d.pop("creationTimeUtc", UNSET)
        creation_time_utc: datetime.datetime | Unset
        if isinstance(_creation_time_utc, Unset):
            creation_time_utc = UNSET
        else:
            creation_time_utc = isoparse(_creation_time_utc)

        is_version_error = d.pop("isVersionError", UNSET)

        def _parse_version_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version_error_message = _parse_version_error_message(d.pop("versionErrorMessage", UNSET))

        configuration_restore_point_metadata = cls(
            product_version=product_version,
            flr_version=flr_version,
            product_name=product_name,
            standard_repository_count=standard_repository_count,
            archive_repository_count=archive_repository_count,
            vm_policy_count=vm_policy_count,
            sql_policy_count=sql_policy_count,
            file_share_policy_count=file_share_policy_count,
            cosmos_db_policy_count=cosmos_db_policy_count,
            protection_policy_vm_count=protection_policy_vm_count,
            service_account_count=service_account_count,
            repository_account_count=repository_account_count,
            session_count=session_count,
            size=size,
            instance_id=instance_id,
            creation_time_utc=creation_time_utc,
            is_version_error=is_version_error,
            version_error_message=version_error_message,
        )

        configuration_restore_point_metadata.additional_properties = d
        return configuration_restore_point_metadata

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
