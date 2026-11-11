from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.data_retrieval_priority import DataRetrievalPriority
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestorePointDataRetrievalJobInfo")


@_attrs_define
class RestorePointDataRetrievalJobInfo:
    """Information on retrieved restore points.

    Attributes:
        restore_point_id (None | Unset | UUID): System ID assigned to a restore point in the Veeam Backup for Microsoft
            Azure REST API.
        sql_restore_point_id (None | Unset | UUID): System ID assigned to a SQL restore point in the Veeam Backup for
            Microsoft Azure REST API.
        cosmos_db_restore_point_id (None | Unset | UUID): System ID assigned to a Cosmos DB restore point in the Veeam
            Backup for Microsoft Azure REST API.
        initiator (None | str | Unset): Name of the user that initiated the restore operation.
        instance_name (None | str | Unset): Name of an instance running the backup appliance for which the restore point
            was created.
        days_to_keep (int | Unset): Specifies number of days to keep restore points in configuration database.
        data_retrieval_priority (DataRetrievalPriority | Unset): Specifies the priority type for the data retrieval
            operation.
    """

    restore_point_id: None | Unset | UUID = UNSET
    sql_restore_point_id: None | Unset | UUID = UNSET
    cosmos_db_restore_point_id: None | Unset | UUID = UNSET
    initiator: None | str | Unset = UNSET
    instance_name: None | str | Unset = UNSET
    days_to_keep: int | Unset = UNSET
    data_retrieval_priority: DataRetrievalPriority | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_point_id: None | str | Unset
        if isinstance(self.restore_point_id, Unset):
            restore_point_id = UNSET
        elif isinstance(self.restore_point_id, UUID):
            restore_point_id = str(self.restore_point_id)
        else:
            restore_point_id = self.restore_point_id

        sql_restore_point_id: None | str | Unset
        if isinstance(self.sql_restore_point_id, Unset):
            sql_restore_point_id = UNSET
        elif isinstance(self.sql_restore_point_id, UUID):
            sql_restore_point_id = str(self.sql_restore_point_id)
        else:
            sql_restore_point_id = self.sql_restore_point_id

        cosmos_db_restore_point_id: None | str | Unset
        if isinstance(self.cosmos_db_restore_point_id, Unset):
            cosmos_db_restore_point_id = UNSET
        elif isinstance(self.cosmos_db_restore_point_id, UUID):
            cosmos_db_restore_point_id = str(self.cosmos_db_restore_point_id)
        else:
            cosmos_db_restore_point_id = self.cosmos_db_restore_point_id

        initiator: None | str | Unset
        if isinstance(self.initiator, Unset):
            initiator = UNSET
        else:
            initiator = self.initiator

        instance_name: None | str | Unset
        if isinstance(self.instance_name, Unset):
            instance_name = UNSET
        else:
            instance_name = self.instance_name

        days_to_keep = self.days_to_keep

        data_retrieval_priority: str | Unset = UNSET
        if not isinstance(self.data_retrieval_priority, Unset):
            data_retrieval_priority = self.data_retrieval_priority.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if restore_point_id is not UNSET:
            field_dict["restorePointId"] = restore_point_id
        if sql_restore_point_id is not UNSET:
            field_dict["sqlRestorePointId"] = sql_restore_point_id
        if cosmos_db_restore_point_id is not UNSET:
            field_dict["cosmosDbRestorePointId"] = cosmos_db_restore_point_id
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name
        if days_to_keep is not UNSET:
            field_dict["daysToKeep"] = days_to_keep
        if data_retrieval_priority is not UNSET:
            field_dict["dataRetrievalPriority"] = data_retrieval_priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_restore_point_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restore_point_id_type_0 = UUID(data)

                return restore_point_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        restore_point_id = _parse_restore_point_id(d.pop("restorePointId", UNSET))

        def _parse_sql_restore_point_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sql_restore_point_id_type_0 = UUID(data)

                return sql_restore_point_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sql_restore_point_id = _parse_sql_restore_point_id(d.pop("sqlRestorePointId", UNSET))

        def _parse_cosmos_db_restore_point_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cosmos_db_restore_point_id_type_0 = UUID(data)

                return cosmos_db_restore_point_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        cosmos_db_restore_point_id = _parse_cosmos_db_restore_point_id(d.pop("cosmosDbRestorePointId", UNSET))

        def _parse_initiator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initiator = _parse_initiator(d.pop("initiator", UNSET))

        def _parse_instance_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instance_name = _parse_instance_name(d.pop("instanceName", UNSET))

        days_to_keep = d.pop("daysToKeep", UNSET)

        _data_retrieval_priority = d.pop("dataRetrievalPriority", UNSET)
        data_retrieval_priority: DataRetrievalPriority | Unset
        if isinstance(_data_retrieval_priority, Unset):
            data_retrieval_priority = UNSET
        else:
            data_retrieval_priority = DataRetrievalPriority(_data_retrieval_priority)

        restore_point_data_retrieval_job_info = cls(
            restore_point_id=restore_point_id,
            sql_restore_point_id=sql_restore_point_id,
            cosmos_db_restore_point_id=cosmos_db_restore_point_id,
            initiator=initiator,
            instance_name=instance_name,
            days_to_keep=days_to_keep,
            data_retrieval_priority=data_retrieval_priority,
        )

        return restore_point_data_retrieval_job_info
