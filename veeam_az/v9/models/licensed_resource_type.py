from enum import Enum


class LicensedResourceType(str, Enum):
    COSMOS_DB_APACHE_GREMLIN = "Cosmos DB Apache Gremlin"
    COSMOS_DB_MONGODB = "Cosmos DB MongoDB"
    COSMOS_DB_NOSQL = "Cosmos DB NoSQL"
    COSMOS_DB_POSTGRESQL = "Cosmos DB PostgreSQL"
    COSMOS_DB_TABLE = "Cosmos DB Table"
    FILE_SHARE = "File Share"
    MANAGED_DATABASE = "Managed Database"
    MANAGED_DISK = "Managed Disk"
    SQL_MANAGED_INSTANCE = "SQL managed instance"
    SQL_SERVER = "SQL server"
    UNKNOWN = "Unknown"
    UNMANAGED_DATABASE = "Unmanaged Database"
    UNMANAGED_DISK = "Unmanaged Disk"
    VIRTUAL_MACHINE = "Virtual Machine"

    def __str__(self) -> str:
        return str(self.value)
