FROM python:3.11.0

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root --only main

ENV PYTHONPATH=/app

COPY ./app /app/app

# start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
