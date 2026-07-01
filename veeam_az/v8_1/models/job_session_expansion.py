from enum import Enum


class JobSessionExpansion(str, Enum):
    ALL = "All"
    CHECKEDITEMS = "CheckedItems"
    DATARETRIEVALPARAMETERS = "DataRetrievalParameters"
    GROUPEDSESSIONS = "GroupedSessions"
    LOG = "Log"
    NONE = "None"
    PROTECTEDITEMRESOURCESPARENTS = "ProtectedItemResourcesParents"
    PROTECTEDITEMS = "ProtectedItems"
    RATES = "Rates"
    RESTOREPARAMETERS = "RestoreParameters"

    def __str__(self) -> str:
        return str(self.value)
