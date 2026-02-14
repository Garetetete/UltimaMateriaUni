import random

def generar_numero():
    """Generate random 4-digit number (1000-9999)"""
    return random.randint(0000, 9999)

def validar_numero(valor):
    """Validate if value is a valid single digit (0-9)"""
    try:
        num = int(valor)
        if 0 <= num <= 9:
            return True, num
        else:
            return False, None
    except (ValueError, TypeError):
        return False, None

def comparar(numero_secreto, intentos_dict):
    """Compare guessed digits with secret number and return progress"""
    secreto_str = str(numero_secreto)
    resultado = ""
    digitos_correctos = 0
    
    for i in range(4):
        if i in intentos_dict:
            if int(intentos_dict[i]) == int(secreto_str[i]):
                resultado += str(intentos_dict[i])
                digitos_correctos += 1
            else:
                resultado += "X"
        else:
            resultado += "X"
    
    return resultado, digitos_correctos
