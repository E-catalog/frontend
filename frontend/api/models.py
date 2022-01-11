from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field


class Individual(BaseModel):
    uid: int = Field(alias='id')
    place: str
    name: str
    year_of_excavation: Optional[int]
    sex: Optional[str]
    age: Optional[str]
    individual_type: Optional[str]
    preservation: Optional[str]
    epoch: Optional[str]
    comments: Optional[str]
