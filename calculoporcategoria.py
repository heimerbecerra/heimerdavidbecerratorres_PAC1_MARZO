descuentos = {
    "Ferretería": 0.10,
    "Aseo": 0.05,
    "Seguridad": 0.15,
    "Alimentos": 0.08,
    "Electrodomésticos": 0.12
}

# Cantidad de productos comprados por categoría
cantidades = {
    "Ferretería": 0,
    "Aseo": 0,
    "Seguridad": 0,
    "Alimentos": 0,
    "Electrodomésticos": 0
}

# Total recaudado
total_recaudado = 0

# Menú de opciones
def menu():
    print("1. Ingresar producto")
    print("2. Mostrar cantidad de productos comprados por categoría")
    print("3. Mostrar total recaudado")
    print("4. TERMINAR")
    opcion = int(input("Ingrese una opción: "))
    return opcion

# Ingresar producto
def ingresar_producto():
    global total_recaudado  # Declarar la variable global
    categoria = input("Ingrese la categoría: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidades[categoria] += 1
    descuento = precio * descuentos[categoria]
    total_recaudado += precio - descuento
    print("Producto ingresado correctamente")

# Mostrar cantidad de productos comprados por categoría
def mostrar_cantidades():
    for categoria, cantidad in cantidades.items():
        print(f"{categoria}: {cantidad}")

# Mostrar total recaudado
def mostrar_total_recaudado():
    print(f"Total recaudado: {total_recaudado}")

# Bucle principal
while True:
    opcion = menu()
    if opcion == 1:
        ingresar_producto()
    elif opcion == 2:
        mostrar_cantidades()
    elif opcion == 3:
        mostrar_total_recaudado()
    elif opcion == 4:
        print("Sistema terminado 7u7")
        break
    else:
        print("Opción inválida")
        
