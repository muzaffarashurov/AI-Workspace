from domain.command import Intent
from domain.plan import Plan


class Planner:
    """
    Формирует план действий по намерению пользователя.
    """

    def build_plan(self, intent: Intent) -> Plan:

        if intent == Intent.START_WORKDAY:
            return Plan(
                steps=[
                    "Проверить Fast Response Board",
                    "Проверить новые накладные",
                    "Подготовить отчет к совещанию",
                    "Проверить рабочую почту",
                ]
            )

        return Plan(
            steps=[
                "Команда не распознана"
            ]
        )