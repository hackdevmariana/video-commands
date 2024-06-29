# fxscanlines

Crea una textura de líneas oscuras sobre la imagen.

Uso:

``` sh
applyeffect fxscanlines imagen_original [imagen_destino]
```

Para cambiar la cantidad de líneas oscuras, usar el modificador `--intensity`. El valor por defecto es 50.

Si no se indica un nombre para el fichero destino, aplicará el sufijo `_fxscanlines.png`

Resultado:

![imagen original](../../images/image.jpg)
![fxscanlines](../../images/image_fxscanlines.png)
