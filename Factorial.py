import Menu_Principal
def calculo_Factorial(num_factorial): 
    """
    Dos funciones que calculen el factorial de cualquier número entero mayor igual a cero y menor que 25. 
    Una de las función debe resolverlo de forma recursiva y el otro de forma iterativa (opcional).
    """
    if num_factorial >= 0 and num_factorial <= 25 :
        if  num_factorial == 0 : 
            return 1 
        else :
            fact = 1 
            while (num_factorial > 1):
                fact *=num_factorial
                num_factorial-=1
            return f"El factorial es {fact}" 
        while True : 
                continuar = input("Desea realizar otro cálculo? (Y|N): ")
                if continuar.lower() == "y":
                    try:
                        num_factorial = int(input("Ingrese un numero para calcular su factorial: "))
                    except : 
                        print("Ingrese un valor numerico para poder calcular el factorial")
                    calculo_Factorialfactorial(num_factorial)
                elif continuar.lower() == "n" :
                    print("Saliendo de la aplicación... ¡Vuelva pronto! :)")
                    Menu_Principal.menu_principal()
                    print("")
                    break  
                else:
                    print("Opción no válida. Por favor, Ingrese 'Y' para continuar o 'N' para salir.")    
    else : 
        return "Ingrese un valor dentro del rango de 0 a 25"
    