from collections import Counter
from datetime import date
import itertools

def filter_last_month(transactions):
    """Оставляет транзакции за последний календарный месяц"""
    # TODO: реализовать фильтрацию по дате
    for item in transactions:
        yield item


def count_products(transactions):
    """Считает общее количество проданных единиц по product_id"""
    # TODO: использовать Counter для подсчёта quantity по product_id
    return Counter()


def top_n(counter, n=3):
    """Возвращает top-n самых продаваемых товаров"""
    # TODO: вернуть counter.most_common(n)
    return []


def group_by_date(transactions):
    """Группирует транзакции по дате и считает суммарное количество"""
    # TODO: сортировка по дате и groupby
    for dt, group in itertools.groupby([], key=lambda x: x[0]):
        yield dt, 0