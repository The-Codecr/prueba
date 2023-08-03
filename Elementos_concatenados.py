def elementos_concatenados(*args):
    """
    Una función que reciba una cantidad cualquiera de elementos 
    y devuelva todos los elementos concatenados separados por un espacio:
    @args: 
    @args: 
    @args: 
    """
    elementos = []
    while True:
        elemento = input("Ingrese un elemento (o escriba 'salir' para detenerse): ")
        if elemento.lower() == "salir":
            break
        elementos.append(elemento)
    resultado = " ".join(elementos)
    return resultado