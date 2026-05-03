from car import Car
from book import Book
from stadium import Stadium

def main():
    """Головна функція для демонстрації роботи всіх класів."""
    while True:
        print("\n" + "="*30)
        print("   ГОЛОВНЕ МЕНЮ ПРОЕКТУ")
        print("="*30)
        print("1. Створити об'єкт 'Автомобіль'")
        print("2. Створити об'єкт 'Книга'")
        print("3. Створити об'єкт 'Стадіон'")
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