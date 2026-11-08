"""Модуль для отримання поточної дати та часу."""
from datetime import date, datetime, time


def get_current_date() -> date:
    """Повертає поточну (локальну) дату.

    Returns:
        Об'єкт ``datetime.date`` з поточною датою.
    """
    return datetime.now().date()


def get_current_time() -> time:
    """Повертає поточний (локальний) час без мікросекунд.

    Returns:
        Об'єкт ``datetime.time`` з поточним часом (години, хвилини, секунди).
    """
    return datetime.now().time().replace(microsecond=0)


def get_current_datetime() -> datetime:
    """Повертає поточну дату та час разом.

    Дата і час беруться з одного моменту, щоб уникнути розбіжності
    близько опівночі.

    Returns:
        Об'єкт ``datetime.datetime`` без мікросекунд.
    """
    return datetime.now().replace(microsecond=0)
