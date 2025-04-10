# Base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .

# Collect static files (اختیاریه ولی برای جنگو لازمه)
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run the server
CMD ["gunicorn", "event.wsgi:application", "--bind", "0.0.0.0:8000"]

