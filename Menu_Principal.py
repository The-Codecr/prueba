import Operaciones ,Mediana , Elementos_concatenados , Diccionario_de_Datos , Dos_Valores,Piedra_Papel_Tijera,sys 

def menu_principal():
    print("-------------Menu Principal--------------")   
    print("(1).Operaciones")
    print("(2).Mediana")
    print("(3).Listado de Elementos")
    print("(4).Diccionario de datos")
    print("(5).Reciba dos valores")
    print("(6).Factorial")
    print("(7).Piedra ,Papel o Tijera")
    print("(8).Salir")
    print("----------------------------------------")   
    print("")
    try: 
        opcion = int(input("Ingrese la opcion que desea ejecutar: "))
        if opcion == 1 :
            print("-------------Operaciones - Funcion #1 --------------")  
            print("Para realizar una operacion debe de ingresar la operacion que desea y luego los dos numero que desea calcular ")
            print("") 
            operando = input("Ingrese el nombre de la operacion que desee realizar : ('suma', 'resta' , 'multiplicacion' , 'modulo'): ")
            num_1 = int(input("Ingrese el primer numero:"))
            num_2 = int(input("Ingrese el segundo numero:"))
            Operaciones.Operaciones(operando,num_1,num_2)
        elif  opcion == 2 :
                print("-------------Listas - Funcion #2 --------------")  
                lista = []
                accion = True
                while accion == True:  
                    num = input("> Ingrese un número (o desea detenerse, ingrese 'salir'): ")
                    if num.lower() == "salir" :
                        print("Mi lista de números es:")  
                        accion = False  
                        break
                    lista.append(num) 
                print(lista)
                print("")
                Mediana.calcular_mediana(lista)  
        elif opcion == 3 :
                print("-------------Elementos Concatenados - Funcion #3 --------------")  
                resultado = Elementos_concatenados.elementos_concatenados()
                print("Elementos concatenados:", resultado)    
        elif opcion == 4 :
                print("-------------Diccionario de Elementos - Funcion #4 --------------")  
                datos_personales = Diccionario_de_Datos.diccionario_de_datos(
                    Nombre=input("Ingrese su nombre: "),
                    Apellidos=input("Ingrese sus apellidos: "),
                    Direccion=input("Ingrese su direccion: "),
                    Edad=int(input("Ingrese su edad: ")),
                    Profesion=input("Ingrese su profesion: "),
                    Email=input("Ingrese su email: "),
                    Telefono=input("Ingrese su telefono: ")
                )
                print(f"Diccionario de datos :\n {datos_personales}")
        elif opcion == 5 :
                print("-------------Dos Valores - Funcion #5 --------------")  
                valor_1 = input("Ingrese un valor: ")
                valor_2 = input("Ingrese otro valor: ")
                resultado = Dos_Valores.dos_valores(valor_1,valor_2)
                print(resultado)
        elif opcion == 6 :
                print("-------------Factorial - Funcion #6 --------------") 
        elif opcion == 7 :
                print("----------Piedra , Papel o Tijera - Funcion #7 --------------") 
                try : 
                    jugardor_1 = input("Ingrese el nombre del Jugador 1:")
                    jugardor_2 = input("Ingrese el nombre del Jugador 2:")
                    valor_1 = input(f"Jugardor 1 : {jugardor_1} : Ingrese Piedra , Papel o Tijera: ")
                    valor_2 = input(f"Jugardor 2 : {jugardor_2} : Ingrese Piedra , Papel o Tijera: ")
                except: 
                    print("Ingreso un valor incorrecto intente de nuevo ")
                resultado =  Piedra_Papel_Tijera.piedra_papel_tijera(valor_1,valor_2,jugardor_1,jugardor_2)
                print(f"El resultado del juego es {resultado}")
        elif opcion == 8 :
              print("Saliendo de la aplicación... ¡Vuelva pronto! :)")
              sys.exit()
        else : 
            print("")
            print("No ha ingresado ninguna opcion del menu intente de nuevo ")
    except Exception as e : 
            print("")
            print(f"Ocurrio un error ingreso un dato erroneo.Porfavor los datos que se le solicitan, Intente de nuevo ")
            print(f"Descipcion de error : {e} ")
 
