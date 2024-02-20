# Usamos una imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos de la aplicación al contenedor
COPY . .

# Instalamos las dependencias
RUN pip install --no-cache-dir Flask Flask-MongoEngine gunicorn

# Exponemos el puerto en el que la aplicación Flask va a correr
EXPOSE 3002

# Comando para ejecutar la aplicación
CMD ["python", "api.py"]

