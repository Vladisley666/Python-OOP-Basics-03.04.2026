from typing import List

# Завдання 1: MVC для класу Взуття
class Shoe:
    def __init__(self, gender: str, kind: str, color: str, price: float, manufacturer: str, size: float):
        self.gender = gender
        self.kind = kind
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

class ShoeView:
    def display_shoe_details(self, shoe: Shoe):
        print("=== ДЕТАЛІ ВЗУТТЯ ===")
        print(f"Тип: {shoe.gender} {shoe.kind}")
        print(f"Колір: {shoe.color}, Розмір: {shoe.size}")
        print(f"Виробник: {shoe.manufacturer}")
        print(f"Ціна: {shoe.price} грн")
        print("-" * 20)

class ShoeController:
    def __init__(self, model: Shoe, view: ShoeView):
        self.model = model
        self.view = view

    def set_price(self, new_price: float):
        self.model.price = new_price

    def update_view(self):
        self.view.display_shoe_details(self.model)

# Завдання 2: MVC для класу Рецепт
class Recipe:
    def __init__(self, name: str, author: str, dish_type: str, description: str, video_link: str, ingredients: List[str], cuisine: str):
        self.name = name
        self.author = author
        self.dish_type = dish_type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine

class RecipeView:
    def display_recipe(self, recipe: Recipe):
        print(f"=== РЕЦЕПТ: {recipe.name.upper()} ===")
        print(f"Автор: {recipe.author} | Кухня: {recipe.cuisine}")
        print(f"Категорія: {recipe.dish_type}")
        print(f"Опис: {recipe.description}")
        print(f"Інгредієнти: {', '.join(recipe.ingredients)}")
        print(f"Відео-інструкція: {recipe.video_link}")
        print("-" * 20)

class RecipeController:
    def __init__(self, model: Recipe, view: RecipeView):
        self.model = model
        self.view = view

    def update_description(self, new_description: str):
        self.model.description = new_description

    def update_view(self):
        self.view.display_recipe(self.model)

if __name__ == "__main__":
    # Використання Завдання 1
    shoe_model = Shoe("Чоловіче", "Кросівки", "Білий", 3200.0, "Adidas", 43)
    shoe_view = ShoeView()
    shoe_controller = ShoeController(shoe_model, shoe_view)

    print("Завдання 1:")
    shoe_controller.update_view()
    shoe_controller.set_price(2999.99)
    print("Оновлено ціну:")
    shoe_controller.update_view()

    # Використання Завдання 2
    ingredients = ["Мука", "Вода", "Сіль", "Томати", "Моцарела", "Базилік"]
    recipe_model = Recipe(
        "Піца Маргарита", 
        "Луїджі", 
        "Другі страви", 
        "Класична піца", 
        "https://youtu.be/pizza", 
        ingredients, 
        "Італійська"
    )
    recipe_view = RecipeView()
    recipe_controller = RecipeController(recipe_model, recipe_view)

    print("\nЗавдання 2:")
    recipe_controller.update_view()