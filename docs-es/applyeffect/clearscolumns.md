# clearscolumns

Aclara los colores de la imagen en franjas verticales (columnas).

Uso:

``` sh
applyeffect clearscolumns imagen_original [imagen_destino]
```

Para indicar el número de columnas:

``` sh
applyeffect clearscolumns imagen_original [imagen_destino] --columns 5
```

O:

``` sh
applyeffect clearscolumns imagen_original [imagen_destino] -c 5
```

Por defecto, el número de columnas es tres.

Si no se indica un nombre para el fichero destino, aplicará el sufijo `_clearscolumns.png`

Resultado:

![imagen original](../../images/image.jpg)
![clearscolumns](../../images/image_clearscolumns.png)
