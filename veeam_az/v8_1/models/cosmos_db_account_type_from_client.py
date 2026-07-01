from enum import Enum


class CosmosDbAccountTypeFromClient(str, Enum):
    GREMLIN = "Gremlin"
    MONGORU = "MongoRU"
    NOSQL = "NoSql"
    POSTGRESSQL = "PostgresSql"
    TABLE = "Table"

    def __str__(self) -> str:
        return str(self.value)
