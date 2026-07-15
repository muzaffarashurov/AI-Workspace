# NEXT TASK

Полный список задач и история — в `project/BACKLOG.md`. Этот файл — короткий
указатель на текущую точку, чтобы не читать весь бэклог каждый раз.

---

## Current Sprint

Sprint 3 — Заполнение базы знаний (без кода)

---

## Current Task

3.1 — Заполнить `processes/workday/tuesday.md` реальными шагами.

Файл сейчас содержит честный TODO (не выдуманный контент). Нужны реальные
данные от пользователя: что происходит во вторник, если это не день Fast
Response Board (тот — по Пн/Ср/Пт, см. `processes/production/P001_Production_Defect_Report.md`).

---

## Definition of Done

- В `processes/workday/tuesday.md` секция `## Workflow` содержит реальные
  шаги, а не `TODO`.
- Убедиться, что `ProcessEngine.get_workflow_steps()` их корректно парсит.
- Отметить пункт 3.1 в `project/BACKLOG.md` как `[x]`.
- Добавить строку в `CHANGELOG.md`.

---

## Important

Не создавать новые документы без необходимости.

Не менять архитектуру без серьёзной причины.

Основная задача — двигаться по `project/BACKLOG.md` сверху вниз, не перескакивая
через спринты.
