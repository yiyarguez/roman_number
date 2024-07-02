# Tests

- Crear una función que pase de arabigo a romano (menor de 4000)
```
to_roman(n: int) -> str
```

TEST:

Romanos simples:
* 1 -> 'I'
* 5 -> 'V'

Romanos del 1 al 9:
* 2 -> 'II'
* 3 -> 'III'
* 4 -> 'IV'

Romanos del 10 al 90:
* 10 -> 'X'
* 20 -> 'XX'
* 30 -> 'XXX'
* 40 -> 'XL'
* 50 -> 'L'

Después de la investigación hemos decidido que un buen algoritmo es:
1. Dividir el número (siempre menor de 4000) en millares, centenas, decenas y unidades. Poner en una lista
2. Procesar cada item de la lista tranformandolo en romano. Tendré que retocar el algoritmo que ya tengo.
3. Concatenar de mayor a menor los simbolos romanos obtenidos.




