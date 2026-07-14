from commands.base_command import BaseCommand
from domain.command import Command


class StartWorkdayCommand(BaseCommand):
    """
    Обработчик команды 'Начни мой рабочий день'.
    """

    def execute(self, command: Command):
        print("\n========== Рабочий день ==========\n")

        print("Доброе утро, Музаффар!")

        print("\nСегодня необходимо:")

        print("✔ Проверить Fast Response Board")
        print("✔ Проверить новые накладные")
        print("✔ Подготовить отчёт к 10:00")
        print("✔ Проверить рабочую почту")