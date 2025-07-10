import logging
from datetime import datetime

def read_transactions(path):
    """Генератор чтения и валидации строк из transactions.log"""
    with open(path, 'r', encoding='utf-8') as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 3:
                logging.error(f"[line {lineno}] invalid format: {line!r}")
                continue
            date_str, pid, qty_str = parts
            try:
                dt = datetime.strptime(date_str, '%Y-%m-%d').date()
                qty = int(qty_str)
            except Exception as e:
                logging.error(f"[line {lineno}] parse error ({e}): {line!r}")
                continue
            yield dt, pid, qty