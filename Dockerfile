FROM python:3.12-slim

WORKDIR /app

# Install Python packages first (caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ALL project files to /app/ root
COPY . .

# Fix permissions
RUN chmod -R 755 /app

EXPOSE 8000

# Gunicorn command (Django will run from /app/)
CMD ["gunicorn", "ebanking.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
