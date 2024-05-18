FROM python:latest

#inside of my image/container i am trying to create a directory
WORKDIR /app

ENV FLASK_APP=app.py

COPY ./requirements.txt .

RUN pip install -r requirements.txt
RUN pip install flask flask_cors
RUN pip install flask flask_MySQLdb

COPY . .

CMD [ "python", "hello.py" ]