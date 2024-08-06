FROM python:3.10-alpine AS backend

ENV PYTHONBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV POETRY_VERSION=1.8.3

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /goodreads

COPY . .

RUN poetry config virtualenvs.create false

FROM backend AS backend-dev

WORKDIR /goodreads/src

RUN poetry install --no-interaction --no-root --no-ansi

CMD python manage.py runserver 0.0.0.0:8000

