from commands.start_workday import StartWorkdayCommand
from domain.command import Command, Intent
from domain.plan import Plan


class CommandDispatcher:
    """
    Выбирает обработчик для команды.
    """

    def __init__(self):

        self._handlers = {
            Intent.START_WORKDAY: StartWorkdayCommand(),
        }

    def dispatch(self, command: Command, plan: Plan) -> None:

        handler = self._handlers.get(command.intent)

        if handler is None:
            print("Команда пока не поддерживается.")
            return

        handler.execute(command, plan)