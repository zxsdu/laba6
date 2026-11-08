"""Модуль для форматування дати та часу у різних виглядах."""
from datetime import datetime

MONTHS_GENITIVE = (
    "січня", "лютого", "березня", "квітня", "травня", "червня",
    "липня", "серпня", "вересня", "жовтня", "листопада", "грудня",
)
WEEKDAYS = (
    "понеділок", "вівторок", "середа", "четвер",
    "п’ятниця", "субота", "неділя",
)

#: Назви готових форматів, доступні у функції :func:`format_date_time`.
FORMATS = ("iso", "ua", "us", "date", "time", "long", "full")


def format_date_time(dt: datetime, fmt: str = "ua") -> str:
    """Форматує дату та час у вибраному вигляді.

    Args:
        dt: Об'єкт ``datetime.datetime`` для форматування.
        fmt: Назва готового формату або рядок формату ``strftime``
            (будь-який рядок, що містить символ ``%``). Готові формати:

            * ``iso``  - ``2026-11-08 14:30:05``
            * ``ua``   - ``08.11.2026 14:30``
            * ``us``   - ``11/08/2026 02:30 PM``
            * ``date`` - ``08.11.2026``
            * ``time`` - ``14:30:05``
            * ``long`` - ``8 листопада 2026 р., 14:30``
            * ``full`` - ``неділя, 8 листопада 2026 р., 14:30:05``

    Returns:
        Відформатований рядок.

    Raises:
        TypeError: якщо ``dt`` не є ``datetime`` або ``fmt`` не є рядком.
        ValueError: якщо ``fmt`` - невідома назва формату.
    """
    if not isinstance(dt, datetime):
        raise TypeError(
            f"dt має бути datetime, отримано {type(dt).__name__}"
        )
    if not isinstance(fmt, str):
        raise TypeError(
            f"fmt має бути рядком, отримано {type(fmt).__name__}"
        )

    month = MONTHS_GENITIVE[dt.month - 1]
    if fmt == "iso":
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    if fmt == "ua":
        return dt.strftime("%d.%m.%Y %H:%M")
    if fmt == "us":
        return dt.strftime("%m/%d/%Y %I:%M %p")
    if fmt == "date":
        return dt.strftime("%d.%m.%Y")
    if fmt == "time":
        return dt.strftime("%H:%M:%S")
    if fmt == "long":
        return f"{dt.day} {month} {dt.year} р., {dt:%H:%M}"
    if fmt == "full":
        weekday = WEEKDAYS[dt.weekday()]
        return f"{weekday}, {dt.day} {month} {dt.year} р., {dt:%H:%M:%S}"
    if "%" in fmt:
        return dt.strftime(fmt)
    raise ValueError(
        f"Невідомий формат '{fmt}'. Доступні: {', '.join(FORMATS)} "
        "або рядок strftime, наприклад '%d/%m/%y'"
    )
