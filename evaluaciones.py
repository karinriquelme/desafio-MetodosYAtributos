from pizza import Pizza
from limpiar import limpiar

limpiar()
#a
print("** ATRIBUTOS DE LA CLASE PIZZA**\n")
print(f"1. Lista de proteinas:{Pizza.proteinas}")
print(f"2. Lista de vegetales:{Pizza.vegetales}")
print(f"3. Lista de masas    :{Pizza.masas}")
print(f"4. Tamaños           :{Pizza.tamano}")
print(f"5. Precio            :{Pizza.precio}")

#b
salsa=Pizza.validar_elementos("salsa de tomates", ["salsa de tomates","salsa bbq"])
print(f"\nSalsa de tomates es una salsa valida: {'Si' if salsa else 'No'}.\n")

#c
mi_pizza=Pizza()
mi_pizza.tomar_pedido()

#d

print(f"\n Es una pizza valida {'Si' if mi_pizza.es_valida else 'No'}")

#e
print(f"la clase pizza es valida? {'SI' if Pizza.es_valida else 'NO'}")