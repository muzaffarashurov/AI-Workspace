import os
import subprocess
import sys
from pathlib import Path

from commands.base_command import BaseCommand
from domain.command import Command
from domain.plan import Plan

# Путь к существующему, уже проверенному скрипту автоматизации.
# Скрипт живёт вне AI-Workspace (отдельный проект InvoiceAutomation),
# поэтому путь настраивается через переменную окружения.
DEFAULT_SCRIPT_PATH = "InvoiceAutomation_Console_Mode_v4.2.2_headless.py"


class SendInvoicesCommand(BaseCommand):
    """
    Обработчик команды 'Отправь накладные' (IV-001).

    Jarvis не переизобретает логику самой автоматизации — она уже
    реализована и проверена в InvoiceAutomation. Команда становится
    единой точкой входа: печатает план (из IV-001), затем запускает
    существующий скрипт как есть, с его собственным вводом данных
    и подтверждениями.
    """

    def execute(self, command: Command, plan: Plan):
        print("\n========== Отправка накладных ==========\n")
        print("План:")

        for index, step in enumerate(plan.steps, start=1):
            print(f"{index}. {step}")

        script_path = os.environ.get("INVOICE_AUTOMATION_SCRIPT", DEFAULT_SCRIPT_PATH)

        if not Path(script_path).exists():
            print(f"\nСкрипт не найден: {script_path}")
            print(
                "Укажи правильный путь через переменную окружения "
                "INVOICE_AUTOMATION_SCRIPT."
            )
            return

        print(f"\nЗапускаю {script_path} ...\n")

        # Скрипт интерактивный: сам просит вставить данные, подтвердить
        # запуск браузера и т.д. Запускаем с наследованием консоли,
        # чтобы все его подсказки и подтверждения работали как обычно.
        result = subprocess.run([sys.executable, script_path])

        if result.returncode == 0:
            print(
                "\nНакладные обработаны. Не забудь написать в "
                "Telegram-канал: 'ОК отправил'."
            )
        else:
            print(f"\nСкрипт завершился с ошибкой (код {result.returncode}).")
