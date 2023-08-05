import Menu_Principal , Piedra_Papel_Tijera
"""
Funnción que recibe dos parámetros. Cada uno de los parámetros puede ser: 
piedra
papel
tijeras
"""
def piedra_papel_tijera(objeto_1, objeto_2 ,jugardor_1,jugardor_2):
    if  objeto_1 == objeto_2 :
         print("")
         print("Hay empate intente de  nuevo :(  ")
    elif objeto_1.lower() == "papel" or objeto_2.lower() == "piedra":
         Ganador = jugardor_1
         print(f"El Ganador es :{jugardor_1}")
    elif objeto_1.lower() == "piedra" or objeto_2.lower() == "papel":
         Ganador = jugardor_2
         print(f"El Ganador es :{jugardor_2}")
    elif objeto_1.lower() == "piedra" and objeto_2.lower() == "tijera":
         Ganador = jugardor_1
         print(f"El Ganador es :{jugardor_1}")
    elif objeto_1.lower() == "tijera" and objeto_2.lower() == "piedra":
         Ganador = jugardor_2
         print(f"El Ganador es :{jugardor_2}")
    elif objeto_1.lower() == "tijera" and objeto_2.lower() == "papel":
         Ganador = jugardor_1
         print(f"El Ganador es :{jugardor_1}")
    elif objeto_1.lower() == "papel" and objeto_2.lower() == "tijera":
         Ganador = jugardor_2
         print(f"El Ganador es :{jugardor_2}")
    while True: 
         opcion = input("Desea jugar de nuevo? (Y|N) : ")
         if opcion.lower() == "y" :
            try: 
                valor_1 = input(f"{jugardor_1} : Ingrese Piedra , Papel o Tijera: ")
                valor_2 = input(f"{jugardor_2} : Ingrese Piedra , Papel o Tijera: ")
            except: 
                print("Ingreso un valor incorrecto intente de nuevo ")
            resultado =  Piedra_Papel_Tijera.piedra_papel_tijera(valor_1,valor_2,jugardor_1,jugardor_2)
            print(f"El resultado del juego es {resultado}")
         elif opcion.lower() == "n":
            Menu_Principal.menu_principal()
         else :
               print("Opción no válida. Por favor, ingrese 'Y' para continuar o 'N' para salir al menu principal.")
         