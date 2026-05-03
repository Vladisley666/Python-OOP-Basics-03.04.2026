import time
from functools import wraps
from typing import List, Dict, Any

# Завдання 1 та 2: Пошук простих чисел та декоратор підрахунку часу
def execution_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Час виконання функції '{func.__name__}': {duration:.6f} секунд.")
        return result
    return wrapper

@execution_timer
def get_primes(start: int = 0, end: int = 1000) -> List[int]:
    primes = []
    for num in range(max(2, start), end + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Завдання 3: Фінансова звітність для різних установ
def tax_office_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return f"--- ЗВІТ ДЛЯ ПОДАТКОВОЇ ---\nКомпанія: {data['company']}\nДохід: {data['revenue']}грн\nПодаток (18%): {data['revenue'] * 0.18}грн\n------------------------"
    return wrapper

def bank_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        status = "Кредитоспроможний" if data['revenue'] > 500000 else "Ризикований"
        return f"[БАНКІВСЬКА ВИПИСКА]\nОрганізація: {data['company']}\nЧистий прибуток: {data['revenue']}\nСтатус: {status}"
    return wrapper

def get_financial_data():
    # Базова функція, що повертає «сирі» дані
    return {
        "company": "Tech Solutions LLC",
        "revenue": 750000,
        "year": 2023
    }

if __name__ == "__main__":
    # Демонстрація Завдань 1 та 2
    print("--- Завдання 1 та 2 ---")
    primes_0_1000 = get_primes(0, 1000)
    print(f"Знайдено {len(primes_0_1000)} простих чисел.")
    # print(primes_0_1000) # Можна розкоментувати для перегляду чисел

    print("\nПошук у кастомному діапазоні (500 - 2000):")
    primes_custom = get_primes(500, 2000)

    # Демонстрація Завдання 3
    print("\n--- Завдання 3 ---")
    
    # Динамічне застосування декораторів
    report_for_tax = tax_office_decorator(get_financial_data)
    report_for_bank = bank_decorator(get_financial_data)

    print(report_for_tax())
    print("\n")
    print(report_for_bank())