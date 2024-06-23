# blury

Difumina la imagen verticalmente.

Uso:

``` sh
applyeffect blury imagen_original [imagen_destino]
```

Para modificar la intensidad del desenfoque, se puede usar:

``` sh
applyeffect blury imagen_original [imagen_destino] --intensity intensidad
```

Siendo intensidad un número entero. Su valor por defecto es 20.

Si no se indica un nombre para el fichero destino, aplicará el sufijo `_blurred_y.png`

Resultado:

![imagen original](../../images/image.jpg)
![blury](../../images/image_blurred_y.png)
