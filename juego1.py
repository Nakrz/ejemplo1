import random

#palabra aleatoria
def creacion_de_palabra_aleatoria():
    palabras = ["programacion", "python", "variables", "definir", "bucle"]
    palabraSecreta = random.choice(palabras)
    return palabraSecreta

#mostrar en pantalla las lineas donde estaran ubicadas las letras adivinadas
def mostrar_tablero_lineas(palabraSecreta,letrasAdivinadas):
    lineas = ""
    for letra in palabraSecreta:
        if letra in letrasAdivinadas:
            lineas+=letra
        else:
            lineas+="_"
    print(lineas)
                   
#aqui se juega, ingresando la letra que confome la palabra secreta, segun la letra que sea seleccionada, si corresponde a la palabra secreta
#una linea se rellenara con la letra digitada y no se contara como intento perdido                 
def jugarAhorcado():
    palabraSecreta=creacion_de_palabra_aleatoria()
    letrasAdivinadas=[]
    intentosRestantes = 3
    
    
    while intentosRestantes>0:
        mostrar_tablero_lineas(palabraSecreta,letrasAdivinadas)
        letra=input("Digite una letra: ").lower()
        
        if letra in palabraSecreta:
            letrasAdivinadas.append(letra)
            if set (letrasAdivinadas)==set(palabraSecreta):
                print("Excelente, has descifrado la palabra secreta")
                print(f"La palabra secreta era: {palabraSecreta}")
                break
               
        else:
            intentosRestantes-=1
            print(f"Letra incorrecta. Te quedan {intentosRestantes}")
        if intentosRestantes==0:
            print(f"Has perdido el juego. La palabra secreta era: {palabraSecreta}")
            
jugarAhorcado()