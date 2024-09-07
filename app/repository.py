# app/repository.py
import json
import os
from datetime import datetime

class RecipeRepository:
    def __init__(self, storage_path="recipes"):
        # Create the directory if it doesn't exist
        self.storage_path = storage_path
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

    def save(self, title: str, ingredients: str, instructions: str) -> str:
        # Create the recipe data as a dictionary
        recipe_data = {
            "title": title,
            "ingredients": ingredients,
            "instructions": instructions,
            "created_at": datetime.now().isoformat()
        }
        # Create a filename based on the recipe title
        file_name = f"{title.replace(' ', '_').lower()}.json"
        file_path = os.path.join(self.storage_path, file_name)
        
        # Save the recipe as a JSON file on disk
        with open(file_path, "w") as json_file:
            json.dump(recipe_data, json_file, indent=4)

        return file_path
