
FROM python:3-alpine

WORKDIR /App

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY templates /App/templates
COPY app.py /App/
COPY requirements.txt /App/

RUN useradd -m -g users flaskapp
USER flaskapp

CMD [ "python3", "app.py" ]