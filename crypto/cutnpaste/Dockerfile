FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y socat && pip install -r requirements.txt

CMD socat TCP-LISTEN:80,fork EXEC:'python3 server.py'
