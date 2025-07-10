from reader import read_transactions
from analyzer import filter_last_month, count_products, top_n, group_by_date
from reporter import write_report


def main():
    """Точка входа: собирает весь конвейер"""
    # Читаем транзакции
    transactions = read_transactions('transactions.log')
    # Фильтруем за последний месяц
    recent = filter_last_month(transactions)
    # Считаем продажи по товарам
    counter = count_products(recent)
    # Берём топ-3
    top3 = top_n(counter, 3)
    # Для группировки нужно перечитать или сохранить список
    # Здесь для примера перечитать изначально
    transactions = read_transactions('transactions.log')
    recent = filter_last_month(transactions)
    daily = group_by_date(recent)
    # Пишем отчет
    write_report('report.txt', top3, daily)


if __name__ == '__main__':
    main()