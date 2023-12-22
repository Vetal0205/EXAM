FROM python:3.11.5-slim

WORKDIR /app


COPY Piramida.py .


CMD ["python", "Piramida.py"]
