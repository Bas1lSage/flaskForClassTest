
FROM python:3.12-slim-bookworm

WORKDIR /App

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY templates /App/templates
COPY app.py /App/
COPY requirements.txt /App/

RUN groupadd -r flaskapp && useradd -r -g flaskapp flaskapp
USER flaskapp

CMD [ "python3", "app.py" ]