FROM python:3

ENV LANG C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive
# Allow SECRET_KEY to be passed via arg so collectstatic can run during build time
ARG SECRET_KEY
# libpq-dev and python3-dev help with psycopg2
RUN apt-get update \
  && apt-get clean all \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/webapp
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --deploy --system

RUN python3 manage.py collectstatic --no-input

RUN adduser --disabled-password --gecos "" django
USER django

CMD daphne vytrac_26930.asgi:application --port $PORT --bind 0.0.0.0
#CMD daphne Alerts.fastapi:fastApiApp --port $PORT --bind 0.0.0.0
