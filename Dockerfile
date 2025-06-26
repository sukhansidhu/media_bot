FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY media_bot/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY media_bot .

RUN mkdir -p downloads uploads thumbnails metadata

CMD ["python", "main.py"]
