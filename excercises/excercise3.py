def excercise3():
    print(
            """
                Escribir el algoritmo que permite calcular la nota correspondiente al primer parcial de “análisis” para un
                estudiante cualquiera. Se debe considerar que hay dos talleres y un quiz, que en conjunto valen un 30% de
                la nota y el resto (70%) corresponde a la nota del examen parcial. 
            """
                )
    
    nota = float(input("Ingresa la nota del estudiante: "))
    quiz = float(input("Ingresa la nota del quiz del estudiante: "))
    taller1 = float(input("Ingresa la nota del primer taller del estudiante: "))
    taller2 = float(input("Ingresa la nota del segundo taller del estudiante: "))
    
    parcial1 = ((nota + quiz + taller1 + taller2)/4) * 0.3 
    parcial2 = nota * 0.7
    examen = parcial1 + parcial2
    print(f"La nota del estudiante es {examen}")
