print('¡Hola Acabas De Ingresar Al Calculador de Temperaturas Mas prestigioso Del mundo!')



def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print('Aqui Estan Las Opciones De Conversion')
    print('________Elige Sabiamente 7u7____________')
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Finalizar")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(temperatura)
        print("La temperatura en grados Fahrenheit es:", fahrenheit)
        print(f"Eso es equivalente a {fahrenheit:.2f}°F.")
    elif opcion == '2':
        temperatura = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_a_celsius(temperatura)
        print("La temperatura en grados Celsius es:", celsius)
        print(f"Eso es equivalente a {celsius:.2f}°C.")
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")