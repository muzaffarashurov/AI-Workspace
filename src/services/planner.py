from domain.command import Intent
from domain.plan import Plan
from services.process_engine import ProcessEngine


class Planner:
    """
    Формирует план действий по намерению пользователя,
    используя описания процессов из Markdown.
    """

    PROCESS_MAP = {
        Intent.START_WORKDAY: "Production/P001_Production_Defect_Report.md",
    }

    def __init__(self):
        self.process_engine = ProcessEngine()

    def build_plan(self, intent: Intent) -> Plan:
        process_name = self.PROCESS_MAP.get(intent)

        if process_name is None:
            return Plan(steps=["Команда не распознана"])

        steps = self.process_engine.get_workflow_steps(process_name)

        if not steps:
            return Plan(steps=["Процесс не найден или пуст"])

        return Plan(steps=steps)
