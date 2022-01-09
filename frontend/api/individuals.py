import httpx
from pydantic import BaseModel


class Individual(BaseModel):
    uid: int
    place: str
    name: str


class IndividualsClient:

    def __init__(self, url: str) -> None:
        self.url = f'{url}/individuals'

    def get_all(self) -> list[Individual]:
        response = httpx.get(f'{self.url}/')
        response.raise_for_status()
        data = response.json()
        return [Individual(**item) for item in data]
