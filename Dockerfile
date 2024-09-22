FROM python:3.9.18-bullseye as build

ENV POETRY_VERSION=1.6.1

RUN groupadd --gid 1000 python \
  && useradd --uid 1000 --gid python --shell /bin/bash --create-home python \
  && pip install "poetry==$POETRY_VERSION"

USER python
WORKDIR /home/python

COPY --chown=python:python poetry.lock pyproject.toml README.md ./
RUN poetry export --no-interaction --no-ansi -f requirements.txt -o requirements.txt \
  && pip install --user --ignore-installed --no-cache-dir --timeout=3600 --no-input -r requirements.txt

COPY --chown=python:python src/ ./src
RUN poetry build --no-interaction --no-ansi -f wheel \
  && pip install --user --ignore-installed --no-cache-dir --no-input --no-deps dist/*.whl

FROM python:3.9.18-slim-bullseye

RUN groupadd --gid 1000 python \
  && useradd --uid 1000 --gid python --shell /bin/bash --create-home python

USER python
WORKDIR /home/python

ENV PATH=/home/python/.local/bin:$PATH

COPY --chown=python:python --from=build /home/python/.local ./.local

CMD [ "connector", "start", "--app", "connector:create_app" ]
