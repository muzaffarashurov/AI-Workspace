import re
from pathlib import Path


class ProcessEngine:
    """
    Загружает и разбирает процессы проекта.
    """

    _STEP_PATTERN = re.compile(r"^\d+\.\s*(.+)$")

    def __init__(self):
        self.process_root = Path("Processes")

    def get_process(self, process_name: str):
        process_file = self.process_root / process_name

        if process_file.exists():

            return process_file.read_text(
                encoding="utf-8"
            )

        return None

    def get_workflow_steps(self, process_name: str) -> list[str]:
        """
        Извлекает шаги из секции '## Workflow' процесса.
        Возвращает пустой список, если процесс не найден.
        """

        content = self.get_process(process_name)

        if content is None:
            return []

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
