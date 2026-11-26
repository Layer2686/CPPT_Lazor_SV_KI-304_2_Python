# LAB_06 · Метеостанція

Варіант 18. Пакет потребує Python 3.11 або новішого. Для локальної роботи
й CI обрано Python 3.12. Команди нижче запускаються з каталогу `LAB_06`.

## Bash

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m kzp_lab06.cli --help
kzp-lab06 --version
python -m pytest
python -m ruff check .
python -m ruff format --check .
python -m build
python ../.github/scripts/check_wheel.py
```

## PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m kzp_lab06.cli --help
.\.venv\Scripts\kzp-lab06.exe --version
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m build
.\.venv\Scripts\python.exe ../.github/scripts/check_wheel.py
```

`--help` показує два обов’язкові шляхи і завершується з кодом 0.
`--version` друкує `0.1.0`. Запуск без аргументів дає код 2.
Скрипт перевірки wheel очікує один файл `.whl` у `dist/`.
На етапі каркаса команда з двома шляхами завершується з кодом 1
із повідомленням про стан реалізації.

## Вхідні дані

Контрольний файл [data/input.csv](data/input.csv) містить шість вимірювань.
Кодування UTF-8, роздільник — кома.

```csv
date,temperature,humidity,pressure,wind
2025-01-03,-6.5,82,1018.2,0
```

Дата записується як `YYYY-MM-DD`. Температура задана в °C, вологість у %,
тиск у гПа, вітер у м/с. Межовий запис має вітер `10.5` м/с.
Приклад екранування тексту з комою є в
[quoted-example.csv](tests/fixtures/quoted-example.csv).
