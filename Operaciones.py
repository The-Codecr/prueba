import Menu_Principal
def Operaciones(operando, num_1,num_2):
    """
    Funcion que recibe tres parametros (Operador , numero_1 , numero_2 )realiza una 
    operacion entre ambos  numeros.
    @args: 
    @args: 
    @args: 
    """
    if operando.lower() == "suma": 
                resultado = num_1 + num_2
                print(f"El resultado de la {operando} de ambos numero es : {resultado}" ) 
    elif operando.lower() == "resta": 
                resultado = num_1 - num_2
                print(f"El resultado de la {operando} de ambos numeros es : {resultado}" )
    elif operando.lower() == "multiplicacion": 
                resultado = num_1 * num_2
                print(f"El resultado de la {operando} de ambos numeros es : {resultado}" ) 
    elif operando.lower() == "modulo": 
                resultado = num_1 % num_2
                print(f"El resultado de la {operando} de ambos numeros es : {resultado}" )             
    else :
                print("Operando no valido intente de nuevo. Por favor use 'suma' , 'resta', 'multiplicacion'  o 'division' ") 
    while True:
        continuar = input("Desea realizar otro cálculo? (Y|N): ")
        if continuar.lower() == "y":
                operando = input(" Ingrese el nombre de la operacion que desee realizar ('suma', 'resta' , 'multiplicacion' , 'modulo'): ")
                num_1 = float(input("Ingrese el primer número: "))
                num_2 = float(input("Ingrese el segundo número: "))
                Operaciones(operando, num_1, num_2)
        elif continuar.lower() == "n" :
                print("Saliendo de la aplicación... ¡Vuelva pronto! :)")
                Menu_Principal.menu_principal()
                print("")
                break  
        else:
                print("Opción no válida. Por favor, ingrese 'Y' para continuar o 'N' para salir.")


