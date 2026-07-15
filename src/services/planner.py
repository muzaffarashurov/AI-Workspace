from datetime import date

from config.process_registry import WEEKDAY_PROCESS
from domain.command import Intent
from domain.plan import Plan
from services.process_engine import ProcessEngine


class Planner:
    """
    Формирует план действий по намерению пользователя,
    используя описания процессов из Markdown.
    """

    def __init__(self):
        self.process_engine = ProcessEngine()

    def build_plan(self, intent: Intent) -> Plan:
        process_name = self._resolve_process(intent)

        if process_name is None:
            return Plan(steps=["Команда не распознана"])

        try:
            steps = self.process_engine.get_workflow_steps(process_name)
        except FileNotFoundError:
            return Plan(steps=["Процесс не найден или пуст"])

        if not steps:
            return Plan(steps=["Процесс не найден или пуст"])

        return Plan(steps=steps)

    def _resolve_process(self, intent: Intent):
        if intent == Intent.START_WORKDAY:
            weekday = date.today().weekday()
            return WEEKDAY_PROCESS[weekday]

        return None
