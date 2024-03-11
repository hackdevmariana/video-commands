# removebg

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
