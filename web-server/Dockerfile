FROM python:3.10.12 
#Aqui se le dice la version de python para el contenedor

WORKDIR /web-server 
#esta es la carpeta que se va a crear dentro del contenedor, el espacio de trabajo
COPY requirements.txt /web-server/requirements.txt
#Con copy se copia el archivo de los requirements para el espacio de trabajo.

RUN pip install --no-cache-dir --upgrade -r /web-server/requirements.txt
#Aqui se instalan las dependencias del archivo requeriments.
#--no-cache-dir --upgrade es para que no aplique el cache y que si hay actualizaciones del gestor de paquetes, las haga.

COPY . /web-server
#Con este copiamos todo(con el .) lo que hay en la carpeta que le indiquemos

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
#Este comando mantiene encendido el contenedor, en este caso una lista de instrucciones, primero que en uvicorn ingrese al archivo main:app, se pone el host que es el puerto 0.0.0.0 y el puesto --port que será el 80