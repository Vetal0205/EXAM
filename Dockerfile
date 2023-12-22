FROM python:3.11.5-slim

WORKDIR /app


COPY Progression.py .


CMD ["python", "Progression.py"]
