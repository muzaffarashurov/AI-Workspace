from pathlib import Path


class ProcessEngine:
    """
    Загружает процессы проекта.
    """

    def __init__(self):
        self.process_root = Path("processes")

    def get_process(self, process_name: str):

        process_file = self.process_root / process_name

        if process_file.exists():

            return process_file.read_text(
                encoding="utf-8"
            )

        return None