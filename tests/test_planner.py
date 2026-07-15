import datetime
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from domain.command import Intent
from services.planner import Planner


def test_start_workday_monday_returns_fast_response_steps():
    with patch("services.planner.date") as mock_date:
        mock_date.today.return_value = datetime.date(2026, 7, 13)  # понедельник

        plan = Planner().build_plan(Intent.START_WORKDAY)

    # Не проверяем точный текст шага — только что реальный контент
    # подтянулся, а не заглушка. Точное сравнение сломается от любой
    # правки формулировки в Markdown.
    assert "Заполнить Fast Response Board." in plan.steps
    assert len(plan.steps) >= 1


def test_start_workday_unfilled_day_returns_todo_placeholder():
    with patch("services.planner.date") as mock_date:
        mock_date.today.return_value = datetime.date(2026, 7, 14)  # вторник

        plan = Planner().build_plan(Intent.START_WORKDAY)

    assert any("TODO" in step for step in plan.steps)


def test_unknown_intent_returns_fallback_step():
    plan = Planner().build_plan(Intent.UNKNOWN)

    assert plan.steps == ["Команда не распознана"]


def test_missing_process_file_returns_fallback_instead_of_crashing():
    with patch("services.planner.WEEKDAY_PROCESS", {0: "workday/does_not_exist.md"}):
        with patch("services.planner.date") as mock_date:
            mock_date.today.return_value = datetime.date(2026, 7, 13)  # понедельник

            plan = Planner().build_plan(Intent.START_WORKDAY)

    assert plan.steps == ["Процесс не найден или пуст"]
