# Лабораторна робота №6. Модулі та пакети в Python (Варіант 5)

Пакет `date_time` для роботи з поточною датою та часом.

```
date_time/
├── __init__.py        # ініціалізація пакета
├── current_info.py    # get_current_date, get_current_time, get_current_datetime
└── formatting.py      # format_date_time
main.py                # головна програма
test_date_time.py      # unit-тести
requirements.txt       # сторонній пакет python-dateutil
```

## Запуск

```bash
pip install -r requirements.txt
python main.py
python -m unittest test_date_time -v
python -m pydoc date_time.formatting    # документація з docstrings
```
