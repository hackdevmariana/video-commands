# writeinimage

Escribe un texto en una imagen.

## Subcomandos

- new: crea un fichero con un lienzo de un color uniforme y el texto superpuesto.

- simple: escribe sobre una imagen. Devuelve una imagen fija.

- animated: crea una animación con las letras.

- wordbyword: escribe el letrero palabra a palabra.

- typewriter: crea una animación con las letras apareciendo de una en una.

## Parámetros

- --size: tamaño de la imagen a generar con el subcomando `new`. Por defecto: 1920x1080.

- --bgcolor: recibe el color de fondo para el subcomando `new` o para el fondo del letrero.

- --color: color de las letras.

- --font: tipografía del letrero.

- --font-size: tamaño de las letras.

- --text-size: tamaño del letrero a escribir sobre la imagen, en caso de que no se indique --font-size.

- --gravity: posición de letrero: N, NE, E, SE, S, SW, W, NW o C (North, North-East, East, South, South-West, West, North-West o Center).

- --margin: margen respecto al punto gravity.

- --config: fichero de configuración con la tipografía, color, posición...

- --x: posición horizontal del comienzo de la escritura.

- --y: posición vertical del comienzo de la escritura.

- --input: imagen de entrada.

- --output: imagen de salida.

- --time: duración de la animación.

- --animation: modo de animación (según plantilla).

- --effect: efecto sobre las letras.

- --list: lista las animaciones, efectos, colores o las tipografías disponibles (según el valor recibido).

## Fichero de configuración

El comando `writeinimage` admite un fichero de configuración en formato YAML con la siguiente estructura:

``` yaml

```
