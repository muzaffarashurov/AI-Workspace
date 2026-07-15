import re
from pathlib import Path


class ProcessEngine:
    """
    Загружает и разбирает процессы проекта.
    """

    _STEP_PATTERN = re.compile(r"^\d+\.\s*(.+)$")

    def __init__(self):
        # __file__ = src/services/process_engine.py
        # parents[0] = services, [1] = src, [2] = корень проекта.
        # Работает независимо от того, откуда запущен процесс
        # (python src/main.py, pytest, python -m src.main, Docker и т.д.).
        project_root = Path(__file__).resolve().parents[2]
        self.process_root = project_root / "processes"

    def get_process(self, process_name: str) -> str:
        """
        Возвращает содержимое файла процесса.
        Бросает FileNotFoundError, если файл отсутствует —
        вместо None, чтобы явно отличать "файла нет" от "файл пустой".
        """

        process_file = self.process_root / process_name

        if not process_file.exists():
            raise FileNotFoundError(f"Процесс не найден: {process_file}")

        return process_file.read_text(encoding="utf-8")

    def get_workflow_steps(self, process_name: str) -> list[str]:
        """
        Извлекает шаги из секции '## Workflow' процесса.
        Пробрасывает FileNotFoundError, если процесс не найден —
        обработка на уровне Planner.
        """

        content = self.get_process(process_name)

        steps = []
        in_workflow = False

        for raw_line in content.splitlines():
            line = raw_line.strip()

            if line.startswith("## "):
                in_workflow = line.lower() == "## workflow"
                continue

            if not in_workflow:
                continue

            if not line or line == "---":
                continue

            match = self._STEP_PATTERN.match(line)
            steps.append(match.group(1) if match else line)

        return steps
