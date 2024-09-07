# app/routes.py
from fastapi import APIRouter
from pydantic import BaseModel
from services import RecipeService

router = APIRouter()

# Pydantic model for request body
class RecipeCreate(BaseModel):
    title: str
    ingredients: str
    instructions: str

@router.post("/recipes/")
def create_recipe(recipe: RecipeCreate):
    service = RecipeService()
    file_path = service.create_recipe(recipe.title, recipe.ingredients, recipe.instructions)
    return {"message": "Recipe saved successfully", "file_path": file_path}
