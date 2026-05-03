class UnitConverter:
    """Клас для конвертування одиниць вимірювання довжини."""

    @staticmethod
    def meters_to_feet(meters: float) -> float:
        """Метри у фути."""
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet: float) -> float:
        """Фути у метри."""
        return feet / 3.28084

    @staticmethod
    def kilometers_to_miles(km: float) -> float:
        """Кілометри у милі."""
        return km * 0.621371

    @staticmethod
    def miles_to_kilometers(miles: float) -> float:
        """Милі у кілометри."""
        return miles / 0.621371

if __name__ == "__main__":
    dist_m = 10
    print(f"{dist_m} метрів = {UnitConverter.meters_to_feet(dist_m):.2f} футів")
    
    dist_km = 100
    print(f"{dist_km} км = {UnitConverter.kilometers_to_miles(dist_km):.2f} миль")
    
    print(f"5 миль = {UnitConverter.miles_to_kilometers(5):.2f} км")