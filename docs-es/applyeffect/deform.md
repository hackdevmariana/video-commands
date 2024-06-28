# deform

Ondula la imagen.

Uso:

``` sh
applyeffect deform imagen_original [imagen_destino]
```

Para cambiar la intensidad de la deformación:

``` sh
applyeffect deform imagen_original [imagen_destino] --intensity 5
```

El valor por defecto es 10.

Si no se indica un nombre para el fichero destino, aplicará el sufijo `_deform.png`

Resultado:

![imagen original](../../images/image.jpg)
![deform](../../images/image_deform.png)
