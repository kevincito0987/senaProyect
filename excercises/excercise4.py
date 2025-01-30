def excercise4():
    print(
            """
                Un capital C está situado a un tipo de interés R anual ¿al término de cuántos años se doblará? 
            """
                )
    
    r = float(input("Ingresa el capital en $: "))
    anual = float(input("Ingresa el % de interés: "))
    
    años = r / anual
    print(f"El capital se doblará en {años} años")
    
