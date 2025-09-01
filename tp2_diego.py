# Ejercicio 1
def ada():
    first_name = "AdA"
    last_name = "LoVeLAce"
    full_name = f"{first_name} {last_name}"
    print(full_name.lower())
    print(full_name.title())
    print(full_name.upper())
    print("\t" + full_name.lower())
    
ada()

# Ejercicio 2
def earth():
    x = "Bangladesh"
    y = "Barbados"
    
    x_comes_first = x > y
    y_comes_first = y > x
    
    print(f"The result of {x} comes first in the dictionary than {y} is {x_comes_first}.")
    print(f"The result of {y} comes first in the dictionary than {x} is {y_comes_first}.")

earth()

# Ejercicio 3
def change():
    expense = 23.75
    money = 100

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = int((vuelto - pesos)*100)
    print(pesos)
    print("Centavos:")
    print(centavos)

change()