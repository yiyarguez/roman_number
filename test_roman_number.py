from roman_funcs import to_roman, dividir_en_digitos,arabigo_a_romano

def test_romanos_simples():
    assert to_roman(1) == 'I'
    assert to_roman(5) == 'V'
    assert to_roman(10) == 'X'
    assert to_roman(50) == 'L'
    assert to_roman(100) == 'C'
    assert to_roman(500) == 'D'
    assert to_roman(1000) == 'M'

def test_romanos_1_al_9():
    assert to_roman(1) == 'I'
    assert to_roman(2) == 'II'
    assert to_roman(3) == 'III'
    assert to_roman(4) == 'IV'
    assert to_roman(5) == 'V'
    assert to_roman(6) == 'VI'
    assert to_roman(7) == 'VII'
    assert to_roman(8) == 'VIII'

# Tarea
def test_romanos_10_al_90():
    assert to_roman(10) == 'X'
    assert to_roman(20) == 'XX'
    assert to_roman(30) == 'XXX'
    assert to_roman(40) == 'XL'
    assert to_roman(50) == 'L'
    assert to_roman(60) == 'LX'
    assert to_roman(70) == 'LXX'
    assert to_roman(80) == 'LXXX'
    assert to_roman(90) == 'XC'         


def test_dividir_en_digitos():
    assert dividir_en_digitos(34) == [0,0,30,4]
    assert dividir_en_digitos(2024) == [2000,0,20,4]
    assert dividir_en_digitos(100) == [0,100,0,0]

def test_cualquier_romano():
    assert arabigo_a_romano(1999) == 'MCMXCIX'