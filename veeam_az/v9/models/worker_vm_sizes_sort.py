from enum import Enum


class WorkerVmSizesSort(str, Enum):
    MEMORYASC = "MemoryAsc"
    MEMORYDESC = "MemoryDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    NUMBEROFCORESASC = "NumberOfCoresAsc"
    NUMBEROFCORESDESC = "NumberOfCoresDesc"

    def __str__(self) -> str:
        return str(self.value)
