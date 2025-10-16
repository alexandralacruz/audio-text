# Use official Python base image
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
# Install system dependencies
#RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# ENV DEBIAN_FRONTEND=noninteractive le dice a apt que no intente abrir diálogos.
ENV DEBIAN_FRONTEND=noninteractive 
# --no-install-recommends evita instalar paquetes innecesarios.
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*
# esto apt-get install -y ffmpeg && => es para instalar ffmpeg que se requiere para procesar audio
# esto rm -rf /var/lib/apt/lists/* => es para limpiar la cache de apt y reducir el tamaño de la imagen

# Instalar todas las dependencias de Python del requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
