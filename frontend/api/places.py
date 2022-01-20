import httpx

from frontend.api.schemas import Place


class PlacesClient:

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

    def add(self, payload: Place) -> None:
        new_place = payload.dict()
        response = httpx.post(f'{self.url}/', json=new_place)
        response.raise_for_status()

    def update(self, uid: int, payload: Place) -> None:
        updated_place = payload.dict()
        response = httpx.put(f'{self.url}/{uid}', json=updated_place)
        response.raise_for_status()

    def delete(self, uid: int) -> None:
        response = httpx.delete(f'{self.url}/{uid}')
        response.raise_for_status()
