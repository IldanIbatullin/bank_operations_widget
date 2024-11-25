from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список транзакций по состоянию.
    :param transactions: Список словарей с данными о транзакциях.
    :param state: Статус транзакции для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей с отфильтрованными транзакциями.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список транзакций по дате.
    :param transactions: Список словарей с данными о транзакциях.
    :param descending: Параметр сортировки (по умолчанию — убывание).
    :return: Новый отсортированный список словарей.
    """
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)
