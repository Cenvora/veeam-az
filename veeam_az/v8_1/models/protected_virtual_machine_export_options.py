from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.data_retrieval_status import DataRetrievalStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedVirtualMachineExportOptions")


@_attrs_define
class ProtectedVirtualMachineExportOptions:
    """
    Attributes:
        virtual_machine_ids (list[str] | None | Unset): Specifies system IDs assigned in the Veeam Backup for Microsoft
            Azure REST API to protected Azure VMs information on which will be exported.
        search_pattern (None | str | Unset): Exports only data on those items of a resource collection that match the
            specified search pattern in the parameter value.
        flr_session (bool | None | Unset): Defines whether to export data on Azure VMs for which file-level recovery
            sessions are launched.
        data_retrieval_statuses (list[DataRetrievalStatus] | None | Unset): Exports only data on Azure VMs with the
            specified data retrieval status.
    """

    virtual_machine_ids: list[str] | None | Unset = UNSET
    search_pattern: None | str | Unset = UNSET
    flr_session: bool | None | Unset = UNSET
    data_retrieval_statuses: list[DataRetrievalStatus] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        virtual_machine_ids: list[str] | None | Unset
        if isinstance(self.virtual_machine_ids, Unset):
            virtual_machine_ids = UNSET
        elif isinstance(self.virtual_machine_ids, list):
            virtual_machine_ids = self.virtual_machine_ids

        else:
            virtual_machine_ids = self.virtual_machine_ids

        search_pattern: None | str | Unset
        if isinstance(self.search_pattern, Unset):
            search_pattern = UNSET
        else:
            search_pattern = self.search_pattern

        flr_session: bool | None | Unset
        if isinstance(self.flr_session, Unset):
            flr_session = UNSET
        else:
            flr_session = self.flr_session

        data_retrieval_statuses: list[str] | None | Unset
        if isinstance(self.data_retrieval_statuses, Unset):
            data_retrieval_statuses = UNSET
        elif isinstance(self.data_retrieval_statuses, list):
            data_retrieval_statuses = []
            for data_retrieval_statuses_type_0_item_data in self.data_retrieval_statuses:
                data_retrieval_statuses_type_0_item = data_retrieval_statuses_type_0_item_data.value
                data_retrieval_statuses.append(data_retrieval_statuses_type_0_item)

        else:
            data_retrieval_statuses = self.data_retrieval_statuses

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if virtual_machine_ids is not UNSET:
            field_dict["virtualMachineIds"] = virtual_machine_ids
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern
        if flr_session is not UNSET:
            field_dict["flrSession"] = flr_session
        if data_retrieval_statuses is not UNSET:
            field_dict["dataRetrievalStatuses"] = data_retrieval_statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_virtual_machine_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                virtual_machine_ids_type_0 = cast(list[str], data)

                return virtual_machine_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        virtual_machine_ids = _parse_virtual_machine_ids(d.pop("virtualMachineIds", UNSET))

        def _parse_search_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_pattern = _parse_search_pattern(d.pop("searchPattern", UNSET))

        def _parse_flr_session(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        flr_session = _parse_flr_session(d.pop("flrSession", UNSET))

        def _parse_data_retrieval_statuses(data: object) -> list[DataRetrievalStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_retrieval_statuses_type_0 = []
                _data_retrieval_statuses_type_0 = data
                for data_retrieval_statuses_type_0_item_data in _data_retrieval_statuses_type_0:
                    data_retrieval_statuses_type_0_item = DataRetrievalStatus(data_retrieval_statuses_type_0_item_data)

                    data_retrieval_statuses_type_0.append(data_retrieval_statuses_type_0_item)

                return data_retrieval_statuses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DataRetrievalStatus] | None | Unset, data)

        data_retrieval_statuses = _parse_data_retrieval_statuses(d.pop("dataRetrievalStatuses", UNSET))

        protected_virtual_machine_export_options = cls(
            virtual_machine_ids=virtual_machine_ids,
            search_pattern=search_pattern,
            flr_session=flr_session,
            data_retrieval_statuses=data_retrieval_statuses,
        )

        return protected_virtual_machine_export_options
