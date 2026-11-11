from enum import Enum


class CosmosDbAccountType(str, Enum):
    GREMLIN = "Gremlin"
    MONGORU = "MongoRU"
    NOSQL = "NoSql"
    POSTGRESSQL = "PostgresSql"
    TABLE = "Table"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
