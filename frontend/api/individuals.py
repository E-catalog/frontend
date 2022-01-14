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

    def update(self, uid: int, payload: Individual) -> int:
        updated_individual = payload.dict()
        response = httpx.put(f'{self.url}/{uid}', json=updated_individual)
        response.raise_for_status()
        return HTTPStatus.OK

    def delete(self, uid: int) -> int:
        response = httpx.delete(f'{self.url}/{uid}')
        response.raise_for_status()
        return HTTPStatus.NO_CONTENT
