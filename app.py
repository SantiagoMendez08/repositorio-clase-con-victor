# Aquí empieza mi app
# Aplicación de citas para barbería
# Autor: Santiago Méndez

print("==============================")
print("       CITAS BARBER")
print("==============================")

nombre = input("¿Cómo te llamas? ")
cortes = int(input("¿Cuántos cortes quieres agendar? "))

precio = 25000
total = cortes * precio

print("")
print(f"Hola {nombre}, bienvenido a Citas Barber.")
print(f"Agendaste {cortes} cortes.")
print(f"El precio de cada corte es ${precio:,}.")
print(f"El total de tus cortes es ${total:,}.")
print("¡Gracias por utilizar Citas Barber!")