#Primer trabajo entregable Curso Selección Back End MTPE
#Alumno: Rubén Alonso Iturrarán Saavedra
#Asignatura: Hacer una trivia

from pickle import TRUE

rpta_firme = ["C", "A", "B"]  #Estas son las respuestas correctas
iniciar_trivia = True  #Esto permite tener un trigger para poder loopear la trivia
correcto = 0  #Este es el contador de respuestas correctas
rpta_resultado = [
]  #Este es un array vacío donde se llenan los resultados ya sea Bien o Mal, esto se obtiene de comparar dos arrays: rpta_firme y rpta_alumno


def llenar_resultado(
        rptaa, rptaf,
        i):  #Método que recibe dos respuestas, rptaLumno y rptaFirme
    #junto con el index al que pertenecen
    global correcto  #Lo pongo global para poder usar el int correcto dentro del scope de la función
    if rptaa[i] == rptaf[i]:  #Compara respuesta del alumno con respuesta firme
        rpta_resultado.append("Bien")  #Agrega Bien al array rpta_resultado.
        correcto += 1  #Agrega +1 al contador correcto
    else:
        rpta_resultado.append("Mal")  #Agrega Mal al array rpta_resultado :)


print("---------Cuestionario de Redes---------")
nombre = input("\nIngrese su nombre: ")
intro = """Espero haya estudiado"""
print("Bienvenid@ {}, {} ".format(nombre.upper(), intro))
while iniciar_trivia == True:  #Como su estado inicial es True, inicia el loop

    print("""1. Qué topologías se usa en los sistemas de cableado estructurado
    A. BUS
    B. ANILLO
    C. ESTRELLA
    D. MALLA
    E. N/A""")
    rpta1 = input("\nRespuesta 1: ").upper()

    print("""2. ¿Qué significa SFTP?
    A. Shielded Foiled Twisted Pair
    B. Super Foiled Twisted Pair
    C. Shielded For Twisted Pair
    D. Shielded Foiled Two Pair
    E. N/A""")
    rpta2 = input("\nRespuesta 2: ").upper()

    print(
        """3. ¿Qué tipo de cable se utiliza para enlazar dos equipos de networking?
    A. Patch-Cord
    B. Crossover
    C. Long-Cord
    D. Short-Cord
    E. N/A""")
    rpta3 = input("\nRespuesta 3: ").upper()

    rpta_alumno = [rpta1, rpta2, rpta3
                   ]  #Llena el array rpta_alumno con las respuestas del alumno
    #Llenamos el array resultado, se puede hacer en un método aparte bien bonito
    #pero no tuve tiempo Profesor :( recién hoy aprendí python :(
    llenar_resultado(rpta_alumno, rpta_firme, 0)
    llenar_resultado(rpta_alumno, rpta_firme, 1)
    llenar_resultado(rpta_alumno, rpta_firme, 2)

    print("""Resultados:
      N° // Respuesta del Alumno // Respuesta correcta""")

    for index, rpta in enumerate(
            rpta_alumno,
            start=1):  #Con la función enumerate wrappeando rpta_alumno,
        # se tienen ahora dos valores:el index donde estamos y el valor de rpta_alumno
        print(index, rpta, rpta_firme[index - 1], rpta_resultado[
            index - 1])  #Pongo -1 en la posición de los otros arrays porque
        #el index dentro de enumerate(rpta_alumno) empieza desde 1 mas no 0

    print("Su puntaje es {} de 3".format(
        correcto))  #Ïmprime puntaje como pide la tarea

    repetir_trivia = input("Repetir? Si/No:").lower(
    )  #Desde acá se permite iniciar la trivia denuevo como pide la tarea
    if repetir_trivia != "si":
        print("Espero te hayas divertido, {} :)".format(nombre))
        iniciar_trivia = False
    else:
        correcto = 0  #Reinicia el contador de respuestas correctas
        rpta_resultado = []  #vacía el index rpta_resultado
