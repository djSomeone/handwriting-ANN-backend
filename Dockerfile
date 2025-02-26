# Stage 1: Builder
FROM python:3.11-alpine AS builder

WORKDIR /app

# Install necessary dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

# Create a virtual environment
RUN python3 -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runner
FROM python:3.11-alpine AS runner

WORKDIR /app

# Copy virtual environment from builder stage
COPY --from=builder /app/venv venv

# Copy application files
COPY app.py app.py

# Set environment variables
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV FLASK_APP=app.py

# Expose port 8000 for Koyeb
EXPOSE 8000

# Run the app using Gunicorn on port 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "app:app"]
