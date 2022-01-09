import httpx

from typing import Any


class IndividualsClient:

    def __init__(self, url: str) -> None:
        self.url = f'{url}/individuals'

    def get_all(self) -> list[dict[str, Any]]:
        response = httpx.get(f'{self.url}/')
        response.raise_for_status()
        return response.json()
