# Implementación de Autómatas y Expresiones Regulares

## Alejandro Adrián García Martínez

## Descripción
Para este proyecto se ha elegido un lenguaje de tipo matemático el cuál tiene las siguientes reglas:
1. Los únicos carácteres en el lenguaje son 0, 1 y 2.
2. La cadena debe terminar con 111 o con 122.
3. La cadena no puede tener en ningún momento 211, de lo contrario no será válido.

## Autómata
Para solucionar y generar el algortimo que verifique la cadena, se diseñó un automata para vizualizar los dieferentes estados por lo que podría pasar y poder entender y diseñar de forma eficiente el algoritmo más adelante en prolog.
### Primer diseño
El primer diseño diagrama del automata es el siguiente:
![Automata evidence 1](automata1.jpeg)
En este primer diseño se buscó dar prioridad a la segunda regla del lenguaje, de ahí se añadieron rutas que faciliten la trancisión entre todos los posbles estados y se integró el estado "h" en el que la única forma para llegar es incumplir la tercera regla.

### Segundo diseño
Para el segundo diseño del diagrama se contempló la posibilidad de que la cadea pueda transiciónar en el estado "d" o estado final y no necesariamente terminar ahí, de esta forma evitar que en un punto se coloque 111 o 122 y que el automata lo cuente como correcto incumpliendo la segunda o incluso la tercera regla.
Finalmente se consiguió este diseño:
![Automata evidence 1](automata2.jpeg)

## Expresión regular
Así mismo se diseño una expresión regular que permitiera solucionar el problema como el autonomapor medio de la lectura de caracteres y restricciones en el mismo

### Primer diseño
En el primer diseño se busco principalmente la pprhibición de que se rompa la tecercera regla del lenguaje, por lo que rápidamente se volió muy restringido como se pede ver a continuación:
```
/(0|1|2)?((0|2)?|(00|01|02|10|20)?)+(111|122)$/gm
```
Así mismo se podía burlar facilmente las mismas restricciones y romper la tercer regla, también no permitía que existieran todas las posibles combinaciones del lenguaje, es por eso que se decidió cambiar de estrategia y utilizar "Assertions".

### Segundo diseño
Con ayuda de los "Assertions" se pudo simplificar de gran manera la expresión regular, ya que al utilizar el Assertion ``` ?! ``` podemos negar todas las instancias de un caracter o un grupo de caracteres de este punto en adelante, de esta manera podemos simplemente indicar que niegue todas las instancias de 211, restringir que los únicos caracteres disponibles sean los del lenguaje e indicar que debe terminar en 111 o 122, dando como resultado el segundo diseño:
```
^(?!.*211)[012]*(111|122)$
```

## Algoritmo Automata
