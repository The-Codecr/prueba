import Menu_Principal ,Dos_Valores
"""
Una función que reciba dos valores, y devuelva el resultado de aplicar el operador + entre ambos datos. 
Si el operador no se puede utilizar entre los datos enviados, debe devolver un mensaje que diga 
"No se puede aplicar este operador a los datos enviados".
"""
def dos_valores(valor_1, valor_2):
        try :
         if isinstance(valor_1, (int, float)) and isinstance(valor_2, (int, float)):    
                resultado = valor_1 + valor_2
                return  resultado
         else :
                return print("No se puede aplicar este operador a los datos enviados")  
        except  TypeError : 
                print("No se puede aplicar este operador a los datos enviados")  
        while True: 
            opcion = input("Desea realizar otro calculo? Ingrese ( Y | N ): ")
            if opcion.lower() == "y" :
                    valor_1 = input("Ingrese un valor: ")
                    valor_2 = input("Ingrese otro valor: ")
                    Dos_Valores.dos_valores(valor_1,valor_2)
            elif opcion.lower()  == "n" :
                    Menu_Principal.menu_principal()
            else : 
                print("Desea realizar otra concatenacion? ( Y | N )")
