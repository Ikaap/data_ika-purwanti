FROM python:3.12.0-slim

WORKDIR /app

COPY . /app

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r /app/requirements.txt
RUN pip install --no-cache /wheels/*

CMD ["python", "main.py"]
