# gaussianblur

Aplica un desenfoque gaussiano a la imagen.

Uso:

``` sh
applyeffect gaussianblur imagen_original [imagen_destino]
```

Para indicar la intensidad del desenfoque:

``` sh
applyeffect gaussianblur imagen_original [imagen_destino] --intensity 10
```

Por defecto, la intensidad es 5.

Si no se indica un nombre para el fichero destino, aplicará el sufijo `_gaussianblurs.png`

Resultado:

![imagen original](../../images/image.jpg)
![gaussianblur](../../images/image_gaussianblur.png)
