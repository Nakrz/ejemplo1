import random


def palabraAleatoria():
    palabras = ["programacion", "python", "variables", "definir", "bucle"]
    palabraSecreta = random.choice(palabras)
    return palabraSecreta


def tablero(palabraSecreta,letrasAdivinadas):
    lineas = ""
    for letra in palabraSecreta:
        if letra in letrasAdivinadas:
            lineas+=letra
        else:
            lineas+="_"
    print(lineas)
                   

def jugarAhorcado():
    palabraSecreta=palabraAleatoria()
    letrasAdivinadas=[]
    intentosRestantes = 3
    
    
    while intentosRestantes>0:
        tablero(palabraSecreta,letrasAdivinadas)
        letra=input("Digite una letra: ").lower()
        
        if letra in palabraSecreta:
            letrasAdivinadas.append(letra)
            if set (letrasAdivinadas)==set(palabraSecreta):
                print("Excelente, has descifrado la palabra secreta")
                print(f"La palabra secreta era: {palabraSecreta}")
                break
               
        else:
            intentosRestantes-=1
            print(f"Letra incorrecta. Te quedan {intentosRestantes} intentos")
        if intentosRestantes==0:
            print(f"Has perdido el juego. La palabra secreta era: {palabraSecreta}")
            
jugarAhorcado()
