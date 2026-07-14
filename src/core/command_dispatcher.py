from commands.start_workday import StartWorkdayCommand
from domain.command import Intent


class CommandDispatcher:
    """
    Выбирает обработчик для команды.
    """

    def __init__(self):

        self._handlers = {
            Intent.START_WORKDAY: StartWorkdayCommand(),
        }

    def dispatch(self, command):

        handler = self._handlers.get(command.intent)

        if handler is None:
            print("Команда пока не поддерживается.")
            return

        handler.execute(command)