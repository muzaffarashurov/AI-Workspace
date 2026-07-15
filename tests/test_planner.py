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

    assert plan.steps[0] == "Заполнить Fast Response Board."
    assert len(plan.steps) == 12


def test_start_workday_unfilled_day_returns_todo_placeholder():
    with patch("services.planner.date") as mock_date:
        mock_date.today.return_value = datetime.date(2026, 7, 14)  # вторник

        plan = Planner().build_plan(Intent.START_WORKDAY)

    assert plan.steps == ["TODO: заполнить реальными шагами вторника."]


def test_unknown_intent_returns_fallback_step():
    plan = Planner().build_plan(Intent.UNKNOWN)

    assert plan.steps == ["Команда не распознана"]
