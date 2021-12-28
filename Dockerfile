FROM python:3.9-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev

COPY frontend /app/frontend

CMD ["poetry", "run", "python", "-m", "frontend"]
