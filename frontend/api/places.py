from http import HTTPStatus

import httpx

from frontend.api.models import Place


class PlacesClients:

    def __init__(self, url: str) -> None:
        self.url = f'{url}/places'

    def get_all(self) -> list[Place]:
        response = httpx.get(f'{self.url}/')
        response.raise_for_status()
        data = response.json()
        return [Place(**item) for item in data]

    def get(self, uid: int) -> Place:
        response = httpx.get(f'{self.url}/{uid}')
        response.raise_for_status()
        data = response.json()
        return Place(**data)

    def add(self, payload: Place) -> int:
        new_place = payload.dict()
        response = httpx.post(f'{self.url}/', json=new_place)
        response.raise_for_status()
        return HTTPStatus.CREATED

    def update(self, uid: int, payload: Place) -> int:
        updated_place = payload.dict()
        response = httpx.put(f'{self.url}/{uid}', json=updated_place)
        response.raise_for_status()
        return HTTPStatus.OK

    def delete(self, uid: int) -> int:
        response = httpx.delete(f'{self.url}/{uid}')
        response.raise_for_status()
        return HTTPStatus.NO_CONTENT