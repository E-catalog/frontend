from typing import Any, Optional

import httpx
from pydantic import BaseModel


class Individual(BaseModel):
    id: Optional[int]
    place: str
    name: str
    year_of_excavation: Optional[int]
    sex: Optional[str]
    age: Optional[str]
    individual_type: Optional[str]
    preservation: Optional[str]
    epoch: Optional[str]
    comments: Optional[str]


class IndividualsClient:

    def __init__(self, url: str) -> None:
        self.url = f'{url}/individuals'

    def get_all(self) -> list[Individual]:
        response = httpx.get(f'{self.url}/')
        response.raise_for_status()
        data = response.json()
        return [Individual(**item) for item in data]

    def add(self, form_data: dict[str, Any]) -> str:
        response = httpx.post(f'{self.url}/', json=form_data)
        response.raise_for_status()
        return 'Индивид успешно создан'
