from dataclasses import dataclass
from enum import Enum


class TaskStatus(Enum):
    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


@dataclass
class Task:
    """
    Внутреннее представление задачи.
    """

    task_id: str
    status: TaskStatus