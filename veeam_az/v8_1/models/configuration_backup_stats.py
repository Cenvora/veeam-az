from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configuration_restore_product_information import ConfigurationRestoreProductInformation


T = TypeVar("T", bound="ConfigurationBackupStats")


@_attrs_define
class ConfigurationBackupStats:
    """
    Attributes:
        standard_repository_count (int): Number of backup repositories added to the Veeam Backup for Microsoft Azure
            configuration database.
        archive_repository_count (int): Number of archive repositories added to the Veeam Backup for Microsoft Azure
            configuration database.
        vm_policy_count (int): Number of Azure VM schedule-based backup policies currently present in the Veeam Backup
            for Microsoft Azure configuration database.
        sql_policy_count (int): Number of SQL backup policies currently present in the Veeam Backup for Microsoft Azure
            configuration database.
        file_share_policy_count (int): Number of File Share backup policies currently present in the Veeam Backup for
            Microsoft Azure configuration database.
        cosmos_db_policy_count (int): Number of Cosmos DB backup policies currently present in the Veeam Backup for
            Microsoft Azure configuration database.
        protection_policy_vm_count (int): Number of Azure VM SLA-based backup policies currently present in the Veeam
            Backup for Microsoft Azure configuration database.
        service_account_count (int): Number of service accounts currently present in the Veeam Backup for Microsoft
            Azure configuration database.
        session_count (int): Number of sessions saved in the Veeam Backup for Microsoft Azure configuration database.
        product_information (ConfigurationRestoreProductInformation | Unset):
        size (int | Unset): Size of the configuration backup file (in bytes).
    """

    standard_repository_count: int
    archive_repository_count: int
    vm_policy_count: int
    sql_policy_count: int
    file_share_policy_count: int
    cosmos_db_policy_count: int
    protection_policy_vm_count: int
    service_account_count: int
    session_count: int
    product_information: ConfigurationRestoreProductInformation | Unset = UNSET
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        standard_repository_count = self.standard_repository_count

        archive_repository_count = self.archive_repository_count

        vm_policy_count = self.vm_policy_count

        sql_policy_count = self.sql_policy_count

        file_share_policy_count = self.file_share_policy_count

        cosmos_db_policy_count = self.cosmos_db_policy_count

        protection_policy_vm_count = self.protection_policy_vm_count

        service_account_count = self.service_account_count

        session_count = self.session_count

        product_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_information, Unset):
            product_information = self.product_information.to_dict()

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "standardRepositoryCount": standard_repository_count,
                "archiveRepositoryCount": archive_repository_count,
                "vmPolicyCount": vm_policy_count,
                "sqlPolicyCount": sql_policy_count,
                "fileSharePolicyCount": file_share_policy_count,
                "cosmosDbPolicyCount": cosmos_db_policy_count,
                "protectionPolicyVmCount": protection_policy_vm_count,
                "serviceAccountCount": service_account_count,
                "sessionCount": session_count,
            }
        )
        if product_information is not UNSET:
            field_dict["productInformation"] = product_information
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration_restore_product_information import ConfigurationRestoreProductInformation

        d = dict(src_dict)
        standard_repository_count = d.pop("standardRepositoryCount")

        archive_repository_count = d.pop("archiveRepositoryCount")

        vm_policy_count = d.pop("vmPolicyCount")

        sql_policy_count = d.pop("sqlPolicyCount")

        file_share_policy_count = d.pop("fileSharePolicyCount")

        cosmos_db_policy_count = d.pop("cosmosDbPolicyCount")

        protection_policy_vm_count = d.pop("protectionPolicyVmCount")

        service_account_count = d.pop("serviceAccountCount")

        session_count = d.pop("sessionCount")

        _product_information = d.pop("productInformation", UNSET)
        product_information: ConfigurationRestoreProductInformation | Unset
        if isinstance(_product_information, Unset):
            product_information = UNSET
        else:
            product_information = ConfigurationRestoreProductInformation.from_dict(_product_information)

        size = d.pop("size", UNSET)

        configuration_backup_stats = cls(
            standard_repository_count=standard_repository_count,
            archive_repository_count=archive_repository_count,
            vm_policy_count=vm_policy_count,
            sql_policy_count=sql_policy_count,
            file_share_policy_count=file_share_policy_count,
            cosmos_db_policy_count=cosmos_db_policy_count,
            protection_policy_vm_count=protection_policy_vm_count,
            service_account_count=service_account_count,
            session_count=session_count,
            product_information=product_information,
            size=size,
        )

        configuration_backup_stats.additional_properties = d
        return configuration_backup_stats

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
