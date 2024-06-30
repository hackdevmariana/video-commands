# subtitle

Conjunto de comandos para generar subtítulos.

## toaudio

Convierte vídeo a audio.

Uso:

``` sh
subtitle toaudio FICHERO_DE_VIDEO [FICHERO_DE_AUDIO]
```

Si no se le indica un nombre de fichero de salida, genera un fichero con el mismo nombre y la extensión `.mp3`.

## totext

Convierte el audio a texto.

Uso:

``` sh
subtitle totext FICHERO_DE_AUDIO [FICHERO_DE_TEXTO]
```

Si no se le indica un nombre de fichero de salida, genera un fichero con el mismo nombre y la extensión `.txt`.

## Conversiones del texto

### uppercase

Convierte el texto a mayúsculas.

Uso:

``` sh
subtitle uppercase FICHERO_DE_TEXTO [FICHERO_DE_TEXTO]
```

Si no se le indica un nombre de fichero de salida, genera un fichero con el mismo nombre y el sufijo `_uppercase.txt`.

### sentences

Divide el texto en frases.

Uso:

``` sh
subtitle sentences FICHERO_DE_TEXTO [FICHERO_DE_TEXTO]
```

Si no se le indica un nombre de fichero de salida, genera un fichero con el mismo nombre y el sufijo `_sentences.txt`.

### lines

Divide el texto en frases.

Uso:

``` sh
subtitle sentences FICHERO_DE_TEXTO [-m MÁXIMO_NÚMERO_DE_CARACTERES_POR_LÍNEA] [-o FICHERO_DE_TEXTO]
```

El número máximo de caracteres por línea por defecto es 40.

Si no se le indica un nombre de fichero de salida, genera un fichero con el mismo nombre y el sufijo `_lines.txt`.

## Unificar procesos

Para convertir el vídeo en audio, el audio en texto y transformar el texto para que tenga formato listo para generar los subtítulos, podemos hacerlo con `preparetext`.

Uso:

``` sh
subtitle preparetext FICHERO_DE_TEXTO [-m MÁXIMO_NÚMERO_DE_CARACTERES_POR_LÍNEA] [-o FICHERO_DE_TEXTO]
```

El número máximo de caracteres por línea por defecto es 40.

Si no se le indica un nombre de fichero de salida, genera un fichero con el mismo nombre y el sufijo `_prepared.txt`.
