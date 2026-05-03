class Fraction:
    """Клас для представлення математичного дробу."""
    _count = 0  # Статичне поле для підрахунку об'єктів

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        if denominator == 0:
            raise ValueError("Знаменник не може бути рівним нулю.")
        self.denominator = denominator
        Fraction._count += 1

    @staticmethod
    def get_object_count():
        """Статичний метод, що повертає кількість створених об'єктів."""
        return Fraction._count

    def display(self):
        """Виведення дробу на екран."""
        print(f"{self.numerator}/{self.denominator}")

if __name__ == "__main__":
    print(f"Початкова кількість об'єктів: {Fraction.get_object_count()}")
    
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    f3 = Fraction(5, 8)
    
    f1.display()
    f2.display()
    
    print(f"Кількість створених дробів: {Fraction.get_object_count()}")