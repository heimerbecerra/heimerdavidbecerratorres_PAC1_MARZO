def ingresar_valor(vocales):
    """Solicita al usuario que ingrese un valor y actualiza el diccionario vocales."""
    valor = input("Ingrese un valor: ")
    for letra in valor:
        if letra.lower() in vocales:
            vocales[letra.lower()] += 1

def verificar_vocales(vocales):
    """Imprime la cantidad de vocales ingresadas, de cada una y la cantidad total."""
    print("\nVocales ingresadas:")
    for vocal, cantidad in vocales.items():
        print(f"{vocal}: {cantidad}")
    print(f"Total de vocales: {sum(vocales.values())}")

def ingresar_valores():
    """Solicita al usuario que ingrese valores y cuenta las vocales."""
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    while True:
        print("\nOpciones:")
        print("1. Ingresar valor")
        print("2. Verificar vocales")
        print("3. Finalizar")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            ingresar_valor(vocales)

        elif opcion == 2:
            verificar_vocales(vocales)

        elif opcion == 3:
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción inválida. Por favor, intente de nuevo.")

# Llama a la función para iniciar el programa
ingresar_valores()1