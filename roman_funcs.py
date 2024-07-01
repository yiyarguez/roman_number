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
        result = n * values[1]
    elif n == 4: 
        result = values[1] + values[5]
    elif n < 9:
        result = values[5] + (n - 5) * values[1]
    elif n == 9:
        result = values[1] + values[10]
    else:
        result = values[n]
    return result
        




    
#   result = values[n]

# Los ifs no son necesarios solo son para mostrar como se realizó antes de implementar
# el diccionario

"""
    if n == 1:
        result = 'I'
    elif n == 5:
        result = 'V'
    elif n == 10:
        result = 'X'
    elif n == 50:
        result = 'L'
    elif n == 100:
        result = 'C'
    elif n == 500:
        result = 'D'
    elif n == 1000:
        result = 'M'
    
    return result
"""