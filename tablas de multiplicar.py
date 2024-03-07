print('////////////////////////////////////////')
print('Bienvenido')
print('¿Que Numero Deseas Multiplicar?')
N = int(input("Por favor,SOLO enteros positivos (N): "))

# Verificar si N es positivo
if N > 0:
    # Generar y mostrar la tabla de multiplicar
    for i in range(1, 11):
        print(f"{N} x {i} = {N * i}")
else:
    print("Lo siento, el número debe ser positivo.")


print('Tablas de Multiplicar Realizadas con exito')
print('///////////////////////////////////////////')