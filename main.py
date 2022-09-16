import random
import time
from colorama import Back, Fore, Style, init
init()


preguntas = [
    '¿Cuál es una sintaxis correcta para mostrar "Hello World" en Python?',
    '¿Cómo se insertan COMENTARIOS en el código de Python?',
    '¿Cómo se crea una variable con el valor numérico 5?',
    '¿Cuál es la extensión de archivo correcta para los archivos de Python?',
    '¿Cómo se crea una variable con el número flotante 2.8?',
    '¿Cuál es la sintaxis correcta para generar el tipo de una variable u objeto en Python?',
    'En Python, "Hello", es lo mismo que "Hello"',
    '¿Cuál es una sintaxis correcta para devolver el primer carácter de una cadena?',
    '¿Qué método se puede usar para devolver una cadena en letras mayúsculas?',
    '¿Qué operador se usa para multiplicar números?',
    '¿Qué operador se puede usar para comparar dos valores?',
    '¿Cuál de estas colecciones define una LISTA?',
    '¿Cómo empiezas a escribir una declaración if en Python?',
    '¿Cómo empiezas a escribir un bucle while en Python?',
    '¿Cómo empiezas a escribir un bucle for en Python?',
    '¿Qué declaración se usa para detener un bucle?'
]

alternativas = [
    ['echo("Hello World")', 'p("Hello World")',
     'echo "Hello World"', 'print("Hello World")'],
    ['/*This is a comment*/', '#This is a comment', '//This is a comment'],
    ['x=5', 'Ambas respuestas son correctas', 'x=int(5)'],
    ['pyt', 'py', 'pt', 'pyth'],
    ['x=2.8', 'x=float(2.8)', 'Ambas respuestas son correctas'],
    ['print(typeOf(x))', 'print(typeof(x))',
     'print(typeof x)', 'print(type(x))'],
    ['False', 'True'],
    ['x="Hello".sub(0,1)', '"Hello"[0]', 'sub("Hello,0,1)'],
    ['uppercase()', 'toUpperCase()', 'upperCase()', 'upper()'],
    ['#', '*', 'x', '%'],
    ['<>', '=', '><', '=='],
    ['("apple", "banana", "cherry")', '{"apple", "banana", "cherry"}',
     '{"name":"apple", "color":"green"}', '["apple", "banana", "cherry"]'],
    ['if x > y then:', 'if x > y', 'if(x > y)'],
    ['while(x > y)', 'while x > y:', 'x > y while {', 'while x > y {'],
    ['for x in y:', 'for each x in y:', 'for x > y'],
    ['return', 'exit', 'break', 'stop']
]

respuestas_correctas = ['d', 'b', 'b', 'b', 'c', 'b',
                        'b', 'b', 'd', 'b', 'd', 'd', 'a', 'b', 'a', 'c']

letras = ['a', 'b', 'c', 'd', 'e']

puntaje = 0

puntajes = []

iniciar_trivia = True

intentos = 0

acumulador = 0

print(Back.RED + Style.BRIGHT + "\U0001F44B" + ("BIENVENIDO A MI TRIVIA SOBRE PYTHON").center(50, "="))
time.sleep(2)
print("PONDREMOS A PRUEBA TUS CONOCIMIENTOS" + Back.RESET)
print("\n\U0001F600")
time.sleep(2)
print("Empezaras con un puntaje de ", puntaje)
time.sleep(1)
print(Fore.BLUE + "\nPara hacer más interesante la trivia por cada respuesta correcta que")
print("tengas se te adicionará un puntaje aleatorio entre 5 y 10 puntos y por")
print("cada respuesta incorrecta se te descontará aleatoriamente entre 0 a 5 puntos\n" + Fore.RESET)
time.sleep(3)
print(Fore.GREEN + "ahh!!, lo olvidaba. Para premiar tu esfuerzo por cada 3 preguntas concecutivas correctas")
print("podrás tirar el dado y esos puntos se sumarán a tu puntaje final" + Fore.RESET)
print("\n")
time.sleep(2)
print(Fore.RED + "No te lo recomiendo, pero puedes escribir 'exit' en cualquier momento si no quieres terminar todas las preguntas" + Fore.RESET)
time.sleep(1)
print("\nEMPEZEMOS...\U0001F4AA\n")
time.sleep(1)
nombre = input(Fore.CYAN + "\n¿CUÁL ES TU NOMBRE?\n" + Fore.RESET)
print(Fore.GREEN + "\n Muy bien", Back.BLUE + nombre.upper() + Back.RESET, ", responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n" + Fore.RESET)

while iniciar_trivia == True:
    intentos += 1
    puntaje = 0

    print(Fore.GREEN + "\nEste es tu intento número: ", intentos, Fore.RESET)
    input("\nSi estás listo presiona " + Back.YELLOW + "Enter" + Back.RESET + " para empezar\n")

    for i in range(0, len(preguntas), 1):
        print(Back.RED + "Pregunta", i+1, Back.RESET)
        print(Fore.LIGHTMAGENTA_EX + preguntas[i],'\n' + Fore.RESET)
        for j in range(0, len(alternativas[i]), 1):
            print(letras[j],") ", alternativas[i][j])

        respuesta = input(Fore.YELLOW + "Tu respuesta: " + Fore.RESET)
        if respuesta == "exit":
          # iniciar_trivia = False
          break
        if respuesta == respuestas_correctas[i]:
            puntaje += random.randint(5,10)
            print(Fore.GREEN + "\nMuy bien", nombre,"\U0001F603!\n" + Fore.RESET)
            acumulador += 1
            if acumulador == 3:
              print(Fore.GREEN + Back.YELLOW + "Bien", nombre.upper(), "has logrado 3 respuestas correctas concecutivas" + Back.RESET + " \U0001F60E\n")
              print("\nPresiona 'Enter' para tirar el dado, el puntaje que te salga se sumará a tu puntaje final")
              input("\nTirar dado \U0001F3B2")
              tirar_dado = random.randint(1,6)
              print("\nHas ganado", tirar_dado, "puntos\n" + Fore.RESET)
              puntaje += tirar_dado
              acumulador = 0
        else:
          puntaje -= random.randint(0,5)
          acumulador = 0
          if puntaje < 0:
            puntaje = 0
          print(Fore.RED + "\nIncorrecto", nombre,"! \U0001F615\n" + Fore.RESET)
        time.sleep(1.5)

    puntajes.append(puntaje)
    print("Gracias", nombre, "espero que te hayas divertido, en este intento alcanzaste",
    puntaje, "puntos")

    print("\n¿Quieres intentarlo de nuevo?")
    repetir_trivia = input(
        "Ingresa " + Back.GREEN + "'si'" + Back.RESET + " para continuar o " + Back.RED + "'no'" + Back.RESET + " para finalizar: ").lower()

    if repetir_trivia != "si":
      print(Fore.GREEN + "\nEstos son todos los puntajes que obtuviste en tus intentos", nombre + Fore.RESET)
      print("\n")
      print("+--------------------+----------+")
      print("|Intento             |Puntaje   |")
      print("+--------------------+----------+")
      for i in range(0, len(puntajes)):
        intento = i + 1
        puntaje = puntajes[i]
        cadena = "|{:<20}|{:>10.2f}|".format(intento, puntaje)
        print(cadena)
        print("+--------------------+----------+")

      print(
          Fore.GREEN + "\nEspero que te hayas divertido", nombre, "ojalá vuelvas pronto!!" + Fore.RESET)
      iniciar_trivia = False
