FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

ENV POETRY_HOME=/etc/poetry

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="${POETRY_HOME}/bin:${PATH}"

RUN poetry completions bash >> ~/.bash_completion
