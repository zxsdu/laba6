"""Головна програма: використання пакета ``date_time``.

Демонструє імпорт модулів власного пакета, модуля зі стандартної
бібліотеки (``datetime``) та стороннього пакета (``python-dateutil``,
встановленого через pip).
"""
from datetime import datetime  # стандартна бібліотека

from dateutil.relativedelta import relativedelta  # сторонній пакет (pip)

from date_time.current_info import get_current_date, get_current_time
from date_time.formatting import format_date_time


def main():
    today = get_current_date()
    now_time = get_current_time()
    moment = datetime.combine(today, now_time)

    print(f"Поточна дата: {today}")
    print(f"Поточний час: {now_time}")
    print()

    print("Різні формати дати та часу:")
    for name in ("iso", "ua", "us", "date", "time", "long", "full"):
        print(f"  {name:<5} -> {format_date_time(moment, name)}")
    print(f"  власний '%d/%m/%y' -> {format_date_time(moment, '%d/%m/%y')}")
    print()

    new_year = datetime(today.year + 1, 1, 1)
    left = relativedelta(new_year, moment)
    print(
        f"До Нового року залишилось: {left.months} міс. {left.days} дн. "
        f"{left.hours} год. {left.minutes} хв."
    )

    try:
        format_date_time(moment, "unknown")
    except ValueError as error:
        print(f"Обробка помилки: {error}")


if __name__ == "__main__":
    main()
