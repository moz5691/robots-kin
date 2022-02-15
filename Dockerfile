# pull official base image
FROM python:3.10.1-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.1.12
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml ./

## Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$BUILD_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . .

COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]