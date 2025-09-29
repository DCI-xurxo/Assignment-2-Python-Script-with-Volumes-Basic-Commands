FROM python:3.11-slim

WORKDIR /app


COPY logger.py /app/logger.py


CMD ["python", "/app/logger.py"]