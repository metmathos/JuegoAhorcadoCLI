"""
JUEGO DE AHORCADO VERSION 1.0

Autor: Matias Eduardo Herrera

Clasico juego de ahorcado en version para consola CLI de Windows, escrito en Python. 

Caracteristicas del juego:

    * Tiene 8 oportunidades de acertar las letras correctas
    * Grafico en arte ASCII de progreso de "ahorcado"
    * Muestra en un linea, las letras descartadas
    * Limpia la pantalla en cada etapa
"""

import random, os

#Base de datos para las palabras a adivinarse
lista_palabras = ["elefante","perro","cocina","lavarropas","murcielago","camioneta","televisor","computadora", \
                   "anillo", "gato", "raton", "automovil", "departamento", "gaviota", "tobogan", "radio", \
                   "estetoscopio", "estratosfera","zorro", "electricidad", "maquillaje", "casa", "guitarra"\
                    "plato", "comida", "manzana" , "banana" , "cama" , "lapicera" , "escoba" , "agua"]

#Lista con las etapas de 'ahorcado'
etapas = [
        '''
        _______
     |/      |
     |         
     |         
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |         
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \  
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \| 
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /  
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
 ____|___
 '''
    ]


#Preparacion de variables a usarse en el juego

palabra_a_adivinarse = random.choice(lista_palabras) #Eleccion aleatoria de palabra de base de datos
posicion_dibujo = 0  #Inicializacion de indice para grafica de ahorcado
lista_letras_erroneas = [] #Lista de letras erroneas
game_over = 0 #Inicializacion de cantidad de intentos erroneos
palabra_a_mostrar = [] #Lista de palabras a acertarse (al comienzo solo estara llena de guiones bajos '_')
for guion in range(0, len(palabra_a_adivinarse)):
    palabra_a_mostrar.append("_")

#Bucle principal del juego
while (game_over < 7):

    #Preparacion de grafica principal del juego
    print("**"*40)
    print("**"*40)

    print(f"QUEDAN {7 - game_over} INTENTOS")
    print(etapas[game_over])

    letras_erroneas = "-".join(lista_letras_erroneas)
    print(f"LETRAS ERRONEAS: {letras_erroneas}")

    palabra = " ".join(palabra_a_mostrar)
    print(palabra)

    #Ingreso de letra por el usuario
    while True:
        letra_a_probar = input("Ingrese una letra:")
        #Limpieza de pantalla en esta etapa (Asi no limpia toda la pantalla, se usa la pausa de input de letra)
        os.system("cls")
        #Verificacion de ingreso de un solo caracter estrictamente alfabetico
        if (letra_a_probar.isalpha() and len(letra_a_probar) == 1):
            break
        else:
            print("Ingreso no valido")


    #Adiccion de letra a lista de palabras acertadas
    for index, let in enumerate(palabra_a_adivinarse):
        if (let == letra_a_probar):
            palabra_a_mostrar[index] = letra_a_probar.upper()

    #Adiccion de letras erronea a lista de letras erroneas e incremento de cantidad de intentos errados
    if (letra_a_probar not in palabra_a_adivinarse):
        lista_letras_erroneas.append(letra_a_probar.upper())
        game_over += 1

    #Mensaje de victoria y salida del juego
    if ('_' not in palabra_a_mostrar):
        print("Ganaste!")
        break

    print("**"*40)
    print("**"*40)

#Verificacion de perdida del juego y mensaje de derrota
if(game_over == 7):
    print("Perdiste") 
