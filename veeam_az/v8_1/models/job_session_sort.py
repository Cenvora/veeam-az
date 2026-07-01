from enum import Enum


class JobSessionSort(str, Enum):
    DURATIONASC = "DurationAsc"
    DURATIONDESC = "DurationDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    POLICYNAMEASC = "PolicyNameAsc"
    POLICYNAMEDESC = "PolicyNameDesc"
    REASONASC = "ReasonAsc"
    REASONDESC = "ReasonDesc"
    STARTTIMEASC = "StartTimeAsc"
    STARTTIMEDESC = "StartTimeDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"
    STOPTIMEASC = "StopTimeAsc"
    STOPTIMEDESC = "StopTimeDesc"
    TYPEASC = "TypeAsc"
    TYPEDESC = "TypeDesc"
    USNASC = "UsnAsc"
    USNDESC = "UsnDesc"

    def __str__(self) -> str:
        return str(self.value)
