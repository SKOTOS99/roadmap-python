# Imagen base
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /backend

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del proyecto
COPY . .

# Configurar el directorio actual como parte del PYTHONPATH
ENV PYTHONPATH=/backend

# Exponer el puerto en el que corre Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]