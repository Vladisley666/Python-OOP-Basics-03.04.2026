from car import Car
from book import Book
from stadium import Stadium
from fraction import Fraction
from temp_converter import TemperatureConverter
from unit_converter import UnitConverter

def main():
    """Головна функція для демонстрації роботи всіх класів."""
    while True:
        print("\n" + "="*30)
        print("   ГОЛОВНЕ МЕНЮ ПРОЕКТУ")
        print("="*30)
        print("1. Створити об'єкт 'Автомобіль'")
        print("2. Створити об'єкт 'Книга'")
        print("3. Створити об'єкт 'Стадіон'")
        print("4. Робота з дробами (Static Method)")
        print("5. Конвертер температури (Static Method)")
        print("6. Конвертер довжини (Static Method)")
        print("0. Вихід")
        
        choice = input("\nОберіть пункт меню: ")
        
        if choice == "1":
            item = Car()
            item.input_data()
            item.display_data()
        elif choice == "2":
            item = Book()
            item.input_data()
            item.display_data()
        elif choice == "3":
            item = Stadium()
            item.input_data()
            item.display_data()
        elif choice == "4":
            f1 = Fraction(1, 2)
            f2 = Fraction(3, 4)
            print(f"Створено два дроби. Загальна кількість об'єктів: {Fraction.get_object_count()}")
        elif choice == "5":
            temp = float(input("Введіть температуру в Цельсіях: "))
            fahr = TemperatureConverter.celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {fahr}°F")
            print(f"Кількість розрахунків: {TemperatureConverter.get_calculation_count()}")
        elif choice == "6":
            meters = float(input("Введіть метри для конвертації у фути: "))
            feet = UnitConverter.meters_to_feet(meters)
            print(f"{meters} м = {feet:.2f} футів")
        elif choice == "0":
            print("Програма завершена. Гарного дня!")
            break
        else:
            print("Помилка: Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограму перервано користувачем.")