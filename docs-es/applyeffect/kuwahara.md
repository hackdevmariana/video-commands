# kuwahara

Aplica un efecto Kuwahara a la imagen.

Uso:

``` sh
applyeffect kuwahara imagen_original [imagen_destino]
```

Para modificar la intensidad, usar el modificador `--intensity`. Valor por defecto: 7.

Si no se indica un nombre para el fichero destino, aplicará el sufijo `_kuwahara.png`

Resultado:

![imagen original](../../images/image.jpg)
![kuwahara](../../images/image_kuwahara.png)
