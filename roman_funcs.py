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












