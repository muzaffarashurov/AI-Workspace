from domain.command import Command, Intent


class CommandRouter:
    """
    Преобразует текст пользователя в объект Command.
    """

    def __init__(self):
        self._commands = {
            "начни мой рабочий день": Intent.START_WORKDAY,
        }

    def parse(self, text: str) -> Command:
        normalized_text = text.strip().lower()

        intent = self._commands.get(
            normalized_text,
            Intent.UNKNOWN
        )

        return Command(
            original_text=text,
            intent=intent,
        )