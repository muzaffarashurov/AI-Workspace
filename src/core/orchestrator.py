from core.command_router import CommandRouter
from core.task_manager import TaskManager
from services.planner import Planner
from core.command_dispatcher import CommandDispatcher


class Orchestrator:
    """
    Центральный координатор AI-Workspace.
    """

    def __init__(self):
        self.router = CommandRouter()
        self.task_manager = TaskManager()
        self.planner = Planner()
        self.dispatcher = CommandDispatcher()

    def start(self):
     print("=" * 45)
     print(" AI Workspace Orchestrator v0.1")
     print("=" * 45)

     text = input("\nВведите команду: ")

     command = self.router.parse(text)

     plan = self.planner.build_plan(command.intent)

     task = self.task_manager.create_task()

     print("\nКоманда распознана.")
     print(f"\nIntent: {command.intent.value}")

     print("\nПлан действий:")

     for index, step in enumerate(plan.steps, start=1):
         print(f"{index}. {step}")

     print(f"\nTask ID: {task.task_id}")
     print(f"Status : {task.status.value}")

     self.dispatcher.dispatch(command)