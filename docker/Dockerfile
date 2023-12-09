FROM registry.opensuse.org/opensuse/bci/python:3.11

RUN zypper --non-interactive install python311-poetry

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --with=production

WORKDIR /app
COPY buildher buildher
COPY manage.py .

COPY docker/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000/TCP
CMD exec gunicorn buildher.wsgi:application --bind 0.0.0.0:8000
