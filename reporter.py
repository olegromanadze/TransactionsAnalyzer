import time
import functools

def timing(fn):
    """Декоратор для измерения времени выполнения функций"""
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        print(f"[{fn.__name__}] time: {end - start:.4f}s")
        return result
    return wrapper

@timing
def write_report(path, top_products, daily_totals):
    """Генерирует текстовый отчет report.txt"""
    # TODO: открыть файл и записать top-3 товара и продажи по датам
    pass
