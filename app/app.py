import sys
from tests.string_function import generar_numero, validar_numero, comparar

def main():
    """Interactive game application with CLI input support"""
    numero_secreto = generar_numero()
    intentos = {}
    total_intentos = 0
    
    print("\n" + "="*60)
    print("JUEGO DE ADIVINANZA - NÚMERO DE 4 DÍGITOS")
    print("="*60)
    print("Adivina cada dígito del número (posición 1-4)")
    print("Ingresa dígitos del 0-9\n")
    
    while len(intentos) < 4:
        try:
            posicion_input = input("¿Qué posición deseas adivinar? (1-4): ").strip()
            
            if not posicion_input.isdigit() or int(posicion_input) not in [1, 2, 3, 4]:
                print("❌ Ingresa una posición válida (1-4)\n")
                continue
            
            pos = int(posicion_input) - 1
            
            if pos in intentos:
                print(f"✓ Ya adivinaste la posición {posicion_input}: {intentos[pos]}\n")
                continue
            
            digito_input = input(f"Ingresa el dígito para la posición {posicion_input} (0-9): ").strip()
            
            valido, num = validar_numero(digito_input)
            if not valido:
                print("❌ Debes ingresar un dígito entre 0 y 9\n")
                continue
            
            intentos[pos] = num
            total_intentos += 1
            
            progreso, correctos = comparar(numero_secreto, intentos)
            
            print(f"\n{'='*60}")
            print(f"📍 Progreso: {progreso}")
            print(f"✓ Dígitos correctos: {correctos}/4")
            print(f"📊 Intento #{total_intentos}")
            print(f"{'='*60}\n")
            
            if correctos == 4:
                print("="*60)
                print(f"🎉 ¡GANASTE! Adivinaste el número: {numero_secreto}")
                print(f"📊 Total de intentos: {total_intentos}")
                print("="*60 + "\n")
                break
        
        except EOFError:
            print(f"\n\nEntrada terminada. El número era: {numero_secreto}")
            break
        except KeyboardInterrupt:
            print(f"\n\nJuego cancelado. El número era: {numero_secreto}")
            break
        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    main()