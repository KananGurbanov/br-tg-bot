# Use a base image with Python
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium \
    chromium-driver

# Set environment variables for Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_BIN=/usr/bin/chromedriver

# Copy the project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

# Run the bot
CMD ["python", "app/main.py"]
