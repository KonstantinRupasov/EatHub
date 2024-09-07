# app/services.py
from repository import RecipeRepository

class RecipeService:
    def __init__(self):
        # Initialize the repository
        self.repository = RecipeRepository()

    def create_recipe(self, title: str, ingredients: str, instructions: str):
        # Call the repository to save the recipe
        return self.repository.save(title, ingredients, instructions)
