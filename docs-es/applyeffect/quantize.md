# quantize

Posteriza la imagen, permitiendo elegir el número de colores.

Uso:

``` sh
applyeffect quantize imagen_original [imagen_destino]
```

Para modificar el número de colores, usar el modificador `--intensity`. Valor por defecto: 5.

Si no se indica un nombre para el fichero destino, aplicará el sufijo `_quantize.png`.

Resultado:

![imagen original](../../images/image.jpg)
![quantize](../../images/image_quantize.png)
