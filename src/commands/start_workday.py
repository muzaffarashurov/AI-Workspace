from commands.base_command import BaseCommand
from domain.command import Command
from domain.plan import Plan


class StartWorkdayCommand(BaseCommand):
    """
    Обработчик команды 'Начни мой рабочий день'.
    """

    def execute(self, command: Command, plan: Plan):
        print("\n========== Рабочий день ==========\n")

        print("Доброе утро, Музаффар!")

        print("\nПлан на сегодня:")

        for index, step in enumerate(plan.steps, start=1):
            print(f"{index}. {step}")
