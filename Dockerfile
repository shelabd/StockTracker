FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY TickerAdd.py .

EXPOSE 5000

CMD [ "python", "TickerAdd.py" ]
