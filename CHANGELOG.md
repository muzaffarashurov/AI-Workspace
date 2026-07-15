# CHANGELOG

Формат: что реально изменилось, коротко. Дата = сессия работы, не обязательно
дата коммита. Полный список задач и статус — в `project/BACKLOG.md`.

## v0.2.1 — Code review fixes

- `ProcessEngine.process_root` теперь строится через `Path(__file__).resolve()`,
  а не относительно текущей директории — работает из `pytest`, `python -m src.main`,
  Docker и т.д.
- Каталог `processes/` (и все подпапки) переведён в единый нижний регистр —
  устраняет риск поломки на Linux при разном регистре.
- `ProcessEngine.get_process()` бросает `FileNotFoundError` вместо `None`.
  `Planner` ловит исключение и возвращает понятный fallback-план.
- `WEEKDAY_PROCESS` вынесен из `Planner` в `src/config/process_registry.py`.
- `CommandDispatcher.dispatch()` типизирован (`Command`, `Plan`, `-> None`).
- Тесты избавлены от хрупких точных сравнений (`in` вместо `==` там, где важен
  факт наличия шага, а не точная формулировка); добавлен тест на
  `FileNotFoundError`.

## v0.2 — Markdown & Process Engine

- Добавлен `ProcessEngine.get_workflow_steps()` — парсинг шагов из `## Workflow`.
- `Planner` перестал использовать хардкод, берёт шаги из `processes/`.
- Убрано дублирование плана между `Planner` и `StartWorkdayCommand`.
- "Начни мой рабочий день" стал weekday-aware (`processes/workday/{день}.md`).
- Добавлены тесты: `tests/test_planner.py`.
- Импортирован реальный каталог процессов из `PROCESS_CATALOG_v2_0_222.xlsx`
  (19 строк → 21 md-файл), введена ID-схема категорий, обновлён
  `Docs/PROCESS_CATALOG.md` и `Templates/PROCESS_TEMPLATE.md`.
- Создан `project/BACKLOG.md` — единый список задач от начала до v1.0.

## v0.1 — Hello Orchestrator

- Базовая архитектура: `Orchestrator`, `CommandRouter`, `TaskManager`, `Planner`.
- Command-паттерн: `BaseCommand`, `CommandDispatcher`, `StartWorkdayCommand`.
- Первая рабочая команда: "начни мой рабочий день" → план (хардкод) → Task.
