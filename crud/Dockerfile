#FROM mcr.microsoft.com/devcontainers/python:3.9

# [Optional] If your requirements.txt is in the root of your project, uncomment the following lines
#COPY ../requirements.txt /tmp/pip-tmp/
#RUN pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# Use an official Python runtime as the base image.
# IMAGEN BASE
FROM python:3.13.2-alpine3.21

# VARIABLES DE ENTORNO
ENV PYTHONUNBUFFERED=1

# DIRECTORIO DE TRABAJO
WORKDIR /app

# INSTALACION DE DEPENDENCIAS
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip

# COPIAR ARCHIVOS
COPY ./requirements.txt ./

# INSTALACION DE DEPENDENCIAS
RUN pip install -r requirements.txt

# COPIAR ARCHIVOS
COPY ./ ./

# EXPOSICION DE PUERTO
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]