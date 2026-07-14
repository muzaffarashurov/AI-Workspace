from dataclasses import dataclass
from enum import Enum


class Intent(Enum):
    """Поддерживаемые намерения пользователя."""

    START_WORKDAY = "START_WORKDAY"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class Command:
    """
    Команда, полученная от пользователя после анализа текста.
    """

    original_text: str
    intent: Intent