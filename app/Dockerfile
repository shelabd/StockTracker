FROM python:3.9-alpine

RUN mkdir /app
WORKDIR /app

COPY app/config.ini StockTracker/
COPY StockTracker/TickerAdd.py StockTracker/
COPY StockTracker/requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "StockTracker/TickerAdd.py"]
