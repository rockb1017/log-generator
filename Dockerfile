FROM python:3-alpine

COPY . .
ENTRYPOINT  ["python", "-u", "loggen.py"]