# blur

Difumina la imagen.

Uso:

``` sh
applyeffect blur imagen_original [imagen_destino]
```

Para modificar la intensidad del desenfoque, se puede usar:

``` sh
applyeffect blur imagen_original [imagen_destino] --intensity intensidad
```

Siendo intensidad un número entero. Su valor por defecto es 2.

Si no se indica un nombre para el fichero destino, aplicará el sufijo `_blurred.png`

Resultado:

![imagen original](../../images/image.jpg)
![blur](../../images/image_blurred.png)
