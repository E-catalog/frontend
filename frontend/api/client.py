from frontend.api.individuals import IndividualsClient
from frontend.api.places import PlacesClient


class Client:

    def __init__(self, url: str) -> None:
        url = f'{url}/api/v1'

        self.individuals = IndividualsClient(url)
        self.places = PlacesClient(url)
