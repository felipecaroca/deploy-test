FROM python:3.10


WORKDIR /app

RUN ls -l .

COPY . .
COPY ./test.json /app/test.json

RUN ls -l /app/

RUN pip install --no-cache-dir -r requirements.txt

ENV MY_ENV=lala

EXPOSE 8080


CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app"]