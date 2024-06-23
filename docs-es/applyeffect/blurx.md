# blurx

Difumina la imagen horizontalmente.

Uso:

``` sh
applyeffect blurx imagen_original [imagen_destino]
```

Para modificar la intensidad del desenfoque, se puede usar:

``` sh
applyeffect blurx imagen_original [imagen_destino] --intensity intensidad
```

Siendo intensidad un número entero. Su valor por defecto es 20.

Si no se indica un nombre para el fichero destino, aplicará el sufijo `_blurred_x.png`

Resultado:

![imagen original](../../images/image.jpg)
![blurx](../../images/image_blurred_x.png)
