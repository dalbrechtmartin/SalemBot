FROM python:alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install PostgreSQL dependencies (Alpine uses apk)
RUN apk update && apk add --no-cache gcc musl-dev postgresql-dev curl

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Command is specified in docker-compose.yml
CMD ["python", "src/main.py"]