from enum import Enum


class PolicySort(str, Enum):
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    PRIORITYASC = "PriorityAsc"
    PRIORITYDESC = "PriorityDesc"
    USNASC = "UsnAsc"
    USNDESC = "UsnDesc"

    def __str__(self) -> str:
        return str(self.value)
