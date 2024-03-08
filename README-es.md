# video_commands

##### Conjunto de herramientas para trabajar con imágenes, vídeos y audio desde la línea de comandos

Read the documentation in [English](README.md)

## Instalación

Vaya a un directorio desde donde pueda ejecutar los comandos. En GNU/Linux puede ver los directorios donde almacenar ejecutables con la variable $PATH:

``` sh
echo $PATH
```

Descargue el proyecto git:

``` sh
git clone https://github.com/hackdevmariana/video-commands.git
```

O, individualmente, los comandos que desee utilizar:

``` sh
git clone https://github.com/hackdevmariana/video-commands.git
```

Cree el entorno virtual:

``` sh
python3 -m venv venv
```

Active el entorno virtual. En GNU/Linux y otros sistemas Unix:

``` sh
source venv/bin/activate
```

En Windows:

``` sh
.\venv\Scripts\activate
```

Para desactivar el entorno virtual:

``` sh
deactivate
```

Instale las dependencias:

``` sh
pip install -r requirements.txt
```

Y dele permisos de ejecución a los comandos. En GNU/Linux, puede hacerlo con `chmod`:

``` sh
chmod +x makecanvas removebg tintbg tintimage
```

## Comandos simples (sin subcomandos)

### removebg

Crea un fichero con la imagen en primer plano del fichero recibido como primer parámetro. Si no recibe el nombre del fichero de salida como segundo parámetro, genera un fichero con el mismo nombre del fichero original y el sufijo `_removed.png`.

Uso simple:

``` sh
removebg imagen.jpg
```

Genera un fichero sin fondo llamado `imagen_removed.png`.

Indicando el fichero de salida:

``` sh
removebg imagen.jpg sin_fondo.png
```

Genera un fichero sin fondo llamado `imagen_removed.png`.

Es importante que le indiquemos un formato que admita transparencia para poder generar una imagen sin fondo.

### tintimage

### tintbg
