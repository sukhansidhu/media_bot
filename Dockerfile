# Use Python 3.10 base image
FROM python:3.10-slim-buster

# Install system dependencies and FFmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV BOT_TOKEN=$BOT_TOKEN
ENV PYTHONPATH=/app

# Set work directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create media directories
RUN mkdir -p downloads uploads thumbnails metadata

# Run the bot
CMD python main.py
