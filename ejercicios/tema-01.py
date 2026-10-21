
# =============================================================
# Tema 01 · Variables, tipos, entrada y salida · EJERCICIOS
# Nombre completo: Santiago Méndez
# Mi app se llama: Citas Barber
# =============================================================


# EJERCICIO 1 · Tarjeta de presentación

nombre = "Santiago"
edad = 18
estatura = 1.70

print(f"Soy {nombre}, tengo {edad} años y mido {estatura} m.")


# EJERCICIO 2 · ¿De qué tipo es?

a = "100"
b = 100
c = 100.0
d = "cien"

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Respuesta:
# "100" es un texto y 100 es un número entero.
# Python los reconoce como tipos de datos diferentes.


# EJERCICIO 3 · La cuenta del almuerzo

cuenta = int(input("Valor de la cuenta: "))
personas = int(input("¿Cuántas personas van a pagar? "))
porcentaje = int(input("Porcentaje de propina: "))

propina = cuenta * porcentaje / 100
total = cuenta + propina
cada_persona = total / personas

print(f"Propina:       ${propina:,.0f}")
print(f"Total:         ${total:,.0f}")
print(f"Cada uno paga: ${cada_persona:,.0f}")


# EJERCICIO 4 · Encuentra el error

precio = int(input("Precio del producto: "))
unidades = int(input("Unidades: "))

total = precio * unidades

print(f"Total a pagar: ${total:,.0f}")

# Error 1:
# input() recibe los datos como texto.
# Por eso convertimos precio a entero con int().

# Error 2:
# No se debe unir el texto con precio * unidades usando +.
# Primero multiplicamos los números y después mostramos el resultado.


# EJERCICIO 5 · Inventario rápido

producto = input("Nombre del producto: ")
unidades = int(input("¿Cuántas unidades hay? "))
precio = int(input("Precio de cada unidad: "))

valor_total = unidades * precio

print("===== INVENTARIO =====")
print(f"Producto:    {producto}")
print(f"Unidades:    {unidades}")
print(f"Precio:      ${precio:,.0f}")
print(f"Valor total: ${valor_total:,.0f}")
print("======================")
