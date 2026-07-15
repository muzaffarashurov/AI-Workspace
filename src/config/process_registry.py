"""
Реестр соответствий Intent -> файл процесса.

Вынесено из Planner отдельно, потому что по мере роста количества
процессов и команд этот словарь станет большим — не хотим раздувать
класс Planner (см. review в project/BACKLOG.md, Sprint 2 fixes).
"""

from domain.command import Intent

# date.weekday(): Monday=0 ... Sunday=6
WEEKDAY_PROCESS = {
    0: "workday/monday.md",
    1: "workday/tuesday.md",
    2: "workday/wednesday.md",
    3: "workday/thursday.md",
    4: "workday/friday.md",
    5: "workday/saturday.md",
    6: "workday/sunday.md",
}

# Обычные intent -> процесс, не зависящие от дня недели.
INTENT_PROCESS = {
    Intent.SEND_INVOICES: "invoices/IV-001_send_invoices.md",
}
