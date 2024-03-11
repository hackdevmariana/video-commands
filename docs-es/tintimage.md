# removebg

Crea un fichero con la imagen coloreada a partir de una imagen recibida.

El resto de parámetros que admite son:

- color: El color con el que teñir la imagen. Por defecto, el negro, por lo que oscurece la imagen.

- mode: Modo de tintado:

  - light (por defecto): mantiene las zonas claras (los blancos de la imagen original) y tiñe las oscuras.

  - dark: mantiene las zonas oscuras (los negros de la imagen original) y tiñe las claras.

- image_dst: nombre del fichero destino.

Si no recibe el nombre del fichero de salida como parámetro, genera un fichero con el mismo nombre del fichero original y el sufijo `_tinted.png`.

## Uso

Uso simple:

``` sh
tintimage imagen.jpg
```

Genera un fichero con una imagen oscurecida llamado `imagen_tinted.png`.

Indicando el color a teñir:

``` sh
removebg imagen.jpg blue
```

Genera un fichero con una imagen teñida de azul las zonas oscuras llamado `imagen_tinted.png`.

``` sh
removebg imagen.jpg blue dark
```

Genera un fichero con las zonas claras de la imagen original teñidas de azul llamado `imagen_tinted.png`.

``` sh
removebg imagen.jpg blue dark blue-dark.png
```

Genera un fichero con las zonas claras de la imagen original teñidas de azul llamado `blue-dark.png`.
