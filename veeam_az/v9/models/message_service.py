from enum import Enum


class MessageService(str, Enum):
    QUEUESTORAGE = "QueueStorage"
    SERVICEBUS = "ServiceBus"

    def __str__(self) -> str:
        return str(self.value)
