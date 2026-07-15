from datetime import date

from domain.command import Intent
from domain.plan import Plan
from services.process_engine import ProcessEngine


class Planner:
    """
    Формирует план действий по намерению пользователя,
    используя описания процессов из Markdown.
    """

    # date.weekday(): Monday=0 ... Sunday=6
    WEEKDAY_PROCESS = {
        0: "Workday/monday.md",
        1: "Workday/tuesday.md",
        2: "Workday/wednesday.md",
        3: "Workday/thursday.md",
        4: "Workday/friday.md",
        5: "Workday/saturday.md",
        6: "Workday/sunday.md",
    }

    def __init__(self):
        self.process_engine = ProcessEngine()

    def build_plan(self, intent: Intent) -> Plan:
        process_name = self._resolve_process(intent)

        if process_name is None:
            return Plan(steps=["Команда не распознана"])

        steps = self.process_engine.get_workflow_steps(process_name)

        if not steps:
            return Plan(steps=["Процесс не найден или пуст"])

        return Plan(steps=steps)

    def _resolve_process(self, intent: Intent):
        if intent == Intent.START_WORKDAY:
            weekday = date.today().weekday()
            return self.WEEKDAY_PROCESS[weekday]

        return None
