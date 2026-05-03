from typing import List
from dataclasses import dataclass

# === Завдання 1: MVC для класу Взуття ===

@dataclass
class Shoe:
    """Модель даних для взуття"""
    gender: str
    kind: str
    color: str
    price: float
    manufacturer: str
    size: float

class ShoeView:
    """Представлення для відображення даних про взуття"""
    @staticmethod
    def display_shoe_details(shoe: Shoe):
        print("\n=== ДЕТАЛІ ВЗУТТЯ ===")
        print(f"Тип: {shoe.gender} {shoe.kind}")
        print(f"Колір: {shoe.color}, Розмір: {shoe.size}")
        print(f"Виробник: {shoe.manufacturer}")
        print(f"Ціна: {shoe.price:,.2f} грн")
        print("-" * 25)

class ShoeController:
    """Контролер для керування логікою взуття"""
    def __init__(self, model: Shoe, view: ShoeView):
        self._model = model
        self._view = view

    def set_price(self, new_price: float):
        if new_price > 0:
            self._model.price = new_price
        else:
            print("Помилка: ціна повинна бути додатною.")

    def update_view(self):
        self._view.display_shoe_details(self._model)


# === Завдання 2: MVC для класу Рецепт ===

@dataclass
class Recipe:
    """Модель даних для рецепта"""
    name: str
    author: str
    dish_type: str
    description: str
    video_link: str
    ingredients: List[str]
    cuisine: str

class RecipeView:
    """Представлення для відображення рецептів"""
    @staticmethod
    def display_recipe(recipe: Recipe):
        print(f"\n=== РЕЦЕПТ: {recipe.name.upper()} ===")
        print(f"Автор: {recipe.author} | Кухня: {recipe.cuisine}")
        print(f"Категорія: {recipe.dish_type}")
        print(f"Опис: {recipe.description}")
        print(f"Інгредієнти: {', '.join(recipe.ingredients)}")
        print(f"Відео: {recipe.video_link}")
        print("-" * 30)

class RecipeController:
    """Контролер для керування рецептами"""
    def __init__(self, model: Recipe, view: RecipeView):
        self._model = model
        self._view = view

    def update_description(self, new_description: str):
        self._model.description = new_description

    def update_view(self):
        self._view.display_recipe(self._model)


# === Демонстрація роботи ===

if __name__ == "__main__":
    # Робота зі взуттям
    shoe_m = Shoe("Чоловіче", "Кросівки", "Чорний", 3500.0, "Nike", 42.5)
    shoe_c = ShoeController(shoe_m, ShoeView())
    shoe_c.update_view()

    # Робота з рецептами
    recipe_m = Recipe(
        name="Борщ",
        author="Шеф-кухар",
        dish_type="Перші страви",
        description="Традиційна українська страва.",
        video_link="https://youtu.be/example",
        ingredients=["Буряк", "М'ясо", "Капуста", "Картопля"],
        cuisine="Українська"
    )
    recipe_c = RecipeController(recipe_m, RecipeView())
    recipe_c.update_view()