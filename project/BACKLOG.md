# BACKLOG

> Единый источник правды о том, что сделано и что делать дальше.
> Перед началом работы любой ИИ должен открыть этот файл и найти
> первый пункт без [x], помеченный ▶ CURRENT.
>
> Правило: одна генерация ИИ = один пункт (или явно указанная группа
> пунктов). Не браться за следующий Sprint, пока не закрыт текущий.
>
> После выполнения пункта: отметить [x] здесь, добавить запись в
> `CHANGELOG.md`, при необходимости — обновить `NEXT_TASK.md`.

---

## Sprint 1 — Hello Orchestrator (v0.1)

- [x] 1.1 Структура проекта и документация (PROJECT_MANIFEST, PROJECT_RULES, ROADMAP)
- [x] 1.2 Orchestrator, CommandRouter, TaskManager, Planner (hardcoded)
- [x] 1.3 Command-паттерн: BaseCommand, CommandDispatcher, StartWorkdayCommand
- [x] 1.4 Рабочий MVP: "начни мой рабочий день" → план → Task создаётся

## Sprint 2 — Markdown & Process Engine (v0.2)

- [x] 2.1 `ProcessEngine.get_workflow_steps()` — парсинг `## Workflow` из Markdown
- [x] 2.2 `Planner` берёт шаги из `Processes/`, хардкод убран
- [x] 2.3 Убрано дублирование плана между `Planner` и `StartWorkdayCommand`
- [x] 2.4 Weekday-routing: "начни мой рабочий день" → `Processes/Workday/{день}.md`
- [x] 2.5 `tests/test_planner.py` — 3 теста
- [x] 2.6 Импорт реального каталога процессов (19 строк из xlsx → 21 md-файл),
      ID-схема WD/RP/IV/QL/MT/PN/CM/PS/SD/LR/KM/AW, `Docs/PROCESS_CATALOG.md`

## Sprint 3 — Заполнение базы знаний (без кода)

- [ ] 3.1 Заполнить `Processes/Workday/tuesday.md` реальными шагами
- [ ] 3.2 Заполнить `Processes/Workday/thursday.md` реальными шагами
- [ ] 3.3 Заполнить `Processes/Workday/saturday.md` и `sunday.md` (или пометить нерабочими)
- [ ] 3.4 Заполнить `Processes/Communication/CM-001/002/003` (BYD/UzAuto/ZEISS)
- [ ] 3.5 Заполнить `Processes/Presentations/PS-001` (PowerPoint)

## Sprint 4 — Подключить больше команд (код)

- [ ] 4.1 Новый Intent + Command для RP-001 ("проверь Fast Response Board")
- [ ] 4.2 Новый Intent + Command для IV-001 ("проверь накладные")
- [ ] 4.3 Новый Intent + Command для QL-001 ("зарегистрируй дефект")
- [ ] 4.4 Расширить `CommandRouter`: несколько формулировок на один Intent
      (пока без NLP — просто больше строк в словаре)

## Sprint 5 — Жизненный цикл Task

- [ ] 5.1 Персистентность Task (файл/SQLite вместо счётчика в памяти)
- [ ] 5.2 Статусы Task: CREATED → IN_PROGRESS → DONE (по `Docs/orchestrator/TASK_SCHEMA.md`)
- [ ] 5.3 Лог выполнения по каждому Task

## Sprint 6 — Первая настоящая AI-интеграция

- [ ] 6.1 `integrations/anthropic.py` — минимальный рабочий враппер над Anthropic API
- [ ] 6.2 Заменить хардкод в `CommandRouter` на LLM-based intent recognition
- [ ] 6.3 `config/models.yaml` — конфиг ролей → моделей (без хардкода конкретного вендора в коде)

## Sprint 7 — Telegram (v0.3)

- [ ] 7.1 Минимальный Telegram-бот: принимает текст, пересылает в Orchestrator
- [ ] 7.2 Разворачивание/запуск бота

## Sprint 8 — Голосовой ввод (v0.3)

- [ ] 8.1 Voice-to-text на входе
- [ ] 8.2 Подключение к тому же Orchestrator (один вход, разные источники)

## Sprint 9 — Реальное выполнение работы, а не только план

- [ ] 9.1 IV-001: Orchestrator реально запускает `InvoiceAutomation_Console_Mode_v4.2.2.py`
- [ ] 9.2 MT-001/002: связать с реальным пайплайном CMM (Surface Inspector)

## Sprint 10 — v1.0: автономный AI Orchestrator

- [ ] 10.1 AI Planner — динамическое планирование, а не только чтение готового файла
- [ ] 10.2 Диспетчеризация по ролям (Programmer/Reviewer/Researcher и т.д.)
- [ ] 10.3 Полный автономный цикл выполнения без участия пользователя на каждом шаге

---

## ▶ CURRENT

Sprint 3, пункт 3.1 — заполнить `Processes/Workday/tuesday.md` реальными шагами.
