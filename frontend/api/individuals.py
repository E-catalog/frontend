import httpx

from frontend.api.schemas import Individual


class IndividualsClient:

    def __init__(self, url: str) -> None:
        self.url = f'{url}/individuals'

    def get_all(self) -> list[Individual]:
        response = httpx.get(f'{self.url}/')
        response.raise_for_status()
        data = response.json()
        return [Individual(**item) for item in data]

    def get(self, uid: int) -> Individual:
        response = httpx.get(f'{self.url}/{uid}')
        response.raise_for_status()
        data = response.json()
        return Individual(**data)

    def add(self, payload: Individual) -> None:
        new_individual = payload.dict()
        response = httpx.post(f'{self.url}/', json=new_individual)
        response.raise_for_status()

    def update(self, uid: int, payload: Individual) -> None:
        updated_individual = payload.dict()
        response = httpx.put(f'{self.url}/{uid}', json=updated_individual)
        response.raise_for_status()

    def delete(self, uid: int) -> None:
        response = httpx.delete(f'{self.url}/{uid}')
        response.raise_for_status()
