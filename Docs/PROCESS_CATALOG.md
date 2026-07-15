# PROCESS_CATALOG

> Каталог всех рабочих процессов AI-Workspace.
> Источник: PROCESS_CATALOG_v2.0 (19 записей), загружено пользователем.

Статус: Active
Версия: 0.3

## Схема идентификаторов

| Префикс | Категория            | Папка                     |
|---------|----------------------|-----------------------------|
| WD      | Workday              | `processes/workday/`        |
| RP      | Reports / Fast Response Board | `processes/reports/` |
| IV      | Invoices             | `processes/invoices/`       |
| QL      | Quality Engineering  | `processes/quality/`        |
| MT      | Metrology            | `processes/metrology/`      |
| PN      | Production Quality   | `processes/production/`     |
| CM      | Communication        | `processes/communication/`  |
| PS      | Presentations        | `processes/presentations/`  |
| SD      | Software Development | `processes/development/`    |
| LR      | Learning             | `processes/learning/`       |
| KM      | Knowledge Management | `processes/knowledge/`      |
| AW      | AI Workspace         | `processes/workspace/`      |

## Текущие процессы

| ID     | Название                                | Файл                                                     | Статус |
|--------|-------------------------------------------|------------------------------------------------------------|--------|
| WD-001 | Рабочий день — понедельник                | `processes/workday/monday.md`                               | Draft |
| WD-002 | Рабочий день — вторник                    | `processes/workday/tuesday.md`                              | Draft, требует заполнения |
| WD-003 | Рабочий день — среда                      | `processes/workday/wednesday.md`                            | Draft |
| WD-004 | Рабочий день — четверг                    | `processes/workday/thursday.md`                             | Draft, требует заполнения |
| WD-005 | Рабочий день — пятница                    | `processes/workday/friday.md`                               | Draft |
| WD-006 | Рабочий день — суббота                    | `processes/workday/saturday.md`                             | Draft, требует заполнения |
| WD-007 | Рабочий день — воскресенье                | `processes/workday/sunday.md`                               | Draft, требует заполнения |
| PN-001 | Production Defect Report                  | `processes/production/P001_Production_Defect_Report.md`     | Active |
| QL-001 | Расследование производственного дефекта   | `processes/quality/QL-001_defect_investigation.md`          | Active |
| MT-001 | Измерение стекла (CALYPSO)                | `processes/metrology/MT-001_calypso_measurement.md`         | Active |
| MT-002 | Измерение стекла (HOLOS)                  | `processes/metrology/MT-002_holos_measurement.md`           | Active |
| IV-001 | Отправка накладных                        | `processes/invoices/IV-001_send_invoices.md`                | Active |
| RP-001 | Контроль Fast Response Board              | `processes/reports/RP-001_fast_response_board.md`           | Draft |
| CM-001 | Техническая коммуникация (BYD)            | `processes/communication/CM-001_byd_communication.md`       | Draft, требует заполнения |
| CM-002 | Техническая коммуникация (UzAuto)         | `processes/communication/CM-002_uzauto_communication.md`    | Draft, требует заполнения |
| CM-003 | Техническая коммуникация (ZEISS)          | `processes/communication/CM-003_zeiss_communication.md`     | Draft, требует заполнения |
| PS-001 | Подготовка презентаций (PowerPoint)       | `processes/presentations/PS-001_powerpoint.md`               | Draft, требует заполнения |
| SD-001 | Разработка ПО (Java)                      | `processes/development/SD-001_java.md`                       | Active |
| SD-002 | Разработка ПО (Python)                    | `processes/development/SD-002_python.md`                     | Active |
| LR-001 | Изучение AI                               | `processes/learning/LR-001_ai_learning.md`                   | Active |
| KM-001 | Управление знаниями (База знаний)         | `processes/knowledge/KM-001_knowledge_base.md`                | Active |
| AW-001 | Развитие AI Workspace                     | `processes/workspace/AW-001_ai_workspace_development.md`     | Active |

## Решения, принятые при переносе таблицы в Markdown

1. **QL-001** объединяет 5 строк исходной таблицы (One Page Report, 5 Why Analysis,
   8D Report, Containment Action, Corrective Action) — это один процесс расследования
   дефекта, документы являются его результатами, а не отдельными процессами.
2. **SD-001, SD-002, LR-001, KM-001, AW-001** оставлены с текстом "как в таблице" —
   цель/входные данные/шаги у этих 5 строк в исходнике идентичны и не были
   индивидуализированы. Это зафиксировано в поле `Notes` каждого файла.
3. **RP-001 ≠ PN-001.** Это разные процессы: PN-001 — подготовка отчёта по дефектам
   (Пн/Ср/Пт), RP-001 — ежедневный контроль доски Fast Response Board.
4. **CM-001/002/003 и PS-001** — в исходной таблице для этих строк заполнено только
   название, остальные поля пустые. Оставлены как честные заготовки (`Draft —
   требует заполнения`), содержание не придумано.

## Что дальше

Ни один из новых процессов (кроме WD-001/003/005 и, косвенно, PN-001) пока не
подключён к `Planner` — сейчас `Orchestrator` умеет выполнять только команду
"Начни мой рабочий день". Подключение остальных процессов к командам —
следующий шаг по коду, не по базе знаний.
