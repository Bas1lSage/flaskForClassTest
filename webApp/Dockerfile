
FROM python:3-alpine

WORKDIR /App

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY templates /App/templates
COPY app.py /App/
COPY requirements.txt /App/

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN groupadd -r flaskapp && useradd -r -g flaskapp flaskapp
USER flaskapp

CMD [ "python3", "app.py" ]