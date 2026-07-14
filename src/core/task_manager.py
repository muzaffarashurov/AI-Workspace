from itertools import count

from domain.task import Task, TaskStatus


class TaskManager:
    """
    Создаёт и регистрирует задачи.
    """

    _counter = count(1)

    def create_task(self) -> Task:
        task_number = next(self._counter)

        return Task(
            task_id=f"TASK-{task_number:06d}",
            status=TaskStatus.CREATED,
        )