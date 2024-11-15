import httpx
from pydantic import BaseModel, validator, Field
from typing import List, Optional


class CreateSpyCat(BaseModel):
    name: str
    years_of_experience: int
    breed: str
    salary: float

    @validator("breed")
    def validate_breed(cls, breed):
        with httpx.Client() as client:
            response = client.get(f"https://api.thecatapi.com/v1/breeds")
        if not response.json() or breed not in [breed_data['name'] for breed_data in response.json()]:
            raise ValueError("Wrong breed")
        return breed

class CatUpdate(BaseModel):
    salary: float

    class Config:
        orm_mode = True

class CreateTarget(BaseModel):
    name: str
    country: str
    mission_id: int
    complete: bool = False
    notes: Optional[str] = None


class CreateMission(BaseModel):
    cat_id: int
    targets: List[CreateTarget] = Field(..., min_items=1, max_items=3)
    complete: bool = False
