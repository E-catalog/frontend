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

    def add(self, payload: Individual) -> int:
        new_individual = {
            'name': payload.name,
            'place': payload.place,
            'sex': payload.sex,
            'age': payload.age,
            'year_of_excavation': payload.year_of_excavation,
            'individual_type': payload.individual_type,
            'preservation': payload.preservation,
            'epoch': payload.epoch,
            'comments': payload.comments,
        }
        response = httpx.post(f'{self.url}/', json=new_individual)
        response.raise_for_status()
        return response.status_code
