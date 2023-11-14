
FROM python:3-alpine

WORKDIR /App

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txtgi

COPY . .

CMD [ "python3", "app.py" ]