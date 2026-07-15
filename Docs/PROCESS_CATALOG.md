# PROCESS_CATALOG

> Каталог всех рабочих процессов AI-Workspace.
> Источник: PROCESS_CATALOG_v2.0 (19 записей), загружено пользователем.

Статус: Active
Версия: 0.3

## Схема идентификаторов

| Префикс | Категория            | Папка                     |
|---------|----------------------|-----------------------------|
| WD      | Workday              | `Processes/Workday/`        |
| RP      | Reports / Fast Response Board | `Processes/Reports/` |
| IV      | Invoices             | `Processes/Invoices/`       |
| QL      | Quality Engineering  | `Processes/Quality/`        |
| MT      | Metrology            | `Processes/Metrology/`      |
| PN      | Production Quality   | `Processes/Production/`     |
| CM      | Communication        | `Processes/Communication/`  |
| PS      | Presentations        | `Processes/Presentations/`  |
| SD      | Software Development | `Processes/Development/`    |
| LR      | Learning             | `Processes/Learning/`       |
| KM      | Knowledge Management | `Processes/Knowledge/`      |
| AW      | AI Workspace         | `Processes/Workspace/`      |

## Текущие процессы

| ID     | Название                                | Файл                                                     | Статус |
|--------|-------------------------------------------|------------------------------------------------------------|--------|
| WD-001 | Рабочий день — понедельник                | `Processes/Workday/monday.md`                               | Draft |
| WD-002 | Рабочий день — вторник                    | `Processes/Workday/tuesday.md`                              | Draft, требует заполнения |
| WD-003 | Рабочий день — среда                      | `Processes/Workday/wednesday.md`                            | Draft |
| WD-004 | Рабочий день — четверг                    | `Processes/Workday/thursday.md`                             | Draft, требует заполнения |
| WD-005 | Рабочий день — пятница                    | `Processes/Workday/friday.md`                               | Draft |
| WD-006 | Рабочий день — суббота                    | `Processes/Workday/saturday.md`                             | Draft, требует заполнения |
| WD-007 | Рабочий день — воскресенье                | `Processes/Workday/sunday.md`                               | Draft, требует заполнения |
| PN-001 | Production Defect Report                  | `Processes/Production/P001_Production_Defect_Report.md`     | Active |
| QL-001 | Расследование производственного дефекта   | `Processes/Quality/QL-001_defect_investigation.md`          | Active |
| MT-001 | Измерение стекла (CALYPSO)                | `Processes/Metrology/MT-001_calypso_measurement.md`         | Active |
| MT-002 | Измерение стекла (HOLOS)                  | `Processes/Metrology/MT-002_holos_measurement.md`           | Active |
| IV-001 | Отправка накладных                        | `Processes/Invoices/IV-001_send_invoices.md`                | Active |
| RP-001 | Контроль Fast Response Board              | `Processes/Reports/RP-001_fast_response_board.md`           | Draft |
| CM-001 | Техническая коммуникация (BYD)            | `Processes/Communication/CM-001_byd_communication.md`       | Draft, требует заполнения |
| CM-002 | Техническая коммуникация (UzAuto)         | `Processes/Communication/CM-002_uzauto_communication.md`    | Draft, требует заполнения |
| CM-003 | Техническая коммуникация (ZEISS)          | `Processes/Communication/CM-003_zeiss_communication.md`     | Draft, требует заполнения |
| PS-001 | Подготовка презентаций (PowerPoint)       | `Processes/Presentations/PS-001_powerpoint.md`               | Draft, требует заполнения |
| SD-001 | Разработка ПО (Java)                      | `Processes/Development/SD-001_java.md`                       | Active |
| SD-002 | Разработка ПО (Python)                    | `Processes/Development/SD-002_python.md`                     | Active |
| LR-001 | Изучение AI                               | `Processes/Learning/LR-001_ai_learning.md`                   | Active |
| KM-001 | Управление знаниями (База знаний)         | `Processes/Knowledge/KM-001_knowledge_base.md`                | Active |
| AW-001 | Развитие AI Workspace                     | `Processes/Workspace/AW-001_ai_workspace_development.md`     | Active |

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
