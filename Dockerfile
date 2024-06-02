# Lo siguiente es para indicar cual imagen utilizará el Docker File
FROM python:3.8-alpine3.19

# La fuente '.' se copiará en el directorio '/usr/src/app'
COPY . /usr/src/app

# Se establece el directorio cuando se utilice el contenedor...
WORKDIR /usr/src/app

# Se instalan las dependencias del archivo 'requirements.txt'
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]
