import Menu_Principal

def calcular_mediana(lista):
    """Funcion que recibe un lista y luego envia la mediana de la misma
    @args: 
    @args: 
    @args: 
    """
    sum_list = 0    
    print("Mediana de los indices: ")
    for recorrido in lista:
        sum_list += int(recorrido)    
    tamanio = len(lista)
    mediana = sum_list / tamanio
    print(f"La mediana es de: {round(mediana)}")
    print("")
    while True:
        continuar = input("Desea realizar otro cálculo? (Y|N): ")
        if continuar.lower() == "y":
                calcular_mediana(lista)
                """Preguntar al profe como poder utilizar esta funcion 
                recursiva pero llamar a otros valores distintos de la lista"""
        elif continuar.lower() == "n" :
                print("Saliendo de la aplicación... ¡Vuelva pronto! :)")
                Menu_Principal.menu_principal()
                print("")
                break  
        else:
                print("Opción no válida. Por favor, Ingrese 'Y' para continuar o 'N' para salir.")
