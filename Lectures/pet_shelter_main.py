# Pet Shelter API — Lesson 4 teacher solution
# Run with:  fastapi dev pet_shelter_main.py   then open http://127.0.0.1:8000/docs
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Pet Shelter API",
              description="Our class pet shelter!")
pets = []                     # our pets live in this list


class Pet(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    species: str
    age: int = Field(ge=0, le=30)


@app.get("/")
def home():
    return {"message": "Welcome to the Pet Shelter!"}


@app.get("/pets")
def list_pets():
    return pets


@app.post("/pets")
def add_pet(pet: Pet):        # FastAPI checks it with Pydantic!
    pets.append(pet)
    return {"added": pet, "total": len(pets)}


@app.get("/pets/{pet_id}")
def get_pet(pet_id: int):
    if pet_id < 0 or pet_id >= len(pets):
        raise HTTPException(status_code=404,
                            detail="No pet with that number")
    return pets[pet_id]
