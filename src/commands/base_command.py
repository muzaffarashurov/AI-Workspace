from abc import ABC, abstractmethod

from domain.command import Command
from domain.plan import Plan


class BaseCommand(ABC):
    """
    Базовый класс для всех команд системы.
    """

    @abstractmethod
    def execute(self, command: Command, plan: Plan):
        """Выполнить команду, используя уже построенный план."""
        pass