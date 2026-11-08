"""Пакет ``date_time`` для роботи з поточною датою та часом.

Пакет містить два модулі:

* :mod:`date_time.current_info` - отримання поточної дати та часу;
* :mod:`date_time.formatting` - форматування дати та часу у різних виглядах.

Приклад:
    >>> from date_time.current_info import get_current_date
    >>> from date_time.formatting import format_date_time
"""

__version__ = "1.0.0"
__all__ = ["current_info", "formatting"]
