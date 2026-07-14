from dataclasses import dataclass


@dataclass(frozen=True)
class Plan:
    """
    План выполнения задачи.
    """
    steps: list[str]