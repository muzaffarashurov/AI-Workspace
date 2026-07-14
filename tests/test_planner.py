import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from domain.command import Intent
from services.planner import Planner


def test_start_workday_returns_steps_from_process_file():
    planner = Planner()

    plan = planner.build_plan(Intent.START_WORKDAY)

    assert len(plan.steps) > 0
    assert plan.steps[0] == "Получить данные."


def test_unknown_intent_returns_fallback_step():
    planner = Planner()

    plan = planner.build_plan(Intent.UNKNOWN)

    assert plan.steps == ["Команда не распознана"]
