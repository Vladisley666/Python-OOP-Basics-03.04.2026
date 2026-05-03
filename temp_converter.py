class TemperatureConverter:
    """Клас для конвертування температури."""
    _calculation_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Конвертує Цельсій у Фаренгейт."""
        TemperatureConverter._calculation_count += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Конвертує Фаренгейт у Цельсій."""
        TemperatureConverter._calculation_count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_calculation_count():
        """Повертає загальну кількість виконаних конвертацій."""
        return TemperatureConverter._calculation_count

if __name__ == "__main__":
    c = 25
    f = TemperatureConverter.celsius_to_fahrenheit(c)
    print(f"{c}°C дорівнює {f}°F")
    
    f_val = 100
    c_val = TemperatureConverter.fahrenheit_to_celsius(f_val)
    print(f"{f_val}°F дорівнює {c_val:.2f}°C")
    
    print(f"Всього операцій конвертації: {TemperatureConverter.get_calculation_count()}")