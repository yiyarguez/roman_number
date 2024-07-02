# Diccionario
values = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}



"""
# Mi solución
def to_roman(n: int) -> str:
    if n <= 3:
        result = n * values[1]   # si n = 2, result = 2 * values[1] -> 2 * 'I'
    elif n == 4: 
        result = values[1] + values[5] # 'I' + 'V'
    elif n < 9:
        result = values[5] + (n - 5) * values[1] # si n = 8, result = 'V' + (8 - 5) * 'I' ->
    elif n == 9:
        result = values[1] + values[10]
    elif n <= 30:
        result = int(str(n).replace('0', '')) * values[10] # n = 20, result = 2 * 'X'
    elif n == 40:
         result = values[10] + values[50]
    elif n < 90:
        result_str = str(n - 50).replace('0', '')
        result = values[50] + (int(result_str) if result_str else 0) * values[10]
    elif n == 90:
        result = values[10] + values[100] #'X' + 'C'
    else:
        result = values[n]
    return result
"""

# Solución Mon
def to_roman(n: int) -> str:
    if n <= 3:
        result = n * values[1]   # si n = 2, result = 2 * values[1] -> 2 * 'I'
    elif n == 4: 
        result = values[1] + values[5] # 'I' + 'V'
    elif n < 9:
        result = values[5] + (n - 5) * values[1] # si n = 8, result = 'V' + (8 - 5) * 'I' ->
    elif n == 9:
        result = values[1] + values[10]
    elif n <= 30:
        result = n//10 * values[10]  # n//10 da como resultado un numero entero, n / 10 nos da un resultado con decimales
    elif n == 40:
        result = values[10] + values[50]
    elif n < 90:
        result = values[50] + (n//10 - 5) * values[10]  
    elif n == 90:
        result = values[10] + values[100] #'X' + 'C'  
    elif n <= 300:
        result = n//100 * values[100]  # n//10 da como resultado un numero entero, n / 10 nos da un resultado con decimales
    elif n == 400:
        result = values[100] + values[500]
    elif n < 900:
        result = values[500] + (n//100 - 500) * values[100] 
    elif n == 900:
        result = values[100] + values[1000]
    elif n == 3000:
        result = n//1000 * values[1000] #'X' + 'C'  
    else:
        result = values[n]
    return result


def dividir_en_digitos(n:int):
    """
    TODO: Evitar que entren números mayores de 3999. Lanzar exception

    """
    cad = f"{n:04d}"
    millares = 0
    centenas = 0
    decenas = 0
    unidades = 0

#Ejemplo: 2024
    millares = int(cad[0]) * 1000 # 2000
    centenas = int(cad[1]) * 100 # 0
    decenas = int(cad[2]) * 10 # 20
    unidades = int(cad[3]) * 1 # 4

    return[millares,centenas,decenas,unidades]


def digitos_a_romanos(lista):
    result = ""
    for numero in lista:
        result += to_roman(numero)
    return result

def arabigo_a_romano(n:int):
    lista = dividir_en_digitos(n)
    return digitos_a_romanos(lista)














