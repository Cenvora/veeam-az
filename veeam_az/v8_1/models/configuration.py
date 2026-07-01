from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Configuration")


@_attrs_define
class Configuration:
    """
    Attributes:
        reserved_memory_in_mb (int): TBD Memory reserved for VBAz to run without additional resources to protect
        backup_window_in_minutes (int): TBD In what time we expect all backups being done. If all backups were
            distributed equally during the day then the window would be 24 hours -> 1440 minutes. If 8 hours -> 480 minutes.
        vms_per_core_per_day (int): TBD How many VMs can be backup with one CPU core in 24 hour period
        disks_per_core_per_day (int): TBD How much disks can be backup with one CPU core in 24 hour period
        disks_gb_size_per_core_per_day (int): TBD How much disk space can be backup with one CPU core in 24 hour period
        vms_per_worker_core_per_day (int): TBD How many VMs can be backup with single CPU core for worker in 24 hour
            period
        disks_per_worker_core_per_day (int): TBD How many disks can be backup with single CPU core for worker in 24 hour
            period
        disks_gb_size_per_worker_core_per_day (int): TBD How much disk space can be backup with single CPU core for
            worker in 24 hour period
        m_bs_per_vm_per_day (float): TBD How much memory is needed for one Vm on average in 24 hour period
        m_bs_per_disk_per_day (float): TBD How much memory is needed for one disk on average in 24 hour period
        disks_gb_size_per_mb_per_day (float): TBD How much disk space can be backup per memory on average in 24 hour
            period
        resources_consumption_hard_issue_threshold (float): TBD Hard issue threshold, how much resources has to be
            consumed to consider it hard issue. Range(0.0, 1.0)
        resources_consumption_soft_issue_threshold (float): TBD Soft issue threshold, how much resources has to be
            consumed to consider it soft issue. Range(0.0, 1.0)
        number_of_backups_per_backup_window (int | Unset): TBD How many backups there will be per instance in one backup
            window.
    """

    reserved_memory_in_mb: int
    backup_window_in_minutes: int
    vms_per_core_per_day: int
    disks_per_core_per_day: int
    disks_gb_size_per_core_per_day: int
    vms_per_worker_core_per_day: int
    disks_per_worker_core_per_day: int
    disks_gb_size_per_worker_core_per_day: int
    m_bs_per_vm_per_day: float
    m_bs_per_disk_per_day: float
    disks_gb_size_per_mb_per_day: float
    resources_consumption_hard_issue_threshold: float
    resources_consumption_soft_issue_threshold: float
    number_of_backups_per_backup_window: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reserved_memory_in_mb = self.reserved_memory_in_mb

        backup_window_in_minutes = self.backup_window_in_minutes

        vms_per_core_per_day = self.vms_per_core_per_day

        disks_per_core_per_day = self.disks_per_core_per_day

        disks_gb_size_per_core_per_day = self.disks_gb_size_per_core_per_day

        vms_per_worker_core_per_day = self.vms_per_worker_core_per_day

        disks_per_worker_core_per_day = self.disks_per_worker_core_per_day

        disks_gb_size_per_worker_core_per_day = self.disks_gb_size_per_worker_core_per_day

        m_bs_per_vm_per_day = self.m_bs_per_vm_per_day

        m_bs_per_disk_per_day = self.m_bs_per_disk_per_day

        disks_gb_size_per_mb_per_day = self.disks_gb_size_per_mb_per_day

        resources_consumption_hard_issue_threshold = self.resources_consumption_hard_issue_threshold

        resources_consumption_soft_issue_threshold = self.resources_consumption_soft_issue_threshold

        number_of_backups_per_backup_window = self.number_of_backups_per_backup_window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ReservedMemoryInMB": reserved_memory_in_mb,
                "BackupWindowInMinutes": backup_window_in_minutes,
                "VmsPerCorePerDay": vms_per_core_per_day,
                "DisksPerCorePerDay": disks_per_core_per_day,
                "DisksGBSizePerCorePerDay": disks_gb_size_per_core_per_day,
                "VmsPerWorkerCorePerDay": vms_per_worker_core_per_day,
                "DisksPerWorkerCorePerDay": disks_per_worker_core_per_day,
                "DisksGBSizePerWorkerCorePerDay": disks_gb_size_per_worker_core_per_day,
                "MBsPerVmPerDay": m_bs_per_vm_per_day,
                "MBsPerDiskPerDay": m_bs_per_disk_per_day,
                "DisksGBSizePerMBPerDay": disks_gb_size_per_mb_per_day,
                "ResourcesConsumptionHardIssueThreshold": resources_consumption_hard_issue_threshold,
                "ResourcesConsumptionSoftIssueThreshold": resources_consumption_soft_issue_threshold,
            }
        )
        if number_of_backups_per_backup_window is not UNSET:
            field_dict["NumberOfBackupsPerBackupWindow"] = number_of_backups_per_backup_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reserved_memory_in_mb = d.pop("ReservedMemoryInMB")

        backup_window_in_minutes = d.pop("BackupWindowInMinutes")

        vms_per_core_per_day = d.pop("VmsPerCorePerDay")

        disks_per_core_per_day = d.pop("DisksPerCorePerDay")

        disks_gb_size_per_core_per_day = d.pop("DisksGBSizePerCorePerDay")

        vms_per_worker_core_per_day = d.pop("VmsPerWorkerCorePerDay")

        disks_per_worker_core_per_day = d.pop("DisksPerWorkerCorePerDay")

        disks_gb_size_per_worker_core_per_day = d.pop("DisksGBSizePerWorkerCorePerDay")

        m_bs_per_vm_per_day = d.pop("MBsPerVmPerDay")

        m_bs_per_disk_per_day = d.pop("MBsPerDiskPerDay")

        disks_gb_size_per_mb_per_day = d.pop("DisksGBSizePerMBPerDay")

        resources_consumption_hard_issue_threshold = d.pop("ResourcesConsumptionHardIssueThreshold")

        resources_consumption_soft_issue_threshold = d.pop("ResourcesConsumptionSoftIssueThreshold")

        number_of_backups_per_backup_window = d.pop("NumberOfBackupsPerBackupWindow", UNSET)

        configuration = cls(
            reserved_memory_in_mb=reserved_memory_in_mb,
            backup_window_in_minutes=backup_window_in_minutes,
            vms_per_core_per_day=vms_per_core_per_day,
            disks_per_core_per_day=disks_per_core_per_day,
            disks_gb_size_per_core_per_day=disks_gb_size_per_core_per_day,
            vms_per_worker_core_per_day=vms_per_worker_core_per_day,
            disks_per_worker_core_per_day=disks_per_worker_core_per_day,
            disks_gb_size_per_worker_core_per_day=disks_gb_size_per_worker_core_per_day,
            m_bs_per_vm_per_day=m_bs_per_vm_per_day,
            m_bs_per_disk_per_day=m_bs_per_disk_per_day,
            disks_gb_size_per_mb_per_day=disks_gb_size_per_mb_per_day,
            resources_consumption_hard_issue_threshold=resources_consumption_hard_issue_threshold,
            resources_consumption_soft_issue_threshold=resources_consumption_soft_issue_threshold,
            number_of_backups_per_backup_window=number_of_backups_per_backup_window,
        )

        configuration.additional_properties = d
        return configuration

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
