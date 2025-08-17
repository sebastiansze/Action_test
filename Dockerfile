FROM python:3.11-slim

# Arbeitsverzeichnis setzen
WORKDIR /app

# Dependencies installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App Code kopieren
COPY app.py .

# Port für FastAPI
EXPOSE 8000

# Startbefehl
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
