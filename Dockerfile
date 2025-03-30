FROM python:3.10

RUN cd home && ls -l .
RUN cd usr && ls -l .

WORKDIR /app


COPY . .

RUN ls -l .

COPY ./test.json ./test.json

RUN ls -l /app/

RUN pip install --no-cache-dir -r requirements.txt

ENV MY_ENV=lala

EXPOSE 8080


CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app"]