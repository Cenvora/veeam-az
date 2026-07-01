from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedWorkloadsReport")


@_attrs_define
class ProtectedWorkloadsReport:
    """
    Attributes:
        virtual_machines_total_count (int | Unset): Total number of available VMs.
        virtual_machines_protected_count (int | Unset): Total number of available VMs that got protected during the
            specified period.
        sql_databases_total_count (int | Unset): Total number of available SQL databases.
        sql_databases_protected_count (int | Unset): Total number of available SQL databases that got protected during
            the specified period.
        file_shares_total_count (int | Unset): Total number of available file shares.
        file_shares_protected_count (int | Unset): Total number of available file shares that got protected during the
            specified period.
    """

    virtual_machines_total_count: int | Unset = UNSET
    virtual_machines_protected_count: int | Unset = UNSET
    sql_databases_total_count: int | Unset = UNSET
    sql_databases_protected_count: int | Unset = UNSET
    file_shares_total_count: int | Unset = UNSET
    file_shares_protected_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_machines_total_count = self.virtual_machines_total_count

        virtual_machines_protected_count = self.virtual_machines_protected_count

        sql_databases_total_count = self.sql_databases_total_count

        sql_databases_protected_count = self.sql_databases_protected_count

        file_shares_total_count = self.file_shares_total_count

        file_shares_protected_count = self.file_shares_protected_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtual_machines_total_count is not UNSET:
            field_dict["virtualMachinesTotalCount"] = virtual_machines_total_count
        if virtual_machines_protected_count is not UNSET:
            field_dict["virtualMachinesProtectedCount"] = virtual_machines_protected_count
        if sql_databases_total_count is not UNSET:
            field_dict["sqlDatabasesTotalCount"] = sql_databases_total_count
        if sql_databases_protected_count is not UNSET:
            field_dict["sqlDatabasesProtectedCount"] = sql_databases_protected_count
        if file_shares_total_count is not UNSET:
            field_dict["fileSharesTotalCount"] = file_shares_total_count
        if file_shares_protected_count is not UNSET:
            field_dict["fileSharesProtectedCount"] = file_shares_protected_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        virtual_machines_total_count = d.pop("virtualMachinesTotalCount", UNSET)

        virtual_machines_protected_count = d.pop("virtualMachinesProtectedCount", UNSET)

        sql_databases_total_count = d.pop("sqlDatabasesTotalCount", UNSET)

        sql_databases_protected_count = d.pop("sqlDatabasesProtectedCount", UNSET)

        file_shares_total_count = d.pop("fileSharesTotalCount", UNSET)

        file_shares_protected_count = d.pop("fileSharesProtectedCount", UNSET)

        protected_workloads_report = cls(
            virtual_machines_total_count=virtual_machines_total_count,
            virtual_machines_protected_count=virtual_machines_protected_count,
            sql_databases_total_count=sql_databases_total_count,
            sql_databases_protected_count=sql_databases_protected_count,
            file_shares_total_count=file_shares_total_count,
            file_shares_protected_count=file_shares_protected_count,
        )

        protected_workloads_report.additional_properties = d
        return protected_workloads_report

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
