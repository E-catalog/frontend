from http import HTTPStatus

import httpx

from frontend.api.models import Individual


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

    def add(self, payload: Individual) -> int:
        new_individual = payload.dict()
        response = httpx.post(f'{self.url}/', json=new_individual)
        response.raise_for_status()
        return HTTPStatus.CREATED
