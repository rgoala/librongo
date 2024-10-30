import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Book(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    edition: str = Field(...)
    category: str = Field(...)
    author: str = Field(...)
    synopsis: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Python Basics - A Practical Introduction to Python 3",
                "edition": "4th",
                "category": "Software Programming, Python 3",
                "author": "David Amos, Dan Bader, Joanna Jablonski",
                "synopsis": "..."
            }
        }


class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Python Basics - A Practical Introduction to Python 3",
                "author": "David Amos, Dan Bader, Joanna Jablonski, Fletcher Heisler",
                "synopsis": "Don Quixote is a Spanish novel by Miguel de Cervantes..."
            }
        }