FROM python:3.12.0b1-slim

WORKDIR .
COPY . .

RUN pip3 install -r requirements.txt

CMD ["python", "main.py"]

