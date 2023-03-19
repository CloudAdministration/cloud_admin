FROM python:3.10.10

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    python3-pip \
    && pip install --upgrade pip \
    && pip install localstack

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["localstack", "start"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
