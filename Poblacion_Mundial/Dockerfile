FROM python:3.10.12 
#Aqui se le dice la version de python para el contenedor

WORKDIR /Poblacion_Mundial 
#esta es la carpeta que se va a crear dentro del contenedor, el espacio de trabajo
COPY requirements.txt /Poblacion_Mundial/requirements.txt
#Con copy se copia el archivo de los requirements para el espacio de trabajo.

RUN pip install --no-cache-dir --upgrade -r /Poblacion_Mundial/requirements.txt
#Aqui se instalan las dependencias del archivo requeriments.
#--no-cache-dir --upgrade es para que no aplique el cache y que si hay actualizaciones del gestor de paquetes, las haga.

COPY . /Poblacion_Mundial
#Con este copiamos todo(con el .) lo que hay en la carpeta que le indiquemos

CMD bash -c "while true; do sleep1; done"
#Este comando mantiene encendido el contenedor (es bash)