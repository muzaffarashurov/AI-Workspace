from abc import ABC, abstractmethod

from domain.command import Command


class BaseCommand(ABC):
    """
    Базовый класс для всех команд системы.
    """

    @abstractmethod
    def execute(self, command: Command):
        """Выполнить команду."""
        pass